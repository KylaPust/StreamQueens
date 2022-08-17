from flask import Flask, jsonify, render_template, request, flash, session, redirect
from model import Watch, Movie, connect_to_db, db
import users, movie_api, crud, model

from jinja2 import StrictUndefined

app = Flask(__name__)
app.secret_key = "dev"
app.jinja_env.undefined = StrictUndefined

@app.route('/')
def homepage():
    genres = movie_api.genres_dict

    return render_template("homepage.html", genres=genres)

@app.route('/login', methods=['POST'])
def user_login():

    email = request.form.get("email") 
    password = request.form.get("password")
    login_user = crud.get_user_by_email(email)  
    
    if login_user:
        if login_user.password != password:
            flash("Your password is wrong, try again")
        else:
            session['email'] = email
            flash(f"{login_user.email}, you're all set!")
    else:
        flash("Invalid Email. Try again.")
    return redirect("/")

@app.route('/newaccount', methods=["POST"])
def create_newaccount():

    email = request.form.get("email")
    password = request.form.get("password")
    existing_user = crud.get_user_by_email(email)
    
    if existing_user:
        flash(f"An account already exists for this email: {email}")
    else:
        user = crud.create_user(email, password)
        db.session.add(user)
        db.session.commit()
        flash(f"Thanks {email}!  Your account is now created")
    
    return redirect("/")


@app.route('/createdsearch')
def query_results():

    genre = int(request.args.get("genre-id"))
    result_type = request.args.get("result_type")
    print(result_type)
    services = request.args.get("service").split(",")
    print(services)
    json_movies = {}

    for service in services:
    
        movies = movie_api.get_api_results(genre, result_type, service)

        for movie in movies:
            json_movies[movie.movie_id] = movie.to_dict()
 
    # flash("Here are your results")
    # return render_template("createdsearch.html",movies=movies)
    return jsonify(json_movies)
    #return movies

@app.route("/addtowatchlist")
def add_watchlist():

    if 'email' in session:
        movie_id = int(request.args.get("movie"))
        email = session['email']
        user = users.get_user_by_email(email)
        user_id = user.user_id

        # if movie_id == 
        allwatched = users.get_all_watched_by_user(user_id)
        allwatched_movieids = users.get_all_watched_movieids_by_user(user_id)

        if movie_id not in allwatched_movieids:
            watchedmovie = users.add_to_watchlist(user_id, movie_id)
            return f"{session['email']}, {watchedmovie} was added to your watchlist {movie_id} not in {allwatched_movieids}"
        else:
            return f"{movie_id} is already in {allwatched_movieids}"
    else:
        return "Please login before adding movies to a watchlist"

@app.route('/account')
def user_account():

    if 'email' in session:
        email = session['email']
        user = users.get_user_by_email(email)
        user_id = user.user_id
        all_watched = users.get_all_watched_by_user(user_id)
        movies = []
        for movie in all_watched:
            movieobj = users.get_movie_by_key(movie.movie_id)
            movies.append(movieobj)
        return render_template("account.html", email=email, all_watched=movies)
    else:
        flash("Oops, please log in before viewing your account")
        return redirect("/")

@app.route('/logout')
def user_logout():

    if 'email' in session:
        session.pop('email', None)
        flash("You are no longer logged in")
        return redirect('/')
    else:
        flash("You're not logged in yet")
        return redirect('/')

if __name__ == "__main__":
    # DebugToolbarExtension(app)

    connect_to_db(app)

    app.run(host="0.0.0.0", debug=True)

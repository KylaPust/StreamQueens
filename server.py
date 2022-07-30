from flask import Flask, render_template, request, flash, session, redirect
from model import Watch, connect_to_db, db
import users, movie_api, crud

from jinja2 import StrictUndefined

app = Flask(__name__)
app.secret_key = "dev"
app.jinja_env.undefined = StrictUndefined

@app.route('/')
def homepage():

    return render_template("homepage.html")

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
            flash(f"{login_user.email}, you're are all set!")
    else:
        flash("Invalid Email. Try again.")
    return redirect('/')

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
    movies = movie_api.get_api_results("99", "movie", "netflix")
    flash("Here are your results")
    return render_template("createdsearch.html",movies=movies)

@app.route('/account')
def user_account():

    return render_template("account.html")

if __name__ == "__main__":
    # DebugToolbarExtension(app)

    app.run(host="0.0.0.0", debug=True)

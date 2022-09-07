from model import db, User, Movie, Watch, Rating

def create_user(email2, password2):
    """Create and return a new user."""

    user = User(email=email2, password=password2)

    return user

def get_user_by_id(user_id):

    user = User.query.get(user_id)

    return user

def get_user_by_email(email):

    user = User.query.filter_by(email=email).first()

    return user

def get_all_users():

    all_users = User.query.all()

    return all_users

def create_movie(title, overview, poster_path, link, streaming):
    """Create and return a new movie."""
    existing_movie = get_movie_obj_by_title(title, streaming)
    
    if existing_movie:
       return existing_movie
    else:
        movie = Movie(
            title=title, 
            overview=overview,  
            poster_path=poster_path,
            link=link,
            streaming=streaming)
    
        db.session.add(movie)
        db.session.commit()

        return movie

def get_movie_obj_by_title(title, streaming):

    movie = Movie.query.filter_by(title=title, streaming=streaming).first()

    return movie

def get_all_movies():

    all_movies = Movie.query.all()

    return all_movies

def get_movie_by_key(movie_id):

    movie = Movie.query.filter_by(movie_id=movie_id).first()

    return movie

def add_to_watchlist(user_id, movie_id):

    # watchedmovies = get_all_watched_by_user(user_id)
    # allwatched = []
    # for movie in watchedmovies:
    #     allwatched.append(movie.movie_title)

    # if movie_id not in allwatched:

    watched_movie = Watch(
            user_id=user_id,
            movie_id=movie_id
        )
    db.session.add(watched_movie)
    db.session.commit()
    return watched_movie
    # else:
        # return None

def get_all_watched_by_user(user_id):

    watchedmovies = Watch.query.filter_by(user_id=user_id).all()

    return watchedmovies

def get_all_watched_movieids_by_user(user_id):

    watchedmovies = Watch.query.filter_by(user_id=user_id).all()

    movie_ids = []
    for movie in watchedmovies:
        movie_id = movie.movie_id
        print(f"movie type from users: {type(movie_id)}")
        movie_ids.append(movie_id)

    return movie_ids

def get_watched_by_movieid_user(user_id, movie_id):

    watchedmovie = Watch.query.filter_by(user_id=user_id, movie_id=movie_id).first()

    return watchedmovie

def delete_fromwatchlist(watched_id):

    Watch.query.filter(Watch.watched_id==watched_id).delete()
    db.session.commit()

    return None

def create_rating(user_id, movie_id, rating):
    
    existing_rating = find_rating_by_user_movie(user_id, movie_id)
    if existing_rating:
        return existing_rating
    else:
        rating = Rating(user_id=user_id, movie_id=movie_id, rating=rating)

        db.session.add(rating)
        db.session.commit()
        return rating

def find_rating_by_user_movie(user_id, movie_id):
    
    rating = Rating.query.filter_by(user_id=user_id, movie_id=movie_id).first()

    return rating

def genres_dicts():

    genres_dict = {"1":"Biography",
"10402":"Music","10749":"Romance","10751":"Family","10752":"War","10763":"News","10764":"Reality","10767":"Talk Show",
"12":"Adventure","14":"Fantasy","16":"Animation","18":"Drama","2":"Film Noir","27":"Horror","28":"Action","3":"Game Show",
"35":"Comedy","36":"History","37":"Western","4":"Musical","5":"Sport","53":"Thriller","6":"Short","7":"Adult",
"80":"Crime","878":"Science Fiction","9648":"Mystery","99":"Documentary"}

    return genres_dict
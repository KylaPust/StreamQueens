
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class User(db.Model):

    __tablename__ = "users"

    user_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    email = db.Column(db.String, unique=True)
    password = db.Column(db.String(50))

    def __repr__(self):
      return f'<User user_id={self.user_id} email={self.email}>'

class Movie(db.Model):

    __tablename__ = "movies"

    movie_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    title = db.Column(db.String)
    genre = db.Column(db.String)
    overview = db.Column(db.Text)
    poster_path = db.Column(db.String)
    link = db.Column(db.String)
    streaming = db.Column(db.String)

    def __repr__(self):
        return f'<Movie movie_id: {self.movie_id} title: {self.title}> link: {self.link} poster: {self.poster_path}>'

    def to_dict(self):
        return{'movie_id': self.movie_id,
                'title': self.title,
                'poster_path': self.poster_path,
                'link': self.link,
                'streaming': self.streaming}

class Watch(db.Model):

    __tablename__ = "watched"

    watched_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.user_id"))
    movie_id = db.Column(db.Integer, db.ForeignKey("movies.movie_id"))
    
    user = db.relationship("User", backref="watched", foreign_keys=user_id)
    movie = db.relationship("Movie", backref="watched", foreign_keys=movie_id)


    def __repr__(self):
        return f'<Watch watched_id: {self.watched_id} user_id: {self.user_id}> movie_id: {self.movie_id}'

class Rating(db.Model):

    __tablename__ = "ratings"

    rating_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.user_id"))
    movie_id = db.Column(db.Integer, db.ForeignKey("movies.movie_id"))
    rating = db.Column(db.Integer)
    
    user = db.relationship("User", backref="ratings", foreign_keys=user_id)
    movie = db.relationship("Movie", backref="ratings", foreign_keys=movie_id)


    def __repr__(self):
        return f'<Rating rating_id: {self.rating_id} rating: {self.rating} user_id: {self.user_id}> movie_id: {self.movie_id}'


def connect_to_db(flask_app, db_uri="postgresql:///db", echo=True):
    flask_app.config["SQLALCHEMY_DATABASE_URI"] = db_uri
    flask_app.config["SQLALCHEMY_ECHO"] = echo
    flask_app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.app = flask_app
    db.init_app(flask_app)
    db.create_all()
    print("Connected to the db!")


if __name__ == "__main__":
    from server import app

    # Call connect_to_db(app, echo=False) if your program output gets
    # too annoying; this will tell SQLAlchemy not to print out every
    # query it executes.

    connect_to_db(app)
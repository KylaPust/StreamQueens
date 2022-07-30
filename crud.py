from model import db, User, Movie, Watch, connect_to_db

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

if __name__ == '__main__':
    from server import app
    connect_to_db(app)
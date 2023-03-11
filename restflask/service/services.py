"""CRUD functions"""
from ..config import db

from ..models.model import User, user_schema, users_schema
from ..models.model import Post, post_schema, posts_schema


# ==================== Users ====================
def get_users() -> list:
    """
    Retrieves a list of all users.

    :return:
        A list of dictionaries containing user data.
    """
    users = User.query.all()
    users_list = users_schema.dump(users)
    return users_list


def create_user(data: dict) -> str:
    """
    The create_user function takes a dictionary data containing user information,
    creates a new user and saves it in the database.
    It checks if the email or username already exist in the database. If either of them exists,
    it returns an error message. If not, it creates a new user and saves it in the database.
    Returns a string message indicating if the user was created successfully or not.

    :param data: A dictionary containing user information such as username, email, password.

    :return: A string message indicating if the user was created successfully or not.
    If the user was created successfully, the message will be "Success".
    Otherwise, the message will contain an error message indicating what went wrong.
    """
    email_exist = User.query.filter_by(email=data.get('email')).first()
    username_exist = User.query.filter_by(username=data.get('username')).first()
    if email_exist or username_exist:
        return 'Error. Username or email is already exist'

    with db.session() as session:
        new_user = User(**data)
        session.add(new_user)
        session.commit()
    return 'Success'


def get_user(user_id: str) -> dict | None:  # pylint: disable=E1131
    """
    This function takes an integer user_id as input and returns a dictionary of user data associated
    with the given user id. If the user id is not found in the database, the function returns None.

    :param user_id: user_id (str): User id for the user to be retrieved from the database.
    :return:  user_dict (dict): A dictionary of user data associated with the given user id.
    It contains the following keys: id, username, email, password, created_at, and updated_at.
    If the user id is not found in the database, the function returns None.
    """
    if user_id.isdigit():
        user = User.query.filter_by(id=int(user_id)).first()
    else:
        user = User.query.filter_by(email=user_id).first()
    
    if user:
        user_dict = user_schema.dump(user)
        return user_dict
    return None


def update_user(data: dict) -> str:
    """
    Updates the user information in the database based on the given data.

    :param data:
        data (dict): A dictionary containing the user information to update,
        including the ID of the user to update.

    :return:
        str: A string indicating the status of the operation. Either "Success" or an error message
        if the user record does not exist.
    """
    user = User.query.filter_by(id=data.get('id')).first()
    if user:
        user.first_name = data.get('first_name') or user.first_name
        user.last_name = data.get('last_name') or user.last_name
        user.username = data.get('username') or user.username
        user.email = data.get('email') or user.email
        user.location = data.get('location') or user.location
        db.session.commit()
        return 'Success'
    return 'Error. No such user record in the db'


def delete_user(user_id: int) -> str:
    """
    Delete a user record from the database.

    :param user_id:
        user_id (int): The ID of the user to be deleted.

    :return:
        str: A string indicating whether the operation was successful or not.
    """
    user = User.query.filter_by(id=user_id).first()

    if user:
        with db.session() as session:
            session.delete(user)
            session.commit()
        return 'Success'
    return 'No such user record in the db'


# ==================== Posts ====================
def get_posts() -> list:
    """
    The get_posts() function retrieves all posts from the database and returns them
    as a list of dictionaries.

    :return:
        A list of dictionaries, where each dictionary represents a post in the database.
        Each post dictionary includes keys for id, title, content, and created_at.
    """
    posts = Post.query.all()
    posts_list = posts_schema.dump(posts)
    return posts_list


def create_post(data: dict) -> str:
    """
    Creates a new post with the provided data and saves it to the database.

    :param data:
        data (dict): A dictionary with the data for the new post, including
        at least a 'title' and 'body'.

    :return:
        str: A message indicating the success of the operation.
    """
    with db.session() as session:
        new_post = Post(**data)
        session.add(new_post)
        session.commit()
    return 'Success'


def get_post(post_id: int) -> dict | None:  # pylint: disable=E1131
    """
    Retrieves the post with the specified ID from the database.

    :param post_id:
        post_id (int): The ID of the post to retrieve.

    :return:
        dict | None: If a post with the specified ID exists, returns a dictionary with its data.
        Otherwise, returns None.
    """
    post = Post.query.filter_by(id=post_id).first()

    if post:
        post_dict = post_schema.dump(post)
        return post_dict
    return None


def update_post(data: dict) -> str:
    """
    Updates the post with the specified ID with the new data provided.

    :param data:
        data (dict): A dictionary with the new data for the post, including at least an 'id',
        and optionally a 'title' and/or a 'description'.

     :return:
        str: A message indicating the success or failure of the operation.
    """
    post = Post.query.filter_by(id=data.get('id')).first()

    if post:
        post.title = data.get('title') or post.title
        post.description = data.get('description') or post.description
        db.session.commit()
        return 'Success'
    return 'Error. No such post record in the db'


def delete_post(post_id: int) -> str:
    """
    Deletes the post with the specified ID from the database.

    :param post_id:
        post_id (int): The ID of the post to delete.

    :return:
        str: A message indicating the success or failure of the operation.
    """
    post = Post.query.filter_by(id=post_id).first()

    if post:
        with db.session() as session:
            session.delete(post)
            session.commit()
        return 'Success'
    return 'Error. No such post record in the db'

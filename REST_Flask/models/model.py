"""Project Models"""
from marshmallow import fields
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Text, func
from sqlalchemy.orm import relationship
# from sqlalchemy.sql import func

from config import db, ma


class User(db.Model):
    """
        Represents a registered user in the application.

        Attributes:
            id (int): The unique identifier for this user.
            username (str): The user's username, must be unique and have at most 30 characters.
            email (str): The user's email address, must be unique and have at most 255 characters.
            first_name (str): The user's first name, at most 35 characters.
            last_name (str): The user's last name, at most 35 characters.
            location (str): The user's location, at most 45 characters.
            registered_at (datetime): The date and time when this user was registered.
            posts (list of Post): The posts created by this user.
        """
    __tablename__ = 'users'
    id              = Column(Integer, primary_key=True)
    username        = Column(String(30), nullable=False)  # unique
    email           = Column(String(255), unique=True, nullable=False)
    first_name      = Column(String(35), nullable=False)
    last_name       = Column(String(35), nullable=False)
    location        = Column(String(45), nullable=False)
    registered_at   = Column(DateTime(timezone=True), server_default=func.now())  # pylint: disable=E1102
    posts            = relationship('Post', back_populates='user', cascade='all, delete')

    def __repr__(self):
        """Return a string representation of the user object."""
        return f'<User {self.username}>'

    def to_dict(self):
        """Return a dictionary representation of the user object."""
        return {
            'id': self.id,
            'username': self.username,
            'email': self.email,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'location': self.location,
            'registered_at': self.registered_at
        }


class Post(db.Model):
    """
       Represents a post made by a user in the application.

       Attributes:
           id (int): The unique identifier for this post.
           title (str): The title of the post, at most 255 characters.
           description (str): The description of the post, in the form of text.
           created_at (datetime): The date and time when this post was created.
           author_id (int): The unique identifier of the user who created this post.
           user (User): The user who created this post.
       """
    __tablename__ = 'posts'
    id              = Column(Integer, primary_key=True)
    title           = Column(String(255), nullable=False)
    description     = Column(Text, nullable=False)
    created_at      = Column(DateTime(timezone=True), server_default=func.now())  # pylint: disable=E1102
    author_id       = Column(Integer, ForeignKey('users.id'))
    user            = relationship('User', back_populates='posts')

    def __repr__(self):
        """Return a string representation of the user object."""
        return f"<Post {self.id}: {self.title}>"

    def to_dict(self):
        """Returns a dictionary representation of this post."""
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'created_at': self.created_at,
            'author_id': self.author_id
        }


class PostSchema(ma.Schema):
    """ Schema for serializing and deserializing `Post` objects. """

    # pylint: disable=missing-class-docstring,too-few-public-methods
    class Meta:
        fields = ('id', 'title', 'description', 'created_at', 'author_id', 'user')


class UserSchema(ma.Schema):
    """ Schema for serializing and deserializing `User` objects. """
    posts = fields.Nested(PostSchema, many=True)

    # pylint: disable=missing-class-docstring,too-few-public-methods
    class Meta:
        fields = ('id', 'username', 'email', 'first_name', 'last_name', 'location',
                  'registered_at', 'posts')


user_schema = UserSchema()
users_schema = UserSchema(many=True)

post_schema = PostSchema()
posts_schema = PostSchema(many=True)

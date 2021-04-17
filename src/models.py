import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Enum
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class Follower(Base):
    __tablename__ = 'follower'
    # Here we define columns for the table follower.
    id = Column(Integer, primary_key=True)
    user_from_id = Column(Integer, nullable=False)
    user_to_id = Column(Integer, nullable=False)

class User(Base):
    __tablename__ = 'user'
    # Here we define columns for the table User.
    id = Column(Integer, primary_key=True)
    username = Column(String(15), nullable=False)
    firstname = Column(String(15), nullable=False)
    lastname = Column(String(15), nullable=False)
    email = Column(String, unique=True)
    user_id = Column(Integer, ForeignKey('User.id'))
    post = relationship ('Post')
    
class Media(Base):
    __tablename__ = 'media'
    # Here we define columns for the table Media.
    id = Column(Integer, primary_key=True)
    types = Column(Enum('Analytics', 'Blogging', 'Business', 'Comunications', 'Copywriting', 'Digital_Marketing', 'Desing', 'Email _Marketing'), nullable=False)
    url = Column(String(50), nullable=False)
    post_id = Column(Integer, nullable=False)
   
class Post(Base):
    __tablename__ = 'post'
    # Here we define columns for the table Post.
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, nullable=False)
    url = Column(String(50), nullable=False)
    user_id = Column(String, ForeignKey('User.id'))
    
class Comment(Base):
    __tablename__ = 'Comment'
    # Here we define columns for the table Comment.
    id = Column(Integer, primary_key=True)
    comment_text = Column(String(100), nullable=False)
    author_id = Column(Integer, ForeignKey("author.id"))
    user = relationship ("User")
    post_id = Column(Integer, ForeignKey('post.id')) 
    post = relationship ("Post")
    media_id = Column(Integer, ForeignKey('media.id')) 
    media = relationship ("Media")
    follower_id = Column(Integer, ForeignKey('follower.id')) 
    Follower = relationship ("Follower")
    
    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
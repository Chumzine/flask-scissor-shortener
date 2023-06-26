from ..extensions import db, login_manager
from flask_login import UserMixin
from datetime import datetime


class User(db.Model, UserMixin):
    __tablename__='users'
    id = db.Column(db.Integer(), primary_key=True)
    first_name = db.Column(db.String(100), nullable=False)
    last_name = db.Column(db.String(150), nullable=False)
    username = db.Column(db.String(), nullable=False, unique=True)
    email = db.Column(db.String(), nullable=False, unique=True)
    password_hash = db.Column(db.Text(), nullable=False)
    link = db.relationship('Link', backref='user')
    

    def __repr__(self):
        return f"User <{self.username}>"
    
@login_manager.user_loader
def user_loader(id):
    return User.query.get(int(id))  

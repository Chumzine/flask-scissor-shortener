from ..extensions import db
from datetime import datetime
import string
from random import choice


class Link(db.Model):
    __tablename__='links'
    id = db.Column(db.Integer, primary_key=True)
    original_url = db.Column(db.String(500), nullable=False)
    short_url = db.Column(db.String(20), nullable=False, unique=True)
    visits = db.Column(db.Integer, default=0)
    date_created = db.Column(db.DateTime(), nullable=False, default=datetime.now())
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    def __repr__(self):
        return f"Link <{self.short_url}>"
        

def generate_short_url(num_of_chars: int):
    chars = string.digits + string.ascii_letters
    short_url = ''.join(choice(chars) for _ in range(num_of_chars))

    link = Link.query.filter_by(short_url=short_url).first()

    if link:
        return generate_short_url()

    return short_url

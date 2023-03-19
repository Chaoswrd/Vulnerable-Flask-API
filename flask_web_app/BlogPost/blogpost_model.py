from datetime import datetime
from Shared.supermodel import db
from Shared.serialiser import Serialiser

class BlogPost(db.Model, Serialiser):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    author = db.Column(db.String(20), nullable=False, default='N/A')
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __repr__(self) -> str:
        return  "User with user_id %s" % str(self.id)

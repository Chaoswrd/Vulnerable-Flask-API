from datetime import datetime
from shared.supermodel import db
from shared.serialiser import Serialiser

class User(db.Model, Serialiser):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __repr__(self) -> str:
        return  "User with user_id %s" % str(self.id)

    
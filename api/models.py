from app import db
from sqlalchemy.sql import func

class Ad(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    subject = db.Column(db.String, nullable=False)
    body = db.Column(db.String, nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, server_default=func.now())
    email = db.Column(db.String, nullable=False)
    price = db.Column(db.Integer)
    updated_at = db.Column(db.Date, onupdate=func.now())

    def to_dict(self):
        return {
            "id": self.id,
            "subject": self.subject,
            "body": self.body,
            "created_at": str(self.created_at.isoformat()),
            "email": self.email,
            "price" : self.price,
        }

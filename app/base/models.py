from app import db


class users(db.Model):
    __tablename__ = 'users'

    id = db.Column('id', db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)

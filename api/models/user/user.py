from app import db


class User(db.Model):
    __tablename__ = "cars"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    biopic = db.Column(db.Text, nullable=True)
    country = db.Column(db.Text, nullable=True)

    def __init__(self, name, biopic, country):
        self.name = name
        self.model = biopic
        self.doors = country

    def __repr__(self):
        return f"<User {self.title}>"

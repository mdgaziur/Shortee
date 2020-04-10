from app import db

class url_data(db.Model):
    serial = db.Column(db.Integer, primary_key=True)
    id = db.Column(db.String, nullable=False, unique=True)
    url = db.Column(db.String, nullable=False)

#create the database if it doesn't exists
try:
    with open("database.db") as fp:
        pass
except:
    db.create_all()
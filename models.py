from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from views import db 

engine = create_engine('sqlite:///database.db', echo=True)
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))
Base = declarative_base()
Base.query = db_session.query_property()

# Set your classes here.


class User(db.Model):
    __tablename__ = 'Users'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=False)
    email = db.Column(db.String(120), unique=True)
    password = db.Column(db.String(30))

    def __init__(self, name=None, email=None, password=None):
        self.name = name
        self.email = email
        self.password = password

    def __repr__(self):
        return '<User 0>'.format(self.name)

class Team(db.Model):
    __tablename__ = 'Teams'

    id = db.Column(db.Integer, primary_key=True)
    team_name = db.Column(db.String(120), unique=False)
    league = db.Column(db.String(120), unique=False)
    division = db.Column(db.String(30))

    def __init__(self, team_name=None, league=None, division=None):
        self.team_name = team_name
        self.league = league
        self.division = division

    def __repr__(self):
        return '<User 0>'.format(self.name)


# Create tables.
Base.metadata.create_all(bind=engine)

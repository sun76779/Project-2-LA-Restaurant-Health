import os
import os.path
from dotenv import load_dotenv
from flask import Flask
from flask import jsonify
from flask import request
from flask import make_response
from flask import url_for
from flask import render_template

from sqlalchemy import Column, Integer, String, Float, Enum, DateTime, ForeignKey
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from sqlalchemy import text

import pymysql
import json

from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

load_dotenv()
pymysql.install_as_MySQLdb()

# Database Connection (Usually, you'd put these in an .env file)
username = os.getenv("database_username")
password = os.getenv("database_password")
host = os.getenv("database_host")
port = os.getenv("database_port")
database = os.getenv("database_database")

# Format:
# `<Dialect>://<Username>:<Password>@<Host Address>:<Port>/<Database>`
# Using f-string notation: https://docs.python.org/3/reference/lexical_analysis.html#f-strings
# fstrings require Python 3!
connection = f"mysql://{username}:{password}@{host}:{port}/{database}"
# Python 2 compatible string concatenation:
# connection = "mysql://" + username + ':' + password + '@' + host + ':' + port + '/' + database 


engine = create_engine(connection)
conn = engine.connect()
session = Session(bind=engine)

app = Flask(__name__, static_folder='./static', static_url_path='')

class Restaurants(Base):
    __tablename__ = 'Restaurant Data'
    
    facility_id = Column(Integer, primary_key=True)
    facility_name = Column(String)
    score = Column(String)
    grade = Column(Integer)
    latitude = Column(Integer)
    longitude = Column(Integer)

    @property
    def serialize(self):
        """
        Return object data in easily serializeable format (JSON API)
        See https://stackoverflow.com/questions/7102754/jsonify-a-sqlalchemy-result-set-in-flask
        """
        return {
            'facility_id': self.id,
            'type': 'restaurant',
            'attributes': {
                'facility_id': self.facility_id,
                'facility_name': self.facility_name,
                'score': self.score,
                'grade': self.grade,
                'latitude': self.latitude,
                'longitude': self.longitude,
            },
             'links': {
                'self': url_for('get_one_restaurant', id=self.facility_id, _external=True)
            }
        }

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/map")
def map():
    return render_template('map.html')

@app.route("/restaurant_search")
def restaurant_search():
    return render_template('restaurantsearch.html')

@app.route("/violation_by_type")
def violation_by_type():
    return render_template('violationbytype.html')

@app.route("/violation_by_year")
def violation_by_year():
    return render_template('violationbyyear.html')

if __name__ == "__main__":
    app.run(debug=True)
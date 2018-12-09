import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify


#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)

# Save references to the tables
Measurement = Base.classes.measurement
Station = Base.classes.station

# Create our session (link) from Python to the DB
session = Session(engine)

#################################################
# Flask Setup
#################################################
app = Flask(__name__)


#################################################
# Flask Routes
#################################################

@app.route("/")
def welcome():
    """List all available api routes."""
    return (
        f"Available Routes:<br/>"
        f"/api/v1.0/names<br/>"
        f"/api/v1.0/percipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/r>"
    )  
@app.route("/api/v1.0/precipitation")
def percipitation():
    """Return a list of percipitation"""
    # Query all percipitation
    results = session.query(Measurement.prcp, Measurement.date).all()
    
    # Create a dictionary from the row data and append to a list of all_passengers
    all_percipitation = []
    for percipitation in results:
        percipitation_dict = {}
        percipitation_dict["Date"] = percipitation.date
        all_percipitation.append(percipitation_dict)
    return jsonify(all_percipitation)

@app.route("/api/v1.0/stations")
def stations():
    """Return a list of stations"""
    # Query all stations
    results = session.query(Station).all()
        # Convert list of tuples into normal list
    all_stations = list(np.ravel(results))

    return jsonify(all_stations)

@app.route("/api/v1.0/tobs")
def temperatures():
    """Return a list of temperatures"""
    # Query all temperatures
    latest_date = session.query(Measurement.date).order_by(Measurement.date.desc()).first()
    year_ago = dt.date(2017, 8, 23) - dt.timedelta(days=366)
    results = session.query(Measurement.prcp, Measurement.date).\
    filter(Measurement.date > year_ago).all()
        # Convert list of tuples into normal list
    all_temperatures = []
    for temperatures in results:
        temperatures_dict = {}
        temperatures_dict["Date"] = temperatures.date
        all_temperatures.append(temperatures_dict)
    return jsonify(all_temperatures)

    

if __name__ == '__main__':
    app.run(debug=True)
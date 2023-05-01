# Import the dependencies.
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

# Save references to each table
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
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/<start><br/>"
        f"/api/v1.0/<start>/<end>"
    )

@app.route("/api/v1.0/preciptation")
def precipitation():
    # Query 12 months precipitation data
    most_recent = session.query(Measurement.date).order_by(Measurement.date.desc()).first()
    prior_year = most_recent - dt.timedelta(days=366);
    prcp_results = session.query(Measurement.date,Measurement.prcp).filter.strftime(Measurement.date >= prior_year).\
    order_by(Measurement.date).all()

    year_prcp_data = []
    for date, precipitation in prcp_results:
        prcp_dict = {}
        prcp_dict["date"] = date
        prcp_dict["prcp"] = prcp
        year_prcp_data.append(prcp_results)

    return jsonify(precipitation)


# @app.route("/api/v1.0/stations")
# def stations():
#     # Query list of stations
#     active_stations = session.query(Measurement.station).distinct().all()

#     return jsonify(stations)


# @app.route("/api/v1.0/tobs")
# def tobs():

#     return jsonify(tobs)


if __name__ == '__main__':
    app.run(debug=True)
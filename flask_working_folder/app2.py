import pandas as pd
from flask import (
    Flask,
    render_template,
    jsonify)

from flask_sqlalchemy import SQLAlchemy

from sqlalchemy import create_engine

import numpy as np

app =Flask(__name__, template_folder="html")


engine = create_engine('sqlite:///data.sqlite')

@app.route("/")
def home():
    """Render Home Page."""
    return render_template("index2.html")



@app.route("/total")
def total_data():
    """Return total fires and years"""
    connection = engine.connect()

    # Query for total fires per year US
    total_fire = "select fire_year, count(state) as state_count from fires where fire_year >= 1992 group by fire_year order by fire_year"
    # United_States_total = pd.read_sql(total_fire, connection)
    United_States_total = pd.read_sql(total_fire, connection)
    # Format the data for Plotly
    US = {
        "x": United_States_total["FIRE_YEAR"].values.tolist(),
        "y": United_States_total["state_count"].values.tolist(),
        "type": "'mtatter'"
    }
    connection.close()
    return jsonify(US)

@app.route("/acre")
def total_acre():
    """Return acre burned for top 10 States"""
    connection = engine.connect()


    # Query for total burned acres by top 10 states
    acre = "select state, round(sum(FIRE_SIZE)) as sum from fires group by state order by sum(FIRE_SIZE) DESC Limit 10"
    acre_total = pd.read_sql(acre, connection)

    # Format the data for Plotly
    all_years = {
        "x": acre_total["STATE"].values.tolist(),
        "y": acre_total["sum"].values.tolist(),
        "type": "bar"
    }
    connection.close()
    return jsonify(all_years)

@app.route("/fire_cause")
def fire_cause_data():
    """Return top 10 causes of fire for dataset"""
    connection = engine.connect()
    # Query for causes of wildfires and its count
    causes = "select NWCG_GENERAL_CAUSE, count(NWCG_GENERAL_CAUSE) as count from fires group by NWCG_GENERAL_CAUSE order by count(NWCG_GENERAL_CAUSE) DESC LIMIT 10"
    causes_fire = pd.read_sql(causes, connection)

    # Format the data for Plotly
    fire_causes = {
        "x": causes_fire["NWCG_GENERAL_CAUSE"].values.tolist(),
        "y": causes_fire["count"].values.tolist(),
        "type": "pie"
    }
    connection.close()
    return jsonify(fire_causes)   

@app.route("/state/<state>")
def state_data(state):
    """Return state fires and years"""
    connection = engine.connect()

    state_name = state.upper()

    # Query for total fires per year NV
    state_fire = f"select fire_year, count(state) as state_count from fires where state = '{state_name}' group by fire_year order by fire_year"
    state_total = pd.read_sql(state_fire, connection)

    # Format the data for Plotly
    state = {
        "x": state_total["FIRE_YEAR"].values.tolist(),
        "y": state_total["state_count"].values.tolist(),
        "type": "mtatter"
    }
    connection.close()
    return jsonify(state)

@app.route("/acre/<year>")
def acre(year):
    """Return acre burned for top 10 States in 2011"""
    connection = engine.connect()


    # Query for total burned acres for 2020
    acre = f"select state, round(sum(FIRE_SIZE)) as sum from fires where fire_year = {year} group by state order by sum(FIRE_SIZE) DESC LIMIT 10"
    acre_total = pd.read_sql(acre, connection)

    # Format the data for Plotly
    year = {
        "x": acre_total["STATE"].values.tolist(),
        "y": acre_total["sum"].values.tolist(),
        "type": "bar"
    }
    connection.close()
    return jsonify(year)

@app.route("/fire_cause/<year>")
def fire_cause(year):
    """Return top 10 causes of fire for dataset"""
    connection = engine.connect()
    # Query for causes of wildfires and its count
    causes = f"select NWCG_GENERAL_CAUSE, count(NWCG_GENERAL_CAUSE) as count from fires where fire_year = {year} group by NWCG_GENERAL_CAUSE order by count(NWCG_GENERAL_CAUSE) DESC LIMIT 10"
    causes_fire = pd.read_sql(causes, connection)

    # Format the data for Plotly
    fire_causes = {
        "x": causes_fire["NWCG_GENERAL_CAUSE"].values.tolist(),
        "y": causes_fire["count"].values.tolist(),
        "type": "pie"
    }
    connection.close()
    return jsonify(fire_causes)   


if __name__ == "__main__":
    app.run(debug = True)




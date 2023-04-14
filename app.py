import pandas as pd
from flask import (
    Flask,
    render_template,
    jsonify)

from flask_sqlalchemy import SQLAlchemy

from sqlalchemy import create_engine

import numpy as np

app =Flask(__name__)


engine = create_engine('sqlite:///data.sqlite')

@app.route("/")
def home():
    """Render Home Page."""
    return render_template("index.html")



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
    # db.session.close()
    return jsonify(US)

@app.route("/ak")
def ak_data():
    """Return ca fires and years"""
    connection = engine.connect()

    # Query for total fires per year AK
    ak_fire = "select fire_year, count(state) as state_count from fires where fire_year >= 1992 and state = 'AK' group by fire_year order by fire_year"
    alaska_total = pd.read_sql(ak_fire, connection)

    # Format the data for Plotly
    alaska = {
        "x": alaska_total["FIRE_YEAR"].values.tolist(),
        "y": alaska_total["state_count"].values.tolist(),
        "type": "mtatter"
    }
    connection.close()
    return jsonify(alaska)

@app.route("/ca")
def ca_data():
    """Return ca fires and years"""
    connection = engine.connect()

    # Query for total fires per year CA
    ca_fire = "select fire_year, count(state) as state_count from fires where fire_year >= 1992 and state = 'CA' group by fire_year order by fire_year"
    california_total = pd.read_sql(ca_fire, connection)

    # Format the data for Plotly
    California = {
        "x": california_total["FIRE_YEAR"].values.tolist(),
        "y": california_total["state_count"].values.tolist(),
        "type": "mtatter"
    }
    connection.close()
    return jsonify(California)

@app.route("/id")
def id_data():
    """Return id fires and years"""
    connection = engine.connect()


    # Query for total fires per year ID
    id_fire = "select fire_year, count(state) as state_count from fires where fire_year >= 1992 and state = 'ID' group by fire_year order by fire_year"
    idaho_total = pd.read_sql(id_fire, connection)

    # Format the data for Plotly
    idaho = {
        "x": idaho_total["FIRE_YEAR"].values.tolist(),
        "y": idaho_total["state_count"].values.tolist(),
        "type": "mtatter"
    }
    connection.close()
    return jsonify(idaho)

@app.route("/tx")
def tx_years_data():
    """Return tx fires and years"""
    connection = engine.connect()



    # Query for total fires per year TX
    tx_fire = "select fire_year, count(state) as state_count from fires where fire_year >= 1992 and state = 'TX' group by fire_year order by fire_year"
    texas_total = pd.read_sql(tx_fire, connection)

    # Format the data for Plotly
    Texas = {
        "x": texas_total["FIRE_YEAR"].values.tolist(),
        "y": texas_total["state_count"].values.tolist(),
        "type": "mtatter"
    }
    connection.close()
    return jsonify(Texas)

@app.route("/nv")
def nv_data():
    """Return nv fires and years"""
    connection = engine.connect()

    # Query for total fires per year NV
    nv_fire = "select fire_year, count(state) as state_count from fires where fire_year >= 1992 and state = 'NV' group by fire_year order by fire_year"
    neveda_total = pd.read_sql(nv_fire, connection)

    # Format the data for Plotly
    neveda = {
        "x": neveda_total["FIRE_YEAR"].values.tolist(),
        "y": neveda_total["state_count"].values.tolist(),
        "type": "mtatter"
    }
    connection.close()
    return jsonify(neveda)

@app.route("/or")
def or_data():
    """Return or fires and years"""
    connection = engine.connect()


    # Query for total fires per year or
    or_fire = "select fire_year, count(state) as state_count from fires where fire_year >= 1992 and state = 'OR' group by fire_year order by fire_year"
    oregon_total = pd.read_sql(or_fire, connection)

    # Format the data for Plotly
    oregon = {
        "x": oregon_total["FIRE_YEAR"].values.tolist(),
        "y": oregon_total["state_count"].values.tolist(),
        "type": "mtatter"
    }
    connection.close()
    return jsonify(oregon)

@app.route("/mt")
def mt_data():
    """Return mt fires and years"""
    connection = engine.connect()


    # Query for total fires per year mt
    mt_fire = "select fire_year, count(state) as state_count from fires where fire_year >= 1992 and state = 'MT' group by fire_year order by fire_year"
    montena_total = pd.read_sql(mt_fire, connection)

    # Format the data for Plotly
    montena = {
        "x": montena_total["FIRE_YEAR"].values.tolist(),
        "y": montena_total["state_count"].values.tolist(),
        "type": "mtatter"
    }
    connection.close()
    return jsonify(montena)

@app.route("/az")
def az_data():
    """Return az fires and years"""
    connection = engine.connect()


    # Query for total fires per year az
    az_fire = "select fire_year, count(state) as state_count from fires where fire_year >= 1992 and state = 'AZ' group by fire_year order by fire_year"
    arizona_total = pd.read_sql(az_fire, connection)

    # Format the data for Plotly
    arizona = {
        "x": arizona_total["FIRST_YEAR"].values.tolist(),
        "y": arizona_total["state_count"].values.tolist(),
        "type": "mtatter"
    }
    connection.close()
    return jsonify(arizona)

@app.route("/nm")
def nm_data():
    """Return nm fires and years"""
    connection = engine.connect()


    # Query for total fires per year nm
    nm_fire = "select fire_year, count(state) as state_count from fires where fire_year >= 1992 and state = 'NM' group by fire_year order by fire_year"
    new_mexico_total = pd.read_sql(nm_fire, connection)

    # Format the data for Plotly
    new_mexico = {
        "x": new_mexico_total["FIRE_YEAR"].values.tolist(),
        "y": new_mexico_total["state_count"].values.tolist(),
        "type": "mtatter"
    }
    connection.close()
    return jsonify(new_mexico)

@app.route("/wa")
def wa_data():
    """Return WA fires and years"""
    
    connection = engine.connect()


    # Query for total fires per year WA
    wa_fire = "select fire_year, count(state) as state_count from fires where fire_year >= 1992 and state = 'WA' group by fire_year order by fire_year"
    washington_total = pd.read_sql(wa_fire, connection)

    # Format the data for Plotly
    washington = {
        "x": washington_total["FIRE_YEAR"].values.tolist(),
        "y": washington_total["state_count"].values.tolist(),
        "type": "mtatter"
    }
    connection.close()
    return jsonify(washington)

@app.route("/al")
def al_data():
    """Return al fires and years"""
    connection = engine.connect()


    # Query for total fires per year AL
    al_fire = "select fire_year, count(state) as state_count from fires where fire_year >= 1992 and state = 'AL' group by fire_year order by fire_year"
    alabama_total = pd.read_sql(al_fire, connection)

    # Format the data for Plotly
    Alabama = {
        "x": alabama_total["FIRE_YEAR"].values.tolist(),
        "y": alabama_total["state_count"].values.tolist(),
        "type": "mtatter"
    }
    connection.close()
    return jsonify(Alabama)

@app.route("/acre")
def acre_data():
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

@app.route("/acre_2020")
def acre_2020_data():
    """Return acre burned for top 10 States in 2011"""
    connection = engine.connect()


    # Query for total burned acres for 2020
    acre_2020 = "select state, round(sum(FIRE_SIZE)) as sum from fires where fire_year = 2020 group by state order by sum(FIRE_SIZE) DESC LIMIT 10"
    acre_total_2020 = pd.read_sql(acre_2020, connection)

    # Format the data for Plotly
    year_2020 = {
        "x": acre_total_2020["STATE"].values.tolist(),
        "y": acre_total_2020["sum"].values.tolist(),
        "type": "bar"
    }
    connection.close()
    return jsonify(year_2020)

@app.route("/acre_2019")
def acre_2019_data():
    """Return acre burned for top 10 States in 2019"""
    connection = engine.connect()


    # # Query for total burned acres for 2019
    acre_2019 = "select state, round(sum(FIRE_SIZE)) as sum from fires where fire_year = 2019 group by state order by sum(FIRE_SIZE) DESC Limit 10"
    acre_total_2019 = pd.read_sql(acre_2019, connection)

    # Format the data for Plotly
    year_2019 = {
        "x": acre_total_2019["STATE"].values.tolist(),
        "y": acre_total_2019["sum"].values.tolist(),
        "type": "bar"
    }
    connection.close()
    return jsonify(year_2019)

@app.route("/acre_2018")
def acre_2018_data():
    """Return acre burned for top 10 States in 2018"""
    connection = engine.connect()



    # # Query for total burned acres for 2018
    acre_2018 = "select state, round(sum(FIRE_SIZE)) as sum from fires where fire_year = 2018 group by state order by sum(FIRE_SIZE) DESC Limit 10"
    acre_total_2018 = pd.read_sql(acre_2018, connection)

    # Format the data for Plotly
    year_2018 = {
        "x": acre_total_2018["STATE"].values.tolist(),
        "y": acre_total_2018["sum"].values.tolist(),
        "type": "bar"
    }
    connection.close()
    return jsonify(year_2018)

@app.route("/acre_2017")
def acre_2017_data():
    """Return acre burned for top 10 States in 2017"""
    connection = engine.connect()


    # # Query for total burned acres for 2017
    acre_2017 = "select state, round(sum(FIRE_SIZE)) as sum from fires where fire_year = 2017 group by state order by sum(FIRE_SIZE) DESC Limit 10"
    acre_total_2017 = pd.read_sql(acre_2017, connection)

    # Format the data for Plotly
    year_2017 = {
        "x": acre_total_2017["STATE"].values.tolist(),
        "y": acre_total_2017["sum"].values.tolist(),
        "type": "bar"
    }
    connection.close()
    return jsonify(year_2017)

@app.route("/acre_2016")
def acre_2016_data():
    """Return acre burned for top 10 States in 2017"""

    connection = engine.connect()


    # # Query for total burned acres for 2016
    acre_2016 = "select state, round(sum(FIRE_SIZE)) as sum from fires where fire_year = 2016 group by state order by sum(FIRE_SIZE) DESC Limit 10"
    acre_total_2016 = pd.read_sql(acre_2016, connection)

    # Format the data for Plotly
    year_2016 = {
        "x": acre_total_2016["STATE"].values.tolist(),
        "y": acre_total_2016["sum"].values.tolist(),
        "type": "bar"
    }
    connection.close()
    return jsonify(year_2016)

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


if __name__ == '__main__':
    app.run(debug=True)


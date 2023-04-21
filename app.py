# import pandas as pd
# from flask import (
#     Flask,
#     render_template,
#     jsonify)

# #from flask_sqlalchemy import SQLAlchemy

# from sqlalchemy import create_engine

# import numpy as np

# app =Flask(__name__, template_folder="html")


# engine = create_engine('sqlite:///data.sqlite')

#  # Format the data for geojson
#     # https://notebook.community/captainsafia/nteract/applications/desktop/example-notebooks/pandas-to-geojson
# def df_to_geojson(df, properties, lat='LATITUDE', lon='LONGITUDE'):
#     # create a new python dict to contain our geojson data, using geojson format
#     gjs = {'type':'FeatureCollection', 'features':[]}

#     # loop through each row in the dataframe and convert each row to geojson format
#     for index, row in df.iterrows():
#         # create a feature template to fill in
#         feature = {'type':'Feature',
#                 'properties':{},
#                 'geometry':{'type':'Point',
#                             'coordinates':[]}}

#         # fill in the coordinates
#         feature['geometry']['coordinates'] = [row[lon],row[lat]]

#         # for each column, get the value and add it as a new feature property
#         for prop in properties:
#             feature['properties'][prop] = row[prop]
        
#         # add this feature (aka, converted dataframe row) to the list of features inside our dict
#         gjs['features'].append(feature)
    
#     return gjs



# @app.route("/")
# def home():
#     """Render Home Page."""
#     return render_template("index.html")



# @app.route("/total")
# def total_data():
#     """Return total fires and years"""
#     connection = engine.connect()

#     # Query for total fires per year US
#     total_fire = "select fire_year, count(state) as state_count from fires where fire_year >= 1992 group by fire_year order by fire_year"
#     # United_States_total = pd.read_sql(total_fire, connection)
#     United_States_total = pd.read_sql(total_fire, connection)
#     # Format the data for Plotly
#     US = {
#         "x": United_States_total["FIRE_YEAR"].values.tolist(),
#         "y": United_States_total["state_count"].values.tolist(),
#         "type": "'mtatter'"
#     }
#     connection.close()
#     return jsonify(US)

# @app.route("/acre")
# def total_acre():
#     """Return acre burned for top 10 States"""
#     connection = engine.connect()


#     # Query for total burned acres by top 10 states
#     acre = "select state, round(sum(FIRE_SIZE)) as sum from fires group by state order by sum(FIRE_SIZE) DESC Limit 10"
#     acre_total = pd.read_sql(acre, connection)

#     # Format the data for Plotly
#     all_years = {
#         "x": acre_total["STATE"].values.tolist(),
#         "y": acre_total["sum"].values.tolist(),
#         "type": "bar"
#     }
#     connection.close()
#     return jsonify(all_years)

# @app.route("/fire_cause")
# def fire_cause_data():
#     """Return top 10 causes of fire for dataset"""
#     connection = engine.connect()
#     # Query for causes of wildfires and its count
#     causes = "select NWCG_GENERAL_CAUSE, count(NWCG_GENERAL_CAUSE) as count from fires group by NWCG_GENERAL_CAUSE order by count(NWCG_GENERAL_CAUSE) DESC LIMIT 10"
#     causes_fire = pd.read_sql(causes, connection)

#     # Format the data for Plotly
#     fire_causes = {
#         "x": causes_fire["NWCG_GENERAL_CAUSE"].values.tolist(),
#         "y": causes_fire["count"].values.tolist(),
#         "type": "pie"
#     }
#     connection.close()
#     return jsonify(fire_causes)   

# @app.route("/state/<state>")
# def state_data(state):
#     """Return state fires and years"""
#     connection = engine.connect()

#     state_name = state.upper()

#     # Query for total fires per year NV
#     state_fire = f"select fire_year, count(state) as state_count from fires where state = '{state_name}' group by fire_year order by fire_year"
#     state_total = pd.read_sql(state_fire, connection)

#     # Format the data for Plotly
#     state = {
#         "x": state_total["FIRE_YEAR"].values.tolist(),
#         "y": state_total["state_count"].values.tolist(),
#         "type": "mtatter"
#     }
#     connection.close()
#     return jsonify(state)

# @app.route("/acre/<year>")
# def acre(year):
#     """Return acre burned for top 10 States in 2011"""
#     connection = engine.connect()


#     # Query for total burned acres for 2020
#     acre = f"select state, round(sum(FIRE_SIZE)) as sum from fires where fire_year = {year} group by state order by sum(FIRE_SIZE) DESC LIMIT 10"
#     acre_total = pd.read_sql(acre, connection)

#     # Format the data for Plotly
#     year = {
#         "x": acre_total["STATE"].values.tolist(),
#         "y": acre_total["sum"].values.tolist(),
#         "type": "bar"
#     }
#     connection.close()
#     return jsonify(year)

# @app.route("/fire_cause/<year>")
# def fire_cause(year):
#     """Return top 10 causes of fire for dataset"""
#     connection = engine.connect()
#     # Query for causes of wildfires and its count
#     causes = f"select NWCG_GENERAL_CAUSE, count(NWCG_GENERAL_CAUSE) as count from fires where fire_year = {year} group by NWCG_GENERAL_CAUSE order by count(NWCG_GENERAL_CAUSE) DESC LIMIT 10"
#     causes_fire = pd.read_sql(causes, connection)

#     # Format the data for Plotly
#     fire_causes = {
#         "x": causes_fire["NWCG_GENERAL_CAUSE"].values.tolist(),
#         "y": causes_fire["count"].values.tolist(),
#         "type": "pie"
#     }
#     connection.close()
#     return jsonify(fire_causes)   

# @app.route("/fire_heatmap")
# def geojson_data():
#     """Return geojson format"""
#     connection = engine.connect()

#     # Query fires
#     fire_query = "select LATITUDE, LONGITUDE from fires WHERE FIRE_YEAR == 2020"
#     fire_data = pd.read_sql(fire_query, connection)

   
# #     markers=[
# #    {
# #    'lat':0,
# #    'lon':0,
# #    'popup':'This is the middle of the map.'
# #     }
# #    ]
#     # run df_to_geojson and generate geojson 
#     fire_props = fire_data.loc[:, ~fire_data.columns.isin(['LATITUDE', 'LONGITUDE'])]
#     cols = fire_props.columns.values.tolist()
#     geojson = df_to_geojson(fire_data, cols)

#     connection.close()
#     # db.session.close()
#     return jsonify(geojson)

# # @app.route('/fire_heatmap')
# # def fire_heatmap():
# #    markers=[
# #    {
# #    'lat':0,
# #    'lon':0,
# #    'popup':'This is the middle of the map.'
# #     }
# #    ]
# #    return render_template('index.html',markers=markers )

# if __name__ == "__main__":
#     app.run(debug = True)
import pandas as pd
from flask import (
    Flask,
    render_template,
    jsonify)

#from flask_sqlalchemy import SQLAlchemy

from sqlalchemy import create_engine

import numpy as np

app =Flask(__name__, template_folder="html")


engine = create_engine('sqlite:///data.sqlite')

 # Format the data for geojson
    # https://notebook.community/captainsafia/nteract/applications/desktop/example-notebooks/pandas-to-geojson
def df_to_geojson(df, lat='LATITUDE', lon='LONGITUDE'):
    # create a new python dict to contain our geojson data, using geojson format
    gjs = {'type':'FeatureCollection', 'features':[]}

    # loop through each row in the dataframe and convert each row to geojson format
    for index, row in df.iterrows():
        # create a feature template to fill in
        feature = {'type':'Feature',
                'geometry':{'type':'Point',
                            'coordinates':[]}}

        # fill in the coordinates
        feature['geometry']['coordinates'] = [row[lon],row[lat]]

        # add this feature (aka, converted dataframe row) to the list of features inside our dict
        gjs['features'].append(feature)
    
    return gjs



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

@app.route("/geojson")
def geojson_data():
    """Return geojson format"""
    connection = engine.connect()

    # Query fires
    fire_query = "select LONGITUDE, LATITUDE from FIRES where FIRE_YEAR = 2020 and FIRE_SIZE >= 100"
    fire_data = pd.read_sql(fire_query, connection)
 
     # run df_to_geojson and generate geojson 
    geojson = df_to_geojson(fire_data)

    connection.close()
    return jsonify(geojson)

#fire heatmap
@app.route('/fire_heatmap')
def fire_heatmap():
   markers=[
   {
   'lat':0,
   'lon':0,
   'popup':'This is the middle of the map.'
    }
   ]
   return render_template('index.html',markers=markers )

#photos and/or bullet points explaining data
@app.route('/fire_count')
def firecount():
 return render_template('fire_count.html')

if __name__ == "__main__":
    app.run(debug = True)



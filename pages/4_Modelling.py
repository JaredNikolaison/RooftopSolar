from html.parser import charref
import streamlit as st
import pandas as pd
import statsmodels.api as smf
import altair as alt


import requests
from bs4 import BeautifulSoup
import json
from urllib.parse import urljoin
from sklearn.neighbors import KNeighborsClassifier
from sklearn.neighbors import KNeighborsRegressor
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import StratifiedKFold
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

from sklearn.metrics import r2_score, mean_absolute_error, accuracy_score, mean_squared_error
from sklearn import metrics
from sklearn.cluster import KMeans
from sklearn import preprocessing

# set up pages

st.set_page_config(
    page_title="Modelling",
    layout="wide",


)




st.title("Modelling")






solar_multiplier = st.slider("Solar Muliplier", 0.1, 20.0, 1.0, step=0.05)
net_demand_multiplier = st.slider("Net Demand Multiplier", 0.1, 20.0, 1.0, step=0.05)

gdp = pd.read_csv("Datafiles/pricedemand.csv")

model_solar_quad = smf.iolib.smpickle.load_pickle("Datafiles/model_solar_quad.pkl")


def predictprice(net_demand_series, generation_series):
    return model_solar_quad.predict(pd.DataFrame({"net_grid_demand_gwh": net_demand_series,
                                                  "generation_gwh_y": generation_series}))


gdp['predicted_price'] = predictprice(gdp['net_grid_demand_gwh'], gdp['generation_gwh_y'])

gdp['predicted_price_modified'] = (predictprice(gdp['net_grid_demand_gwh'] * net_demand_multiplier, gdp['generation_gwh_y'] * solar_multiplier))
gdp['predicted_price_modified_smoothed'] = gdp['predicted_price_modified'].rolling(12).mean()
gdp['predicted_volatility_modified_smoothed'] = gdp['predicted_price_modified'].rolling(12).std()
gdp["smoothed_price"] = gdp["price_GWh"].rolling(12).mean()
gdp["smoothed_volatility"] = gdp["price_GWh"].rolling(12).std()

price, volatility = st.tabs(["Wholesale Electricity Price Predictions", "Volatility Predictions"])


with price.container():


    solar_demand  = pd.read_csv("Datafiles/demand_solar_clean.csv")









    predicted_price_line = alt.Chart(gdp).mark_line(color = "red").encode(
        x=alt.X('date:T', axis = alt.Axis(format = '%Y', title = 'Date',tickCount="year"),
        ),
        y=alt.Y('predicted_price_modified_smoothed', axis = alt.Axis(title = 'Price ($/GWh)')).scale(zero = False)


        ).interactive().properties(
        title="Wholesale Electricity Price (Smoothed)"
    )


    actual_price_line = alt.Chart(gdp).mark_line(color = "blue").encode(
        x=alt.X('date:T', axis=alt.Axis(format='%Y', title='Date', tickCount="year"),
                ),
        y=alt.Y('smoothed_price', axis=alt.Axis(title='Price ($/GWh)')).scale(zero=False)

    ).interactive()


    joined_chart = predicted_price_line + actual_price_line

    st.altair_chart(joined_chart, use_container_width=True)
    st.write("blue = actual")
    st.write("red = predicted")

with volatility.container():


    predicted_volatility_line = alt.Chart(gdp).mark_line(color = "red").encode(
        x=alt.X('date:T', axis = alt.Axis(format = '%Y', title = 'Date',tickCount="year"),
        ),
        y=alt.Y('predicted_volatility_modified_smoothed', axis = alt.Axis(title = 'Price ($/GWh)')).scale(zero = False)


        ).interactive().properties(
        title="Wholesale Electricity Volatility (Smoothed)"
    )


    actual_volatility_line = alt.Chart(gdp).mark_line(color = "blue").encode(
        x=alt.X('date:T', axis=alt.Axis(format='%Y', title='Date', tickCount="year"),
                ),
        y=alt.Y('smoothed_volatility', axis=alt.Axis(title='Price ($/GWh)')).scale(zero=False)

    ).interactive()


    joined_chart_volatility = predicted_volatility_line + actual_volatility_line

    st.altair_chart(joined_chart_volatility, use_container_width=True)
    st.write("blue = actual")
    st.write("red = predicted")
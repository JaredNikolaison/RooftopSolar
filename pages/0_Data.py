from os import write

import streamlit as st
import pandas as pd

import altair as alt


# set up pages

st.set_page_config(
    page_title="Data",
    layout="wide",

)


# st.write("""s
# # My first app
# Hello *world!*
# """)
# df = pd.read_excel("wine_data.xls")
#
# st.line_chart(df)


st.title("Data")


solarcapacity_df  = pd.read_csv("Datafiles/solarcapacity.csv")
demand_df = pd.read_csv("Datafiles/Demand_Clean.csv")
pricing_df  = pd.read_csv("Datafiles/Wholesale_Pricing.csv")


capacity_tab, generation_tab, demand_tab, pricing_tab = st.tabs(["Solar Capacity", "Solar Generation", "Demand and Load", "Pricing"])


with capacity_tab.container():
    st.subheader("Solar Capacity Over Time")
    st.line_chart(
        solarcapacity_df,
        x="date",
        y="adjustedcapacity",
        color="blue",
        y_label="Capacity (MW)",
        x_label="Month",
    )

with generation_tab.container():
    st.subheader("Solar Generation Over Time")

    st.line_chart(
        solarcapacity_df,
        x="date",
        y="generation_gwh",
        color="orange",

        y_label="Generation (GWh)",
        x_label="Month",
    )
with demand_tab.container():
    st.subheader("Demand Over Time")
    st.line_chart(
        demand_df,
        x="date",
        y="demand_gwh",
        color="green",
        y_label="Demand (GWh)",
        x_label="Month",
    )
with pricing_tab.container():
    st.subheader("Pricing Over Time")
    st.line_chart(
        pricing_df,
        x="date",
        y="Price ($/MWh)",
        color="red",
        y_label="Price ($/MWh)",
        x_label="Month",
    )






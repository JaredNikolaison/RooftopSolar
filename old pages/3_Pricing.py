import streamlit as st
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns
import altair as alt


# set up pages

st.set_page_config(
    page_title="Pricing",
    layout="wide",


)



st.title("Pricing")



df  = pd.read_csv("Datafiles/Wholesale_Pricing.csv")





tab1, tab2 = st.tabs(["Pricing", "blank"])


tab1.subheader("Solar Capacity Over Time")

with tab1.container():
    st.line_chart(
        df,
        x="date",
        y="Price ($/MWh)",
        color="blue",
        y_label="Price ($/MWh)",
        x_label="Month",
    )


tab2.subheader("Solar Generation Over Time")


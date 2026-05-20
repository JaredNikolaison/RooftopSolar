import streamlit as st
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns
import altair as alt


# set up pages

st.set_page_config(
    page_title="Demand and Load",
    layout="wide",


)



st.title("Demand and Load")



df  = pd.read_csv("Datafiles/Demand_Clean.csv")





tab1, tab2 = st.tabs(["Monthly Demand", "blank"])


tab1.subheader("Solar Capacity Over Time")

with tab1.container():
    st.line_chart(
        df,
        x="date",
        y="demand_gwh",
        color="blue",
        y_label="Demand (GWh)",
        x_label="Month",
    )


tab2.subheader("Solar Generation Over Time")





#
#
# st.subheader("Preview")
# # st.write(df.head())
#
# st.subheader("Data Summary")
# st.write(df.describe())

# columns = df.columns.tolist()
#
# st.subheader("Plotted Data")
# x_column = st.selectbox("select x axis", columns, index=0)
# y_column = st.selectbox("select y axis", columns, index=4)
# st.line_chart(df.set_index(x_column)[y_column])


# def plotChart():
#     st.line_chart(df.set_index(x_column)[y_column])
#     return

# st.button("Plot", on_click=plotChart())




    #
    #
    # sns.lineplot(data=df, x=x_column, y=y_column)
    # plt.xlabel(x_column)
    # plt.ylabel(y_column)
    # st.pyplot(plt.gcf())
    #
    # # chart = (
    # #     alt.Chart(df)
    # #     .mark_circle()
    # #     .encode(x=x_column, y=y_column,  tooltip=[x_column, y_column])
    # # )
    #
    # chart = (
    #     alt.Chart(df).mark_line().encode(
    #     x=x_column ,
    #     y=alt.Y(y_column, type='quantitative'),
    #     color='symbol:N',
    #     ))
    # st.altair_chart(chart)




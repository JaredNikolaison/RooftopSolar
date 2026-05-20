from os import write

import streamlit as st
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns
import altair as alt


# set up pages

st.set_page_config(
    page_title="Solar Capacity",
    layout="wide",

)


# st.write("""s
# # My first app
# Hello *world!*
# """)
# df = pd.read_excel("wine_data.xls")
#
# st.line_chart(df)


st.title("Solar Capacity")


df  = pd.read_csv("Datafiles/solarcapacity.csv")
#
#
# st.subheader("Preview")
# # st.write(df.head())
#
# st.subheader("Data Summary")
# st.write(df.describe())

# st.subheader("Filter Data")
# columns = df.columns.tolist()
# selected_column = st.selectbox("select a column", columns)

# unique_values = df[selected_column].unique()
# selected_value = st.selectbox("select a value", unique_values)
#
# filted_df = df[df[selected_column] == selected_value]
# st.write(filted_df)




# x_column = st.selectbox("select x axis", columns, index=0)
# y_column = st.selectbox("select y axis", columns, index=1)
# st.line_chart(df.set_index("date")["adjustedcapacity"], color="blue")

#



tab1, tab2 = st.tabs(["Solar Capacity", "Solar Generation"])


tab1.subheader("Solar Capacity Over Time")
tab1.line_chart(
    df,
    x="date",
    y="adjustedcapacity",
    color="blue",
    y_label="MW",
    x_label="Month",
)


tab2.subheader("Solar Generation Over Time")

tab2.line_chart(
    df,
    x="date",
    y="generation_gwh",
    color="orange",
    y_label="GWh",
    x_label="Month",
)









    # write("test")
    # st.line_chart(
    #     df,
    #     x="date",
    #     y="generation_gwh",
    #     color="orange",
    #     y_label="",
    # )
    #
    # else:
    # st.line_chart(
    #     df,
    #     x="date",
    #     y="adjustedcapacity",
    #     color="blue",
    #     y_label="",
    # )


#
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




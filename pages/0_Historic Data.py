from os import write

import streamlit as st
import pandas as pd

import altair as alt


# set up pages

st.set_page_config(
    page_title="Historic Data",
    layout="wide",

)



st.title("Historic Data")


# read in  data
solarcapacity_df  = pd.read_csv("Datafiles/solarcapacity.csv")
demand_df = pd.read_csv("Datafiles/Demand_Clean.csv")
pricing_df  = pd.read_csv("Datafiles/Wholesale_Pricing.csv")


# create tabs

capacity_tab, generation_tab, demand_tab, pricing_tab = st.tabs(["Solar Capacity", "Solar Generation", "Demand and Load", "Pricing"])


with capacity_tab.container():

    # old graph style

    # st.subheader("Solar Capacity Over Time")
    # st.line_chart(
    #     solarcapacity_df,
    #     x="date",
    #     y="adjustedcapacity",
    #     color="blue",
    #     y_label="Capacity (MW)",
    #     x_label="Month",
    #
    # )

    # draw capacity graph

    capacity_graph = alt.Chart(solarcapacity_df).mark_line(color = 'blue').encode(
        x=alt.X('date:T', axis=alt.Axis(format='%Y', title='Date', tickCount="year"),
                ),
        y=alt.Y('adjustedcapacity', axis=alt.Axis(title='Capacity (MW)')).scale(zero=False),
       tooltip= [alt.Tooltip('date:T', title = 'Date', format = '%B-%Y'),
                 alt.Tooltip('generation_gwh', title = 'Capacity (MW)')]

    ).interactive().properties(title="Solar Generation Over Time")
    st.altair_chart(capacity_graph, use_container_width=True)




    st.write("The data for New Zealand's roof top solar capacity is provided form August 2013 to December 2025 by the NZ Electricity Authority."
             " Performance decay / degradation has been taken as an average value of 0.5% per year. "
             )

with generation_tab.container():



    # old graph style

    # st.subheader("Solar Generation Over Time")
    #
    # st.line_chart(
    #     solarcapacity_df,
    #     x="date",
    #     y="generation_gwh",
    #     color="orange",
    #
    #     y_label="Generation (GWh)",
    #     x_label="Month",
    #
    # )

    # draw generation graph

    generation_graph = alt.Chart(solarcapacity_df).mark_line(color = 'Red').encode(
        x=alt.X('date:T', axis=alt.Axis(format='%Y', title='Date', tickCount="year"),
                ),
        y=alt.Y('generation_gwh', axis=alt.Axis(title='Generation (GWh)')).scale(zero=False),
       tooltip= [alt.Tooltip('date:T', title = 'Date', format = '%B-%Y'),
                 alt.Tooltip('generation_gwh', title = 'Generation (GWh)')]

    ).interactive().properties(title="Solar Generation Over Time")
    st.altair_chart(generation_graph, use_container_width=True)


    st.write("Power data provided from NASA shows the average daily irradiation values which was then used to calculate solar generation using the formula: Generation(GWh) = Capacity(MW) × HoursinMonth × Capacityfactor / 1000 ")





with demand_tab.container():

    # old graph style

    # st.subheader("Demand Over Time")
    # st.line_chart(
    #     demand_df,
    #     x="date",
    #     y="demand_gwh",
    #     color="green",
    #     y_label="Demand (GWh)",
    #     x_label="Month",
    # )

    demand_df.rename(columns={'demand_gwh': 'Total Demand', 'net_grid_demand_gwh':'Net Grid Demand'}, inplace=True)

    # draw demand graph

    demand_chart = alt.Chart(demand_df).transform_fold(
        fold=['Total Demand', 'Net Grid Demand'],
        as_=['Total', 'Net']
        ).mark_line().encode(
            x = alt.X('date:T', axis=alt.Axis(format='%Y', title='Date', tickCount="year")),
            y=alt.Y('Net:Q', axis=alt.Axis(title='Demand (GWh)')).scale(zero=False),
            color=alt.Color('Total:N', legend=alt.Legend(title="Legend")).scale(
                  domain=['Total Demand', 'Net Grid Demand'],
                  range=['Blue', 'Orange']


            )

        ).interactive().properties(
        title="Total Electricity Demand vs Estimated Net Grid Demand"

    )
    st.altair_chart(demand_chart, use_container_width=True)

    st.write("The total New Zealand power grid demand is provided form January 2013 to December 2025. This includes demand from all sources and is not filtered by industry."
            "  \nNet Demand is calculated using the formula: NetDemand(GWh) = Demand(GWh) − Generation(GWh)")



with pricing_tab.container():
    # st.subheader("Pricing Over Time")
    # st.line_chart(
    #     pricing_df,
    #     x="date",
    #     y="price_GWh",
    #     color="red",
    #     y_label="Price ($/GWh)",
    #     x_label="Month",
    # )

    # draw pricing graph

    pricing_graph = alt.Chart(pricing_df).mark_line(color = 'Green').encode(
        x=alt.X('date:T', axis=alt.Axis(format='%Y', title='Date', tickCount="year"),
                ),
        y=alt.Y('price_GWh', axis=alt.Axis(title='Price ($/GWh)')).scale(zero=False),
       tooltip= [alt.Tooltip('date:T', title = 'Date', format = '%B-%Y'),
                 alt.Tooltip('price_GWh', title = 'Price ($/Gwh)')]

    ).interactive().properties(title="Pricing Over Time")
    st.altair_chart(pricing_graph, use_container_width=True)

    st.write("The monthly wholesale pricing simple average data from the Electricity Authority is provided from January 2013 to December 2025.")






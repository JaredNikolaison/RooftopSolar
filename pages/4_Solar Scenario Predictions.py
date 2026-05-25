# from html.parser import charref
import streamlit as st
import pandas as pd
import statsmodels.api as smf
import altair as alt
import numpy as np


# set up pages

st.set_page_config(
    page_title="Solar Scenario Predictions",
    layout="wide",


)




st.title("Solar Scenario Predictions")






solar_multiplier = st.slider("Solar Generation Muliplier", 0.1, 10.0, 1.0, step=0.05)
net_demand_multiplier = st.slider("Net Demand Multiplier", 0.1, 10.0, 1.0, step=0.05)

gdp = pd.read_csv("Datafiles/pricedemand.csv")

model_solar_quad = smf.iolib.smpickle.load_pickle("Datafiles/model_solar_quad.pkl")


def predictprice(net_demand_series, generation_series):
    return model_solar_quad.predict(pd.DataFrame({"net_grid_demand_gwh": net_demand_series,
                                                  "generation_gwh_y": generation_series}))


gdp['predicted_price'] = predictprice(gdp['net_grid_demand_gwh'], gdp['generation_gwh_y'])

gdp['predicted_price_modified'] = (predictprice(gdp['net_grid_demand_gwh'] * net_demand_multiplier, gdp['generation_gwh_y'] * solar_multiplier))
gdp['Predicted Price'] = gdp['predicted_price_modified'].rolling(12).mean() # Predicted price smoothed - named Predicted Price to get around legend issues in graph legend
gdp['Predicted Volatility'] = gdp['predicted_price_modified'].rolling(12).std() # Predicted volatility smoothed - named Predicted Volatility to get around legend issues in graph legend
gdp["smoothed_price"] = gdp["price_GWh"].rolling(12).mean()
gdp["Base Volatility"] = gdp["price_GWh"].rolling(12).std()

price, volatility, price_impact = st.tabs(["Wholesale Electricity Price Predictions", "Volatility Predictions","Price Impact"])


with price.container():


    # solar_demand  = pd.read_csv("Datafiles/demand_solar_clean.csv")


#     predicted_price_line = alt.Chart(gdp).mark_line().encode(
#         x=alt.X('date:T', axis = alt.Axis(format = '%Y', title = 'Date',tickCount="year"),
#         ),
#         y=alt.Y('predicted_price_modified_smoothed', axis = alt.Axis(title = 'Price ($/GWh)')).scale(zero = False),
#
#         # color=alt.Color('predicted_price_label:N').scale(range=['red']).title('Legend').datum(''),
#         color=alt.datum('Predicted Price'),
#     ).interactive().properties(
#         title=
# "Wholesale Electricity Price (Smoothed)",
#     )
#
#
#     base_price_line = alt.Chart(gdp).mark_line(color = "blue").encode(
#         x=alt.X('date:T', axis=alt.Axis(format='%Y', title='Date', tickCount="year"),
#                 ),
#         y=alt.Y('smoothed_price', axis=alt.Axis(title='Price ($/GWh)')).scale(zero=False),
#         color = alt.datum('Base Price')
#
#     ).interactive()


    gdp.rename(columns = {'smoothed_price':'Base Price'}, inplace = True)


    # st.altair_chart(joined_chart, use_container_width=True)


    price_chart = alt.Chart(gdp).transform_fold(
    fold=['Predicted Price', 'Base Price'],
    as_=['predicted', 'base']
    ).mark_line().encode(
        x = alt.X('date:T', axis=alt.Axis(format='%Y', title='Date', tickCount="year")),
        y=alt.Y('base:Q', axis=alt.Axis(title='Price ($/GWh)')).scale(zero=False),
        color=alt.Color('predicted:N', legend=alt.Legend(title="Legend")).scale(
              domain=['Predicted Price', 'Base Price'],
              range=['orange', 'blue']


        )

    ).interactive().properties(
    title="Wholesale Electricity Price (Smoothed)"
    )

    st.altair_chart(price_chart, use_container_width=True)

    st.write("This shows the base price compared against a predicted price calculated by the multipliers above"
             )

with volatility.container():


    #
    # predicted_volatility_line = alt.Chart(gdp).mark_line(color = 'blue').encode(
    #     x=alt.X('date:T', axis = alt.Axis(format = '%Y', title = 'Date',tickCount="year"),
    #     ),
    #     y=alt.Y('predicted_volatility_modified_smoothed', axis = alt.Axis(title = 'Price ($/GWh)')).scale(zero = False),
    #     # color = alt.datum('Predicted Volatility'),
    #     color = alt.Color(
    #         type="nominal",
    #     legend=alt.Legend(title="Legend")
    # ).scale(domain=['Predicted Volatility'], range=['blue'])
    #
    # ).interactive()
    #
    #
    # base = alt.Chart(gdp).mark_line(color = 'red').encode(
    #     x=alt.X('date:T', axis=alt.Axis(format='%Y', title='Date', tickCount="year"),
    #             ),
    #     y=alt.Y('smoothed_volatility', axis=alt.Axis(title='Price ($/GWh)')).scale(zero=False),
    #     # color = alt.datum('Base Volatility')
    #     color = alt.Color(
    #         type="nominal",
    #     legend=alt.Legend(title="Legend")
    # ).scale(domain=['Base Volatility'], range=['red'])
    # ).interactive()
    #
    #
    # joined_chart_volatility = (predicted_volatility_line + base_volatility_line).properties(
    #     title="Wholesale Electricity Volatility (Smoothed)"
    # )
    #
    # st.altair_chart(joined_chart_volatility, use_container_width=True)


    volatility_chart = alt.Chart(gdp).transform_fold(
        fold=['Predicted Volatility', 'Base Volatility'],
        as_=['predicted', 'base']
        ).mark_line().encode(
            x = alt.X('date:T', axis=alt.Axis(format='%Y', title='Date', tickCount="year")),
            y=alt.Y('base:Q', axis=alt.Axis(title='Price ($/GWh)')).scale(zero=False),
            color=alt.Color('predicted:N', legend=alt.Legend(title="Legend")).scale(
                  domain=['Predicted Volatility', 'Base Volatility'],
                  range=['orange', 'blue']


            )

        ).interactive().properties(
        title="Wholesale Electricity Volatility (Smoothed)"
    )

    st.altair_chart(volatility_chart, use_container_width=True)

    st.write("This shows the base volatility compared against a predicted Volatility calculated by the multipliers above")

with price_impact.container():

    threshold = gdp['Base Price'].quantile(0.95)
    gdp['Price Spike'] = gdp['price_GWh'] > threshold
    gdp['Predicted Price Spike'] = gdp['Predicted Price'] > threshold



    # summary = pd.DataFrame({"Base": [gdp["Base Price"].mean(), gdp["Base Price"].std(), gdp["Price Spike"].mean()],
    #               "Modified": [gdp["Predicted Price"].mean(), gdp["Predicted Price"].std(), gdp["Predicted Price Spike"].mean()],
    #               },
    #              index=["Average Price", "Volatility", "Spike Probability"])

    summary = pd.DataFrame([[gdp["Base Price"].mean(),"Base Price", "Average"],
                             [gdp["Base Price"].std(),"Base Price","Volatility"],
                             [gdp["Price Spike"].mean(),"Base Price","Spike Probability"],
                             [gdp["Predicted Price"].mean(),"Predicted Price","Average"],
                             [gdp["Predicted Price"].std(),"Predicted Price","Volatility"],
                             [gdp["Predicted Price Spike"].mean(),"Predicted Price","Spike Probability"]
                            ],
                             columns=["Value", "Scenario", "Data"])


    # st.write(summary)

    impact_chart = alt.Chart(summary).mark_bar().encode(
        alt.X('Data:N', title="", axis=alt.Axis(labelAngle=0)),
        alt.Y('Value:Q', axis=alt.Axis(grid=False)),
        xOffset='Scenario:N',

        color =  alt.Color('Scenario',).scale(
                  domain=['Base Price', 'Predicted Price'],
                  range=['blue', 'orange'])).properties(title="Price Impact of Predicted Scenario vs Base Values"
)

    st.altair_chart(impact_chart, use_container_width=True)


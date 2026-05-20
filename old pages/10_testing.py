from datetime import datetime
import streamlit as st
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns
import altair as alt



test = st.slider("testing slider modifiers", 0, 130, 25)



df  = pd.read_csv("Demand.csv")



st.subheader("modified data")

df["demand_dollars"] = df.apply(lambda row: row["demand_dollars"] * test, axis=1)
st.line_chart(df, x="date", y="demand_dollars")








    # fig = px.scatter(solar_demand, x = 'generation_gwh', y = ['net_grid_demand_gwh'], trendline="ols" )
    # st.plotly_chart(fig)

    # px.title('Polynomial Regression: Solar Generation vs Net Grid Demand')
    # px.xlabel('Estimated Solar Generation (GWh)')
    # px.ylabel('Estimated Net Grid Demand (GWh)')
    # px.legend()
    # px.grid(True)
    # px.tight_layout()
    # plt.show()
    # st.pyplot(fig)


#
    # columns = solarprice.columns.tolist()
    #
    # st.subheader("Plotted Data")
    # # solarprice.groupby('year')['pricespike'].mean().plot(title='Frequency of Price Spikes')
    #
    # solarprice['pricevolatility']=np.log(solarprice['price_GWh']).rolling(12).std()
    # solarprice['pricesmooth']=solarprice['price_GWh'].rolling(12).mean()
    # solarprice[['pricevolatility', 'pricesmooth', 'generation_gwh']].plot(subplots=True)
    # # plt.show()
    #
    #
    # x_column = st.selectbox("select x axis", columns, index=0)
    # y_column = st.selectbox("select y axis", columns, index=4)
    # st.line_chart(solarprice.set_index(x_column)[y_column])
    #
    #
    #
    # data=solarprice[['generation_gwh','pricevolatility']].dropna()
    # genprice = smf.ols(formula='pricevolatility ~ generation_gwh + I(generation_gwh**2)', data=data).fit()
    #
    # # plt.scatter(data.generation_gwh, data.pricevolatility, s=20, alpha=0.6
    # st.scatter_chart(
    #     data,
    #     x = 'generation_gwh',
    #     y = 'pricevolatility',
    #
    # )
    # # plt.xlabel('Rooftop Solar Generation (GWh)'); plt.ylabel('Wholesale Price Volatility')
    #
    # xsorted = np.linspace(data['generation_gwh'].min(),data['generation_gwh'].max(),100)
    #
    # ypred = genprice.predict({'generation_gwh': xsorted})
    #
    # plt.plot(xsorted,ypred,'b-',label='Quadratic $R^2$ = %.2f' % genprice.rsquared,alpha=0.9)
    #
    # plt.legend(loc='upper left', framealpha=0.5, prop={'size':'small'})
    # plt.title("Price Volatility v's Rooftop Solar Generation", fontsize=14)
    # plt.show()
    #
    #
    # genprice.summary()









# x = solar_demand[['generation_gwh']]
# y = solar_demand['net_grid_demand_gwh']
#
# x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)
#
# solar_demand_model = LinearRegression()
# solar_demand_model.fit(x_train, y_train)
#
# solar_demand_predictions = solar_demand_model.predict(x_test)
#
# solar_demand_mae = mean_absolute_error(y_test, solar_demand_predictions)
# solar_demand_r2 = r2_score(y_test, solar_demand_predictions)
# solar_demand_rmse = np.sqrt(mean_squared_error(y_test, solar_demand_predictions))
#
# st.write("Mean Absolute Error:", solar_demand_mae)
# st.write("R-squared:", solar_demand_r2)
# st.write("RMSE:", solar_demand_rmse)
# st.write("Coefficient:", solar_demand_model.coef_[0])

# plt.figure(figsize=(10, 6))
#
# plt.scatter(solar_demand['generation_gwh'], solar_demand['net_grid_demand_gwh'], s=20, alpha=0.5)
#
# x = pd.DataFrame({'generation_gwh': np.linspace(solar_demand['generation_gwh'].min(),
#                                                 solar_demand['generation_gwh'].max(),
#                                                 len(solar_demand['generation_gwh']))})
#
# poly_1 = smf.ols(formula='net_grid_demand_gwh ~ 1 + generation_gwh', data=solar_demand).fit()
# plt.plot(x['generation_gwh'], poly_1.predict(x), 'b-', label='Poly n=1 R2=%.3f' % poly_1.rsquared, alpha=0.9)
#
# poly_2 = smf.ols(formula='net_grid_demand_gwh ~ 1 + generation_gwh + I(generation_gwh ** 2.0)',
#                  data=solar_demand).fit()
# plt.plot(x['generation_gwh'], poly_2.predict(x), 'g-', label='Poly n=2 R2=%.3f' % poly_2.rsquared, alpha=0.9)
#
# poly_3 = smf.ols(
#     formula='net_grid_demand_gwh ~ 1 + generation_gwh + I(generation_gwh ** 2.0) + I(generation_gwh ** 3.0)',
#     data=solar_demand).fit()
#
# plt.plot(x['generation_gwh'], poly_3.predict(x), 'r-', label='Poly n=3 R2=%.3f' % poly_3.rsquared, alpha=0.9)
#
# plt.title('Polynomial Regression: Solar Generation vs Net Grid Demand')
# plt.xlabel('Estimated Solar Generation (GWh)')
# plt.ylabel('Estimated Net Grid Demand (GWh)')
# plt.legend()
# plt.grid(True)
# plt.tight_layout()
# # plt.show()
# st.pyplot(plt)
#
#
# x["poly1"] = poly_1.predict(x)
# x["poly2"] = poly_2.predict(x)
# x["poly3"] = poly_3.predict(x)
#
#
# st.write(x)


# #REGRESSION MODEL NET DEMAND AND GENERATION
#
#
# x = pd.DataFrame({'generation_gwh': np.linspace(solar_demand['generation_gwh'].min(),
#                                                 solar_demand['generation_gwh'].max(),
#                                                 len(solar_demand['generation_gwh']))})
#
# poly_1 = smf.ols(formula='net_grid_demand_gwh ~ 1 + generation_gwh', data=solar_demand).fit()
# poly_2 = smf.ols(formula='net_grid_demand_gwh ~ 1 + generation_gwh + I(generation_gwh ** 2.0)',
#                  data=solar_demand).fit()
# poly_3 = smf.ols(
#     formula='net_grid_demand_gwh ~ 1 + generation_gwh + I(generation_gwh ** 2.0) + I(generation_gwh ** 3.0)',
#     data=solar_demand).fit()
#
# x["poly1"] = poly_1.predict(x)
# x["poly2"] = poly_2.predict(x)
# x["poly3"] = poly_3.predict(x)
#
#
#
# chart = alt.Chart(solar_demand).mark_circle().encode(
#     x='generation_gwh',
#     y=alt.Y('net_grid_demand_gwh').scale(zero = False),
#
#     ).interactive()
# #x
# # st.write(x.columns)
#
#
# poly_1_line = alt.Chart(x).mark_line(color='blue',point = "transparent" , tooltip = True).encode(
#     x = 'generation_gwh',
#
#     y = alt.Y('poly1').scale(zero = False)).interactive()
#
#
# poly_2_line = alt.Chart(x).mark_line(color='green').encode(
#     x = 'generation_gwh',
#
#     y = alt.Y('poly2').scale(zero = False))
#
# poly_3_line = alt.Chart(x).mark_line(color='red').encode(
#     x = 'generation_gwh',
#
#     y = alt.Y('poly3').scale(zero = False))
#
# joined = chart + poly_1_line + poly_2_line + poly_3_line
#
# joined.properties(title="Polynomial Regression: Solar Generation vs Net Grid Demand")
# st.altair_chart(joined, theme=None, use_container_width=True)





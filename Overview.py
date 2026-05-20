import streamlit as st


# set up pages

st.set_page_config(
    page_title="Overview",
    layout="wide",

)


# st.write("""
# # My first app
# Hello *world!*
# """)
# df = pd.read_excel("wine_data.xls")
#
# st.line_chart(df)


st.title("The Impact of Rooftop Solar on Electricity Demand and Pricing in New Zealand")
# st.sidebar.success("Impact of Rooftop Solar on Electricity Demand and Pricing")

st.write("""
Rooftop solar reduces net demand on the electricity grid during daylight hours altering demand profiles. It also impacts wholesale pricing, and market volatility. The electricity industry has identified solar generation as a driver of changing electricity demand patterns, rather than simply a reduction in total energy consumption.
Understanding how increasing rooftop solar generation affects supply–demand dynamics and price behaviour is a critical driver for the electricity industry.  
""")



#
# uploaded_file = st.file_uploader("Choose a file",
# type="csv")
#
# if uploaded_file is not None:
#     st.write("file uploaded")
#     df  = pd.read_csv(uploaded_file)
#
#     st.subheader("Preview")
#     st.write(df.head())
#
#     st.subheader("Data Summary")
#     st.write(df.describe())
#
#     st.subheader("Filter Data")
#     columns = df.columns.tolist()
#     selected_column = st.selectbox("select a column", columns)
#
#     unique_values = df[selected_column].unique()
#     selected_value = st.selectbox("select a value", unique_values)
#
#     filted_df = df[df[selected_column] == selected_value]
#     st.write(filted_df)
#
#     st.subheader("Plotted Data")
#     x_column = st.selectbox("select x axis", columns)
#     y_column = st.selectbox("select y axis", columns)
#
#     if st.button("Plot"):
#         st.line_chart(df.set_index(x_column)[y_column])
#
#
#
#         sns.lineplot(data=df, x=x_column, y=y_column)
#         plt.xlabel(x_column)
#         plt.ylabel(y_column)
#         st.pyplot(plt.gcf())
#
#         # chart = (
#         #     alt.Chart(df)
#         #     .mark_circle()
#         #     .encode(x=x_column, y=y_column,  tooltip=[x_column, y_column])
#         # )
#
#         chart = (
#             alt.Chart(df).mark_line().encode(
#             x=x_column ,
#             y=alt.Y(y_column, type='quantitative'),
#             color='symbol:N',
#             ))
#         st.altair_chart(chart)
#
#
#
#
#     else:
#         st.warning("waiting on file upload...")
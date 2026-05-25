import streamlit as st


# set up pages

st.set_page_config(
    page_title="Overview",
    layout="wide",

)



st.title("The Impact of Rooftop Solar on Electricity Demand and Pricing in New Zealand")

st.write("""
Rooftop solar reduces net demand on the electricity grid during daylight hours altering demand profiles. It also impacts wholesale pricing, and market volatility. The electricity industry has identified solar generation as a driver of changing electricity demand patterns, rather than simply a reduction in total energy consumption.
Understanding how increasing rooftop solar generation affects supply–demand dynamics and price behaviour is a critical driver for the electricity industry.  
""")


st.image("Datafiles/SolarPanel2.png", caption="Image Designed by Magnific", width="stretch", use_column_width=None, clamp=False, link ="https://www.magnific.com/free-psd/clean-energy-solar-panel-array-powering-sustainable-future_407748312.htm#fromView=keyword&page=1&position=1&uuid=c005b1cf-5574-4194-aaec-f0b29670ddf5&query=Solar+panel" )



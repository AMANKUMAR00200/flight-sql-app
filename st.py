import streamlit as st
import pandas as pd
from dbhelper import DB
import plotly.express as px
import plotly.graph_objects as go

st.sidebar.title("Flight Insights ")

db = DB()

st.set_page_config(
    page_title="Flight Analytics Dashboard",
    page_icon="✈️",
    layout="wide"
)


user_option = st.sidebar.selectbox("Menu",['Route & Traffic Analysis','Price Analysis',
                             'Analytics'])

if user_option == 'Route & Traffic Analysis':

    st.title('Route & Traffic Analysis')

    col1, col2 = st.columns(2)
    with col1:
        source = db.fetch_source()
        source = st.selectbox('Source', sorted(source))

    with col2:
        destination = db.fetch_destination()
        destination = st.selectbox('Destination', sorted(destination))

    if st.button("🔍 Search Flights", use_container_width=True):

        flights = db.fetch_all_flight(source, destination)

        if len(flights) == 0:
            st.error(f"❌ No flights available between {source} and {destination}.")
            st.info("Please select a different source or destination.")
        else:
            st.success(f"✅ {len(flights)} flight(s) found.")
            df = pd.DataFrame(
                flights,
                columns=[
                    "Airline", "Date_of_Journey", "Source", "Destination",
                    "Route",
                     "Price"
                ]
            )

            st.dataframe(df, use_container_width=True)











elif user_option == 'Price Analysis':
    st.title('Price Analysis')
    airline = db.fetch_airline()
    airline = st.selectbox('Airline', sorted(airline))

    col1, col2 = st.columns(2)
    with col1:
        source = db.fetch_source()
        source = st.selectbox('Source', source)
    with col2:
        destination = db.fetch_destination()
        destination = st.selectbox("Destination", destination)

    import pandas as pd

    date ,price = db.date_vs_price(source, destination, airline)


    if not date and not price:
        st.warning("❌ No flights available for the selected route.")
    else:


        fig = px.line(

            x=date,
            y=price,
            markers=True,
            title=f"{airline} Price Analysis"
        )

        st.plotly_chart(fig, use_container_width=True)







elif user_option == 'Analytics':
    st.title('Flight Analytics')
    c1, c2, c3, c4 = st.columns(4)

    total_flight = db.total_flight()
    c1.metric("✈️ Total Flights", total_flight)

    total_airlines, total_cities, avg_price = db.dashboard_kpis()
    c2.metric("🏙 Cities", total_cities)
    c3.metric("🛫 Airlines", total_airlines)
    c4.metric("💰 Avg Price", f"₹ {avg_price}")

    airline, frequency = db.fetch_airline_frequency()
    fig = go.Figure(
        go.Pie(
            labels=airline,
            values=frequency,
            hoverinfo="label+percent",
            textinfo="value"
        ))

    st.subheader("✈️ Flights by Airline")
    st.plotly_chart(fig)


    st.subheader('📍 Flights by Source City')
    city, frequency1 = db.busy_airport()
    fig = px.bar(
        x=city,
        y=frequency1
    )

    st.plotly_chart(fig, theme="streamlit", use_container_width=True)





st.markdown("---")
st.caption("Developed by Raushan Kumar | NIT Jamshedpur | Flight Analytics Dashboard")





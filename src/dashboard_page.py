import streamlit as st 
import pandas as pd
import matplotlib.pyplot as plt

from data_retrieval import Data_Retrieval

@st.cache_data
def load_all_data():
    database_location = "sqlite:///../my_played_tracks.sqlite"
    sql_obj = Data_Retrieval(database_location)
    df = sql_obj.sql_statement('select * from my_played_tracks')
    return df

df = load_all_data()

def show_explore_page():
    st.title("My Spotify Dashboard")

    st.markdown("This dashboard will help you get more information about the my spotify actvities")
    
    # -- Get the user input
    year_col, continent_col, log_x_col = st.columns([5, 5, 5])
    with year_col:
        year_choice = st.slider(
            "Date",
            min_value=1952,
            max_value=2007,
            step=5,
            value=2007,
        )
    with continent_col:
        continent_choice = st.selectbox(
            "What continent would you like to look at?",
            ("All", "Asia", "Europe", "Africa", "Americas", "Oceania"),
        )
    with log_x_col:
        log_x_choice = st.checkbox("Log X Axis?")

    data = df["song_name"].value_counts()

    fig1, ax1 = plt.subplots()
    ax1.pie(data, labels=data.index, autopct="%1.1f%%", shadow=True, startangle=90)
    # equal ensures that pie chart is drawn as a circle
    ax1.axis("equal")      

    st.write("""#### Number of Data from different countries""") 

    st.pyplot(fig1)

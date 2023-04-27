import streamlit as st 
import pandas as pd
import matplotlib.pyplot as plt

from data_retrieval import Data_Retrieval

@st.cache_data
def load_data(sql_statement):
    database_location = "sqlite:///../my_played_tracks.sqlite"
    sql_obj = Data_Retrieval(database_location)
    df = sql_obj.sql_statement(sql_statement)
    return df

def songs_by_artist():
    sql_songs_by_artist = "SELECT artist_name, COUNT(artist_name) AS 'Number of Songs' FROM my_played_tracks GROUP BY artist_name ORDER BY COUNT(artist_name) DESC LIMIT 5"
    result_df = load_data(sql_songs_by_artist)
    return result_df

def songs_by_timestamp():
    sql_songs_by_timestamp = "SELECT timestamp, COUNT(timestamp) AS 'Number of Songs' FROM my_played_tracks GROUP BY timestamp ORDER BY COUNT(timestamp) DESC LIMIT 5"
    result_df = load_data(sql_songs_by_timestamp)
    return result_df

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

    # data = df["song_name"].value_counts()

    # fig1, ax1 = plt.subplots()
    # ax1.pie(data, labels=data.index, autopct="%1.1f%%", shadow=True, startangle=90)
    # # equal ensures that pie chart is drawn as a circle
    # ax1.axis("equal")      

    # st.write("""#### Number of Data from different countries""") 

    # st.pyplot(fig1)

    # Group data by timestamp and count the number of songs played
    st.write("""#### Number of songs played""") 
    st.line_chart(data=songs_by_timestamp(), x ='timestamp', y ='Number of Songs')

    # Group data by artist and count the number of songs played
    st.write("""#### Number of songs played by artist""") 
    st.bar_chart(data=songs_by_artist(), y ='Number of Songs', x='artist_name')

import sqlalchemy
import sqlite3
import pandas as pd

class Data_Retrieval(object):
    def __init__(self, database_location):
        self.database_location = database_location
        self.engine = sqlalchemy.create_engine(self.database_location)
        self.conn = sqlite3.connect('my_played_tracks.sqlite')

    def retrieve_data(self, sql_statement):
        test = pd.read_sql(sql_statement, self.engine)
        self.conn.close()
        print("Close database successfully")
        return test

    # Create a sql statement that retrieve all data from the database
    def sql_statement(self, sql_statement):
        result = self.retrieve_data(sql_statement)
        return result

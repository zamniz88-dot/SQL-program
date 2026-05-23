
"""#### **2. Connect with SQLite Database**"""
import sqlite3

database = 'database.sqlite'

conn = sqlite3.connect(database)

print('Opened data successfully')
import pandas as pd
tables = pd.read_sql("""SELECT *
                     FROM sqlite_master
                     WHERE type='table';""", conn)
tables

teams = pd.read_sql("""SELECT *
                         FROM Team;""", conn)
teams

matches = pd.read_sql("""SELECT *
                           FROM Match;""", conn)

"""**Conclusion -**

-12 Numeric features (Integer and Numeric) and 1 categorical feature
(Text)
-3 columns with null values
"""

matches
MI_wins = pd.read_sql("""SELECT *
                        FROM Match
                        WHERE Match_Winner == 7;""", conn)
MI_wins
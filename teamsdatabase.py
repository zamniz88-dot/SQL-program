
import sqlite3

database = 'database.sqlite'

conn = sqlite3.connect(database)
print('Opened data successfully')

import pandas as pd
tables = pd.read_sql("""SELECT *
                     FROM sqlite_master
                     WHERE type='table';""", conn)
tables

matches = pd.read_sql("""SELECT *
                        FROM Match;""", conn)

matches.head()

"""**Conclusion-**

- 12 Numeric features (Integer and Numeric) and 1 catogorical feature (Text)
- 3 columns with null values
"""

result1 = pd.read_sql("""SELECT AVG(Win_Margin), Match_Winner
                      FROM Match
                      WHERE Season_Id == 9
                      GROUP BY Match_Winner
                      Order BY AVG(Win_Margin);""", conn)
result1
result2 = pd.read_sql("""SELECT COUNT(DISTINCT Venue_Id)
                        FROM Match
                        WHERE Season_Id == 9;""", conn)
result2

result3 = pd.read_sql("""SELECT MIN(Win_Margin), Max(Win_Margin), Avg(Win_Margin),
COUNT(DISTINCT(Man_of_the_Match))
                      FROM Match;""", conn)
result3

result4 = pd.read_sql("""SELECT SUM(Win_Margin)
                        FROM Match
                        WHERE Season_Id == 9;""", conn)
result4
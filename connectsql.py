
"""### **2. Connect with AQLite Dtabase**"""

import sqlite3
datbase = 'datbase.sqlite'

conn = sqlite3.connect(database)
print('Opened data successfully')

import pandas as pd
tables = pd.read_sql("""SELECT *
                     FROM sqlite_master
                     WHERE type='table';""", conn)
tables
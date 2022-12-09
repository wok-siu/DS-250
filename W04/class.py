#%%
import pandas as pd
import sqlite3

# %%
con = sqlite3.connect('lahmansbaseballdb.sqlite')

df = pd.read_sql_query("SELECT * FROM fielding LIMIT 5", con)
df

# %%
df = pd.read_sql_query("""
    SELECT playerID, yearID, teamID, h, er, hr, bb, so
    FROM Pitching  
    WHERE yearid = 1874 AND hr >= 1
    ORDER BY hr
    LIMIT 5
    """, con)
df
# %%

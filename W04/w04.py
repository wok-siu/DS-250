#%%
import pandas as pd
import sqlite3
import altair as alt

# %%
con = sqlite3.connect('lahmansbaseballdb.sqlite')

df = pd.read_sql_query("SELECT * FROM fielding LIMIT 5", con)
df

# %%
df = pd.read_sql_query("""
    SELECT DISTINCT Salaries.playerID, CollegePlaying.schoolID, Salaries.teamID, Salaries.Salary, Salaries.yearID
    FROM Salaries 
    JOIN CollegePlaying ON Salaries.playerID = CollegePlaying.playerID
    WHERE CollegePlaying.schoolID LIKE "%BYUI%"
    ORDER BY salary DESC
    """, con)

df
# %%
df = pd.read_sql_query("""
    SELECT playerid, yearID, (h*1.0)/ab AS "Batting Average"
    FROM batting
    WHERE ab >= 1
    ORDER BY "Batting Average" DESC, playerid 
    LIMIT 5
    """, con)

df
# %%
df = pd.read_sql_query("""
    SELECT playerid, yearID, (h+0.0)/ab AS "Batting Average"
    FROM batting
    WHERE ab >= 10
    ORDER BY "Batting Average" DESC, playerid
    LIMIT 5
    """, con)

df
# %%
df = pd.read_sql_query("""
    SELECT playerid, yearID, SUM(ab) AS totalAB, SUM(h) AS totalH, (SUM(h)+0.0)/SUM(ab) AS "Career Batting Average"
    FROM batting
    GROUP BY playerid
    HAVING SUM(ab) >= 100
    ORDER BY "Career Batting Average" DESC
    LIMIT 5
    """, con)

df
# %%
compare = pd.read_sql_query("""
    SELECT teamID, w
    FROM Pitching
    ORDER BY w DESC
    LIMIT 2
    """, con)

compare

# %%
chart = (alt.Chart(compare, title = "Team Comparison")
        .encode(
            x = alt.Y("teamID", title = "Teams"),
            y = alt.X("W", title = "Wins"),
            color = alt.Color("teamID", title = "Teams")
        ).mark_bar()
)

chart
# %%

#%%
import pandas as pd
import altair as alt
import datetime as dt

#%% load data
url = "https://github.com/byuidatascience/data4names/raw/master/data-raw/names_year/names_year.csv"
names = pd.read_csv(url, parse_dates=['year'])

# %%
## My name
name = names.query("name == 'Duane'")

# %%
## Graph of my name
chart = (alt.Chart(name)
        .encode(
            x = "year",
            y = "Total",
            color = alt.Color("name")
        ).mark_line()
)
chart
# %%
## Brittany appearnace
name = (names
    .query("name == 'Brittany'")
    .assign(Age=lambda name:2022 - name['year'].dt.year)
)

#%%
chart = (
    alt.Chart(name)
    .encode(
        x = "Age",
        y = "Total",
        color = alt.Color("name")
    ).mark_line()
)
chart
# %%
## Mary, Martha, Peter, and Paul
name = (names
    .query("name == ['Mary', 'Martha', 'Peter', 'Paul']")
    .query("year >= 1920 & year <= 2000")
)

chart = (alt.Chart(name)
        .encode(
            x = "year",
            y = "Total",
            color = alt.Color("name")
        ).mark_line()
)
chart


# %%
mary = (names
    .query('name == "Mary"')
)
martha = (names
    .query('name == "Martha"')
)
peter = (names
    .query('name == "Peter"')
)
paul = (names
    .query('name == "Paul"')
)

mary_chart = (alt.Chart(mary)
        .mark.line("red")
        .encode(
            x = "year",
            y = "Total"
        )
)

martha_chart = (alt.Chart(martha)
        .mark.line("orange")
        .encode(
            x = "year",
            y = "Total"
        )
)

peter_chart = (alt.Chart(peter)
        .mark.line("green")
        .encode(
            x = "year",
            y = "Total"
        )
)

paul_chart = (alt.Chart(paul)
        .mark.line("blue")
        .encode(
            x = "year",
            y = "Total"
        )
)

mary_chart + martha_chart + peter_chart + paul_chart
# %%
## Star Wars: |Anakin| = Vader!
name = (names
    .query("name == 'Anakin'")
)

chart = (alt.Chart(name)
    .mark_line()
    .encode(
        x = "year",
        y = "Total",
        color = alt.Color("name")
    )
)
 
movie_release = names.query("name == 'Anakin' & year == '2005'")

chart1 = (alt.Chart(movie_release)
    .mark_rule(color='red')
    .encode(
        x = "year"
    )
)
chart + chart1
# %%

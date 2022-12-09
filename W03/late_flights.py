#%%
import pandas as pd
import altair as alt
import numpy as np

#%% load data
url = "https://github.com/byuidatascience/data4missing/raw/master/data-raw/flights_missing/flights_missing.json"
flights = pd.read_json(url)
flights['time_hour'] = pd.to_datetime(flights.time_hour, format = "%Y-%m-%d %H:%M:%S")
flights.fillna(0)

#%%
flights.head()

# %%
flights.airport_name.unique()

# %%
## 
airport = (flights
    .query("airport_name")
)
chart = (alt.Chart(airport)
        .encode(
            x = "month",
            y = "minutes_delayed_total",
            color = alt.Color("airport")
        ).mark_line()
)
chart
# %%
flights.info()

# %%



#%%
import pandas as pd
import numpy as np
import altair as alt

#%%
url = "https://github.com/byuidatascience/data4python4ds/raw/master/data-raw/mpg/mpg.csv"
mpg = pd.read_csv(url)

# %%
mpg.head()

# %%
chart = (alt.Chart(mpg)
  .encode(
    x='cty', 
    y='hwy',
    color = "displ")
  .mark_circle()
)
chart


# %%
# Filter out columns
print(mpg
  .head(5)
  .filter(["manufacturer", "model","year", "hwy"])
  .to_markdown(index=False))
# %%

#%%
import pandas as pd
import altair as alt
import numpy as np

#%% load data
cars = pd.read_json("mtcars_missing.json")

# %%
cars.head()

# %%
cars = cars.replace(["", 999], np.nan, inplace=True)

cars
# %%
cars1 = (cars
    .query('cyl == 4')
    )
cars1["wt"].mean()
# %%
cars2 = (cars
    .query('cyl == 6')
    )
cars2["wt"].mean()

#%%
cars3 = (cars
    .query('cyl == 8')
    )
cars3["wt"].mean()
cars = (cars
    .dropna(subset = ["wt", "cyl"])
    .groupby("cyl")
    .mean()
)

cars
# %%
hp_mean = cars.hp.mean()

cars.hp.replace(np.nan, hp_mean, inplace=True)

cars
# %%

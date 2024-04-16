import pandas as pd
import matplotlib.pylab as plt

headers = ["symboling","normalized-losses","make","fuel-type","aspiration", "num-of-doors","body-style",
         "drive-wheels","engine-location","wheel-base", "length","width","height","curb-weight","engine-type",
         "num-of-cylinders", "engine-size","fuel-system","bore","stroke","compression-ratio","horsepower",
         "peak-rpm","city-mpg","highway-mpg","price"]

df = pd.read_csv('auto.csv', names = headers)
df

import numpy as np
df.replace("?", np.nan, inplace = True)
df

df.info()

# REMOVE NAN

df.dropna(subset=["price"], axis=0, inplace=True)

# reset index, because we droped two rows
df.reset_index(drop=True, inplace=True)

df['normalized-losses'] = pd.to_numeric(df['normalized-losses'], errors='coerce')
mean1 = df['normalized-losses'].mean()
df["normalized-losses"]=df['normalized-losses'].fillna(mean1)

df['horsepower'] = pd.to_numeric(df['horsepower'], errors='coerce')
mean_horsepower = df['horsepower'].mean()
df['horsepower'] = df['horsepower'].fillna(mean_horsepower)


df['bore'] = pd.to_numeric(df['bore'], errors='coerce')
mean_bore = df['bore'].mean()
df['bore'] = df['bore'].fillna(mean_bore)

df['stroke'] = pd.to_numeric(df['stroke'], errors='coerce')
stroke = df['stroke'].mean()
df['stroke'] = df['stroke'].fillna(stroke)




df['peak-rpm'] = pd.to_numeric(df['peak-rpm'], errors='coerce')
peak = df['peak-rpm'].mean()
df['peak-rpm'] = df['peak-rpm'].fillna(peak)

#df['num-of-doors'] = pd.to_numeric(df['num-of-doors'], errors='coerce')
mean_col2 = df['num-of-doors'].mode()[0]
df['num-of-doors'] = df['num-of-doors'].fillna(mean_col2)

df.info()

bins = np.linspace(min(df["horsepower"]), max(df["horsepower"]), 4)
bins
group_names = ['Low', 'Medium', 'High']
df['horsepower-binned'] = pd.cut(df['horsepower'], bins, labels=group_names, include_lowest=True )
df[['horsepower','horsepower-binned']].head(20)

df.head()

import pandas as pd
import numpy as np

df = pd.read_csv("https://raw.githubusercontent.com/thecodinguru/lambdata/master/lambdata/data/GlobalTemperatures.csv")

from lambdata import wrangle

df2 = wrangle(df)

print(df2.head())
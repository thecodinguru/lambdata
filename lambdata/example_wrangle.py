import pandas as pd
import numpy as np

url = "https://raw.githubusercontent.com/thecodinguru/lambdata/master/lambdata/data/GlobalTemperatures.csv"

df = pd.read_csv(url, error_bad_lines=False)
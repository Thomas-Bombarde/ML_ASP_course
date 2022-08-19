
import pandas as pd

FNAME = "http://www.stat.ucla.edu/~rgould/datasets/twins.dat"

df = pd.read_csv(FNAME, delimiter = "\t", na_values="?")

df["AGECB"] = df["AGE"]**3
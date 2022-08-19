
import pandas as pd

FNAME = "http://www.stat.ucla.edu/~rgould/datasets/twins.dat"

df = pd.read_csv(FNAME, sep = "\t", na_values="?")
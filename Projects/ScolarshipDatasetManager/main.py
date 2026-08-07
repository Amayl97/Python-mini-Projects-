import pandas as pd
from modules.search import search_menu

df = pd.read_csv("data/scholarship.csv")

search_menu(df)


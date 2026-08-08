import pandas as pd
from modules.search import search_menu
from modules.add_scholarship import add_scholarships

df = pd.read_csv("data/scholarship.csv")

# search_menu(df)

df = add_scholarships(df)
df.to_csv("data/scholarship.csv", index=False)

print(df)
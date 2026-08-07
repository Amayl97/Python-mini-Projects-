import pandas as pd

df = pd.read_csv("data/scholarship.csv")

df = df.drop_duplicates()
df = df.fillna("Unkown")

df['Deadline'] = pd.to_datetime(df['Deadline'])
df['Country'] = df["Country"].str.strip()

print(df)

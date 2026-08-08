import pandas as pd

def clean_data(df):
 df = df.drop_duplicates()
 df = df.fillna("Unkown")

 df['Deadline'] = pd.to_datetime(df['Deadline'])
 df['Country'] = df["Country"].str.strip()

 print(df)

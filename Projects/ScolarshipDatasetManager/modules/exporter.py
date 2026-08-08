import pandas as pd


def save_csv(df, filename):
    df.to_csv(filename, index=False)
    
    print("Dataset saved successfully.")



def save_json(df, filename):
    df.to_json(filename, orient="records", indent=4)
    print("Dataset saved as JSON")
    



import pandas as pd


def delete_scholarship(df):
    name = input("Enter scholarship name to delete: ")
    matches = df[df["Name"].str.contains(name, case=False, na=False)]

    if matches.empty:
        print("Scholarships are not found!")
        return
    print("\nMatching scholarships:")
    print(matches[["Name", "Country", "Degree"]])
    confirm = input("Are you sure you want to delete it(y/n):")
    if confirm.lower() == 'y':
        df = df[~df['Name'].str.contains(name, case=False, na=False)]
        print("Scholarship deleted successfully!")
        print(df)
    else:
        print("Deletion canceled!")



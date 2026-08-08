import pandas as pd

df = pd.read_csv("data/scholarship.csv")

def sort_scholarships(df, column, ascending=True): 
  if column == "Deadline":
    df[column] = pd.to_datetime(df[column])
    sort_by_date = df.sort_values(by=column)
    print(sort_by_date)
  else:
    sorted_df = df.sort_values(by=column, ascending=ascending)
    print(sorted_df)

def sort_menu(df):
    print("\nSort Scholarships")
    print("1. Deadline")
    print("2. Country")
    print("3. CGPA")

    choice = input("Choose:")
    if choice == "1":
       sort_scholarships(df, "Deadline")
    elif choice == "2":
       sort_scholarships(df,"Country")
    elif choice == "3":
       sort_scholarships(df, "CGPA")
    else:
       print("Invalid choice")


sort_menu(df);


import pandas as pd

df = pd.read_csv("data/scholarship.csv")
def update_scholarship(df):
    name = input("Enter name of sccholarship you want to update:")
    matches = df[df['Name'].str.contains(name, case=False, na=False)]
    if matches.empty:
        return
    index = matches.index[0]
    print("\nWhat do you want to update?")
    print("1. Deadline")
    print("2. CGPA")
    print("3. Fully Funded")
    print("4. Field")

    choice = input("Choose:")
    if choice == "1":
        new_deadline = input("Enter new deadline:")
        df.loc[index, 'Deadline'] = new_deadline
    elif choice == "2":
        new_CGPA = float(input("Enter updated CGPA:"))
        df.loc[index, 'CGPA'] = new_CGPA
    elif choice == "3":
        new_fund = input("Enter update about fund:")
        df.loc[index, 'Fully Funded'] = new_fund
    elif choice == "4":
        new_field = input("Enter new field:")
        df.loc[index, 'Field'] = new_field
    else:
        print("Invalid choice")
    print(df)

update_scholarship(df)

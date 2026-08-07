import pandas as pd


def search_scholarship(df, column):
   search = input(f"Enter {column} of scholarship: ")
   result = df[df[f"{column}"].str.contains(search, case=False, na=False)]
   if result.empty:
    print("No scholarship found")
   else:
    print(result)


def search_menu(df):
    print("1. Search by Name")
    print("2. Search by Country")
    print("3. Search by Degree")
    print("4. Search by Field")

    choice = input("Choose an option: ")
    if choice == "1":
      search_scholarship(df, "Name")
    elif choice == "2":
      search_scholarship(df, "Country")
    elif choice == "3":
      search_scholarship(df, "Degree")
    elif choice == "4":
       search_scholarship(df, "Field")
    else:
       print("Invalid choice")





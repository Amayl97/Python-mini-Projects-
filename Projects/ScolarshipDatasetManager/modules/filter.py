import pandas as pd


def filter_scholarships(df, column):
    value = input(f"Enter {column}: ")
    filtered = df[df[column].astype(str).str.lower() == value.lower()]
    if filtered.empty:
        print("No scholarship found.")
    else:
        print(filtered)


def filter_by_cgpa(df):
    cgpa = float(input("Enter minimum cgpa: "))
    filtered = df[df['CGPA'] <= cgpa]
    if filtered.empty:
        print("No scholarship found.")
    else:
        print(filtered)

def filter_menu(df):

    print("\nFilter Scholarships")
    print("1. Country")
    print("2. Degree")
    print("3. Fully Funded")
    print("4. Field")
    print("5. Maximum CGPA")

    choice = input("Choose: ")

    if choice == "1":
        filter_scholarships(df, "Country")

    elif choice == "2":
        filter_scholarships(df, "Degree")

    elif choice == "3":
        filter_scholarships(df, "FullyFunded")

    elif choice == "4":
        filter_scholarships(df, "Field")

    elif choice == "5":
        filter_by_cgpa(df)

    else:
        print("Invalid choice.")


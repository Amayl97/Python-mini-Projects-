import pandas as pd


def add_scholarships(df):
    print("\nAdd New Scholarship")

    name = input("Name: ")
    country = input("Country: ")
    degree = input("Degree: ")
    deadline = input("Deadline (YYYY-MM-DD): ")
    cgpa = float(input("Minimum CGPA: "))
    funded = input("Fully Funded (Yes/No): ")
    field = input("Field: ")

    new_scholarship = {
        "Name" :name,
        "Country": country,
        "Degree": degree,
        "Deadline": deadline,
        "CGPA": cgpa,
        "FullyFunded": funded,
        "Field": field
    }

    df.loc[len(df)] = new_scholarship
    print("\nScholarship added successfully!")

    return df

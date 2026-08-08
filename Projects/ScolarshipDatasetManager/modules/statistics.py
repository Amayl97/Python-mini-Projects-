import pandas as pd

df = pd.read_csv("data/scholarship.csv")

def calculate_stats(df):
    total_scholarships = len(df)
    fully_funded = (df["FullyFunded"].astype(str).str.lower().eq('yes').sum())
    partial_funded = (df["FullyFunded"].astype(str).str.lower().eq('partial').sum())
    average_cgpa = df['CGPA'].mean()
    country_count = df['Country'].value_counts()
    print("\n========== Statistics ==========")

    print(f"\nTotal Scholarships: {total_scholarships}")

    print(f"Fully Funded: {fully_funded}")

    print(f"Partial Funding: {partial_funded}")

    print(f"Average Minimum CGPA: {average_cgpa:.2f}")

    print("\nScholarships by Country:")
    print(country_count)

calculate_stats(df)    

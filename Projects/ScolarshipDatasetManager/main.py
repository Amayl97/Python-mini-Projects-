import pandas as pd
from modules.search import search_menu
from modules.add_scholarship import add_scholarships
from modules.exporter import save_csv, save_json
from modules.cleaner import clean_data
from modules.filter import filter_menu
from modules.sort import sort_menu
from modules.statistics import calculate_stats
from modules.update import update_scholarship
from modules.delete import delete_scholarship

df = pd.read_csv("data/scholarship.csv")

print("What do you want to do?")
print("1. Search")
print("2. Adding scholarship")
print("3. Cleaning of data")
print("4. Apply filters")
print("5. Sort")
print("6. Stats")
print("7. Update")
print("8. Export")
print("9. Delete")

choice = input("Choose:")


if choice == "1":
  search_menu(df)
elif choice == "2":
  add_scholarships(df)
elif choice == "3":
  clean_data(df)
elif choice == "4":
  filter_menu(df)
elif choice == "5":
  sort_menu(df)
elif choice == "6":
  calculate_stats(df)   
elif choice == "7":
  update_scholarship(df)
elif choice == "8":
  save_csv(df,"data/cleaned_scholarships.csv")
  save_json(df, "data/scholarships.json")
elif choice == "9":
  delete_scholarship(df)
else:
  print("Invalid choice")

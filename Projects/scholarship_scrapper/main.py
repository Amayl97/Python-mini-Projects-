from scrapper.website1 import scrape_snu
import json
import pandas as pd

scholarships = scrape_snu()

with open("data/scholarships.json", "w", encoding="utf-8") as file:
    json.dump(scholarships, file, indent=4, ensure_ascii=False)

df = pd.DataFrame(scholarships)

df.to_csv("Data/scholarships.csv", index=False)


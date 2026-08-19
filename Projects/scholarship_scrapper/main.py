from scrapper.website1 import scrape_snu
from scrapper.website2 import scrape_GKS
import json
import pandas as pd

# scholarship_snu = scrape_snu()


# with open("data/scholarships.json", "w", encoding="utf-8") as file:
#     json.dump(scholarships, file, indent=4, ensure_ascii=False)

# df = pd.DataFrame(scholarship_snu)

# df.to_csv("Data/scholarships.csv", index=False)

scholarship_gks = scrape_GKS()
with open("data/scholarship_gks.html", "w", encoding="utf-8") as file:
    file.write(scholarship_gks)

import requests
from bs4 import BeautifulSoup

url = "https://scholarshipscorner.website/global-korea-scholarship/"

response = requests.get(url)

soup = BeautifulSoup(response.text,"html.parser")

# with open("./data/scholarship_corner_gks.html", "w", encoding="utf-8") as file:
#      file.write(response.text)
# print("File created successfully✨🌷")

# Just for readability
print("===============================================")
# First Display the title of scholarship
title = soup.find("h1")
title = title.text
print(title)

headings = soup.find_all("h3")

wanted_headings = [
    "Host Country:",
    "Course Level:",
    "GKS Scholarship Duration:",
    "Benefits of the Korean Government Scholarship 2026:",
    "Eligibility Criteria of Global Korea Scholarship 2026 in South Korea:"
]

for heading in soup.find_all("h3"):
    if heading.get_text(strip=True) in wanted_headings:
        print(heading.get_text(strip=True))
        ul = heading.find_next("ul")
        for li in ul:
            print(li.get_text(strip=True))
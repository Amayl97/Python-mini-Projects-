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

for heading in headings:
    print(heading.text)

    ul = heading.find_next("ul")
    print(ul)
    for li in ul.find_all("li"):
        print(li.text)
     
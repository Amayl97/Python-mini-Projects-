# ============================================
# WEB SCRAPING LESSON 1
# Requests + BeautifulSoup + Pandas
# ============================================

# Import requests library
import requests

# Import BeautifulSoup library
from bs4 import BeautifulSoup

# Import pandas library
import pandas as pd


# ============================================
# 1. GET THE WEBSITE
# ============================================

# URL of the website that you want to scrape
url = "https://en.snu.ac.kr/admission/graduate/scholarships/before_application"

# This sends an HTTP request to the website
response = requests.get(url)

# Check whether the request was successful
response.raise_for_status()


# ============================================
# 2. CREATE BEAUTIFULSOUP OBJECT
# ============================================

# response.text contains the HTML returned by the website.
#
# BeautifulSoup converts that HTML into a structure
# that we can search and navigate.

soup = BeautifulSoup(response.text, "html.parser")


# ============================================
# 3. BASIC HTML INFORMATION
# ============================================

# Print the title of the website
print("Website title:")
print(soup.title.get_text(strip=True))


# Find the first <h1> tag
print("\nFirst H1:")
h1 = soup.find("h1")

if h1:
    print(h1.get_text(" ", strip=True))
else:
    print("No H1 found")


# Find ALL <h1> tags
print("\nAll H1 headings:")

headings = soup.find_all("h1")

for heading in headings:
    print(heading.get_text(" ", strip=True))


# ============================================
# 4. CONVERT SCRAPED DATA INTO PANDAS
# ============================================

# Convert the headings into a list of strings first.
# Passing BeautifulSoup Tag objects directly to a
# DataFrame is usually not what we want.

heading_data = [
    heading.get_text(" ", strip=True)
    for heading in headings
]

df = pd.DataFrame(
    heading_data,
    columns=["heading"]
)

print("\nDataFrame:")
print(df)


# ============================================
# 5. SEARCHING BY CLASS
# ============================================

# IMPORTANT:
#
# ".scholarship-card", ".country", ".deadline", etc.
# were examples from our practice HTML.
#
# The SNU page does NOT necessarily contain these
# exact classes.
#
# Therefore, don't expect this to return results:
#
# cards = soup.find_all("div", class_="scholarship-card")


# Instead, first inspect the classes that actually
# exist on the webpage.

print("\nSome classes found on the page:")

elements_with_class = soup.find_all(class_=True)

for element in elements_with_class[:20]:
    print(element.get("class"))


# ============================================
# 6. GETTING LINKS
# ============================================

print("\nLinks:")

links = soup.find_all("a")

for link in links:

    # Get the visible text of the link
    text = link.get_text(" ", strip=True)

    # Get the href attribute
    href = link.get("href")

    print("Text:", text)
    print("URL:", href)
    print("---")


# ============================================
# 7. CSS SELECTORS
# ============================================

# CSS selectors allow us to search HTML using
# familiar CSS-style syntax.

# Element selector
print("\nH2 elements:")
print(soup.select("h2"))


# Class selector
#
# This only works if the website actually has
# elements with this class.
#
# Example:
# soup.select(".scholarship-card")


# ID selector
#
# This only works if an element has id="scholarships".
#
# Example:
# soup.select("#scholarships")


# Nested selector
#
# Example:
# soup.select(".scholarship-card h2")


# Select one element
#
# Example:
# soup.select_one(".scholarship-card")


# ============================================
# 8. HANDLING MISSING ELEMENTS
# ============================================

# This is an important pattern for real scrapers.

# Example:

# card = soup.find("div", class_="scholarship-card")

# if card:
#
#     deadline_card = card.find(
#         "p",
#         class_="deadline"
#     )
#
#     if deadline_card:
#         deadline = deadline_card.get_text(
#             " ",
#             strip=True
#         )
#     else:
#         deadline = None
#
#     print(deadline)


# ============================================
# 9. SCRAPING TABLES
# ============================================

# A webpage may contain <table>, <tr>, <th>, and <td>
# elements.
#
# However, the SNU page you're practicing on does not
# appear to expose the scholarship information as a
# normal HTML <table>.
#
# So DON'T do this blindly:
#
# table = soup.find("table")
# rows = table.find_all("tr")
#
# Because if no table exists:
#
# table == None
#
# and this will crash:
#
# table.find_all("tr")


# Instead, always check first:

table = soup.find("table")

if table:

    print("\nTable found!")

    rows = table.find_all("tr")

    for row in rows:

        cells = row.find_all(["th", "td"])

        data = [
            cell.get_text(" ", strip=True)
            for cell in cells
        ]

        print(data)

else:

    print("\nNo HTML table found on this page.")


# ============================================
# END
# ============================================


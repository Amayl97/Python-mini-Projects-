import requests
from bs4 import BeautifulSoup

def scrape_snu():
    url = "https://en.snu.ac.kr/admission/graduate/scholarships/before_application"

    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    
    # headings = soup.find_all(["h1", "h2", "h3","h4"])
    # for heading in headings:
    #     print(heading.get_text(strip=True))

    # This get the text when we don't know the tag
    # scholarship = soup.find(string=lambda text: "SNU President Fellowship Program (SPF)" in text)
    # print(scholarship)
    #This gives us the tag and structure of the text
    # print(scholarship.parent)
    # Now extract al the headings of scholarships
    # scholarships = soup.find_all("h2", class_="common-contitle")
    # for scholarship in scholarships:
    #     print(scholarship.get_text(strip=True))

    #prettify prints html in a readable formate
    scholarship = soup.find("h2", class_="common-contitle")
    print(scholarship.parent.prettify())

    #Now we have to find the details of scholarships
    sections = scholarship.parent.find_all("div", class_="text-content")
    for section in sections:
      title = section.find("p", class_="title")
      values = section.find("p", class_="dot-list")
      print("\n" + title.get_text(strip=True))
      for value in values:
          print("-", value.get_text(strip=True))

import requests
from bs4 import BeautifulSoup

url = "https://scholarshipscorner.website/global-korea-scholarship/"

def scrape_GKS():
   response = requests.get(url)
   soup = BeautifulSoup(response.text, "html.parser")
   scholarship_gks_info = []
   scholarship_title = soup.find_all("h1")
   scholarship_about = soup.find("div", class_="post-cont")
   print(scholarship_about.find_all("p"))

  
   return response.text
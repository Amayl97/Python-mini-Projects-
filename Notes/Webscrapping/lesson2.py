import requests
from bs4 import BeautifulSoup

url = "https://en.snu.ac.kr/admission/graduate/scholarships/before_application"
response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")

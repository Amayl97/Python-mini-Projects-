import requests
from bs4 import BeautifulSoup


URL = "https://en.snu.ac.kr/admission/graduate/scholarships/before_application"


def scrape_snu():

    response = requests.get(URL)

    soup = BeautifulSoup(response.text, "html.parser")

    scholarships = []

    scholarship_titles = soup.find_all(
        "h2",
        class_="common-contitle"
    )

    key_mapping = {
        "Eligibility  (must be BOTH)": "eligibility",
        "Number of Recipients": "number_of_recipients",
        "Details": "details",
        "Application Period": "application_period",
        "Selection Procedure": "selection_procedure",
        "Contact": "contact"
    }

    for scholarship in scholarship_titles:

        scholarship_data = {
            "title": scholarship.get_text(strip=True),
            "university": "Seoul National University",
            "country": "South Korea",
            "source": "SNU"
        }

        container = scholarship.parent

        sections = container.find_all(
            "div",
            class_="text-content"
        )

        for section in sections:

            title = section.find(
                "p",
                class_="title"
            )

            values = section.find_all(
                "p",
                class_="dot-list"
            )

            section_title = title.get_text(strip=True)

            section_values = [
                value.get_text(strip=True)
                for value in values
            ]

            key = key_mapping.get(section_title)

            if key:
                scholarship_data[key] = section_values

        scholarships.append(scholarship_data)

    return scholarships
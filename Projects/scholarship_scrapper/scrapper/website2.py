import requests
from bs4 import BeautifulSoup


url = "https://scholarshipscorner.website/global-korea-scholarship/"


def scrape_GKS():

    # 1. Get the webpage
    response = requests.get(url)

    # 2. Parse the HTML
    soup = BeautifulSoup(response.text, "html.parser")

    # 3. Get scholarship title
    scholarship_title = soup.find("h1")

    # 4. Create dictionary to store scraped data
    gks_data = {
        "title": scholarship_title.get_text(strip=True),
        "requirements": [],
        "benefits": []
    }

    # 5. Find all h3 headings
    scholarship_details_headings = soup.find_all("h3")

    # 6. Loop through headings
    for heading in scholarship_details_headings:

        heading_text = heading.get_text(strip=True)

        # Extract eligibility/requirements
        if heading_text == "Eligibility Criteria of Global Korea Scholarship 2026 in South Korea:":

            ul = heading.find_next("ul")

            for li in ul.find_all("li"):
                requirement = li.get_text(strip=True)

                gks_data["requirements"].append(requirement)

        # Extract benefits
        elif heading_text == "Benefits of the Korean Government Scholarship 2026:":

            ul = heading.find_next("ul")

            for li in ul.find_all("li"):
                benefit = li.get_text(strip=True)

                gks_data["benefits"].append(benefit)

    return gks_data
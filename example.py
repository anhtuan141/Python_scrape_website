import requests
from bs4 import BeautifulSoup

URL = "https://santruyen.com/doc-ton-truyen-ky-thanh-van-mon.614/"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")

# # Find id
# results = soup.find(id="ResultsContainer")
# #
# # print(results.prettify())
#
# job_elements = results.find_all("div", class_="card-content")
#
# python_jobs = results.find_all(
#     "h2", string=lambda text: "python" in text.lower()
# )
#
# python_job_elements = [
#     h2_element.parent.parent.parent for h2_element in python_jobs
# ]
#
# for job_element in python_job_elements:
#     title_element = job_element.find("h2", class_="title")
#     company_element = job_element.find("h3", class_="company")
#     location_element = job_element.find("p", class_="location")
#     print(title_element.text.strip())
#     print(company_element.text.strip())
#     print(location_element.text.strip())
#     print()
#     links = job_element.find_all("a")
#     for link in links:
#         link_url = link["href"]
#         print(f"Apply here: {link_url}\n")

#Begin Scrape
results = soup.find(id="truyen")

# Scrape story name
story_name = results.find(class_="title")
print(story_name.text)
print()

#

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

# Begin Scrape
results = soup.find(id="truyen")
resultsChapter = soup.find(id="chapter-list")

# Scrape story name
story_name = results.find("h3", class_="title")
print(f"Story name: {story_name.text}")
print()

# Scrape story description
story_description = results.find("div", class_="story-desc")
inner_html = story_description.contents

# Extract description
for element in inner_html:
    print(f"Story description: {element}")

print()

# Scrape chapter list
chapter_list = resultsChapter.find("ul", class_="list-chapter")

# Find all the <a> tags within the <ul> for chapters
chapter_links = chapter_list.find_all("a")

# Extract chapter information
for link in chapter_links:
    chapter_url = link.get("href")
    chapter_title = link.get("title")
    print(f"Chapter Title: {chapter_title}, Chapter URL: {chapter_url}")
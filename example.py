import requests
import pandas
from bs4 import BeautifulSoup

URL = "https://santruyen.com/doc-ton-truyen-ky-thanh-van-mon.614/"


def scrape_story(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")

    # Begin Scrape
    results = soup.find(id="truyen")
    resultsChapter = soup.find(id="chapter-list")

    # Scrape story name
    story_name = results.find("h3", class_="title")
    story_name_text = f"Story name: {story_name.text}"

    # Scrape story description
    story_description = results.find("div", class_="story-desc")
    inner_html = story_description.contents

    story_description_extract = "".join(map(str, inner_html))

    data_extract = [
        story_name_text,
        story_description_extract
    ]


    dataFrame = pandas.DataFrame(data_extract)

    # Save the DataFrame to the CSV file
    dataFrame.to_csv(r"C:\Users\TuanBHA\story_info.csv", index=False)



scrape_story(URL)

import requests
import pandas as pd
from bs4 import BeautifulSoup

URL = "https://santruyen.com/doc-ton-truyen-ky-thanh-van-mon.614/"


def scrape_story(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")

    # Begin Scrape
    results = soup.find(id="truyen")

    # Scrape story name
    story_name = results.find("h3", class_="title").text.strip()

    # Scrape story description
    story_description = results.find("div", class_="story-desc")
    inner_html = story_description.contents
    story_description_text = "".join(map(str, inner_html))

    # Create a DataFrame to save the data
    data = {
        "URL": [url],
        "Story Name": [story_name],
        "Story Description": [story_description_text]
    }

    df = pd.DataFrame(data)

    # Save the DataFrame to the CSV file
    df.to_csv(r"C:\Users\TuanBHA\story_info.csv", encoding="utf_8_sig", index=False)


scrape_story(URL)

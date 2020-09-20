from typing import Dict

from bs4 import BeautifulSoup
import requests

HOME_URL = "https://americanliterature.com"
URL = "https://americanliterature.com/short-stories-for-children"


def get_story_links() -> Dict[str, str]:
    response = requests.get(URL)
    soup = BeautifulSoup(response.text, "lxml")
    story_links = {}
    for tag in soup.find_all("a", recursive=True):
        try:
            if "childrens-stories" in (link := tag["href"]):
                title = tag.text
                story_links[title] = link
        except KeyError:
            continue
    return story_links


def get_stories(titles_to_links: Dict[str, str]) -> Dict[str, str]:
    titles_to_stories = {}
    for title, link in titles_to_links.items():
        response = requests.get(HOME_URL + link)
        soup = BeautifulSoup(response.text, "lxml")
        story_section = soup.find("div", attrs={"class": "jumbotron"})
        story_text = ""
        try:
            for tag in story_section:
                name = tag.text
                story_text += name
            preface = soup.find("div", attrs={"class": "preface"}).text
            story_text = story_text.replace(preface, "", 1)
            titles_to_stories[title] = story_text
        except (TypeError, AttributeError):
            continue
    return titles_to_stories


with open("all_books.txt", "w") as f:
    f.write(str(get_stories(get_story_links())))

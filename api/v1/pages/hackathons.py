#!/usr/bin/python3
import requests
from api.v1.pages import app_pages
from flask import jsonify
from datetime import datetime
from bs4 import BeautifulSoup as bs

year = datetime.now().date().strftime("%Y")

@app_pages.route("/hackathons", strict_slashes=False)
def get_mlh_events():
    """get upcoming events from mlh website"""

    url = f"https://mlh.io/seasons/{year}/events"
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}

    result = requests.get(url, headers=headers)
    html = result.content.decode()

    soup = bs(html, 'lxml')
    event_wrapper = soup.find_all("div", attrs={"class": "event-wrapper"})
    events = {}
    for div in event_wrapper:
        dct = {}
        dct["title"] = div.find("h3").text
        dct["startDate"] = div.find("meta", attrs={"itemprop": "startDate"}).attrs["content"]
        dct["endDate"] = div.find("meta", attrs={"itemprop": "endDate"}).attrs["content"]
        dct["event_date"] = div.find("p", class_="event-date").text
        dct["state"] = div.find("span", attrs={"itemprop": "state"}).text
        dct["city"] = div.find("span", attrs={"itemprop": "city"}).text
        dct["logo"] = div.find("div", class_="event-logo").img.attrs["src"]
        dct["image_wrap"] = div.find("div", class_="image-wrap").img.attrs["src"]
        dct["link"] = div.find("a").attrs["href"]
        events[dct["title"]] = dct
    
    return jsonify(events)

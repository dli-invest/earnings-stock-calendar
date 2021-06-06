import os
import requests
from es_cal.discord import send_message
BASE_SEARCH_URL="https://www.googleapis.com/customsearch/v1?"


def searchGoogle(query: str):
    gsk = os.getenv("GOOGLE_SEARCH_KEY")
    gsecx = os.getenv("GOOGLE_SEARCH_ENGINE_CX")
    search_url = f"{BASE_SEARCH_URL}q={query}&key={gsk}&cx={gsecx}"
    r = requests.get(search_url)
    data = r.json()
    return parseResponse(data)


def parseResponse(searchData: dict):
    item = searchData.get('items', [None])[0]
    if item == None:
        raise Exception ('No search data returned')
    return item

def mapItemForDiscord(item: dict):
    content = item.get('title')
    embed = {
        'description': item.get('snippet'),
        'url': item.get('link'),
    }
    embeds = [embed]
    return content, embeds
# import libraries
import requests
from bs4 import BeautifulSoup
import json
from pprint import pprint


def create_responsable_json(type=None, chapter=None, title=None, link=None):
    if type == 'empty':
        return json.dumps({"Error": "news attribute can't be negative"})
    elif type == 'not_empty':
        news_data = []
        for i in range(0, len(title)):
            try:
                news_data.append({'title': title[i], 'URL': link[i]})
            except BaseException:
                break

        a = {"chapter": chapter,
             "news": news_data
             }
        return json.dumps(a)


def bbc_scrap(type, length):
    if length < 0:
        return create_responsable_json(type='empty')

    url = "https://www.bbc.com/{}".format(type)
    try:
        page = requests.get(url)
    except BaseException:
        return create_responsable_json(type='empty')

    soup = BeautifulSoup(page.text, 'html.parser')
    divs = soup.find_all('div')

    top_divs = [div for div in divs if 'gel-layout gel-layout--equal' in str(div)]

    try:
        content = top_divs[2]
    except BaseException:
        return json.dumps({'Error': "Couldn't find a data"})

    links = content.find_all('a')

    link_titles = [link.text for link in links if len(link.text.split()) > 2]
    link_url = ["https://www.bbc.com/{}".format(link['href']) for link in links if len(link.text.split()) > 2]

    link_titles_for_response = list(dict.fromkeys(link_titles))[:length]
    link_urls_for_response = list(dict.fromkeys(link_url))[:length]

    return create_responsable_json(
        type='not_empty',
        chapter=type,
        title=link_titles_for_response,
        link=link_urls_for_response)

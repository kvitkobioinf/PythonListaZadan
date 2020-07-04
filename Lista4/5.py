import requests
from bs4 import BeautifulSoup

if __name__ == "__main__":
    res = requests.get("https://en.wikipedia.org/wiki/COVID-19_pandemic_in_Poland").text
    res = BeautifulSoup(res, 'html.parser')
    info = res.findAll("tr", {"class": "sortbottom"})[0].find_all("td")

    suspected = info[1].text.replace(",", "")
    confirmed = info[6].text.replace(",", "")
    dead = info[9].text.replace(",", "")

    print("Confirmed cases:", confirmed)
    print("Suspected cases:", suspected)
    print("Deaths:", dead)
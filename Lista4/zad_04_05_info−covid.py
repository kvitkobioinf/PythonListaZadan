import requests
from bs4 import BeautifulSoup
import re

if __name__ == "__main__":
    res = requests.get("https://en.wikipedia.org/wiki/COVID-19_pandemic_in_Poland").text
    res = BeautifulSoup(res, 'html.parser')
    #table = res.find("table", {"id": "infobox"})
    table = res.select("table.infobox")[0]
    trs = table.findChildren("tr")

    confirmed = trs[len(trs) - 3].findAll("td")[0].text.split('[')[0].replace(',', '')
    recovered = trs[len(trs) - 2].findAll("td")[0].text.split('[')[0].replace(',', '')
    dead = trs[len(trs) - 1].findAll("td")[0].text.split('[')[0].replace(',', '')

    print("Confirmed cases:", confirmed)
    print("Recovered cases:", recovered)
    print("Deaths:", dead)
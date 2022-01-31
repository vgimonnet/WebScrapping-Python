import requests
from bs4 import BeautifulSoup

import re
import json

# latelierdesbieres = "https://www.latelierdesbieres.fr/12-achat-bieres-en-ligne?page="

dbFile = open("db.json", "w", encoding="utf-8")

beers = []
breweries = []
styles = []
arrayStyles = []

for counter in range (1,40, 1):
  page = requests.get(f'https://www.bieres.com/10-bieres?page={counter}')
  pageContent = BeautifulSoup(page.content, "html.parser")
  beerLinks = pageContent.find_all("a", class_="product_name")

  for beerLink in beerLinks:
    link = re.search(r'href=[\'"]?([^\'" >]+)', str(beerLink)).group(0)[6:]
    beerPage = requests.get(link)
    beerPageContent = BeautifulSoup(beerPage.content, "html.parser")
    jsonBeer = {} 
    jsonStyle = {} 
    jsonBrewery = {} 
    rowCounter = 0

    # Beer and style
    jsonBeer['name'] = beerPageContent.find("h1").text
    beerDescription = ''
    beerDataRowValues = beerPageContent.find_all("dd")
    for beerDataRowKey in beerPageContent.find_all("dt"):
      if beerDataRowKey.text == "Style de bière":
        jsonBeer["style"] = beerDataRowValues[rowCounter].text
        jsonStyle["name"] = beerDataRowValues[rowCounter].text
        styles.append(beerDataRowValues[rowCounter].text)
      elif beerDataRowKey.text == "Amertume":
        jsonBeer["ibu"] = beerDataRowValues[rowCounter].text
      elif beerDataRowKey.text == "Pays":
        jsonBeer["country"] = jsonBrewery["country"] = beerDataRowValues[rowCounter].text
      elif beerDataRowKey.text == "Degrés Alcool":
        jsonBeer["abv"] = beerDataRowValues[rowCounter].text
      elif beerDataRowKey.text == "Robe" or beerDataRowKey.text == "Arômes" or beerDataRowKey.text == "Goûts":
        beerDescription += beerDataRowValues[rowCounter].text + "/n"
      rowCounter += 1
    
    jsonBeer['desc'] = beerDescription

    # Brewery
    breweryInfos = beerPageContent.find("div", class_="manufacturer_description")
    if breweryInfos is not None:
      jsonBeer['brewery'] = jsonBrewery['name'] = breweryInfos.find("h3").text
      breweryDescription = ""
      for breweryDescriptionItem in breweryInfos.find_all("p"):
        breweryDescription += breweryDescriptionItem.text
        
      jsonBrewery['desc'] = breweryDescription
    
    beers.append(jsonBeer)
    breweries.append(jsonBrewery)
    styles.append(jsonStyle)

json.dump({ "beers": beers, "breweries": breweries, "styles": styles  }, dbFile)

dbFile.close

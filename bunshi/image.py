import requests
from bs4 import BeautifulSoup

def getImage(compound):
    imageName = "%s.png" % (compound)
    pageURL = "https://pubchem.ncbi.nlm.nih.gov/compound/%s" % (compound)
    page = requests.get(pageURL)
    soup = BeautifulSoup(page.text, "html.parser")
    imageSource = soup.find("meta", {"property": "og:image"})["content"]
    return imageSource, pageURL

""" Formatted info.py """

import requests
from bs4 import BeautifulSoup
from re import sub

# removes tildes & curly brackets from IUPAC name
def cleanIUPAC(IUPAC):
    newIUPAC = sub("[~{}]", "", IUPAC)
    return newIUPAC

# add superscript and subscript to chemical formula
def prettifyFormula(formula):
    newFormula = []
    for char in formula:
        if char.isalpha():
            newFormula.append("<span>%s</span>" % (char))
        elif char.isdigit():
            newFormula.append("<sub>%s</sub>" % (char))
    return "".join(newFormula)

# returns attributes
def getInfo(compound):

    # IMAGE
    pageURL = "https://pubchem.ncbi.nlm.nih.gov/compound/%s" % (compound)
    page = requests.get(pageURL)
    soup = BeautifulSoup(page.text, "html.parser")
    imageSource = soup.find("meta", {"property": "og:image"})["content"]

    CID = soup.find("meta", {"name": "pubchem_uid_value"})["content"]

    # IUPAC
    iupacURL = "https://pubchem.ncbi.nlm.nih.gov/rest/rdf/descriptor/CID%s_Preferred_IUPAC_Name.html" % (CID)
    iupacPage = requests.get(iupacURL)
    iupacSoup = BeautifulSoup(iupacPage.text, "html.parser")

    # if IUPAC name is found, IUPAC name is tagged as 'preferred'
    try:
        IUPAC = iupacSoup.find("span", {"class": "value"}).string
        preferred = True
    except AttributeError as e:
        IUPAC = soup.find("meta", {"property": "og:title"})["content"]
        preferred = False

    IUPAC = cleanIUPAC(IUPAC)

    # FORMULA
    formulaURL = "https://pubchem.ncbi.nlm.nih.gov/rest/rdf/descriptor/CID%s_Molecular_Formula.html" % (CID)
    formulaPage = requests.get(formulaURL)
    formulaSoup = BeautifulSoup(formulaPage.text, "html.parser")
    formula = formulaSoup.find("span", {"class": "value"}).string
    formula = prettifyFormula(formula)

    # WEIGHT
    weightURL = "https://pubchem.ncbi.nlm.nih.gov/rest/rdf/descriptor/CID%s_Molecular_Weight.html" % (CID)
    weightPage = requests.get(weightURL)
    weightSoup = BeautifulSoup(weightPage.text, "html.parser")
    weight = weightSoup.find("span", {"class": "value"}).string

    return {
        "pageURL": pageURL,
        "imageSource": imageSource,
        "IUPAC": IUPAC,
        "preferred": preferred,
        "formula": formula,
        "weight": weight,
    }

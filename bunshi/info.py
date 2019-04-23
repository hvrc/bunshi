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

# scrapes & returns image address, page address, IUPAC name, chemical formula, molecular weight
def getInfo(compound):

    imageName = "%s.png" % (compound)
    pageURL = "https://pubchem.ncbi.nlm.nih.gov/compound/%s" % (compound)
    page = requests.get(pageURL)
    soup = BeautifulSoup(page.text, "html.parser")
    imageSource = soup.find("meta", {"property": "og:image"})["content"]

    CID = soup.find("meta", {"name": "pubchem_uid_value"})["content"]

    iupacURL = "https://pubchem.ncbi.nlm.nih.gov/rest/rdf/descriptor/CID%s_Preferred_IUPAC_Name.html" % (CID)
    formulaURL = "https://pubchem.ncbi.nlm.nih.gov/rest/rdf/descriptor/CID%s_Molecular_Formula.html" % (CID)
    weightURL = "https://pubchem.ncbi.nlm.nih.gov/rest/rdf/descriptor/CID%s_Molecular_Weight.html" % (CID)

    iupacPage = requests.get(iupacURL)
    formulaPage = requests.get(formulaURL)
    weightPage = requests.get(weightURL)

    iupacSoup = BeautifulSoup(iupacPage.text, "html.parser")
    formulaSoup = BeautifulSoup(formulaPage.text, "html.parser")
    weightSoup = BeautifulSoup(weightPage.text, "html.parser")

    # if IUPAC name is found, IUPAC name is tagged as 'preferred'
    try:
        IUPAC = iupacSoup.find("span", {"class": "value"}).string
        preferred = True
    except AttributeError as e:
        IUPAC = soup.find("meta", {"property": "og:title"})["content"]
        preferred = False

    IUPAC = cleanIUPAC(IUPAC)
    formula = formulaSoup.find("span", {"class": "value"}).string
    formula = prettifyFormula(formula)
    weight = weightSoup.find("span", {"class": "value"}).string

    return imageSource, pageURL, IUPAC, formula, weight, preferred

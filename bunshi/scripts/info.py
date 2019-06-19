import requests
from bs4 import BeautifulSoup
from re import sub

# removes tildes & curly brackets from IUPAC name
def cleanIUPAC(IUPAC):
    return sub("[~{}]", "", IUPAC)

# adds superscript and subscript to chemical formula
def prettifyFormula(formula):
    return "".join(["<span>%s</span>" % (x) if x.isalpha() else "<sub>%s</sub>" % (x) for x in formula])

# returns attributes
def getInfo(compound):

    CID = BeautifulSoup(requests.get("https://pubchem.ncbi.nlm.nih.gov/compound/%s" % (compound)).text, "html.parser").find("meta", {"name": "pubchem_uid_value"})["content"]

    try:
        return {
            "IUPAC": cleanIUPAC(BeautifulSoup(requests.get("https://pubchem.ncbi.nlm.nih.gov/rest/rdf/descriptor/CID%s_Preferred_IUPAC_Name.html" % (CID)).text, "html.parser").find("span", {"class": "value"}).string),
            "preferred": False,
            "pageURL": "https://pubchem.ncbi.nlm.nih.gov/compound/%s" % (compound),
            "imageSource": BeautifulSoup(requests.get("https://pubchem.ncbi.nlm.nih.gov/compound/%s" % (compound)).text, "html.parser").find("meta", {"property": "og:image"})["content"],
            "formula": prettifyFormula(BeautifulSoup(requests.get("https://pubchem.ncbi.nlm.nih.gov/rest/rdf/descriptor/CID%s_Molecular_Formula.html" % (CID)).text, "html.parser").find("span", {"class": "value"}).string),
            "weight": BeautifulSoup(requests.get("https://pubchem.ncbi.nlm.nih.gov/rest/rdf/descriptor/CID%s_Molecular_Weight.html" % (CID)).text, "html.parser").find("span", {"class": "value"}).string,
        }

    except:
        return {
            "IUPAC": cleanIUPAC(BeautifulSoup(requests.get("https://pubchem.ncbi.nlm.nih.gov/compound/%s" % (compound)).text, "html.parser").find("meta", {"property": "og:title"})["content"]),
            "preferred": True,
            "pageURL": "https://pubchem.ncbi.nlm.nih.gov/compound/%s" % (compound),
            "imageSource": BeautifulSoup(requests.get("https://pubchem.ncbi.nlm.nih.gov/compound/%s" % (compound)).text, "html.parser").find("meta", {"property": "og:image"})["content"],
            "formula": prettifyFormula(BeautifulSoup(requests.get("https://pubchem.ncbi.nlm.nih.gov/rest/rdf/descriptor/CID%s_Molecular_Formula.html" % (CID)).text, "html.parser").find("span", {"class": "value"}).string),
            "weight": BeautifulSoup(requests.get("https://pubchem.ncbi.nlm.nih.gov/rest/rdf/descriptor/CID%s_Molecular_Weight.html" % (CID)).text, "html.parser").find("span", {"class": "value"}).string,
        }

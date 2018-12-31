from flask import (Blueprint, flash, render_template, request)
import requests
from bs4 import BeautifulSoup

bp = Blueprint("home", __name__)
recent = []
limit = 5

def getImage(compound):
    imageName = "%s.png" % (compound)
    pageURL = "https://pubchem.ncbi.nlm.nih.gov/compound/%s" % (compound)
    page = requests.get(pageURL)
    soup = BeautifulSoup(page.text, "html.parser")
    imageSource = soup.find("meta", {"property": "og:image"})["content"]
    return imageSource, pageURL

@bp.route("/", methods = ["POST", "GET"])
def home():
    #flash("This is a test")
    if request.method == "POST":
        posts = request.form

        for post in posts.items():
            compound = post[1]

        try:
            error = False
            compoundLinks = getImage(compound)
            imageSource = compoundLinks[0]
            pageURL = compoundLinks[1]

            if compound in recent:
                recent.remove(compound)
            recent.insert(0, compound)

            if len(recent) > limit + 1:
                recent.pop(-1)

        except TypeError as e:
            error = True
            imageSource = ""
            pageURL = ""

        return render_template("home.html",
                               imageSource = imageSource,
                               compound = compound,
                               pageURL = pageURL,
                               error = error,
                               recent = recent)

    return render_template("home.html",
                           recent = recent)

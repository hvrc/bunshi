from bunshi import app
from bunshi.scripts.info import *
from flask import render_template, request

@app.route("/", methods = ["POST", "GET"])
def home():
    if request.method == "POST":
        for post in request.form.items():
            compound = post[1].lower()

        try:
            info = getInfo(compound)
            return render_template(
                "home.html",
                compound=compound,
                pageURL=info["pageURL"],
                imageSource=info["imageSource"],
                IUPAC=info["IUPAC"],
                preferred=info["preferred"],
                formula=info["formula"],
                weight=info["weight"],
                owoEgg=True if info["IUPAC"] == "dioxotungsten" else False,
                acetateEgg=True if info["IUPAC"] == "acetate" else False,
                error=False,
            )

        except TypeError as e:
            return render_template("home.html", compound=compound, pageURL="", imageSource="", IUPAC="", preferred=False, formula="", weight="", owoEgg=False, acetateEgg=False, error=True,)

    return render_template("home.html", compound="", pageURL="", imageSource="", IUPAC="", preferred=False, formula="", weight="", owoEgg=False, acetateEgg=False, error=False,)

from bunshi import app
from bunshi.info import getInfo
from flask import flash, render_template, session, request

recent = []
recentMax = 5

@app.route("/", methods = ["POST", "GET"])
def home():
    # flash(recent)
    easterEgg = False
    error = False
    imageSource = ""
    pageURL = ""
    IUPAC = ""
    formula = ""
    weight = ""

    if request.method == "POST":
        posts = request.form
        for post in posts.items():
            compound = post[1].lower()

        try:
            info = getInfo(compound)
            imageSource = info[0]
            pageURL = info[1]
            IUPAC = info[2]
            formula = info[3]
            weight = info[4]

            if IUPAC == "dioxotungsten":
                easterEgg = True

            # if compound in recent:
            #     recent.remove(compound)
            # recent.insert(0, compound)
            #
            # if len(recent) > recentMax:
            #     recent.pop(-1)

        except TypeError as e:
            error = True

        return render_template("home.html",
                               imageSource = imageSource,
                               compound = compound,
                               pageURL = pageURL,
                               IUPAC = IUPAC,
                               formula = formula,
                               weight = weight,
                               error = error,
                               recent = recent,
                               easterEgg = easterEgg)

    return render_template("home.html",
                           recent = recent)

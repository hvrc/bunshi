from bunshi import app
from bunshi.image import getImage
from flask import flash, render_template, session, request

recent = []
recentMax = 5
triggers = ["split atom", "explode"]

@app.route("/", methods = ["POST", "GET"])
def home():
    # flash(recent)
    easterEgg = False
    error = False
    imageSource = ""
    pageURL = ""

    if request.method == "POST":
        posts = request.form
        for post in posts.items():
            compound = post[1].lower()

        if compound in triggers:
            easterEgg = True

        else:
            try:
                links = getImage(compound)
                imageSource = links[0]
                pageURL = links[1]

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
                               error = error,
                               recent = recent,
                               easterEgg = easterEgg)

    return render_template("home.html",
                           recent = recent)

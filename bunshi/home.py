from bunshi import app
from bunshi.image import getImage
from flask import flash, render_template, session, request

recent = []
recentMax = 5

@app.route("/", methods = ["POST", "GET"])
def home():
    flash(request.method)
    flash(posts)
    flash(recent)
    if request.method == "POST":
        posts = request.form

        for post in posts.items():
            compound = post[1].lower()

        try:
            error = False
            links = getImage(compound)
            imageSource = links[0]
            pageURL = links[1]

            if compound in recent:
                recent.remove(compound)
            recent.insert(0, compound)

            if len(recent) > recentMax:
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

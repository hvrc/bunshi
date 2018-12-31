from bunshi import app
from bunshi.image import getImage
from flask import flash, render_template, session, request

recent = []
maxRecent = 5

@app.route("/", methods = ["POST", "GET"])
def home():
    #flash("This is a test")
    if request.method == "POST":
        posts = request.form

        for post in posts.items():
            session["compound"] = post[1].lower()

        try:
            error = False
            compoundLinks = getImage(session["compound"])
            imageSource = compoundLinks[0]
            pageURL = compoundLinks[1]

            if session["compound"] in recent:
                recent.remove(session["compound"])
            recent.insert(0, session["compound"])

            if len(recent) > maxRecent + 1:
                recent.pop(-1)

        except TypeError as e:
            error = True
            imageSource = ""
            pageURL = ""

        return render_template("home.html",
                               imageSource = imageSource,
                               compound = session["compound"],
                               pageURL = pageURL,
                               error = error,
                               recent = recent)

    return render_template("home.html",
                           recent = recent)

from flask import Flask, render_template

app = flask(__name__)

@app.rout("/")
def home():
    return render_template(r"index.html")

if__name__="__main__":
    app.run(debug=False, port=5000)

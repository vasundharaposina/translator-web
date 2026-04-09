from flask import Flask, render_template, request
from translator import context_translate

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    translated_text = ""

    if request.method == "POST":
        text = request.form["text"]
        lang = request.form["language"]

        translated_text = context_translate(text, lang)

    return render_template("index.html", result=translated_text)

import os

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
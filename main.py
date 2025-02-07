import flask
from flask import Flask, render_template
import pandas as pd
app = Flask("API Documentation")



@app.route("/")
def home():
    return render_template("Documentation.html")


@app.route("/api1/v1/<word>/")
def api(word):
    df=pd.read_csv("dictionary.csv")
    definition=df.loc[df["word"]==word]["definition"].squeeze()
    # definition = word.upper()
    return {"definition": definition, "word": word}


if __name__ == "__main__":
    app.run(debug=True,port=5001)

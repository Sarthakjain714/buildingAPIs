from flask import Flask, render_template
import pandas as pd

app = Flask("Wines_information")

@app.route("/")
def home():
    return render_template("wines.html")


@app.route("/most_expensive_wine/")
def most_expensive_wine():
    df = pd.read_csv("wines.csv")
    mostexpensivewine = df.loc[df["price"] == df["price"].max()].squeeze()
    return {"name": mostexpensivewine["name"],
            "price": mostexpensivewine["price"]}


@app.route("/all_wines_data/")
def all_data():
    df = pd.read_csv("wines.csv", nrows=10)
    return df.to_dict(orient="records")


@app.route("/most_highly_rated_wines/")
def highlyratedwines():
    df = pd.read_csv("wines.csv")
    bestwines = df.loc[df["points"] == 100].squeeze()

    return (bestwines[["name","price","points"]].to_dict(orient="records"))
    # return (bestwines.to_dict(orient="records"))


if __name__ == "__main__":
    app.run(debug=True, port=5002)

from flask import Flask,render_template
import pandas as pd

app=Flask("WeatherReposrt")

@app.route("/")
def home():
    return render_template("weatherReportTempelate.html")

@app.route("/api1/v2/<station>/<date>")
def info(station,date):
    filepath="data_small/TG_STAID"+str(station).zfill(6)+".txt"
    df=pd.read_csv(filepath,skiprows=20,parse_dates=["    DATE"])
    temperature=df.loc[df["    DATE"]==date]["   TG"].squeeze()/10
    print(temperature)
    # temperature=23
    return {
        "station" :station,
        "date" :date,
        "temperature" :temperature
    }

if __name__ == "__main__":
    app.run(debug=True)
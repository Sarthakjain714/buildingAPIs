from flask import Flask,render_template
import pandas as pd

app=Flask("WeatherReposrt")

tabledata=pd.read_csv("data_small/stations.txt",skiprows=17)
tabledata=tabledata[["STAID","STANAME                                 "]]


@app.route("/")
def home():
    return render_template("weatherReportTempelate.html",data=tabledata.to_html())

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

@app.route("/api1/v2/<station>/")
def Historicaldata(station):
    filepath = "data_small/TG_STAID" + str(station).zfill(6) + ".txt"
    df = pd.read_csv(filepath, skiprows=20, parse_dates=["    DATE"])

    return df.to_dict(orient="records")

@app.route("/api1/v2/yearly/<station>/<year>/")
def yearlydata(station,year):
    filepath = "data_small/TG_STAID" + str(station).zfill(6) + ".txt"
    df = pd.read_csv(filepath, skiprows=20)
    # print("here")
    # print(df.head(10))
    df["    DATE"]=df["    DATE"].astype(str)
    result=df.loc[df["    DATE"].str.startswith(str(year))].to_dict(orient="records")
    return result


if __name__ == "__main__":
    app.run(debug=True)
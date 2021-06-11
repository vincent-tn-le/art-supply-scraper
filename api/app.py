from flask import Flask
from flask_cors import CORS
import pandas as pd
import json

app = Flask(__name__)
cors = CORS(app)

@app.route("/")
def default():
  return "API WORKING!"

@app.route("/table/<searchInput>")
def getTableData(searchInput):
  df = pd.read_csv("test.csv")
  list = []
  tableDataDf = df.loc[df["name"] == searchInput]
  tableDataDf = tableDataDf.drop_duplicates(subset=["productId"], keep="last")
  result = tableDataDf.to_json(orient="table")
  parsed = json.loads(result)
  for i in parsed["data"]:
    dict = {
      "name": i["name"],
      "productId": i["productId"],
      "store": i["store"],
      "stock": i["stock"],
      "price": i["price"]
    }
    list.append(dict)
  return { "data" : list }

@app.route("/graph/<productId>")
def getGraphData(productId):
  df = pd.read_csv("test.csv")
  graphdDf = df.loc[df["productId"] == productId]
  graphdDf = graphdDf.tail(5) # 5 most recent prices
  result = graphdDf.to_json(orient="table")
  parsed = json.loads(result)
  for i in parsed["data"]:
    dict = {
      "productId": i["productId"],
      "date": i["date"],
      "price": i["price"]
    }
    list.append(dict)
  return {
    "data": list
  }

@app.route("/email/<emailInput>")
def postEmail(email):
  print("hi")
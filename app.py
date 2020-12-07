# app.py
import requests

from flask import Flask
app = Flask(__name__)

@app.route("/time_to_load/<url>", methods=["GET"])
def funct(url):
  response = requests.post(url)
  return response.elapsed.total_seconds()

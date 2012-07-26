from flask import Flask, request, Response, render_template
import urllib
import json
import os

GITHUB_API_BASE_URL = "https://api.github.com"

def query_api(query):
    url = "%s%s" % (GITHUB_API_BASE_URL, query)
    api = urllib.urlopen(url)
    result = api.read()    
    result_obj = json.loads(result)
    api.close()
    return result_obj

def get_gist(gist_id):
    return query_api("/gists/%s" % gist_id)

app = Flask(__name__)
app.debug = True

@app.route("/")
def index():
  return render_template("index.html")

@app.route("/<gist_id>")
def gist(gist_id):
  gist = get_gist(gist_id)
  return render_template("gist.html", gist=gist)

if __name__ == "__main__":
  app.run()
from flask import Flask, request, Response, render_template
import urllib
import json
import os

GITHUB_API_BASE_URL = "https://api.github.com"

def query_api(path, raw=False, base_url=GITHUB_API_BASE_URL):
  url = "%s%s" % (base_url or '', path)
  api = urllib.urlopen(url)
  result = api.read()
  api.close()
  return raw and result or json.loads(result)

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
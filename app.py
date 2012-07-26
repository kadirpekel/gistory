from flask import Flask, request, Response, render_template
import urllib
import json
import os

GITHUB_API_BASE_URL = "https://api.github.com"

def query_api(uri, raw=False, base_url=GITHUB_API_BASE_URL):
  url = "%s%s" % (base_url or '', uri)
  api = urllib.urlopen(url)
  result = api.read()
  api.close()
  return raw and result or json.loads(result)

def get_gist(gist_id):
  print("getting gist %s" % gist_id)
  gist = query_api("/gists/%s" % gist_id)
  gist['history'].reverse()
  for version in gist['history']:
    version['gist'] = query_api(version['url'], base_url=None)
  return gist  

app = Flask(__name__)
app.debug = True

@app.route("/<int:gist_id>")
def gist(gist_id):
  gist = get_gist(gist_id)
  return render_template("gist.html", gist=gist)

if __name__ == "__main__":
  app.run()
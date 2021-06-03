from flask import Flask, render_template, request
from urllib.request import urlopen
import simplejson

app = Flask(__name__)

BASE_PATH='http://solr-1:8983/solr/demo/select?wt=json&df=name&rows=250&q='

@app.route('/')
def hello():
    return 'Hello, World!'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
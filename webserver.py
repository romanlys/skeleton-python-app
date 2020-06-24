import os
from flask import Flask
from flask import request

from queryprocessor import process_query

app = Flask(__name__)

@app.route("/")
def root():
    return "The server is running!"

@app.route("/test")
def test():
    return "test!"

@app.route("/test4")
def test4():
    return "test4!"


@app.route("/test5")
def test5():
    return "test5!"

@app.route("/api")
def api():
	query = request.args.get('q')
	return process_query(query)

if __name__ == "__main__":
	port = int(os.environ.get('PORT', 5000))
	app.run(port=port)
# Skeleton NodeJS app

A skeleton Python web app using [Flask](https://flask.palletsprojects.com/en/1.1.x/).

## Create Your Own Fork

Fork this project to create a repo under your own GitHub account, so that you can commit and push to it.
Then clone the code from your fork onto your machine.


## Install Dependencies

Make sure you have Python 3 installed.


## Running Locally

```sh
$ cd skeleton-python-app
$ python3 -m venv venv
$ source venv/bin/activate
$ pip install -r requirements.txt
$ python webserver.py
```

Now try the following request in your browser: [http://localhost:5000/api?q=Who wrote Romeo and Juliet?]
This should call the code in `queryprocessor.py`.

## Run the unit tests

The skeleton app comes with a small set of unit tests (see the file `queryprocessortest.py`), which you can add to as you add functionality. Run the tests like this:

```sh
$ cd skeleton-node-js-app
$ pytest queryprocessortest.py
```

# Skeleton Python app

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

## Enabling Travis CI

Log in to https://travis-ci.org using your GitHub account. Click the `+` or `Add New Respository` on the left, find your new repository and click the slider to enable builds.


## Deploy to Heroku

1. Manually.

	Download the Heroku CLI and use it to log in.

	Once you've logged in to Heroku and created an app, this will add a generated Heroku Git remote to your local Git repository.

    This adds a Git `remote` to your local repository so that you can run `git push heroku master` to deploy it manually by transferring your code to Heroku's Git repo. You should see this if you run:

	```
    git remote -v
    ```

    Another way to add the remote is to run a command like:
    
    ```
    heroku git:remote -a robbie-spike-horse-bucket
    ```

    Test your application is deployed at a URL similar to [https://robbie-spike-horse-bucket.herokuapp.com](https://robbie-spike-horse-bucket.herokuapp.com/api?q=romeo%20and%20juliet)
    
2. Deploy automatically after a green build

    1. Run `heroku auth:token` to generate an Heroku authorisation token. 
    1. You would encrypt this value with the `travis` command but if you don't have the Travis CLI installed, use [this site](http://rkh.github.io/travis-encrypt/public/index.html) (use something like `rchatley/skeleton-java-app` for the repository field)
    
    1. Create a `deploy` section to your `travis.yml` (see the [Travis docs](https://docs.travis-ci.com/user/deployment/heroku/))
    1. Add the encrypted value to the `deply` section of your `travis.yml`.
    1. Make a change and push, check the travis log to see if it deploys.
    
NB. You will likely need to add the `app` value if your GitHub repo's name doesn't match the Heroku app name. 

Your `travis.yml` should look something like this.

```
language: python
python:
  - "3.6"    
# command to install dependencies
install:
  - pip install -r requirements.txt
# command to run tests
script:
  - pytest queryprocessortest.py

deploy:
  provider: heroku
  api_key:
    secure: EPYf4T4U9WfJzHi4/CVp4Eom3PXark9x5fbQ23DGw/bjGxpnqMbqv8=
  app: robbie-spike-horse-bucket
```
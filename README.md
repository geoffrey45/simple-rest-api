This is a simple Django REST API written for [Decoded Africa](https://developers.decoded.africa)'s [How to build a RESTful API in Django](developers.decoded.africa/introduction-to-restful-apis-in-django/) article.

### Getting started

Run the following commands in a terminal to setup the project.
```bash
# clone via https
$ git clone https://github.com/geoffrey45/simple-rest-api.git
# or clone via ssh
$ git clone git@github.com:geoffrey45/simple-rest-api.git
# open cloned folder
$ cd simple-rest-api
# create a virtual environment
$ python3 -m venv virtual
# activate virtual environment
$ source virtual/bin/activate
# install requirements
$ pip install -r requirements.txt
# create db and migrate
$ python manage.py migrate
# run api
$ python manage.py runserver
```

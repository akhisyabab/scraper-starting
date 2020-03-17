# Scraper Starting
Scraper starting app with flask

# Table of contents
1. Get started on local
2. Deploy to heroku.

<hr>

## GET STARTED (Local):
#### create database and user on your local: 
```
CREATE DATABASE db_name;

CREATE USER dbuser WITH password 'dbpassword';
GRANT ALL PRIVILEGES ON database db_name to dbuser;
ALTER USER dbuser SUPERUSER;
```


#### Setup:
```sh
$ virtualenv -p python3 venv
$ source venv/bin/activate
$ pip install -r requirements.txt
```

#### upgrade db for init data:
```
$ source ./scripts/dev_env.sh
$ python manage.py db upgrade
```


#### Running:
```
$ source ./scripts/run.sh
```
**open localhost:5000*

#### Running prod: 
```
gunicorn --bind 0.0.0.0:80 manage:app --daemon
```
<hr><hr>

## Deploy (Heroku):

```sh
$ heroku login
$ heroku create app_name
$ git remote add heroku heroku_git_url
$ heroku addons:create heroku-postgresql:hobby-dev --app app_name
```

See database url with command:
```sh
$ heroku config --app app_name
```
Then Paste database URL to scripts/heroku_config.sh. Next commit your code changes and then:

```shell script
$ git push heroku master
$ ./scripts heroku_config.sh
$ heroku run python manage.py db upgrade
```
**Open app_name.herokuapp.com on your browser*

<hr><hr>

## NOTES
**Drop database**
```shell script
DROP DATABASE db_name;
```

**How migration**:
```
$ python manage.py db migrate
$ python manage.py db upgrade
```




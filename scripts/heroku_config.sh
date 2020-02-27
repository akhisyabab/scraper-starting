heroku config:set FLASK_ENV=production
heroku config:set DATABASE_URL='postgres://xxx:xxx@xxx:5432/xxx'
heroku config:set APP_SETTINGS='project.config.ProductionConfig'
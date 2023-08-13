rem heroku login
git init .
heroku create nameofrep --buildpack http://github.com/heroku/heroku-buildpack-python.git
git add .
git commit -am "make it better"
git push heroku master
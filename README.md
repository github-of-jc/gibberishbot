===how to deploy===
git add .
git commit -m "my msg"
git push prod master
heroku run python manage.py db upgrade --app gibberishbot


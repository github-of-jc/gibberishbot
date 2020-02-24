===how to deploy===
git add .
git commit -m "my msg"
git push prod master
heroku run python manage.py db upgrade --app gibberishbot

===import new package and commit to heroku===
pip freeze > requirements.txt
git add .
git commit -m "my msg"
git push prod master
heroku run python manage.py db upgrade --app gibberishbot


==design considerations==
the main page will display topics and twitter status

then the button will add topics

the like is done automatically in the background

python manage.py runserver




need button to start and stop the recurring task

source venv/bin/activate


===randomly pick a tweet to like from all the topics===



===start the app locally===
open postgresql ui
click on book_store
\dt to see the tables
drop table alembic_version
drop table topics

make sure app_Settings is pointing to an existing db
python manage.py db init
migrate
upgrade


to run
python manage.py runserver


===generate text based on topics selected===
1. a set of topics need enough text to do analysys -- selected by me
2. pull all the tweets from that topic -- store into a txt file maybe
3. generate a tweet based on all the topic tweets -- do offline mkv analysis separately


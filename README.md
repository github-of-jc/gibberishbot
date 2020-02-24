===how to deploy===
git add .
git commit -m "my msg"
git push prod master
heroku run python manage.py db upgrade --app gibberishbot

===import new package and commit to heroku===
source env/bin/activate
pip install Flask
export APP_SETTINGS="config.DevelopmentConfig"
export DATABASE_URL="postgresql://postgres:1ady1ight&@localhost:5433/books_store"
pip install flask_sqlalchemy
pip install flask_script
 pip install flask_migrate
pip install psycopg2-binary

open postgresql ui
click on book_store
\dt to see the tables
dropgi table alembic_version;
drop table topics;


python manage.py db init
python manage.py db migrate
python manage.py db upgrade
python manage.py runserver
pip install gunicorn

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
dropgi table alembic_version;
drop table topics;

make sure app_Settings is pointing to an existing db
python manage.py db init
python manage.py db migrate
python manage.py db upgrade


to run
python manage.py runserver


===generate text based on topics selected===
1. a set of topics need enough text to do analysys -- selected by me
2. pull all the tweets from that topic -- store into a txt file maybe
3. generate a tweet based on all the topic tweets -- do offline mkv analysis separately

test the tweet function -- works

need a way to refresh the tweet dict

added a tweetText table to store all the texts

this table should be refreshed entirely everytime gen_str is called




===viewing window to see changes my the bot===
has delays of ~5 min


===app crash after successful deployment===

heroku releases --app gibberishbot

heroku rollback v23 --app gibberishbot


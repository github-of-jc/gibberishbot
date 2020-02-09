import os
from flask import Flask, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
# make sure to use the up-to-date import formet: from flast_module import Module
# DO NOT use deprecated from flask.ext.module import Module
import tweepy

app = Flask(__name__)

app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# app.config.setdefault('TWEEPY_CONSUMER_KEY', 'R4M3HyEF5FcDbdd0s3Xyohdeq')
# app.config.setdefault('TWEEPY_CONSUMER_SECRET', 'KpWOI1udl9gXDJow3mGx9yK9OPncqZ0PvMs8whdWfHEyEImPCy')
# app.config.setdefault('TWEEPY_ACCESS_TOKEN_KEY', '1198415155752849409-XLDpSZ3irzZQGhP1CUKs27Xgfey1Me')
# app.config.setdefault('TWEEPY_ACCESS_TOKEN_SECRET', 'tH2lp62ZgqSC4KE70VXJ6vSfHuyudXS3Br7uKTOcG5Dj9')
# tweepy = Tweepy(app)

auth = tweepy.OAuthHandler('R4M3HyEF5FcDbdd0s3Xyohdeq', 'KpWOI1udl9gXDJow3mGx9yK9OPncqZ0PvMs8whdWfHEyEImPCy')
auth.set_access_token('1198415155752849409-XLDpSZ3irzZQGhP1CUKs27Xgfey1Me', 'tH2lp62ZgqSC4KE70VXJ6vSfHuyudXS3Br7uKTOcG5Dj9')

api = tweepy.API(auth)

db = SQLAlchemy(app)
print("tweepy")
print(tweepy)

class Topic(db.Model):
    __tablename__ = 'topics'

    id = db.Column(db.Integer, primary_key=True)
    topicName = db.Column(db.String())

    def __init__(self, topicName):
        self.topicName = topicName


    def __repr__(self):
        return '<id {}>'.format(self.id)
    
    def serialize(self):
        return {
            'id': self.id, 
            'topicName': self.topicName
        }

@app.route("/")
def hello():
    return "Hello World!"

@app.route('/tweets')
def show_tweets():
    timeline = api.home_timeline()
    tweets = []
    for t in timeline:
        tweets.append(t.text)
    topicNames = ["no topics"]
    info = "no infotext"
    return render_template("getdata.html", topicNames = topicNames, infotext = info, tweets = tweets)


@app.route("/add")
def add_topic():
    topicName=request.args.get('topicName')
    try:
        topic=Topic(
            topicName=topicName
        )
        db.session.add(topic)
        db.session.commit()
        return "Topic added. Topic id={}".format(topic.id)
    except Exception as e:
        return(str(e))

@app.route("/getall")
def get_all():
    try:
        topics=Topic.query.all()
        return  jsonify([e.serialize() for e in topics])
    except Exception as e:
        return(str(e))

@app.route("/get/<id_>")
def get_by_id(id_):
    try:
        topic=Topic.query.filter_by(id=id_).first()
        return jsonify(topic.serialize())
    except Exception as e:
        return(str(e))

@app.route("/add/form",methods=['GET', 'POST'])
def add_topic_form():
    topics = Topic.query.all()
    topicNames = []
    info = "Add a topic you would like to track"
    for topic in topics:
        topicNames.append(topic.serialize()['topicName'])
    print(topicNames)
    if request.method == 'POST':
        print("Post method")
        topicName=request.form.get('topicName')
        if topicName not in topicNames:
            try:
                topic=Topic(
                    topicName=topicName
                )
                db.session.add(topic)
                db.session.commit()
                topics = Topic.query.all()
                topicNames = []
                for topic in topics:
                    topicNames.append(topic.serialize()['topicName'])
                info = "Added %s to db" % topicName 
                return render_template("getdata.html", topicNames = topicNames, infotext = info)
            except Exception as e:
                return(str(e))
        else:
            info = "%s is in the db already" % topicName 
            return render_template("getdata.html", topicNames = topicNames, infotext = info)   
    print("returning at the bottom")          
    return render_template("getdata.html", topicNames = topicNames, infotext = info)

if __name__ == '__main__':
    app.run()
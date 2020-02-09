import os
from flask import Flask, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy



app = Flask(__name__)

app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

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
    for topic in topics:
        topicNames.append(topic.serialize()['topicName'])
    if request.method == 'POST':
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
    return render_template("getdata.html", topicNames = topicNames, infotext = info)

if __name__ == '__main__':
    app.run()
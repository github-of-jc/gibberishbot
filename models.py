from app import db

class Topic(db.Model):
    __tablename__ = 'topics'

    id = db.Column(db.Integer, primary_key=True)
    topicName = db.Column(db.String())

    def __init__(self, topic):
        self.topicName = topicName


    def __repr__(self):
        return '<id {}>'.format(self.id)
    
    def serialize(self):
        return {
            'id': self.id, 
            'topicName': self.topicName
        }
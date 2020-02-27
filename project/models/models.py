import json
from project import db

class Records(db.Model):
    __tablename__ = 'records'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String())

    def __init__(self, name):
        self.exchanges = name

    def __repr__(self):
        return 'Record name = '.format(self.name)


class TimeFetched(db.Model):
    __tablename__ = 'timefetched'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    date = db.Column(db.String())

    def __init__(self, date):
        self.date = date

    def __repr__(self):
        return 'Last fetched = '.format(self.date)



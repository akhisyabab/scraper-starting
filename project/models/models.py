from project import db

class Records(db.Model):
    __tablename__ = 'records'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String())

    def __init__(self, name):
        self.name = name



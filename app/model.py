from sqlalchemy import Column, Integer, String, Text
from app import db


class Reading(db.Model):
    __tablename__ = 'reading'

    id = Column(Integer, primary_key=True)
    day = Column(Integer)
    month = Column(Integer)
    year = Column(Integer)
    title = Column(String)
    result = Column(Text)

    def __init__(self, day, month, year, title, result):
        self.day = day
        self.month = month
        self.year = year
        self.title = title
        self.result = result

    def __repr__(self):
        return "Reading for {day}/{month}/{year} from {title}".format(
            day=self.day, month=self.month, year=self.year, title=self.title
        )

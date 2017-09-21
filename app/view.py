import logging
import json

from flask.views import MethodView
from flask import request

from app import app
from app.controller import DailyReading


class DailyReadingView(MethodView):

    def __init__(self):
        self.control = DailyReading()

    def get(self):
        logging.info("New GET / request")
        year = request.args.get('year')
        month = request.args.get('month')
        day = request.args.get('day')

        result, status = self.control.get_daily_reading(day, month, year)
        return json.dumps(result), status

app.add_url_rule('/', view_func=DailyReadingView.as_view('daily_reading'))

import logging

from bs4 import BeautifulSoup
from urllib.request import urlopen


URL = "http://www.catholic.org/bible/daily_reading/?select_date={year}-{month:0=2d}-{day:0=2d}"


class DailyReading:

    def get_daily_reading(self, day, month, year):
        full_url = URL.format(day=int(day), month=int(month), year=int(year))
        logging.debug("URL: {}".format(full_url))
        page = urlopen(full_url)
        soup = BeautifulSoup(page, 'html.parser')
        reading = soup.findAll('h3')

        title = reading[2].em.string
        text = reading[2].next_elements

        p_element = filter(lambda x: x.name == "p", text)
        result = []
        for p in p_element:
            sup_element = list(filter(lambda x: x.name == "sup", p.contents))
            for q in sup_element:
                f = list(map(lambda w: w.string, q.next_siblings))
                result.append("".join(f))
        result = "".join(result)

        d = dict()
        logging.debug("Title: {}".format(title))
        logging.debug("Result: {}".format(result))
        d['title'] = title
        d['result'] = result
        return d, 200

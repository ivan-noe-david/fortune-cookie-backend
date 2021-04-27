import logging
from model import FortuneCookieModel as model
logging.basicConfig(level=logging.INFO)


class FortuneCookieService(object):
    file_name = 'data/fortune.txt'

    @classmethod
    def init_data(cls):
        with open(cls.file_name) as _file:
            data = _file.read().splitlines()
            model.init_data(list(map(lambda row: [row], data)))

    @classmethod
    def get_fortune(cls):
        return model.get_fortune()

    @classmethod
    def save_fortune(cls, data):
        model.save_fortune(data)
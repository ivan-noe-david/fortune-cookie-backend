from flask import Flask
from flask_cors import CORS
from flask_script import Manager
from multiprocessing import Process
from app.modules.fortune.api import fortune
from app.modules.fortune.service import FortuneCookieService as service

app = Flask(__name__)
app.register_blueprint(fortune)

CORS(app)
manager = Manager(app)


@manager.command
def runserver():
    p = Process(target=service.init_data)
    p.start()
    app.run()


if __name__ == "__main__":
    manager.run()
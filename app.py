from flask import Flask, render_template
from flask_restful import Api
from flask_cors import CORS
from db import db
from log.logger import Logger
from src.Board_Controller import Board_Controller
from global_controller.global_controller import Global_Controller
from src.my_utils import set_global_controller
from resources.nerve_center import Nerve_Center

app = Flask(__name__)
CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///data.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = "superKevin"
board_controller = Board_Controller()
global_controller = Global_Controller()
api = Api(app)

@app.before_first_request
def create_table():
    db.create_all()
    #start daemon_thread
    board_controller.start_messurments(2)
    set_global_controller(global_controller)

@app.route('/', methods=['GET'])
def home():
    return render_template("index.html")


api.add_resource(Nerve_Center, "/nerveCenter")

if __name__ == "__main__":
    Logger.log(__name__, "\n*****************************\n"\
               "Start application")

    #setup DB
    db.init_app(app)
    
    #start app
    app.run(port=5000, host="0.0.0.0", debug=True)
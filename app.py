from flask import Flask, render_template
#from flask_restful import Api
from flask_cors import CORS
from db import db
from log.logger import Logger
from src.Board_Controller import Board_Controller


app = Flask(__name__)
CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///data.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = "superKevin"
board_controller = Board_Controller()
#api = Api(app)

@app.before_first_request
def create_table():
    db.create_all()

@app.route('/', methods=['GET'])
def home():
    return render_template("index.html")

@app.route('/shutdown', methods=['GET'])
def shutdown():
    board_controller.stop_daemon_thread()
    return "daemon is dead"



if __name__ == "__main__":
    Logger.log(__name__, "\n*****************************\n"\
               "Start application")
    #setup DB
    db.init_app(app)
    
    #start daemon_thread
    board_controller.start_daemon_thread()

    #start app
    app.run(port=5000, host="0.0.0.0", debug=True)
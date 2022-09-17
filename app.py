from flask import Flask, render_template
#from flask_restful import Api
from flask_cors import CORS
from db import db
from src.log.logger import Logger


app = Flask(__name__)
CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///data.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = "superKevin"
#api = Api(app)

@app.before_first_request
def create_table():
    db.create_all()
    #create instance of Pump_controller
    Logger.log(__name__, "setup pumpcontroller")
    Logger.log(__name__, "setup completed\n*****************************")

@app.route('/', methods=['GET'])
def home():
    return render_template("index.html")


if __name__ == "__main__":
    Logger.log(__name__, "\n*****************************\n"\
               "Start application")
    #setup DB
    db.init_app(app)
    
    #start app
    app.run(port=5000, host="0.0.0.0", debug=True)
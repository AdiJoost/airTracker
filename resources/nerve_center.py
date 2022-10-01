"""
Created: 30.09
nerve_center is a Ressource, that is talking to the global_controller of the application.
"""

from flask_restful import Resource, reqparse
from sqlalchemy import null
from src.my_utils import create_response
from global_controller.global_controller import Global_Controller

class Nerve_Center(Resource):
    def get(self):
        gc = Global_Controller()
        data = gc.get()
        return create_response(data, 200)

    def post (self):
        parser = self.get_post_parser()
        data = parser.parse_args()
        gc = Global_Controller()
        return_value = {}
        for key in data:
            if (data[key] is not None):
                transform = gc.update(key, data[key])
                return_value.update(transform)
        return_value["message"] = "Components updated"
        create_response(return_value, 200)

        
    
    @classmethod
    def get_post_parser(cls):
        parser = reqparse.RequestParser()
        parser.add_argument(Global_Controller.SHUTDOWN,
                        type = bool)
        parser.add_argument(Global_Controller.BLINKING_SHOW,
                            type=bool)
        return parser
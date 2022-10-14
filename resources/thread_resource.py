"""
Created: 30.09
nerve_center is a Ressource, that is talking to the global_controller of the application.
"""

from flask_restful import Resource, reqparse
from sqlalchemy import null
from src.my_utils import create_response
from global_controller.global_controller import Global_Controller

class Thread_resource(Resource):
    def get(self):
        
        parser = self.get_get_parser()
        data = parser.parse_args()
        gc = Global_Controller()
        if not(data["thread_name"] in gc.thread_names):
            return create_response({"Message": "Threadname not found"}, 404)
        is_online = gc.is_online(data["thread_name"])
        return create_response({data["thread_name"]: is_online}, 200)

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
        return_value["data"] = data
        create_response(return_value, 200)

        
    
    @classmethod
    def get_get_parser(cls):
        parser = reqparse.RequestParser()
        parser.add_argument("thread_name",
                        type = str)

        return parser
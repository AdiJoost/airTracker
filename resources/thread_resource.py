"""
Created: 30.09
nerve_center is a Ressource, that is talking to the global_controller of the application.
"""

from flask_restful import Resource, reqparse
from sqlalchemy import null
from src.my_utils import create_response
from global_controller.global_controller import Global_Controller
from src.Board_Controller import Board_Controller

class Thread_resource(Resource):
    def get(self):
        
        parser = self.get_get_parser()
        data = parser.parse_args()
        gc = Global_Controller()
        if not(data["thread_name"] in gc.thread_names):
            return create_response({"Message": "Threadname not found"}, 404)
        is_online = gc.is_online(data["thread_name"])
        return create_response({"is_online": is_online}, 200)

    def post (self):
        parser = self.get_get_parser()
        thread_name = parser.parse_args()["thread_name"]
        gc = Global_Controller()
        if not(thread_name in gc.thread_names):
            return create_response({"Message": "Threadname not found"}, 404)
        is_online = gc.is_online(thread_name)
        if is_online:
            return create_response({"message":
                                    "Thread already online"}, 200)
        Board_Controller.get_instance().start_thread(thread_name)
        is_online = gc.is_online(thread_name)
        if is_online:
            return create_response({"message":
                                    "Thread stared"}, 200)
        return create_response({"message":
                                    "Internal Error, Ask Adi"}, 500)
        

        
    
    @classmethod
    def get_get_parser(cls):
        parser = reqparse.RequestParser()
        parser.add_argument("thread_name",
                        type = str,
                        required = True)

        return parser
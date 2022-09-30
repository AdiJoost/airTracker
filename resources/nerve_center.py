"""
Created: 30.09
nerve_center is a Ressource, that is talking to the global_controller of the application.
"""

from flask_restful import Resource, reqparse
from tomlkit import boolean
from my_utils import create_response

class Nerve_Center(Resource):
    def get(self):
        pass

    def post (self):
        pass


def get_post_parser():
    parser = reqparse.RequestParser()
    parser.add_argument("shutdown",
                        type = boolean)
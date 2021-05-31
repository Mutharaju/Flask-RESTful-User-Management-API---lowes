from flask_restful import Resource

class About(Resource):
    def get(self):
        return {'About Developer':{ 'name':"Mutharaju H M"}}

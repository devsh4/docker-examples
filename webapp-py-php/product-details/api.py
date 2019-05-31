# Product service
# simple restful API
from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api =  Api(app)

class Product (Resource):
    def get(self):
        return {
        'products': ['Ice-cream',
                    'Chocolate',
                    'Banana']
        }

# Add the resource to the api
api.add_resource(Product,'/')

if __name__ == "__main__":
    # instantiate the app
    app.run(host='0.0.0.0', port=80, debug=True)

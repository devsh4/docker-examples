# Product details service
# simple restful API
from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api =  Api(app)

class productDetails (Resource):
    def get(self):
        return {
        'productDetails': ['Vanilla',
                    'Snickers',
                    'Yellow']
        }

# Add the resource to the api
api.add_resource(productDetails,'/')

if __name__ == "__main__":
    # instantiate the app
    app.run(host='0.0.0.0', port=80, debug=True)

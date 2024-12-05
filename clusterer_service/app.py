from flask import Flask
from flask_restx import Api, Resource

app = Flask(__name__)

# Initialize the Flask-RESTx API
api = Api(app, title="Greeting Service", description="API documentation for the Greeting Service", version="1.0")

# Define a namespace for grouping endpoints
ns = api.namespace("greet", description="Greeting operations")

# Define the endpoint and its documentation
@ns.route("/")
class Greet(Resource):
    def get(self):
        """Returns a greeting message"""
        return {"message": "Hello"}

# Add the namespace to the API
api.add_namespace(ns)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)

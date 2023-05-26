"""
This code demonstrates the usage of Flask to create a web application and import a function from the 'AIapp' module.
"""

# Import the required modules
       
# Import the 'Flask' class from the 'flask' module to create a Flask web application
from flask import Flask, request
from flask_cors import CORS

# Import the 'function' from the 'AIapp' module
from AIapp import function             

# Create an instance of the Flask application
app = Flask(__name__)
CORS(app)  # Allow requests from specific origin

@app.route('/AI/answer', methods=['POST'])

def handle_post():
    return function(request.get_data(as_text=True))

# Run the Flask application if the script is executed directly (not imported)
if __name__ == '__main__':
    app.run()
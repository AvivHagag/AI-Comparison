"""
This code demonstrates the usage of Flask to create a web application and import a function from the 'AIapp' module.
"""

# Import the required modules
       
# Import the 'Flask' class from the 'flask' module to create a Flask web application
from flask import Flask, request
from flask_cors import CORS
import threading
# Import the 'function' from the 'AIapp' module
from AIapp import function             
from AIapp import function1   
from AIapp import function2       
# Create an instance of the Flask application
app = Flask(__name__)
CORS(app)  # Allow requests from specific origin

@app.route('/') 
def main():
  return "<span style='font-size: 32px'>Working...</span>"


def process_result1_and_result2(string, results):
    # Call function1 and get result
    result1 = function1(string)

    # Call function2 and get result
    result2 = function2(string)

    results.extend([result1, result2])

@app.route('/AI/answer', methods=['POST'])

def handle_post():
    val = request.args.get('num') # get num parameter
    print()
    print()
    print(val)
    print()
    print()
# Call function1 and get result\
    string = function(request.get_data(as_text=True),val)
    if(string=="Error1"):
       return "One of the products doesn't have enogth reviews to do this comparison"
    
    # Create a list to hold results and pass it to the threads
    results = []

    # Create two threads to process result1 and result2 concurrently
    thread1 = threading.Thread(target=process_result1_and_result2, args=(string, results))
    thread1.start()

    thread2 = threading.Thread(target=thread1.join)
    thread2.start()

    thread2.join()

    result1, result2 = results

    # Concatenate results
    result = "Similarities and differences between the products" + result1 + "\n\nThe most recommended product" + result2

    return result
  #   result1 = function1(string)  

  # # Call function2 and get result
  #   result2 = function2(string)

  # # Concatenate results 
  #   result = "Similarities and differences between the products" +result1 + "\n\nThe most recommended product" +result2

  #   return result

# Run the Flask application if the script is executed directly (not imported)
if __name__ == '__main__':
    app.run()
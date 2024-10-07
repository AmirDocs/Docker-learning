# app.py

# Creating a new flask application instance (importing flask)
from flask import Flask

app = Flask(__name__)

# Setting a route, defining a route for the root URL /, returning Hello World!
@app.route('/')
def hello_world():
    return 'Hello, World!'

# Running application by doing app.run (running server). Using the app variable and telling it to run on host and port 5000.
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002)

# Outputs 'Hello World!' in local host



# Created a simple python web application using flask and ran it on my local machine. This gives a clear understanding of how the application works before containerisation with Docker.
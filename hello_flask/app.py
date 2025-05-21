# app.py

from flask import Flask
import MySQLdb

app = Flask(__name__)

@app.route('/')
def hello_world():
    # Connect to the MySQL database
    db = MySQLdb.connect(
        host="mydb",    # Hostname of the MySQL container
        user="root",    # Username to connect to MySQL
        passwd="my-secret-pw",  # Password for the MySQL user
        db="mysql"      # Name of the database to connect to
    )                                 # After establishing a connection, query below.
    cur = db.cursor()
    cur.execute("SELECT VERSION()")
    version = cur.fetchone()
    return f'Hello, World! MySQL version: {version[0]}'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002)

# Outputs 'Hello World!' in local host



# Phase 1 - Created a simple python web application using flask and ran it on my local machine. This gives a clear understanding of how the application works before containerisation with Docker.
# Creating a new flask application instance (importing flask) with from.
# Setting a route @app.route, defining a route for the root URL /, returning Hello World!
# # Running application by doing app.run (running server). Using the app variable and telling it to run on host and port 5000.



# PHASE 2 - initiating the build
#               `docker build -t hello-flask .` initiates the build process.

# Docker build initiates the build process, -t tags the image with a name (hello-flask), and the . represents the current directory.



# Phase 3 - Linking containers together
# Linking the flask application to a mySQL database container, which enables us to execute SQL commands within the python application.
# installs flask with mySQL client package. This provides the tools needed to connect to a mySQL database from within python app.
#                   `docker network create my-custom-network' Entered in the terminal creates a custom network.
# Setting network to my-custom-network to connect mySQL to network, adding '-e MYSQL_ROOT_PASSWORD=my-secret-pw' for authentication to database and specifying the version with mysql:5.7.
#                   'docker run -d --name mydb --network my-custom-network -e MYSQL_ROOT_PASSWORD=my-secret-pw mysql:8'







# PHASE 4 - Build Docker image for the flask app with the updated docker file.
#                  'docker build -t hello-flask-mysql .'  (.) for the docker file.
#                  'docker run -d --name myapp45 --network my-custom-network -p 5002:5002 hello-flask-mysql'
#  Allocated to `my app2` as `myapp` already exists for previous container.

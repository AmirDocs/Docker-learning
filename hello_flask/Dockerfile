FROM python:3.8-slim
WORKDIR /app
COPY . .
RUN apt-get update && apt-get install -y \
    gcc \
    python3-dev \
    libmariadb-dev \
    pkg-config
RUN pip install flask mysqlclient
EXPOSE 5002
CMD ["python", "app.py"]






# PHASE 2
#               `docker build -t hello-flask .` initiates the build process.

# Docker build initiates the build process, -t tags the image with a name (hello-flask), and the . represents the current directory.




# First command is always the FROM command.
# WORKDIR - Any command run after this will be run in this directory (app)
# Copy all files (.) from current directory (app.py which is also set as .) and put that into container.
# RUN command to install flask into container
# Expose port 5002 so it can be accessed from a local host
# CMD tells docker to run the python application 


#                   'docker run -d -p 5002:5002 hello-flask' will run as this as a container.
# -d runs the container in detach mode (running in the background), -p 5002:5002 is mapping port 5002 in my machine to port 5002 in my container, hello-flask is the name of the image were using. The output is the container ID.






# PHASE 3 - Linking containers together
# installs flask with mySQL client package. This provides the tools needed to connect to a mySQL database from within python app.
#                   `docker network create my-custom-network' Entered in the terminal creates a custom network.
# Setting network to my-custom-network to connect mySQL to network, adding '-e MYSQL_ROOT_PASSWORD=my-secret-pw' for authentication to database and specifying the version with mysql:5.7.
#                   'docker run -d --name mydb --network my-custom-network -e MYSQL_ROOT_PASSWORD=my-secret-pw mysql:8'







# PHASE 4 - Build Docker image for the flask app with the updated docker file.
#                  'docker build -t hello-flask-mysql .'  (.) for the docker file.
#                  'docker run -d --name myapp100 --network my-custom-network -p 5002:5002 hello-flask-mysql'
#  Allocated to `my app100` after debugging flask sql installation.




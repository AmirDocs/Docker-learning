FROM python:3.8-slim
WORKDIR /app
COPY . .
RUN pip install flask
EXPOSE 5002
CMD ["PYTHON", "app.py"]







# In the command line to initiate the build process: `docker build -t hello-flask .`

# Docker build initiates the build process, -t tags the image with a name (hello-flask), and the . represents the current directory.




# First command is always the FROM command.
# WORKDIR - Any command run after this will be run in this directory (app)
# Copy all files (.) from current directory (app.py which is also set as .) and put that into container.
# RUN command to install flask into container
# Expose port 5002 so it can be accessed from a local host
# CMD tells docker to run the python application 


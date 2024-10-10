# Docker-learning

## Docker Commands:
Command | Description |
|---|---|
`docker run` | Start a container from an image. |
`docker exec` | Run a command inside a container. |
`docker restart` | Restart a running container. |
`docker stop` | Stop a container. |
`docker rm` |	Remove a container. |
`docker ps` |	List running containers. |
`docker cp` |	Copy files to/from a container. |
`docker logs <container_name>` | View the logs (stdout) of a container. To follow logs, add the `-f` option before the container name. Use to debug.

# **Docker Task**

## **Phase 1**:
Created a simple python web application using flask and ran it on my local machine. This gives a clear understanding of how the application works before containerisation with Docker.

![python web app - flask](https://github.com/user-attachments/assets/4982a55d-cf6a-4e0b-8f76-7160d56b5baa)


## **Phase 2**:
Created a Dockerfile to initiate the build process, install flask into container and access it on port 5002 from a local host. Initiated Dockerfile to be ran as a container.

![Dockerfile 1](https://github.com/user-attachments/assets/5b995dd9-6c0d-456d-99bf-000cd594386a)


## **Phase 3**:
Connected flask app to mySQL database. Created a custom network with (my-custom network) in the terminal.

![Linking MySQL to flask](https://github.com/user-attachments/assets/42175ead-7e4c-4106-a13a-2dce6e58459f)


## **Phase 4**: 
Build Docker image for the flask app with the updated docker file.






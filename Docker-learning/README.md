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

# **Docker Hello_flask Task**

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
Built a Docker image for the flask app with the updated docker file. 

![MYSQL custom network](https://github.com/user-attachments/assets/8efae3bb-0b0a-4b0e-9d86-9d6309633383)


# **Pushing flask-mysql to Elastic Container Registry**:

**1) To install the AWS CLI, run the following commands**:

```
$ curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
unzip awscliv2.zip
sudo ./aws/install
```

**2) After installation, generate an access key for your IAM account and log in to your AWS via terminal**.

**3) Push & Pull using these Commands**
 
 Retrieve an authentication token and authenticate your Docker client to your registry.
```
aws ecr get-login-password --region eu-west-2 | docker login --username AWS --password-stdin 872515255126.dkr.ecr.eu-west-2.amazonaws.com
```

 Build your Docker image with:
 ```
 docker build -t flask-mysql .
 ```

 Tag the image to your repository:
 ```
 docker tag flask-mysql:latest 872515255126.dkr.ecr.eu-west-2.amazonaws.com/flask-mysql:latest
 ```

And finally, run the following command to push the image to your newly created AWS repository:
```
docker push 872515255126.dkr.ecr.eu-west-2.amazonaws.com/flask-mysql:latest
```
![ECR pushing flask-mysql ](https://github.com/user-attachments/assets/af27debb-5560-431e-9b6b-ffbc8ddc0c4a)


**4) To pull your images from the ECR repository to your local docker enviroment enter:**
```
docker pull 872515255126.dkr.ecr.eu-west-2.amazonaws.com/flask-mysql:latest
```

followed by:
```
docker run -p 5002:5002 872515255126.dkr.ecr.eu-west-2.amazonaws.com/flask-mysql:latest
```

**5) This did not seem to work because I did not have an active version of mySQL. Create a mySQL mydb database on the custom network with**:
```
docker run -d --name mydb -e MYSQL_ROOT_PASSWORD=my-secret-pw mysql:8
```

then run a Flask container on the custom network, mapping port 5002 and using the specified image:
```
docker run -p 5002:5002 --network my-app-network 872515255126.dkr.ecr.eu-west-2.amazonaws.com/flask-mysql:latest
```

# **BUILDING A MULTICONTAINER APPLICATION CHALLENGE**

Building a Multi-Container Application

## **Objective**:

To create a multi-container application that consists of a simple Python Flask web application and a Redis database. The Flask application Should use Redis to store and retrieve data.

## **Requirements**:

1. **Flask Web Application**:
   - A Flask app that has two routes:
     - `/`: Displays a welcome message.
     - `/count`: Increments and displays a visit count stored in Redis.

2. **Redis Database**:
   - Use Redis as a key-value store to keep track of the visit count.

3. **Dockerize Both Services**:
   - Create Dockerfiles for both the Flask app and Redis.
   - Use Docker Compose to manage the multi-container application.

## Test the Application

Access the Welcome Page:

Open your browser and go to `http://localhost:5000` to see the welcome message.
Test the Visit Count:

Navigate to `http://localhost:5000/count` to see the visit count increment each time you refresh the page.


# RESULTS

```
docker-compose up --scale web=3 --build
```
## Welcome to my Project !:

![AmirBeile5002](https://github.com/user-attachments/assets/d322d970-c715-4004-9ec9-cbc421912be3)

## Count Page :eyes: :

![Count5002](https://github.com/user-attachments/assets/61c84c40-3a59-4d63-9ba1-c0b94c9db90f)
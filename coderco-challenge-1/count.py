import os
from flask import Flask
import redis


app = Flask(__name__)                                               # Creates an instance (flask app)
redis_host = os.getenv('REDIS_HOST', 'REDIS')                       #"os.getenv" import os library. Retrieve redis host from enviroment variables
redis_port = int(os.getenv('REDIS_PORT', 6379))                     # makes application flexible, allowing you to change redis connection details without modifying source code
r = redis.Redis(host=redis_host, port=redis_port)

@app.route('/')
def welcome():
    return 'Welcome to Amir Beile`s Containers Project'

@app.route('/count')
def count():
    count = r.incr('visits')                                         # increments visits
    return f'Your page has been visited {count} times'

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5002)

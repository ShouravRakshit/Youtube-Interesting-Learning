# flask app for hello world
from flask import Flask
import os
import redis
import time

app = Flask(__name__)
cache = redis.Redis(host='redis', port=6379)

def get_hit_count():
    retires=5
    while True:
        try:
            # cache.reset_retry_count()
            return cache.incr('hits')
        except redis.exceptions.ConnectionError as exc:
            if retires == 0:
                raise exc
            retires -= 1
            time.sleep(1)

@app.route('/')
def hello_world():
    count= get_hit_count()
    return f'Hello World! I have been seen {count} times.\n'

import time,os
from flask import Flask
app = Flask(__name__)

hostname = os.environ.get('HOSTNAME','localhost')

@app.route('/')
def hello_world():
    #time.sleep(5)
    return hostname+'v4 - blue deployment \n'

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=8080)

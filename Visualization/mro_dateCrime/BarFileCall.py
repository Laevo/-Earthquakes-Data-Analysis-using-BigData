import os
from flask import Flask
app = Flask(__name__)

@app.route('/')
def welcome():
    return app.send_static_file('index.html')

port = os.getenv('VCAP_APP_PORT', '5012')
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=int(port), debug=True)
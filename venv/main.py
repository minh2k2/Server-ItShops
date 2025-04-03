import time
from flask import Flask
from flask_cors import CORS  # Import CORS

app = Flask(__name__)
CORS(app)  # Cho phép CORS cho tất cả các origin

@app.route('/time')
def get_current_time():
    return {'time': time.time()}

if __name__ == '__main__':
   app.run(debug=True, port=5000)

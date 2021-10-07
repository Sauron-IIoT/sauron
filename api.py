from flask import Flask
from app.route.camera import capture_blueprint

app = Flask(__name__)

app.register_blueprint(capture_blueprint)

@app.route('/', methods=['GET'])
def home():
    return "Hello!"

app.run(host='0.0.0.0', port=5000)
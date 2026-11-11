from flask import Flask
from flask_cors import CORS      # add flask-cors to requirements.txt

app = Flask(__name__)
CORS(app, origins=["https://nexusai-frontend-eight.vercel.app"])
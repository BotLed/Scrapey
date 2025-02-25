from flask import Flask, send_from_directory
from flask_cors import CORS
import os
from api.RedditAPI import Emoo

class App:
    ASSETS_FOLDER = os.path.join(os.path.dirname(__file__), 'assets')

    def __init__(self):
        self.app = Flask(__name__)
        CORS(self.app)
        self.setup_routes()
        
    def setup_routes(self):
        @self.app.route("/")
        def home():
            return {"message": "Welcome to the #1 API"}

        @self.app.route("/message")
        def message():
            return {"title": "The #1 API", "message": "You have entered.... the API ZONE"}
    
        @self.app.route("/assets")
        def assets():
            return {"title": "In assets directory"}

        @self.app.route("/assets/envmap.hdr")
        def send_envmap():
            return send_from_directory(self.ASSETS_FOLDER, "envmap.hdr", as_attachment=False)
        

    def run(self):
        self.app.run(debug=False, host="0.0.0.0", port="7630") # since its just an API

"""Registering the flask blueprints for the web app."""
import os
from flask import Flask
from routes import pages
from pymongo import MongoClient
from dotenv import load_dotenv

load_dotenv()

def create_app():
    """Factory for creating the app"""
    app = Flask(__name__)
    client = MongoClient(os.environ.get("MONGODB_URI"))
    app.db = client.get_default_database()
    
    app.register_blueprint(pages)
    return app


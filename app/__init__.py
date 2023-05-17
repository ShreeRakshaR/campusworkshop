"""Setup at app startup"""
from flask import Flask
import psycopg2


app = Flask(__name__)
postgres = psycopg2.connect(
        host="dpg-chi7n4l269vf5qb9dcig-a.oregon-postgres.render.com",
        database="todo_9hab",
        user="root",
        password="m0K2Eq8u9Z7edbDZAq9dsskXQ9UqxGY1")
# To prevent from using a blueprint, we use a cyclic import
# This also means that we need to place this import here
# pylint: disable=cyclic-import, wrong-import-position
from app import routes

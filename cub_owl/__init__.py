from flask import Flask
from cub_owl.main.test import test as main


app = Flask(__name__)
app.register_blueprint(main)


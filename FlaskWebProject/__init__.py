"""
The flask application package.
"""

from flask import Flask
app = Flask(__name__, static_folder='static', static_url_path='')

import FlaskWebProject.views
import FlaskWebProject.api
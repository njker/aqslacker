from flask import Flask
#from flask_bootstrap import Bootstrap
import os
SECRET_KEY = os.environ['SECRET_KEY']
app = Flask(__name__)
app.config['SECRET_KEY'] = SECRET_KEY
#bootstrap = Bootstrap(app)
from app import routes
app.run(host='0.0.0.0', port=8080)
from flask import Flask
#from flask_bootstrap import Bootstrap
app = Flask(__name__)
app.config['SECRET_KEY'] = "sadhfjaslkdfhasudfh"
#bootstrap = Bootstrap(app)
from app import routes
app.run()
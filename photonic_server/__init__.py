from flask import Flask
from . import modules

app = Flask(__name__)

app.register_blueprint(modules.api.bp, url_prefix="/api")
app.register_blueprint(modules.interface.bp)
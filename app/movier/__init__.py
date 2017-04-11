from flask import abort, Flask, g, render_template, request, send_from_directory
from flask_cors import CORS
from movier.main.routes import main
from movier.config import configure_application
from movier.data.models import db

application = Flask(__name__)
application.config['APPLICATION_ROOT'] = '/daniel'

CORS(application)
configure_application(application)
db.init_app(application)

with application.app_context():
    db.create_all()

application.register_blueprint(main, url_prefix='/')

if __name__ == "__main__":
    application.run(host='0.0.0.0')

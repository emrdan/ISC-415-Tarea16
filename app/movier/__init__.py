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

@application.route("/")
def home():
  return application.send_static_file("reviews.html");

@application.route('/<path:filename>')
def serve_html(filename):
    return send_from_directory("static", filename, as_attachment=False)

@application.route('/css/<path:filename>')
def serve_css(filename):
    return send_from_directory("static/css", filename, as_attachment=False)

@application.route('/js/<path:filename>')
def serve_js(filename):
    return send_from_directory("static/js", filename, as_attachment=False)

if __name__ == "__main__":
    application.run(host='0.0.0.0')

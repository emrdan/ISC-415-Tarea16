from flask import abort, Flask, g, render_template, request, send_from_directory
from flask_cors import CORS
from movier.main.routes import main
from movier.config import configure_app
from movier.data.models import db

app = Flask(__name__)

CORS(app)
configure_app(app)
db.init_app(app)

with app.app_context():
    db.create_all()

app.register_blueprint(main, url_prefix='/')

@app.route("/")
def home():
  return app.send_static_file("reviews.html");

@app.route('/<path:filename>')
def serve_html(filename):
    return send_from_directory("static", filename, as_attachment=False)

@app.route('/css/<path:filename>')
def serve_css(filename):
    return send_from_directory("static/css", filename, as_attachment=False)

@app.route('/js/<path:filename>')
def serve_js(filename):
    return send_from_directory("static/js", filename, as_attachment=False)


# app.py
from flask import Flask
from flask_cors import CORS
from routes.users import users_bp
from routes.scraps import scraps_bp
from routes.stocks import stocks_bp
from routes.comments import comments_bp
from routes.contact import contact_bp
from routes.auth import auth_bp
from routes.watch_list import watch_list_bp
from routes.graph import graph_bp

app = Flask(__name__)

CORS(app, resources={r"/*": {"origins": ["http://localhost:3000", "http://127.0.0.1:3000/"]}})
# CORS(app, resources={
#     r"/users": {"origins": "http://localhost:3000"},
#     r"/another_endpoint": {"origins": ["http://localhost:3000", "http://anotherdomain.com"]}
# })

app.register_blueprint(users_bp)
app.register_blueprint(scraps_bp)
app.register_blueprint(stocks_bp)
app.register_blueprint(comments_bp)
app.register_blueprint(contact_bp)
app.register_blueprint(auth_bp)
app.register_blueprint(watch_list_bp)
app.register_blueprint(graph_bp)

if __name__ == '__main__':
    app.run(debug=True)

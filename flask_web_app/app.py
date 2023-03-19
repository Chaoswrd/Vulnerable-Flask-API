from flask import Flask, jsonify
from models.user_model import User
from Shared.supermodel import db
from Utils.util import log_to_stdout

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:postgres@db:5432/postgres"
db.init_app(app) 

@app.route('/')
def index():
    results = db.session.query(User).all()
    serialised_result = User.serialise_list(results) 
    return jsonify(serialised_result) 


if __name__ == '__main__':
   app.run(debug=True, host="0.0.0.0")

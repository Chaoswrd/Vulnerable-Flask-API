from flask import Flask, jsonify
from models.user import User
from shared.supermodel import db, migrate
from blueprints.sql_injection_endpoint import sql_injection_endpoint


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:postgres@db:5432/postgres"
db.init_app(app) 
migrate.init_app(app, db)
app.register_blueprint(sql_injection_endpoint, url_prefix='/sqlinjection')


@app.route('/')
def index():
    results = db.session.query(User).all()
    serialised_result = User.serialise_list(results) 
    return jsonify(serialised_result) 


if __name__ == '__main__':
   app.run(debug=True, host="0.0.0.0")

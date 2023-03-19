from flask import Flask, jsonify
from BlogPost.blogpost_model import BlogPost
from Shared.supermodel import db
from Utils.util import log_to_stdout

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:postgres@db:5432/postgres"
db.init_app(app) 

with app.app_context():
    db.create_all()

@app.route('/')
def index():
    results = BlogPost.query.all()
    serialised_result = BlogPost.serialise_list(results) 
    return jsonify(serialised_result) 

if __name__ == '__main__':
   app.run(debug=True, host="0.0.0.0")

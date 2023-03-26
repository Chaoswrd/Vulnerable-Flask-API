from flask import Blueprint
from sqlalchemy.sql import text
from Shared.supermodel import db

sql_injection_endpoint = Blueprint('SQL_injection_page', __name__,
                        template_folder='templates')

"""
@sql_injection_endpoint.route('/', defaults={'page': 'index'})
@sql_injection_endpoint.route('/<page>')
def show(page):
    print(f'page: {page}') 
    try:
        return render_template(f'{page}.html')
    except TemplateNotFound:
        abort(404)
"""

@sql_injection_endpoint.route('/<id>')
def unsafe_endpoint(id: int):
    """This endpoint is vulnerable to SQL injection attacks."""
    return [(row.id, row.name) for row in db.session.execute(text(f"SELECT * FROM public.user WHERE id = {id}")).fetchall()]
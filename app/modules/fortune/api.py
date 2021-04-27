from flask import Blueprint, request
from app.core.api_util import create_json_response, ok
from service import FortuneCookieService as service

fortune = Blueprint('fortune', __name__, url_prefix='/api')


@fortune.route('/fortune', methods=['GET'])
def get_fortune():
    response = service.get_fortune()
    return create_json_response(response)


@fortune.route('/fortune/save', methods=['POST'])
def save_fortune():
    data = request.get_json()
    service.save_fortune(data)
    return ok()
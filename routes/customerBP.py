from flask import Blueprint
from controllers.customerController import find_all_paginate, save, find_all

customer_blueprint = Blueprint('customer_bp', __name__)

customer_blueprint.route('/', methods=['POST'])(save)
customer_blueprint.route('/', methods=['GET'])(find_all)
customer_blueprint.route('/paginate', methods=['GET'])(find_all_paginate)
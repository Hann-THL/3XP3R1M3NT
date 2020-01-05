from flask import current_app as app
from flask import Blueprint, jsonify, request
from flask_restful import Api

from routes.classes.public import Public
from routes.classes.protected import Protected

bp = Blueprint('api', __name__)

@bp.before_request
def before_request():
	# Skip validation
	if request.path in ['/api/public']:
		return

	# Secret key validation
	headers = request.headers
	secret_key = headers.get('Secret-Key')
	if secret_key != 'mY53Cr3Tk3Y-':
		return jsonify({ 'message': "INVALID_SECRET_KEY" })

@bp.app_errorhandler(Exception)
def error_handler(error):
	app.logger.exception(error)
	return jsonify({ 'message': "Unhandled exception occured." })

api = Api(bp)

# Routes
api.add_resource(Public, '/public')
api.add_resource(Protected, '/protected')
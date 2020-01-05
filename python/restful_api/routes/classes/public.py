from flask import jsonify, request
from flask_restful import Resource

class Public(Resource):
	def get(self):
		return jsonify({ 'message': 'response from Public.get().' })

	def post(self):
		request_json = request.get_json()
		return jsonify({
			'message': 'You sent the following json to Public.post().',
			'data': request_json
		})
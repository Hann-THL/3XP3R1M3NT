from flask import jsonify, request
from flask_restful import Resource

class Protected(Resource):
	def get(self):
		return jsonify({ 'message': "Hi, I'm from Protected.get()." })

	def post(self):
		request_json = request.get_json()
		return jsonify({
			'message': 'OK, Protected.post() got your data as below.',
			'data': request_json
		})
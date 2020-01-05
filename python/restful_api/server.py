from flask import Flask

def init_app():
	from routes.route import bp
	import db.engines as engines

	app = Flask(__name__)
	init_logger(app)
	engines.init()
	app.register_blueprint(bp, url_prefix='/api')

	return app

def init_logger(app):
	import time
	import logging
	from logging.handlers import TimedRotatingFileHandler

	# Logger
	# filename = time.strftime('log/logfile_%Y-%m-%d %H%M%S.log')
	# handler = TimedRotatingFileHandler(filename, when="midnight", interval=1)
	# handler.suffix = '%Y%m%d %H%M%S'
	# formatter = logging.Formatter('%(asctime)s - %(levelname)s - [in %(pathname)s:%(lineno)d] - %(message)s')
	# handler.setFormatter(formatter)
	# app.logger.addHandler(handler)
	# app.logger.setLevel(logging.INFO)

if __name__ == '__main__':
	app = init_app()
	app.run(host='127.0.0.1', port=5000, debug=True)
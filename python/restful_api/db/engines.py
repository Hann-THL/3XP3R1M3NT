import json

from sqlalchemy import create_engine

engine1 = None
engine2 = None
engine3 = None

def init():
	credentials = None
	with open('./db/config.json', 'r') as f:
		credentials = json.load(f)

	global engine1
	engine1 = __init_engine(credentials['nullpoint_mariadb'])

	global engine2
	engine2 = __init_engine(credentials['dw_mysql'])

	global engine3
	engine3 = __init_engine(credentials['nocrm_mysql'])

def __init_engine(credential):
	username = credential['username']
	password = credential['password']
	host = credential['host']
	port = credential['port']
	db = credential['database']

	return create_engine(f'mysql+pymysql://{username}:{password}@{host}:{port}/{db}', pool_size=50)
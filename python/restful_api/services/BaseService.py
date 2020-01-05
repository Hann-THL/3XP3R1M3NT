import pandas as pd

from flask import Blueprint, jsonify, request

import db.engines as engines

class BaseService:
	def execute(self, query):
		return pd.read_sql_query(query, engines.engine3)
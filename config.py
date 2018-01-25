import os
basedir = os.path.abspath(os.path.dirname(__name__))

class Config(object):
	DEBUG = False
	TESTING = False
	CSRF_ENABLED = True
	SECRET_KEY = 'mr-belvedere'

class ProductionConfig(config):
	DEBUG = False

class StagingConfig(config):
	DEVELOPMENT = True
	DEBUG = True

class TestingConfig(config):
	TESTING = True
	DEBUG = True

class DevelopmentConfig(config):
	TESTING = True
class Config(object):
    TESTING=False
    DEBUG=False
    Uploads="/home/system/Others/pjt/uploads"

class ProductionConfig(Config):
    pass

class DevelopmentConfig(object):
    DEBUG=True

class TestingConfig(object):
    Testing=True

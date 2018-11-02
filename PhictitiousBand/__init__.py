from flask import Flask
from PhictitiousBand.api.routes import mod as api_mod
from PhictitiousBand.site.home.routes import mod as home_mod
from PhictitiousBand.site.merchandise.routes import mod as merch_mod
from PhictitiousBand.site.forum.routes import mod as forum_mod
from PhictitiousBand.admin.routes import mod as admin_mod
import os

def create_app():

    app = Flask(__name__)

    #####################################################
    # Create database resources                         #
    #####################################################
    from PhictitiousBand.admin.models import db as admin_db
    from PhictitiousBand.admin.models import admin_app
    basedir = os.path.abspath(os.path.dirname(__file__))
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////'+os.path.join(basedir, 'data.sqlite')
    # Setting this to false due to warning it was deprecated and being removed in a future release
    # so will not use it at all
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SECRET_KEY'] = 'mysecret'

    #####################################################
    # Init app databases.
    #####################################################
    admin_db.init_app(app)
    #####################################################
    # Register blueprints                               #
    #####################################################
    app.register_blueprint(home_mod)
    app.register_blueprint(api_mod, url_prefix="/api")
    app.register_blueprint(merch_mod, url_prefix='/merchandise')
    app.register_blueprint(forum_mod, url_prefix='/forum')
    app.register_blueprint(admin_mod, url_prefix="/admin") # Admin App for application
    return app

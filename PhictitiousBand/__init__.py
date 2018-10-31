from flask import Flask, current_app
from PhictitiousBand.api.routes import mod as api_mod
from PhictitiousBand.site.home.routes import mod as home_mod
from PhictitiousBand.site.merchandise.routes import mod as merch_mod
from PhictitiousBand.site.forum.routes import mod as forum_mod
from PhictitiousBand.admin.routes import mod as admin_mod

app = Flask(__name__)

# Create database resources
from PhictitiousBand.admin.models import db as admin_db
current_app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////mnt/C/TEMP/FlaskDB/test.db'
current_app.config['SECRET_KEY'] = 'mysecret'

# Admin app database
admin_db.init_app(app)
with app.app_context():
    admin_db.create_all()

app.register_blueprint(home_mod)
app.register_blueprint(api_mod, url_prefix="/api")
app.register_blueprint(merch_mod, url_prefix='/merchandise')
app.register_blueprint(forum_mod, url_prefix='/forum')

# Admin App for application
app.register_blueprint(admin_mod, url_prefix="/admin")

from flask import Flask
from PhictitiousBand.api.routes import mod as api_mod
from PhictitiousBand.site.home.routes import mod as home_mod
from PhictitiousBand.site.merchandise.routes import mod as merch_mod
from PhictitiousBand.site.forum.routes import mod as forum_mod

app = Flask(__name__)

app.register_blueprint(home_mod)
app.register_blueprint(api_mod, url_prefix="/api")
app.register_blueprint(merch_mod, url_prefix='/merchandise')
app.register_blueprint(forum_mod, url_prefix='/forum')

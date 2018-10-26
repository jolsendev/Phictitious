from flask import Flask
from PhictitiousBand.api.routes import mod as api_mod
from PhictitiousBand.site.routes import mod as site_mod

app = Flask(__name__)

app.register_blueprint(site_mod)
app.register_blueprint(api_mod, url_prefix="/api")
print(app.url_map)

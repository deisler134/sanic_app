from sanic import Sanic
from sanic_openapi import swagger_blueprint
from blueprints.manufacturer import blueprint as manufacturer_blueprint
from blueprints.driver import blueprint as driver_blueprint

app = Sanic(__name__)

app.blueprint(swagger_blueprint)
app.blueprint(manufacturer_blueprint)
app.blueprint(driver_blueprint)

app.config.API_VERSION = '1.0.0'
app.config.API_TITLE = 'TEST API'
app.config.API_TERMS_OF_SERVICE = 'Use with caution!'
app.config.API_CONTACT_EMAIL = 'microgalaxy134@gmail.com'

if __name__ == "__main__":
  app.run(host="0.0.0.0", port=8000, debug=True)
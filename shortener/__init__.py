from flask import Flask
from .config.config import config_dict
from .extensions import db, login_manager, cache, limiter
from flask_migrate import Migrate
from .url.routes import shorts
from .qr_code.qr_code import qrcode
from .auth.routes import auth
from .models.users import User
from .models.links import Link



def create_app(config=config_dict['dev']):
    app = Flask(__name__)

    app.config.from_object(config)

    app.config['CACHE_TYPE'] = 'SimpleCache'

    app.config['RATELIMIT_STORAGE_URL'] = 'redis://localhost:6379' 

    db.init_app(app)

    login_manager.init_app(app)

    cache.init_app(app)

    migrate = Migrate(app, db, render_as_batch=True)

    limiter.init_app(app)


    app.register_blueprint(shorts)
    app.register_blueprint(auth)
    app.register_blueprint(qrcode)

    @app.shell_context_processor
    def make_shell_context():
        return {
            'db': db,
            'User': User,
            'Link': Link
        }

    return app
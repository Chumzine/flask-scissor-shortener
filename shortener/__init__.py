from flask import Flask
from .config.config import config_dict
from .extensions import db, login_manager, cache, limiter
from flask_migrate import Migrate
from .url.routes import shorts
from .qr_code.qr_code import qrcode
from .auth.routes import auth
from .models.users import User
from .models.links import Link
from dotenv import load_dotenv



def create_app(config=config_dict['dev']):
    app = Flask(__name__)

    app.config.from_object(config)

    app.config['CACHE_TYPE'] = 'SimpleCache'

    app.config['RATELIMIT_STORAGE_URL'] = 'redis://default:fbthKVsL48xnHQJWiT6kS8PZ0PqzXreU@redis-14288.c114.us-east-1-4.ec2.cloud.redislabs.com:14288' 

    db.init_app(app)

    login_manager.init_app(app)

    cache.init_app(app)

    migrate = Migrate(app, db, render_as_batch=True)

    limiter.init_app(app)

    load_dotenv()


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

    with app.app_context():
        db.create_all()

    return app
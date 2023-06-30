from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_caching import Cache
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address




db = SQLAlchemy()
login_manager = LoginManager()
cache = Cache()
limiter = Limiter(get_remote_address,
  storage_uri= 'redis://default:fbthKVsL48xnHQJWiT6kS8PZ0PqzXreU@redis-14288.c114.us-east-1-4.ec2.cloud.redislabs.com:14288',
  storage_options={"socket_connect_timeout": 30},
  strategy="fixed-window", # or "moving-window"
  )

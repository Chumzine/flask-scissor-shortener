from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_caching import Cache
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address




db = SQLAlchemy()
login_manager = LoginManager()
cache = Cache()
limiter = Limiter(get_remote_address,
  storage_uri= 'redis://localhost:6379',
  storage_options={"socket_connect_timeout": 30},
  strategy="fixed-window", # or "moving-window"
  )

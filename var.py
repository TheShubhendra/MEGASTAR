import os

ENV = bool(os.environ.get("ENV", False))
if ENV:
    from heroku_config import Var as config
else:
    from local_config import Development as config


Var = config

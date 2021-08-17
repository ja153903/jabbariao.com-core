from .common import *

try:
    if ENVIRONMENT == PRODUCTION:
        from .prod import *
    else:
        from .develop import *
except ImportError:
    pass
    
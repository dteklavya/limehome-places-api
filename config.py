from os import getenv


class Config:
    """Set Flask configuration vars from environment."""

    # General Config
    FLASK_APP = getenv('FLASK_APP')
    FLASK_ENV = getenv('FLASK_ENV')
    FLASK_DEBUG = getenv('FLASK_DEBUG')

    HERE_APP_ID = getenv('HERE_APP_ID')
    HERE_APP_CODE = getenv('HERE_APP_CODE')
    HERE_API_URL = getenv('HERE_API_URL')

    IPSTACK_URL=getenv('IPSTACK_URL')
    IPSTACK_API_KEY=getenv('IPSTACK_API_KEY')

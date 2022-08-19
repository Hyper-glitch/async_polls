from aiohttp import web

from aiohttp_polls.setting import postgres_config
from routes import setup_routes

app = web.Application()
setup_routes(app)
app['config'] = postgres_config
web.run_app(app)

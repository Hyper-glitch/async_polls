from aiohttp import web

from aiohttp_polls.db import add_db_engine
from aiohttp_polls.setting import postgres_config
from routes import setup_routes

app = web.Application()
setup_routes(app)
app['config'] = postgres_config
app.cleanup_ctx.append(add_db_engine)
web.run_app(app)

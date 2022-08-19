import aiohttp_jinja2
import jinja2
from aiohttp import web

from aiohttp_polls.db import add_db_engine
from aiohttp_polls.setting import postgres_config, BASE_DIR
from routes import setup_routes

app = web.Application()
setup_routes(app)
app['config'] = postgres_config
aiohttp_jinja2.setup(
    app=app, loader=jinja2.FileSystemLoader(str(BASE_DIR / 'aiohttp_polls' / 'templates'))
)
app.cleanup_ctx.append(add_db_engine)
web.run_app(app)

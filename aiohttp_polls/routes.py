from aiohttp_polls.setting import BASE_DIR
from views import index


def setup_routes(app):
    app.router.add_get('/', index)
    app.router.add_static('/static/', path=BASE_DIR / 'static', name='static')

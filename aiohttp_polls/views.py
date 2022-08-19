from aiohttp import web
import db


async def index(request):
    async with request.app['db'].acquire() as connection:
        cursor = await connection.execute(db.question.select())
        records = await cursor.fetchall()
        questions = [dict(question) for question in records]
        return web.Response(text=str(questions))

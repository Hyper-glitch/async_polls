import aiohttp_jinja2

import db


@aiohttp_jinja2.template('index.html')
async def index(request):
    async with request.app['db'].acquire() as connection:
        cursor = await connection.execute(db.question.select())
        records = await cursor.fetchall()
        questions = [dict(question) for question in records]
        return {'questions': questions}

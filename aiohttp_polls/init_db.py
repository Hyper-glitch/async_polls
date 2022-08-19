from sqlalchemy import MetaData, create_engine

from aiohttp_polls.db import question, choice
from aiohttp_polls.setting import postgres_config

DSN = "postgresql://{user}:{password}@{host}:{port}/{database}"


def create_tables(engine):
    meta = MetaData()
    meta.create_all(bind=engine, tables=[question, choice])


def sample_data(engine):
    connection = engine.connect()
    connection.execute(question.insert(), [
        {
            'question_text': 'What\'s new?',
            'pub_date': '2015-12-15 17:17:49.629+02',
        }
    ])
    connection.execute(choice.insert(), [
        {'choice_text': 'Not much', 'votes': 0, 'question_id': 1},
        {'choice_text': 'The sky', 'votes': 0, 'question_id': 1},
        {'choice_text': 'Just hacking again', 'votes': 0, 'question_id': 1},
    ])
    connection.close()


if __name__ == '__main__':
    db_url = DSN.format(**postgres_config['postgres'])
    engine = create_engine(db_url)
    create_tables(engine)
    sample_data(engine)

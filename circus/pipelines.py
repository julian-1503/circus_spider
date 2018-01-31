import logging

from scrapy import signals

from sqlalchemy import create_engine
from sqlalchemy.engine.url import URL
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import NullPool

from circus.database.base import Base

from circus.database.match import Match
from circus.database.odd import Odd

from circus.items import OddItem, MatchItem

logger = logging.getLogger(__name__)

class CircusPipeline(object):
    def __init__(self, settings):
        self.database = settings.get('DATABASE')
        self.sessions= {}


    @classmethod
    def from_crawler(cls, crawler):
        pipeline = cls(crawler.settings)
        crawler.signals.connect(pipeline.spider_opened, signals.spider_opened)
        crawler.signals.connect(pipeline.spider_closed, signals.spider_closed)
        return pipeline


    def create_engine(self):
        engine = create_engine(URL(**self.database), poolclass=NullPool)
        return engine


    def create_tables(self, engine):
        Base.metadata.create_all(engine, checkfirst=True)


    def create_session(self, engine):
        session = sessionmaker(bind=engine)()
        return session


    def spider_opened(self, spider):
        engine = self.create_engine()
        self.create_tables(engine)
        session = self.create_session(engine)
        self.sessions[spider] = session


    def spider_closed(self, spider):
        session = self.sessions.pop(spider)
        session.close()


    def process_item(self, item, spider):
        session = self.sessions[spider]

        if isinstance(item, OddItem):
            return self.processOdd(item, session)

        if isinstance(item, MatchItem):
            return self.processMatch(item, session)

        return item


    def processOdd(self, item, session):
        odd = Odd(**item)
        try:
            session.add(odd)
            session.commit()
            logger.info('Item {} is in db'.format(odd))
        except:
            session.rollback()
            logger.info('Failed to add {} to db'.format(odd))
            raise

        return item


    def processMatch(self, item, session):
        match = Match(**item)
        try:
            session.add(match)
            session.commit()
            logger.info('Item {} is in db'.format(match))
        except:
            session.rollback()
            logger.info('Failed to add {} to db'.format(match))
            raise

        return item

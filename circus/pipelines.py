# -*- coding: utf-8 -*-

from database.sqlite_database import SQLiteDatabase

class CircusPipeline(object):
    def process_item(self, item, spider):
        with SQLiteDatabase('example.db') as db:
            db.execute("CREATE TABLE ID NOT EXISTS "
                       ""
                      )
        return item

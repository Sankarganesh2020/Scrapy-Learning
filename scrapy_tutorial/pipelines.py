# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import sqlite3


class ScrapyTutorialPipeline(object):

    def __init__(self):
        self.sqlite3_connection()
        self.create_table()

    def sqlite3_connection(self):
        self.conn = sqlite3.connect("myquotes.db")
        self.curr = self.conn.cursor()

    def create_table(self):
        self.curr.execute("""drop table if exists quotes_table""")
        self.curr.execute("""create table quotes_table(
            text text,
            author text,
            tag text
        )""")

    def process_item(self, item, spider):
        self.store_db(item)
        return item

    def store_db(self, item):
        self.curr.execute("""insert into quotes_table values(?,?,?)""",(
            item['text'],
            item['author'],
            item['tag'][0]
        ))
        self.conn.commit()
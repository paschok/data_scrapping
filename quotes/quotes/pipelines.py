# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

# Scraped data -> Item Containers -> json/csv files
# Scraped data -> Item Containers -> Pipeline -> SQL/Mongo DB

import sqlite3


class QuotesPipeline(object):

    def __init__(self):
        self.create_connection()
        self.create_table()

    def create_connection(self):
        self.connection = sqlite3.connect('my_quotes_from_pipeline.db')
        self.cursor = self.connection.cursor()

    def create_table(self):
        # if the table is already created - delete/drop it
        self.cursor.execute("""DROP TABLE IF EXISTS quotes_db""")
        self.cursor.execute("""create table quotes_db(
                                title text,
                                author text,
                                tag text
                                )""")

    def process_item(self, item, spider):
        self.store_db(item)
        return item

    def store_db(self, item):
        self.cursor.execute("""insert into quotes_db values (?, ?, ?)""", (
            item['title'][0],
            item['author'][0],
            item['tag'][0]
        ))
        self.connection.commit()

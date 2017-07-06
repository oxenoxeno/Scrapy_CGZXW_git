# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymssql
import MySQLdb
import json
import codecs
from scrapy.exceptions import DropItem
import sys

# 解决 UnicodeEncodeError: 'ascii' codec can't encode characters in position 126-129: ordinal not in range(128)
reload(sys)
sys.setdefaultencoding('utf-8')

# """ 写JSON """
class ScrapyCgzxwPipeline(object):
    def __init__(self):
        self.file = codecs.open('data.json', mode='wb', encoding='utf-8')  # 数据存储到 data.json

    def process_item(self, item, spider):
        """ json """
        # line = json.dumps(dict(item)) + "\n"
        # self.file.write(line.decode("unicode_escape"))

        """ sql """
        sql = "INSERT INTO [dbo].Article(Title, Contents, DealedContent, NewsType, NewsFrom, ClickCount, AddDate, UpdateDate, Author) VALUES('%s', '%s', '%s', %d, '%s', %d, '%s', GETDATE(), '%s')" \
              % (item['title'], item['content'], item['dealedContent'], item['newsType'], item['newsFrom'],
                 item['clickCount'], item['addDate'], item['author'])
        print sql
        self.file.write(sql + '\n')
        return item


# """ 去重 """
# class DuplicatesPipeline(object):
#
#     def __init__(self):
#         self.ids_seen = set()
#
#     def process_item(self, item, spider):
#         if item['title'] in self.ids_seen:
#             raise DropItem("Duplicate item found: %s" % item)
#         else:
#             self.ids_seen.add(item['id'])
#             return item


""" Mysql """
# class MySQLStorePipeline(object):
#     def __init__(self):
#         self.conn = MySQLdb.connect(user='user', 'passwd', 'dbname', 'host', charset="utf8", use_unicode=True)
#         self.cursor = self.conn.cursor()
#
# def process_item(self, item, spider):
#     try:
#         self.cursor.execute("""INSERT INTO example_book_store (book_name, price)VALUES (%s, %s)""",
#                             (item['book_name'].encode('utf-8'),
#                              item['price'].encode('utf-8')))
#
#         self.conn.commit()
#
#
#     except MySQLdb.Error, e:
#         print "Error %d: %s" % (e.args[0], e.args[1])
#
#     return item


# """ SQL Server """
class SQLServerPipeline(object):
    def __init__(self):
        self.conn = pymssql.connect(host='', user='', password='', database='')
        self.cur = self.conn.cursor()

    def process_item(self, item, spider):
        try:
            sql = "INSERT INTO [dbo].Article(Title, Contents, DealedContent, NewsType, NewsFrom, ClickCount, AddDate, UpdateDate, Author) VALUES('%s', '%s', '%s', %d, '%s', %d, '%s', GETDATE(), '%s')" \
                  % (item['title'], item['content'], item['dealedContent'], item['newsType'], item['newsFrom'],
                     item['clickCount'], item['addDate'], item['author'])
            print sql
            self.cur.execute(sql)
            rows = self.cur.fetchall()
            for row in rows:
                print row[0]
            self.conn.commit()

            # 如果update/delete/insert记得要conn.commit()
            # 否则数据库事务无法提交
            # print (cur.fetchall())
            # all = self.cur.fetchall()

        except pymssql.Error, e:
            print "Error:" + str(e)
            # self.cur.close()
            # self.conn.close()




























































# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


import csv,codecs,cStringIO
from scrapy.conf import settings


class UnicodeWriter:
    def __init__(self, f, dialect=csv.excel, encoding="utf-8-sig", **kwds):
        self.queue = cStringIO.StringIO()
        self.writer = csv.writer(self.queue, dialect=dialect, **kwds)
        self.stream = f
        self.encoder = codecs.getincrementalencoder(encoding)()

    def writerow(self, row):
        '''writerow(unicode) -> None
        This function takes a Unicode string and encodes it to the output.
        '''
        self.writer.writerow([s.encode("utf-8") for s in row])
        data = self.queue.getvalue()
        data = data.decode("utf-8")
        data = self.encoder.encode(data)
        self.stream.write(data)
        self.queue.truncate(0)

    def writerows(self, rows):
        for row in rows:
            self.writerow(row)


class CSVPipeline(object):
    def __init__(self):
        self.csvfile = open('app.csv', 'wb')
        self.workbook = UnicodeWriter(f=self.csvfile)
        fields = settings.get('FIELDS_TO_EXPORT', [])
        if fields:
            self.workbook.writerow(fields)

    def process_item(self, item, spider):
        print 1
        self.workbook.writerow(["GooglePlay",item["name"],item["app_id"],item["category"],item["version"],item["description"],item["improvement"],item["url"],item["update_date"],item["score"],item["download"]])

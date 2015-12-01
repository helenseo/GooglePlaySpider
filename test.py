# !/usr/bin/python
# coding: utf-8

import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )

import re

s = "awvca@GMAIL.com"

pattern = re.compile(r"^[a-z0-9]+([._\\-]*[a-z0-9])*@gmail.com", re.I)

m = pattern.match(s)

if m:
    print m.group(0)


import urllib2

print urllib2.unquote("%E6%89%8B%E6%9C%BA").decode('utf8')


# from scrapy.contrib.loader import ItemLoader
# from myproject.items import Product
# def parse(self, response):
#     l = ItemLoader(item=Product(), response=response)
#     l.add_xpath('name', '//div[@class="product_name"]')
#     l.add_xpath('name', '//div[@class="product_title"]')
#     l.add_xpath('price', '//p[@id="price"]')
#     l.add_css('stock', 'p#stock]')
#     l.add_value('last_updated', 'today') # you can also use literal values	return l.load_item()

# s = "https://play.google.com/store/apps/details?id=com.tencent.mm"
# print s.split("id=")[1]

s = "var fu=true;var pt='chat - Google Play 上的 Andr\u200b\u200boid 应用';" \
    "var ab='';var lmt='';var curl='https://play.google.com/store/search?q\75chat\46c\75apps\46authuser\0750';" \
    "var nbp='[\42/store/search?q\\u003dchat\\u0026c\\u003dapps\42,\42GAEiAghk:S:ANO1ljJkC4I\42,\0420\42,\0420\42,\0420\42]\n';" \
    "var sc='CAESAggG';var pgj=false;var di='';var du=3;window.updateClient = function(){if (fu){if (pt){upt(pt);"

# p1 = r'\'\[.*?\]'
# pattern = r"\'\[.*\\42((?:.(?!\\42))*:S:.*?)\\42.*\]\\n\'"
#
#
# import re
# m = re.match(p1, s, re.M)
# if m:
#     print m.group(0)
# else:
#     print None
#
#
# w = u'\ucee4\ubba4\ub2c8\ucf00\uc774\uc158'
#
# if isinstance(w, unicode):
#     #s=u"中文"
#     print w.encode('gb2312')
# else:
#     #s="中文"
#     print w.decode('utf-8').encode('gb2312')

# import csv,codecs,cStringIO
#
# class UnicodeWriter:
#     def __init__(self, f, dialect=csv.excel, encoding="utf-8-sig", **kwds):
#         self.queue = cStringIO.StringIO()
#         self.writer = csv.writer(self.queue, dialect=dialect, **kwds)
#         self.stream = f
#         self.encoder = codecs.getincrementalencoder(encoding)()
#     def writerow(self, row):
#         '''writerow(unicode) -> None
#         This function takes a Unicode string and encodes it to the output.
#         '''
#         self.writer.writerow([s.encode("utf-8") for s in row])
#         data = self.queue.getvalue()
#         data = data.decode("utf-8")
#         data = self.encoder.encode(data)
#         self.stream.write(data)
#         self.queue.truncate(0)
#
#     def writerows(self, rows):
#         for row in rows:
#             self.writerow(row)
#
#
# EXPORT_FIELDS = [
#     u"市场名",
#     u"名称",
#     u"ID",
#     u"分类",
#     u"版本",
#     u"描述",
#     u"改进",
#     u"URL",
#     u"升级时间",
#     u"评分",
#     u"下载量",
# ]
#
#
#
# with open('your.csv', 'w') as f:
#     uw = UnicodeWriter(f=f)
#     uw.writerow(EXPORT_FIELDS)

import hashlib

s = "d1u9a9n3518"
print hashlib.md5(s).hexdigest()
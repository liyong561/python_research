import scrapy
from scrapy.selector import Selector  # 新的包和类，这些是干啥的呢？HtmlXpath is deprecated
import re
import urllib
import os
import logging


class XiaohuarSpider(scrapy.spiders.Spider):
    """ with open(r"E:\TestFile\xiaohuar.html", "wb") as f:  # 以二进制模式写入，可以直接写对象，w+
          f.write(response.body)
          f.close() 这个地方注释这个类
    """
    name = "xiaohuar"
    allowed_domains = ["xiaohuar.com"]
    start_urls = ['http://www.xiaohuar.com/hua/',
                  ]  # 只爬一个url
    request_urls = []
    test_flags = True
    def parse(self, response):
        # 分析页面,返回的只是一页，如果有分页，要查找分页，其基本原理还是通过解析页面，获得url，然后再发请求。
        # 找到页面中符合规则的内容（校花图片），保存
        # 找到所有的a标签，再访问其他a标签，一层一层的搞下去
        # 如果url是 http://www.xiaohuar.com/list-1-\d+.html,
        # http://www.xiaohuar.com/list-1-7.html 该网页链接就可以访问到内容，说明这个网站很好爬
        hxs = Selector(response)  # 创建查询对象

        self.log("黎勇url" + response.url)
        # reponse.css("title") ,xxx为标签名
        if XiaohuarSpider.test_flags:    # 引用类变量
            for href in response.css("a::attr(href)").extract():
                if re.match("http://www\.xiaohuar\.com/list-1-\d+\.html", href)
                    XiaohuarSpider.request_urls.append(href)
            # print(href) 打印在控制台，格式：  response.css("a::attr(href)")
            # <Selector xpath='descendant-or-self::a/@href' data='http://www.xiaohuar.com/list-1-15.html'>
            # 学习之用，很多不符合代码规范fgr
        if re.match('http://www.xiaohuar.com/p-1-\d+.html', href):
                # 如果url能够匹配到需要爬取的url，即本站url
                 items = hxs.select('//div[@class="item_list infinite_scroll"]/div')  # select中填写查询目标，按scrapy查询语法书写
                 for i in range(len(items)):
                    src = hxs.select(
                        '//div[@class="item_list -=3lkpdfskl;"]/div[%d]//div[@class="img"]/a/img/@src' % i).extract()
                # 查询所有img标签的src属性，即获取校花图片地址
                 name = hxs.select(
                '//div[@class="item_list infinite_scroll"]/div[%d]//div[@class="img"]/span/text()' % i).extract()
               # 获取span的文本内容，即校花姓名
                 school = hxs.select(
                '//div[@class="item_list infinite_scroll"]/div[%d]//div[@class="img"]/div[@class="btns"]/a/text()' % i).extract()
            # 校花学校
                if src:
                    ab_src = "http://www.xiaohuar.com" + src[0]  # 相对路径拼接
                    file_name = "%s_%s.jpg" % (
                     school[0].encode('utf-8'), name[0].encode('utf-8'))
                     # 文件名，因为python27默认编码格式是unicode编码，因此我们需要编码成utf-8
                     file_path = os.path.join("/Users/wupeiqi/PycharmProjects/beauty/pic", file_name)
                     urllib.urlretrieve(ab_src, file_path)

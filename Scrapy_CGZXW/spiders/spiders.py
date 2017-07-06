#   coding:utf-8

from Scrapy_CGZXW.items import ScrapyCgzxwItem
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

class cgzxw_spider(CrawlSpider):
    name = "cgzxw"
    allowed_domains = ["cgzx.org.cn"]
    start_urls = [
        'http://www.cgzx.org.cn/list.php?fid=1&page=1'
    ];

    # 爬取规则: 不带 callback 标识向该类 url 递归爬取
    rules = (
        # Rule(SgmlLinkExtractor(allow=(r'https://nwes.cnblogs.com/n/page\d',))),
        Rule(LinkExtractor(allow=(r'http://www.cgzx.org.cn/list.php\?fid=1&page=\d+',))),
        Rule(LinkExtractor(allow=(r'http://www.cgzx.org.cn/bencandy.php\?fid=1&id=\d+')), callback='parseContent'),
    )

    def parseContent(self, response):
        item = ScrapyCgzxwItem()

        # 解析感兴趣字段
        title = response.xpath('//*[@id="content-con_left-content"]/h3').extract()[0]
        content = response.xpath('//*[@id="content-con_left-content"]//p')  # 拿所有p标签
        # dealedContent = response.xpath('//*[@id="content-con_left-content"]/h3').extract()[0]
        # newsType = response.xpath('//*[@id="content-con_left-content"]/h3').extract()[0]
        newsFrom = response.xpath('//*[@id="content-con_left-content"]/div[1]/span[2]').extract()[0]
        clickCount = response.xpath('//*[@id="content-con_left-content"]/div[1]/span[5]').extract()[0]
        addDate = response.xpath('//*[@id="content-con_left-content"]/div[1]/span[1]').extract()[0]
        # updateDate = response.xpath('//*[@id="content-con_left-content"]/div[1]/span[1]').extract()[0]
        author = response.xpath('//*[@id="content-con_left-content"]/div[1]/span[3]').extract()[0]

        # 填充item
        item['title'] = title[4:-5]                         # <h3>河南实施清洁土壤行动计划</h3>
        item['content'] = ''
        for obj in content:
            item['content'] += obj.extract().replace('\n', '')
        item['dealedContent'] = ''
        item['newsType'] = 0
        item['newsFrom'] = newsFrom[9:-7]                   # <span>来源：农民日报</span>
        item['clickCount'] = int(clickCount[10:-7])         # <span>浏览量：4994</span>
        item['addDate'] = addDate[9:-7]                     # <span>时间：2017-06-21 00:27:47</span>
        # item['updateDate'] = ''
        item['author'] = author[9:-7]                       # <span>作者：张培奇 范亚旭</span>
        print response.url


        yield item


        # 备用
        # for sel in response.xpath('//*[@id="center"]/div[6]/div[1]/div[2]/ul/table/tbody/tr[1]/td/span[1]/a'):
            # item = ScrapyCgzxwItem()
            # item['name'] = sel.xpath('a/div/text()').extract()[0]
            # item['link'] = sel.xpath('a/@href').extract()[0]
            # item['desc'] = sel.xpath('div/text()').extract()[0].strip()
            # yield item






















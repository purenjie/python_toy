import requests
from lxml import html

# 从第一页到第十页爬取数据
for i in range(10):
    url = 'https://book.douban.com/top250?start=%d' % (i * 25)
    content = requests.get(url).content
    sel = html.fromstring(content)

    for i in sel.xpath('//tr[@class="item"]'):
        name = i.xpath('td[2]/div[@class="pl2"]/a/text()')[0].replace(' ', '').replace('\n', '')
        info = i.xpath('td[2]/p[1]/text()')[0]
        rate = i.xpath('td[2]/div[@class="star clearfix"]/span[2]/text()')[0]
        comment_num = i.xpath('td[2]/div[@class="star clearfix"]/span[3]/text()')[0]\
                    .replace('(', '').replace(')','').replace(' ', '').replace('\n', '')

        print(name, info, rate, comment_num)

        with open('豆瓣 Top 250 图书.txt', 'a') as file:
            file.write("书名：%s\n%s\n评分：%s评分人数：%s\n" % (name, info, rate, comment_num))
            file.write("=============================================================\n")
        

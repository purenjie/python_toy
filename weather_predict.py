import requests
from lxml import html

url = 'http://www.weather.com.cn/weather/101091101.shtml'

content = requests.get(url).content
sel = html.fromstring(content)
top = sel.xpath('//ul[@class="t clearfix"]')[0] # 忘记写 [0] top 类型为list
suggestions = sel.xpath('//ul[@class="clearfix"]')[0]

# 生活指数
def shzs():
    l = []
    for i in sel.xpath('//ul[@class="clearfix"]'):
        # 防晒指数
        span_intension = i.xpath('li[1]/span/text()')[0]
        span_product = i.xpath('li[1]/p/text()')[0]
        if len(span_intension) == 1:
            span = '紫外线指数：' + span_intension + '      '+ span_product
        else:
            span = '紫外线指数：' + span_intension + '    '+ span_product
        # 穿衣指数 
        dress_intension = i.xpath('li[4]/a/span/text()')[0]
        dress_sug = i.xpath('li[4]/a/p/text()')[0]
        if len(dress_intension) == 2:
            dress = '穿衣指数：' + dress_intension + '      ' + dress_sug
        else:
            dress = '穿衣指数：' + dress_intension + '    ' + dress_sug
        # 空气指数
        air_condition = i.xpath('li[6]/span/text()')[0]
        air = '空气指数：' + air_condition
        t = (span, dress, air)
        l.append(t)
    return l


def get_tem(top, index):
    tem_low = top.xpath('li[%d]/p[@class="tem"]/i/text()' % index)[0]
    if len(top.xpath('li[%d]/p[@class="tem"]/span' % index)) != 0:
        tem_high = top.xpath('li[%d]/p[@class="tem"]/span/text()' % i)[0] + '℃'
        return tem_low + ' ~' + tem_high
    else:
        return tem_low


for i in range(1, 7+1):
    # 日期
    date = top.xpath('li[%d]/h1/text()' % i)[0]
    # 天气
    weather = top.xpath('li[%d]/p[@class="wea"]/text()' % i)[0]
    # 温度
    tem = get_tem(top, i)
    # 风力
    wind = top.xpath('li[%d]/p[@class="win"]/i/text()' % i)[0]
    print("日期：%s\n天气：%s\n温度：%s\n风力：%s" % (date, weather, tem, wind))
    
    life_condition = shzs() 
    for index in range(3):
        print(life_condition[i-1][index])
    print('==============================================')

    

    
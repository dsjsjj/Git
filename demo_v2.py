import requests
from lxml import etree

url = 'https://so.gushiwen.cn/gushi/tangshi.aspx'
response = requests.get(url)
html = etree.HTML(response.text)
href_list = html.xpath('//div/span/a/@href')
print(href_list)
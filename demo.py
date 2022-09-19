import requests
from lxml import etree

url = 'https://so.gushiwen.cn/shiwenv_b2c5b8e21855.aspx'
response = requests.get(url)
html = etree.HTML(response.text)
#print(response.text)

title = html.xpath('/html/body/div[2]/div[1]/div[2]/div[1]/h1/text()')
author = html.xpath('/html/body/div[2]/div[1]/div[2]/div[1]/p/a[1]/text()')
poetry = html.xpath('//*[@id="contsonb2c5b8e21855"]/text()')



print(title)
print(author)
print(poetry)

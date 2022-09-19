import requests
from lxml import etree





def scrape_index():
    url = "https://so.gushiwen.cn/gushi/tangshi.aspx"
    response = requests.get(url)
    html = etree.HTML(response.text)
    href_list = html.xpath('//div/span/a/@href')
    return url_list

def scrape_detail(url):
    response = requests.get(url)
    html = etree.HTML(response.text)
    title = html.xpath('/html/body/div[2]/div[1]/div[2]/div[1]/h1/text()')
    author = html.xpath('/html/body/div[2]/div[1]/div[2]/div[1]/p/a[1]/text()')
    poetry = html.xpath('//*[@id="contsonb2c5b8e21855"]/text()')
    return {
        'title': title[0],
        'author':author[0],
        'poetry':''.join([i.strip() for i in poetry])
    }
    
    
url_list = scrape_index()
for path in url_list:
    url ='https://so.gushiwen.cn' + path
    detail = scrape_detail(url)

import requests
from lxml import html

def request():
    page = requests.get("https://quotes.toscrape.com/")
    content = html.fromstring(page.content)

    return content


def parse():
    content = request()

    containers = content.xpath('//div[@class="quote"]')

    for container in containers:
        quote = container.xpath('.//span[@class="text"]/text()')
        author = container.xpath('.//small[@class="author"]/text()')
        tags1 = container.xpath('.//div[@class="tags"]/a[1]/text()')
        tags2 = container.xpath('.//div[@class="tags"]/a[2]/text()')
        tags3 = container.xpath('.//div[@class=tags]/a[3]/text()')

        print(quote, author, tags1, tags2, tags3)
parse()
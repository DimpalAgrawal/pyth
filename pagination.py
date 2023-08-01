import requests
from lxml import html


header = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8'
}




page_number = input("Enter no of pages")
for i in range (1,int(page_number)+ 1):
    
    print(i)
    page = requests.get("https://www.flipkart.com/mobiles/pr?sid=tyy%2C4io&p%5B%5D=facets.brand%255B%255D%3DPOCO&ctx=eyJjYXJkQ29udGV4dCI6eyJhdHRyaWJ1dGVzIjp7InRpdGxlIjp7Im11bHRpVmFsdWVkQXR0cmlidXRlIjp7ImtleSI6InRpdGxlIiwiaW5mZXJlbmNlVHlwZSI6IlRJVExFIiwidmFsdWVzIjpbIlNob3AgTm93Il0sInZhbHVlVHlwZSI6Ik1VTFRJX1ZBTFVFRCJ9fX19fQ%3D%3D&otracker=clp_metro_expandable_2_5.metroExpandable.METRO_EXPANDABLE_Shop%2BNow_mobile-phones-store_O1WYX08RHODP_wp2&fm=neo%2Fmerchandising&iid=M_ba10fada-0298-4c59-b1a1-243fa01e6bfa_5.O1WYX08RHODP&ppt=hp&ppn=homepage&ssid=0g09mo6jc00000001680696718637" + str(i), headers = header)
    content = html.fromstring(page.content)

    link = content.xpath("//*[@class='_2kHMtA']/a/@href")
    items = 0
    for url in link:
        page_link = "https://www.flipkart.com" + url
        page = requests.get(page_link, headers=header)
        content = html.fromstring(page.content)
        title = content.xpath('//span[@class="B_NuCI"]/text()')
        price = content.xpath('//div[@class="_25b18c"]/div/text()')
        rating = content.xpath('//div[@class="_3LWZlK"]/text()')
  # image_url = content.xpath('//div[@class="CXW8mj"]/img/@src')
 
        print((title[0]).lstrip(), price[0], rating[0])
        items = items+1

    print(items)

import csv
with open("prawebscraping.py", "r") as fp1:
    with open("pagination1.csv", "w", newline='') as fp2:
        Rs = csv.reader(fp1)
        wp = csv.writer(fp2, delimiter=',')
        for i in Rs:
            wp.writerow(i)
print("File Created") 
    



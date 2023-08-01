import requests
from lxml import html
import csv

header = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8'
}
page_number = input('Enter page number')
with open("amazon_paging.csv", "a", newline="", encoding="utf-8") as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(["Title", "price", "Image"])


    for i in range(1, int(page_number) + 1):
        page = requests.get("https://www.flipkart.com/search?q=monitor&sid=6bo%2Cg0i%2C9no&as=on&as-show=on&otracker=AS_QueryStore_OrganicAutoSuggest_2_8_na_na_na&otracker1=AS_QueryStore_OrganicAutoSuggest_2_8_na_na_na&as-pos=2&as-type=RECENT&suggestionId=monitor%7CMonitors&requestId=d4511c9e-ae73-4c8b-b12d-f27db382a1e5&as-searchtext=monitors&" + str(i), headers = header)
        content = html.fromstring(page.content)
    
    
        link = content.xpath("//div[@class='_2kHMtA']/a/@href")
        for url in link:
            page_link = "https://www.flipkart.com" + url
            page = requests.get(page_link, headers = header)
            content = html.fromstring(page.content)
            title = content.xpath("//span[@class='B_NuCI']/text()")
            price = content.xpath("//div[@class= '_30jeq3 _16Jk6d']/text()")
     
            print(title, price)
            writer.writerow([title, price])
print("CSV Done")

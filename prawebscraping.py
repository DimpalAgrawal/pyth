# import sys
# sys.stdout = open("scrap.csv" ,"w")



import requests
from lxml import html
def request():
  header = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8'
}
  page = requests.get("https://www.amazon.in/Redmi-Mystique-AMOLED-Snapdragon%C2%AE-Triple/dp/B0BQ3PYMCZ/ref=sr_1_1_sspa?keywords=redmi%2Bnote%2B12%2B5g&sr=8-1-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&th=1",headers=header)
  content = html.fromstring(page.content)
  return content
def parse():
  content = request()
  title = content.xpath('//span[@id ="productTitle"]/text()')
  price = content.xpath('//*[@id="corePriceDisplay_desktop_feature_div"]/div[1]/span[2]/span[2]/span[2]/text()')
  rating = content.xpath('//*[@id="acrPopover"]/span[1]/a/span/text()')
  print((title[0]).lstrip(), price[0], rating[0])
parse()
res = request()
print(res)










































import csv
with open("prawebscraping.py", "r") as fp1:
    with open("scrap.csv", "w", newline='') as fp2:
        Rs = csv.reader(fp1)
        wp = csv.writer(fp2, delimiter=',')
        for i in Rs:
            wp.writerow(i)
print("File Created") 




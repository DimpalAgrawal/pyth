import requests
from lxml import html

def email_validator(email):
    url = "https://opportunityhost.com/billing/pwreset.php"
    # csrf_token = "f9fa1c93edd1b99eac8bb5009d6fba897268fe97366a490dcd7ab150"
    action = "reset"
    
      
   
    headers = {'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7', 'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Mobile Safari/537.36', 'content-type' : 'application/x-www-form-urlencoded', 'referer': 'https://www.sunproposal.com/solarizeportal/users/forgotPassword'}

    s = requests.Session()


    response= s.get(url, headers=headers)
    tree = html.fromstring(response.content)
    print(response.status_code)
    csrf_token = tree.xpath('//div[@class="logincontainer"]/form/input/@value')
    token = csrf_token[0]
    print(token)
   

    payload = {"email": email, "token": token, "action": action}
    
    
   



    x = s.post(url, data = payload, headers = headers)
    tree = html.fromstring(x.content)
    print(x.status_code)
    # title = tree.xpath('//div[@class="alert alert-danger text-center"]/text()')
    title = (tree.xpath('//*[@class="col-xs-12 main-content"]/div/div[2]/text()')[0]).strip()
    print(title)

    # print(len(title))
    # title_len = len(title)
    if(title == "No client account was found with the email address you entered"):
        print("Email is not Registered in System")
    else:
        print("Email is Registered in System")


email_validator("aa@gmail.com")
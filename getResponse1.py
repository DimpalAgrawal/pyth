import requests
from lxml import html

def email_validator(email):
    url = "https://www.sunproposal.com/solarizeportal/users/forgotPassword"
    # csrf_token = "f9fa1c93edd1b99eac8bb5009d6fba897268fe97366a490dcd7ab150"
    
      
   
    headers = {'Authority':'www.sunproposal.com', 'Method':'POST',}
# 
    s = requests.Session()


    response= s.get(url, headers=headers)
    tree = html.fromstring(response.content)
    print(response.status_code)
    csrf_token = tree.xpath('///div[@class="users form "]/form/div/input/@value')
    token = csrf_token[0]
    print(token)
   

    payload = {"email": email, "csrf_Token": token}
    
    
   



    x = s.post(url, data = payload, headers = headers)
    tree = html.fromstring(x.content)
    print(x.status_code)
    title = tree.xpath('//div[@class="card-body"]/text()')

    print(title)
    print(len(title))
    title_len = len(title)
    if(title_len == 1):
        print("Email is not Registered in System")
    else:
        print("Email is Registered in System")


email_validator("d.com")
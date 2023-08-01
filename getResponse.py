import requests
from lxml import html

def email_validator(email):
    url = "https://isodiol.com/my-account/lost-password/"
    password = "true"
    woocommerce = "36a8c0bba7"
    referer = "/my-account/lost-password/"

    

    payload = {"user_login": email, "wc_reset_password": password, "woocommerce-lost-password-nonce": woocommerce, "_wp_http_referer": referer}
    headers = {'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8', 'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36'}

    x = requests.post(url, data=payload, headers=headers)
    # print(x.text)
    tree = html.fromstring(x.content)
    # Get element using XPath
    title = tree.xpath('//*[contains(@class, "woocommerce-error")]/li/text()')
    print(title)
    print(len(title))
    title_len = len(title)
    if (title_len== 1):
        print("Invalid username or email.")
    else:
        print("Password reset email has been sent.")

email_validator("d@gmail.com")
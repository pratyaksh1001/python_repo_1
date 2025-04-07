import requests
from bs4 import BeautifulSoup
import smtplib
import lxml

url = "https://www.amazon.com/dp/B075CYMYK6?psc=1&ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6"
user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"
accept_lang = "en-US,en;q=0.7"
header = {
    "User-Agent": user_agent,
    "Accept-Language": accept_lang
}
connection = requests.get(url=url, headers=header)
file = connection.text
soup = BeautifulSoup(file, parser="lxml", features="lxml")
price = soup.select_one("div.a-section.a-spacing-none.aok-align-center.aok-relative span.aok-offscreen")
name = soup.select_one("#productTitle")
print(price.text)
print(name.text)
sender = "pratyakshtest1@gmail.com"
receivers = "pratyakshkarmahe@gmail.com"
mail_connect = smtplib.SMTP("smtp.gmail.com", 587)
mail_connect.login(user="pratyakshtest1@gmail.com",password="hjzo kwbq lujq jqxb")
mail_connect.starttls()
mail_connect.sendmail(from_addr=sender, to_addrs=receivers, msg=f"Subject: Amazon price tracker \n\n{name} \n\n is priced at  - {price}")
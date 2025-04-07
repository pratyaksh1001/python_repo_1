import datetime
from stock import pullstock
from news import pullnews
from twilio.rest import Client
import datetime as dt
l={"apple":"AAPL","IBM":"IBM"}
sender="whatsapp:+14155238886"
receiver="whatsapp:+919303540149"
account_sid="ACb4bfcabf51182731918966066b504110"
auth_token="411a24f447ec5821bfcbd94a52629ee5"
client=Client(account_sid,auth_token)
now=dt.date.today() - datetime.timedelta(days=2)
yesterday = str(now - datetime.timedelta(days=2))
now=str(now)
for i in l.keys():
    stockdata= f"closing of yesterday - {pullstock(l[i])["Time Series (Daily)"][yesterday]["4. close"]} \n closing of today - {pullstock(l[i])["Time Series (Daily)"][now]["4. close"]}\n the difference is - {float(pullstock(l[i])["Time Series (Daily)"][now]["4. close"])-float(pullstock(l[i])["Time Series (Daily)"][yesterday]["4. close"])}"
    final=f"{stockdata}\n\n{pullnews(i)}"
    message=client.messages.create(from_=sender, to=receiver, body=f"{now}\n\n{final}")
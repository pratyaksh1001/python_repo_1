# recover code is - CLMWN3ZT7NTSXJT872W6A362
# TODO the code isn't hosted on pythonanywhere, but environment variables are created on pythonanywhere
from twilio.rest import Client

sender="+14705744259"
receiver="+918708788707"
account_sid="ACb4bfcabf51182731918966066b504110"
auth_token="411a24f447ec5821bfcbd94a52629ee5"
client=Client(account_sid,auth_token)
message=client.messages.create(from_=sender,to=receiver,body=f"")
from twilio.rest import Client
import secrets

client = Client(secrets.account_sid, secrets.auth_token)
def send_message(number,msg):
    message = client.messages.create(
    from_=secrets.from_number,
    to=number,
    body=msg
    )
    return message.sid
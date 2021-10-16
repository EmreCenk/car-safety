from dotenv import load_dotenv

load_dotenv()
import os
from twilio.rest import Client




class sms:
    @staticmethod
    def send(phonenumber, message):
        account_sid = os.environ.get("TWILIO_ACCOUNT_SID")
        auth_token = os.environ.get("TWILIO_AUTH_TOKEN")
        
        sending = Client(account_sid, auth_token)

        our_phone_number = os.environ.get("TWILIO_PHONE_NUMBER")
        sending.messages.create(from_=our_phone_number, to=phonenumber, body=message)
        print("sent successfully")


def on_crash() -> None:
    sms.send("+12265074010", "oh no, this person is dying!")


if __name__ == "__main__":
    sms.send("+12265074010", "testing message")

from twilio.rest import TwilioRestClient
import twilio
import datetime
import os
from dotenv import load_dotenv

load_dotenv()  # Loads variables from .env into the environment


#  KMK MD Account
ACCOUNT_SID = os.getenv(ACCOUNT_SID)
AUTH_TOKEN = os.getenv(AUTH_TOKEN)
PHONE_ALERT = os.getenv(PHONE_ALERT)


# # Lenderboy account
client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN)


# send a message with the error in the body


def error_report_twilio_message(error):
    client.messages.create(
        body='Hello, this is your Vaccine Fridge. The notice is: {}. This happened at {}. '.format(error, datetime.datetime.now()),
        to= PHONE_ALERT
        messaging_service_sid=ACCOUNT_SID

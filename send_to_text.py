from twilio.rest import TwilioRestClient
import twilio
import datetime



#  KMK MD Account
ACCOUNT_SID = "XXXXXXXXXXXXXXXXXXX6f51cd"
AUTH_TOKEN = "XXXXXXXXXXXXXXXXXXXXXXe50ff"

# TESTING Account
TESTING_ACCOUNT_SID = 'XXXXXXXXXXXXXXXXXXXXXXXXXXX9a0f'
TESTING_AUTH_TOKEN = 'XXXXXXXXXXXXXXXXXXXXXXXXXXe97a0d'
TESTING_FROM_NUMBER = '+15005550006'	 # (use this From_:This number passes all validation. No error


# # Lenderboy account
client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN)


# send a message with the error in the body


def error_report_twilio_message(error):
    client.messages.create(
        body='Hello, this is your Vaccine Fridge. The notice is: {}. This happened at {}. '.format(error, datetime.datetime.now()),
        to='5038XXXXXX',
        messaging_service_sid="XXXXXXXXXXXXXXXXXXXXXXXXXX770d7dd")

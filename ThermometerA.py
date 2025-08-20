# !/usr/bin/python
from send_to_text import error_report_twilio_message
import send_to_text
import time
from ubidots import ApiClient
import ubidots
import os 
from dotenv import dotenv

load_dotenv()  # Loads variables from .env into the environment

UBIDOTS_TOKEN = os.getenv(UBIDOTS_TOKEN)
UBIDOTS_VARIABLE_1= os.getenv(UBIDOTS_VARIABLE_1)
UBIDOTS_VARIABLE_2= os.getenv(UBIDOTS_VARIABLE_2)

#id is the id from thermal probe

def main():
    # Script has been called directly
    print 'Waiting for Ethernet'
    time.sleep(30)
    id = '28-00000784c4f5'
    # get temp from file
    print 'Temp : {:.2f} degrees C'.format(gettemp(id) / float(1000))
    print 'Temp : {:.2f} degrees F'.format(gettemp(id) / float(1000) * 9 / 5 + 32)
    celsius = (gettemp(id) / float(1000))
    fahrenheit = 'Temp : {:.2f} degrees F'.format(gettemp(id) / float(1000) * 9 / 5 + 32)
    ubidots_send(celsius)


def gettemp(id):
    try:
        mytemp = ''
        filename = 'w1_slave'
        f = open('/sys/bus/w1/devices/' + id + '/' + filename, 'r')
        line = f.readline()  # read 1st line
        crc = line.rsplit(' ', 1)
        crc = crc[1].replace('\n', '')
        if crc == 'YES':
            line = f.readline()  # read 2nd line
            mytemp = line.rsplit('t=', 1)
        else:
            mytemp = 99999
        f.close()

        return int(mytemp[1])

    except:
        return 99999


### UBIDOTS ###
def ubidots_send(c):
    for x in xrange(5):
        message_send_count = 0
        # todo send notice we are running first loop
        error_report_twilio_message('Lab Vaccine has gone through loop {} times of 5'.format(message_send_count))
        try:
            print "Requesting Ubidots token"
            api = ApiClient(token=UBIDOTS_TOKEN)
            print 'retrieved token'

        except:
            print "No internet connection, retrying..."
            print 'Quitting the program'
            error_report_twilio_message('Lab Fridge has not connected to the internet-retrying')
            continue

        my_variable_C = api.get_variable(UBIDOTS_VARIABLE_1)

        while (1):
            # response = my_variable_C.save_value({"value": c})  # for sending a single variable
            response = api.save_collection([{'variable': UBIDOTS_VARIABLE_1, 'value': c},
                                            {'variable': UBIDOTS_VARIABLE_2, 'value': (32 + (1.8 * c))}])
            print response
				#todo add if statement to send message outside temperature ratings.
				#todo might need a max message count
				#todo get seperate twilio account so can avert comingling and practice
            time.sleep(30)
        message_send_count += 1
        print 'uploaded to ubidots'




def write_values_to_file():
    pass  # want to have a nice dashboard


if __name__ == '__main__':
    main()

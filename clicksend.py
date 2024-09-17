from __future__ import print_function
import os
import random
import clicksend_client
from clicksend_client.rest import ApiException

# Your ClickSend API credentials
api_key = os.environ['clicksend_api_key']
username = os.environ['clicksend_username']

# Configure HTTP basic authorization
configuration = clicksend_client.Configuration()
configuration.username = username
configuration.password = api_key

# Create an instance of the API class
api_instance = clicksend_client.SMSApi(clicksend_client.ApiClient(configuration))

def generate_otp():
    """Generate a random 6-digit OTP."""
    return str(random.randint(100000, 999999))

def send_sms(recipient_number, otp):
    """Send OTP via ClickSend API."""
    message = clicksend_client.SmsMessage(
        to=recipient_number,
        body=f'Your OTP code is {otp}.'
    )
    messages = clicksend_client.SmsMessageCollection(messages=[message])

    try:
        api_response = api_instance.sms_send_post(messages)
        return api_response
    except ApiException as e:
        print("Exception when calling SMSApi->sms_send_post: %s\n" % e)
        return None

def main():
    # Get recipient phone number from user input
    recipient_number = input('Enter the recipient phone number: ')
    
    # Generate and send OTP
    otp = generate_otp()
    response = send_sms(recipient_number, otp)
    
    # Check if SMS was sent successfully
    if response is not None:
        print('OTP sent successfully.')
    else:
        print('Failed to send OTP.')
        return
    
    # Prompt user to enter OTP for verification
    user_otp = input('Enter the OTP you received: ')
    
    # Verify OTP
    if user_otp == otp:
        print('OTP verified successfully.')
    else:
        print('Invalid OTP.')

if __name__ == '__main__':
    main()

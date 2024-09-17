from twilio.rest import Client
import os
import random

# Ensure environment variables are set
twilio_account_sid = os.environ.get('twilio_account_sid')
twilio_auth_token = os.environ.get('twilio_auth_token')
twilio_messaging_service_sid = os.environ.get('twilio_messaging_service_sid')

if not twilio_account_sid or not twilio_auth_token:
    raise EnvironmentError("Twilio account SID and auth token must be set in environment variables.")

if not twilio_messaging_service_sid:
    raise EnvironmentError("Twilio messaging service SID must be set in environment variables.")

client = Client(twilio_account_sid, twilio_auth_token)

# Generate a random OTP code
def generate_otp():
    return str(random.randint(100000, 999999))

# Function to send OTP
def send_otp(phone_number, otp_code):
    try:
        message = client.messages.create(
            from_='+19292544498',
            body=f"Your OTP code is {otp_code}",
            messaging_service_sid=twilio_messaging_service_sid,  # Messaging service is preferred for managing SMS
            to=phone_number
        )
        print(f"OTP code sent to {phone_number}. SID: {message.sid}")
        return True
    except Exception as e:
        print(f"Error sending OTP code: {str(e)}")
        return False

# Function to verify OTP
def verify_code(user_otp, actual_otp):
    return user_otp == actual_otp

if __name__ == "__main__":
    # Step 1: Input phone number via terminal
    phone_number = input("Enter your phone number (in E.164 format, e.g., +1234567890): ")

    # Check if number starts with '+', otherwise assume local Australian format
    if not phone_number.startswith('+'):
        phone_number = '+61' + phone_number[1:]  # Convert to E.164 format for Australia

    # Generate and send OTP
    otp_code = generate_otp()
    send_status = send_otp(phone_number, otp_code)

    if send_status:
        # Step 2: Ask the user for the OTP they received
        user_otp = input("Enter the OTP code sent to your phone: ")

        # Verify the OTP
        if verify_code(user_otp, otp_code):
            print("Phone verification successful!")
        else:
            print("Phone verification failed. Try again.")
    else:
        print("Failed to send OTP.")

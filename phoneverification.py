from twilio.rest import Client
import os
import random

# Twilio credentials (replace with your actual credentials)
account_sid = os.environ['your_account_sid']
auth_token = os.environ['your_auth_token']
verify_service_sid = os.environ['your_verify_service_sid']
twilio_phone_number = os.environ['your_verified_number']

client = Client(account_sid, auth_token)

# Generate a random OTP code
def generate_otp():
    return str(random.randint(100000, 999999))

# Function to send OTP
def send_otp(phone_number, otp_code):
    try:
        message = client.messages.create(
            body=f"Your OTP code is {otp_code}",
            from_=twilio_phone_number,
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

import vonage
import os
import random

# Nexmo API credentials
api_key = os.environ['NEXMO_API_KEY']
api_secret = os.environ['NEXMO_API_SECRET']

# Initialize Nexmo client
client = vonage.Client(key=api_key, secret=api_secret)
sms = vonage.Sms(client)

# Store OTP for verification (in a real application, use a database or a more secure method)
otp_store = {}

# Generate a random OTP code
def generate_otp():
    return str(random.randint(100000, 999999))

# Function to send OTP
def send_otp(phone_number, otp_code):
    responseData = sms.send_message({
        'from': 'YourBrandName',  # Replace with your Nexmo virtual number
        'to': phone_number,
        'text': f'Your OTP code is {otp_code}',
    })
    if responseData['messages'][0]['status'] == '0':
        print(f"OTP sent successfully to {phone_number}")
        return True
    else:
        print(f"Failed to send OTP: {responseData['messages'][0]['error-text']}")
        return False

# Function to verify OTP
def verify_otp(phone_number, otp_code):
    # Retrieve OTP from temporary storage
    stored_otp = otp_store.get(phone_number)
    if stored_otp and stored_otp == otp_code:
        print("Verification successful!")
        return True
    else:
        print("Verification failed. Incorrect OTP.")
        return False

if __name__ == "__main__":
    # Step 1: Input phone number via terminal
    phone_number = input("Enter your phone number (in E.164 format, e.g., +1234567890): ")

    # Generate OTP
    otp_code = generate_otp()

    # Send OTP
    if send_otp(phone_number, otp_code):
        # Store the OTP in the temporary store
        otp_store[phone_number] = otp_code

        # Step 2: Ask the user for the OTP they received
        entered_otp_code = input("Enter the OTP code sent to your phone: ")

        # Step 3: Verify the OTP
        if verify_otp(phone_number, entered_otp_code):
            print("Phone verification successful!")
        else:
            print("Phone verification failed. Try again.")

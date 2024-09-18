from flask import Flask, request, jsonify
from twilio.rest import Client
import os
import random

app = Flask(__name__)

# Ensure environment variables are set
twilio_account_sid = os.environ.get('twilio_account_sid')
twilio_auth_token = os.environ.get('twilio_auth_token')
twilio_messaging_service_sid = os.environ.get('twilio_messaging_service_sid')

if not twilio_account_sid or not twilio_auth_token:
    raise EnvironmentError("Twilio account SID and auth token must be set in environment variables.")
if not twilio_messaging_service_sid:
    raise EnvironmentError("Twilio messaging service SID must be set in environment variables.")

client = Client(twilio_account_sid, twilio_auth_token)

# In-memory storage for OTPs
otp_storage = {}

# Generate a random OTP code
def generate_otp():
    return str(random.randint(100000, 999999))

# Route to test the server is running
@app.route('/')
def home():
    return "Flask is running!"

# Route to send OTP
@app.route('/send-otp', methods=['POST'])
def send_otp():
    phone_number = request.form.get('phone_number')

    if not phone_number:
        return jsonify({"error": "Phone number is required"}), 400

    # Convert phone number to E.164 format if not already
    if not phone_number.startswith('+'):
        phone_number = '+61' + phone_number[1:]  # Convert to E.164 format for Australia

    otp_code = generate_otp()
    try:
        message = client.messages.create(
            from_='+19292544498',
            body=f"Your OTP code is {otp_code}",
            messaging_service_sid=twilio_messaging_service_sid,
            to=phone_number
        )

        # Store OTP code associated with phone number
        otp_storage[phone_number] = otp_code

        return jsonify({"message": "OTP sent", "otp_code": otp_code}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Route to verify OTP
@app.route('/verify-otp', methods=['POST'])
def verify_otp():
    phone_number = request.form.get('phone_number')
    user_otp = request.form.get('user_otp')

    if not phone_number or not user_otp:
        return jsonify({"error": "Phone number and OTP are required"}), 400

    # Convert phone number to E.164 format if not already
    if not phone_number.startswith('+'):
        phone_number = '+61' + phone_number[1:]  # Convert to E.164 format for Australia

    actual_otp = otp_storage.get(phone_number)

    if actual_otp is None:
        return jsonify({"error": "No OTP found for this phone number"}), 404

    if user_otp == actual_otp:
        # OTP verified, remove it from storage
        del otp_storage[phone_number]
        return jsonify({"message": "OTP verified successfully"}), 200
    else:
        return jsonify({"error": "Invalid OTP"}), 400

if __name__ == "__main__":
    app.run(debug=True)

Phone Verification using OTP
Author: Aphiwut Janphet
Repository: phoneverification

📌 Overview
This project implements a phone verification system using One-Time Passwords (OTP). It supports multiple SMS providers, including Twilio, Nexmo (Vonage), and ClickSend, to send verification codes to users' phone numbers.

🚀 Features
Multi-Provider Support: Easily switch between Twilio, Nexmo, and ClickSend for sending OTPs.
Configurable OTP Settings: Customize OTP length, expiration time, and retry attempts.
Secure Verification: Ensures OTPs are securely generated, stored, and validated.
🛠️ Technologies Used
Python 3.x 🐍
Flask 🌐 (for API endpoints)
Requests 📡 (for HTTP requests to SMS providers)
PyOTP 🔑 (for OTP generation and validation)
📥 Installation
1️⃣ Clone the Repository
bash
Copy
Edit
git clone https://github.com/aphiwut-j/phoneverification.git
cd phoneverification
2️⃣ Create a Virtual Environment (Recommended)
bash
Copy
Edit
python -m venv venv
source venv/bin/activate  # For macOS/Linux
venv\Scripts\activate     # For Windows
3️⃣ Install Required Packages
bash
Copy
Edit
pip install -r requirements.txt
If requirements.txt is missing, install the dependencies manually:

bash
Copy
Edit
pip install flask requests pyotp
🏃 Usage
Configure Environment Variables:

Set up the necessary environment variables for your chosen SMS provider:

Twilio:

TWILIO_ACCOUNT_SID
TWILIO_AUTH_TOKEN
TWILIO_PHONE_NUMBER
Nexmo (Vonage):

NEXMO_API_KEY
NEXMO_API_SECRET
NEXMO_FROM_NUMBER
ClickSend:

CLICKSEND_USERNAME
CLICKSEND_API_KEY
CLICKSEND_FROM_NUMBER
Run the Application:

bash
Copy
Edit
python phoneverification.py
API Endpoints:

Send OTP:

http
Copy
Edit
POST /send_otp
Content-Type: application/json

{
  "phone_number": "+1234567890"
}
Verify OTP:

http
Copy
Edit
POST /verify_otp
Content-Type: application/json

{
  "phone_number": "+1234567890",
  "otp": "123456"
}
📂 Project Structure
markdown
Copy
Edit
phoneverification/
├── api/
│   ├── __init__.py
│   ├── routes.py
│   └── utils.py
├── providers/
│   ├── __init__.py
│   ├── clicksend.py
│   ├── nexmo_vonage.py
│   └── twilio_client.py
├── tests/
│   ├── __init__.py
│   └── test_phoneverification.py
├── phoneverification.py
├── requirements.txt
└── README.md

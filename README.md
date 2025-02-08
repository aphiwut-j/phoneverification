# Phone Verification using OTP

**Author:** Aphiwut Janphet  
**Repository:** [phoneverification](https://github.com/aphiwut-j/phoneverification)

## Overview

This project implements a phone verification system using One-Time Passwords (OTP). It supports multiple SMS providers, including Twilio, Nexmo (Vonage), and ClickSend, to send verification codes to users' phone numbers.

## Features

- **Multi-Provider Support:** Easily switch between Twilio, Nexmo, and ClickSend for sending OTPs.
- **Configurable OTP Settings:** Customize OTP length, expiration time, and retry attempts.
- **Secure Verification:** Ensures OTPs are securely generated, stored, and validated.

## Technologies Used

- Python 3.x
- Flask (for API endpoints)
- Requests (for HTTP requests to SMS providers)
- PyOTP (for OTP generation and validation)

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/aphiwut-j/phoneverification.git
cd phoneverification
```

### 2. Create a Virtual Environment (Recommended)

```
python -m venv venv
source venv/bin/activate  # For macOS/Linux
venv\Scripts\activate     # For Windows
```

### 3. Install Required Packages
```
pip install -r requirements.txt
```


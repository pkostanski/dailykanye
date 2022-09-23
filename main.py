"""
This is a simple script that requests a Kanye West's quote from Kanye API and sends it via SMS
"""

import requests
import os
from twilio.rest import Client

TWILIO_ACCOUNT_SID = os.environ.get("TWILIO_API_KEY")
TWILIO_AUTH_TOKEN = os.environ.get("TWILIO_AUTH_TOKEN")

TWILIO_PHONE_NUM = "your_twilio_phone_number"
RECEIVER_PHONE_NUM = "+00123456789"


response = requests.get(url="https://api.kanye.rest")
response.raise_for_status()
data = response.json()
quote = data["quote"]

client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

message = client.messages.create(
            body=f"Your daily Kanye West quote is: {quote}",
            from_=f"{TWILIO_PHONE_NUM}",
            to=f"{RECEIVER_PHONE_NUM}"
        )

print(message.sid)

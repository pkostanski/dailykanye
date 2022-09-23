# Daily Kanye

This is a simple script that requests a Kanye West's quote from Kanye API and sends it via SMS.

## Installation

First, install the dependencies with 
```bash
pip install -r /path/to/requirements.txt
```

Then, set your environment variables with Twilio credentials  
```bash
export TWILIO_ACCOUNT_SID=YOUR_ACC_SID
export TWILIO_AUTH_TOKEN=YOUR_AUTH_TOKEN
```

## Usage

Once you've done with the above steps, you're good to go. Remember to provide main.py with both your and your 
SMS receiver's phone number. When you will have everything set up, simply run the script with 
```bash
python3 main.py
```

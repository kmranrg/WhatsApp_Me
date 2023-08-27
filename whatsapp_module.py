import pywhatkit as kit
from datetime import datetime, timedelta

# Calculate the time for the next minute
now = datetime.now()
next_minute = now + timedelta(minutes=1)

# Format the time in 24-hour format (HH:MM)
send_time = next_minute.strftime("%H:%M")

# Recipient's phone number
recipient_number = open('phno.txt').read()  # Replace with the recipient's WhatsApp number

# Message to send
message = "Hello, this is a message sent using PyWhatKit and scheduled for the next minute!"

# Send the WhatsApp message
kit.sendwhatmsg(recipient_number, message, next_minute.hour, next_minute.minute)
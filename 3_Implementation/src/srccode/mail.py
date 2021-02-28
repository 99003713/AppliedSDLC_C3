import os
import smtplib
import imghdr
from email.message import EmailMessage

EMAIL_ADDRESS = os.environ.get('EMAIL_USER')
EMAIL_PASSWORD = os.environ.get('EMAIL_PASS')

contacts = ['YourAddress@gmail.com', 'test@example.com']

msg = EmailMessage()
msg['Subject'] = 'Check out Bronx as a puppy!'
msg['From'] = 'nadarm433@gmail.com'
msg['To'] = 'okankit1312@gmail.com'

msg.set_content('This is a plain text email')
with open('ok.jpg','rb') as f:
    file_data = f.read()
    file_type = imghdr.what(f.name)
    file_name = f.name
msg.add_attachment(file_data,maintype='image',subtype=file_type)


with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login('nadarm433@gmail.com', 'Ankit@7065')
    smtp.send_message(msg)
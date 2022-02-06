import os
import smtplib
from email.message import EmailMessage

# Email and password saved as environment variables locally.
user = os.environ.get('NOTTER_USER')
password = os.environ.get('NOTTER_PASS')

reciever = ""  # Dummy reciever

# Setup message
msg = EmailMessage()
msg['Subject'] = 'Email Subject'
msg['From'] = user
msg['To'] = reciever
msg.set_content('Email Body')

##WITH SSL##
with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login(user, password)

    smtp.send_message(msg)

##WITHOUT SSL##
# with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
#     smtp.ehlo()
#     smtp.starttls()
#     smtp.ehlo()

#     smtp.login(user, password)

#     subject = 'Email Subject'
#     body = 'Email Body'

#     msg = f'Subject: {subject}\n\n{body}'

#     smtp.sendmail(user, reciever, msg)

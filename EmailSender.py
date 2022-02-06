import os
import smtplib
from email.message import EmailMessage

# Email and password saved as environment variables.
user = os.environ.get('NOTTER_USER')
password = os.environ.get('NOTTER_PASS')

# Setup message
msg = EmailMessage()
msg['Subject'] = 'Test Subject'
msg['From'] = user
msg['To'] = user
msg.set_content('Test Body')

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

#     subject = 'Bae?'
#     body = 'Sammen?'

#     msg = f'Subject: {subject}\n\n{body}'

#     smtp.sendmail(user, user, msg)

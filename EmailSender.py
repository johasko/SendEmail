import os
import smtplib
import imghdr
from email.message import EmailMessage

##Email and password saved as environment variables locally.##
user = os.environ.get('NOTTER_USER')
password = os.environ.get('NOTTER_PASS')

##Dummy recipient##
reciever = "test@testmail.com"

##Setup message##
msg = EmailMessage()
msg['Subject'] = 'Email Subject'
msg['From'] = user
msg['To'] = reciever
msg.set_content('Email Body')

##FILE ATTACHMENT##
with open('test.jpg', 'rb') as f:

    ##.JPG##
    file_data = f.read()
    file_type = imghdr.what(f.name)
    file_name = f.name

    ##.PDF##
    # file_data = f.read()
    # file_name = f.name

##IMAGE##
msg.add_attachment(file_data, maintype='image',
                   subtype='file_type', filename=file_name)

##PDF##
# msg.add_attachment(file_data, maintype='application',
#                    subtype='octet-stream', filename=file_name)

##HTML##
msg.add_alternative("""\
    <!DOCTYPE html>
    <html>
        <body>
            <h1 style="color:SlateGray;">HTML Test</h1>
        </body>
    </html>
""", subtype='html')

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

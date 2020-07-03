'''
Created on 03-Jul-2020

@author: resha
'''
import smtplib
from email.message import EmailMessage

email = EmailMessage()
email['from'] = 'Reshav Raj'
email['to'] = 'reshavabcdexyz@gmail.com'    #receiver email id
email['subject'] = 'Learning Purpose'

email.set_content('Hey. How r u.?? Hope you are doing well.')

with smtplib.SMTP(host='smtp.gmail.com', port = 587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('your_email_address','your_password')
    smtp.send_message(email)
    #print("Message sent.!!")

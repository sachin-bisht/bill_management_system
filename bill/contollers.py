import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email import encoders
import os
import json

from celery import shared_task, task

@task
def ok():
    return 2

# @shared_task()
def sentmail(email, bill_name, bill_amount):

    if(bill_amount == None):
        bill_amount = 'Not available'

    # fromaddr = "no-reply@everyulb.com"
    fromaddr = "sachinbisht939@gmail.com"
    passwd = "kbhezuidtwgubbbc"
    toaddr = email
    try:
        msg = MIMEMultipart()

        msg['From'] = 'sachinbisht939@gmail.com'
        msg['To'] = f'{toaddr.split("@")[0]}'
        msg['Subject'] = "Bill Reminder"

        body = f"Hi {toaddr.split('@')[0]},\nBill name : {bill_name} \nBill amount : {bill_amount}"

        msg.attach(MIMEText(body, 'plain'))

        # FOR file attachment
        # filename = ""
        # attachment = open("", "rb")
        # part = MIMEBase('application', 'octet-stream')
        # part.set_payload((attachment).read())
        # encoders.encode_base64(part)
        # part.add_header('Content-Disposition', "attachment; filename= {}".format(filename))
        # msg.attach(part)
        # SMTP mail.

        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(fromaddr, passwd)
        text = msg.as_string()
        server.sendmail(fromaddr, toaddr, text)
        server.quit()
    except Exception as e:
        print(e)
        return False
    return True
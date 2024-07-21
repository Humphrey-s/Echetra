#!/usr/bin/python3
import smtplib, ssl
from uuid import uuid4
port = 465 

code = str(uuid4())
code = code[-4:]

smtp_server = "smtp.gmail.com"
sender_email = "echetrateam@gmail.com"
receiver_email = "humphreyagoda@gmail.com"
password = "bdry zmnz gcrg plaz"


message = f"""\
Subject: Your sign-in code: {code}
Please copy and paste the 6-digit code below into the number fields of your sign-in process. {code}
"""

context = ssl.create_default_context()

with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message)
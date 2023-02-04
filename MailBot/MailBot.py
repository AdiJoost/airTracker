"""
Author: Adrian Joost
created: September 2022
Notes:

Hellper-functions for sending E-Mails. 
Currently not functional.
"""

import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import os

#^Data to log in
port = 465
password = os.environ.get('airTrackerPW')
sender_mail = os.environ.get('airTrackerMail')
context = ssl.create_default_context()

print(password)
print(sender_mail)
def getFile(path):
	with open(path, "r") as file:
		part = MIMEBase("application", "octet-stream")
		part.set_payload(file.read())
	encoders.encode_base64(part)
	part.add_header(
    "Content-Disposition",
    f"attachment; filename= {path}",
	)
	return part


def sendMail(text = '', subject = '', reciver = sender_mail, path=None):
	message = MIMEMultipart()
	message['Subject'] = subject
	message['From'] = 'AirTracker'
	message['to'] = reciver
	textString = text
	textAsMIME = MIMEText(textString,"plain")
	message.attach(textAsMIME)
	if path:
		part = getFile(path)
		message.attach(part)
	sendTrueMail (message, reciver)


def sendTrueMail(message, reciver):
	server = smtplib.SMTP_SSL("smtp.gmail.com", port)
	server.login(sender_mail,password)
	server.sendmail(sender_mail,reciver,message.as_string())
	server.quit()

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_email(subject, message, sender, receiver, password):
    msg = MIMEMultipart()
    msg['From'] = sender
    msg['To'] = receiver
    msg['Subject'] = subject

    msg.attach(MIMEText(message, 'plain'))

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(sender, password)
    text = msg.as_string()
    server.sendmail(sender, receiver, text)
    server.quit()


with open('receivers.txt', 'r') as file:
    receiver = [line.strip() for line in file]

subject = input("Add subject ")
message=input("Add your message ")
sender = input("Add your email ")
password = input("Add your password ")

x=0
for r in receiver:
    send_email(subject, message, sender, receiver[x], password)
    x=x+1
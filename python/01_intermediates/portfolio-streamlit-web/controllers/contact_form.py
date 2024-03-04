import smtplib, ssl

host = 'smtp.gmail.com'
port = 465

username = 'admin@gmail.com'
password = 'gmail-app-password'

receiver_email = 'visitors@gmail.com'
message = """\
Subject: Hi there

This message is sent from Python."""

context = ssl.create_default_context()

with smtplib.SMTP_SSL(host, port, context=context) as server:
    server.login(username, password)
    server.sendmail(username, receiver_email, message)

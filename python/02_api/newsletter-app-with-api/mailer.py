import smtplib,ssl

def send_mail(message):

    host = "smtp.gmail.com"
    port = 465

    username = "obsidines@gmail.com"

    # Use your own smtp password
    password = "elaxwpzwphybrblu"

    receiver_mail = "obsidines@gmail.com"
    context = ssl.create_default_context()

    server = smtplib.SMTP_SSL(host=host, port=port, context=context)
    server.login(username,password)
    server.sendmail(username,receiver_mail,message)
        
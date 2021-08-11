import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders


def sendanemail(emailid, message, logs):
    sender = "sender@gmail.com"
    password = "password"

    msg = MIMEMultipart()
    msg['From'] = sender
    msg['To'] = emailid
    msg['Subject'] = "Service Status Notification"

    msg.attach(MIMEText(message,'plain'))

    attachment = open(logs, "rb")

    p = MIMEBase('application','octet-stream')
    p.set_payload((attachment).read())

    encoders.encode_base64(p)

    p.add_header('Content-Desposition',"attachment; logs")

    msg.attach(p)

    s = smtplib.SMTP('smtp.gmail.com',587)
    s.starttls()
    s.login(sender, password)
    text = msg.as_string()
    s.sendmail(sender, emailid, text)
    s.quit()
    return print('mail sent')
#coding: utf-8  
import smtplib
from email.mime.text import MIMEText

print("******Welcome to site******")
sender = '******@163.com'
receiver = '******@qq.com'
subject = 'python email test'
host = 'smtp.163.com'
port=25
username = '******@163.com'
password = '******'

message='<h1>Attention</h1><p>This is a message from pi.</p>The address is 192.168.3.6 %s from M</p>' % "thank you."
msg = MIMEText(message, 'html', 'utf-8')
msg['Subject'] = 'raspberrypi'
msg['from'] = sender
msg['to'] = receiver

try:
    smtp = smtplib.SMTP(host, port)
    smtp.login(username, password )
    smtp.sendmail( sender, receiver, msg.as_string())
    print("Send to %s successfully" % receiver)
    smtp.quit()
except smtplib.SMTPException:
        print("******Error!******")

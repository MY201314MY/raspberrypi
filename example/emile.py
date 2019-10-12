#coding: utf-8  
import smtplib
from email.mime.text import MIMEText
def detect(value):
    sender = '176348@163.com'
    receiver = '347766@qq.com'
    host = 'smtp.163.com'
    port=25
    username = '17634@163.com'
    password = ''

    message='<h1>水质报警提醒</h1><p>This is a message from pi.</p>The address is 192.168.3.16 from M</p>'\
        +'<h3>TDS传感器检测到您当前的水质不符合安全标准，请及时更换滤芯以保证水源。</h3>'\
        +'<h3>TDS传感器当前测得的值为:{0}</h3>'.format(value)\
        +'<p>感谢您的使用!</p>'
    msg = MIMEText(message, 'html', 'utf-8')
    msg['Subject'] = '智能饮水'
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

detect(20)

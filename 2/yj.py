import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
#仅适用于发送文本信息邮件
mail_host="smtp.163.com"#你的发件邮箱的服务器地址
mail_sender = "******@163.com"#你的发件邮箱地址
mail_license = "********"#你的发件邮箱授权码
mail_receivers = ["******@***.***"]#你的收件邮箱地址
mm = MIMEMultipart('related') 
subject_content = """Test Email"""#你要发的邮件主题
mm["From"] = "Server<******@163.com>"#发件人信息
mm["To"] = "******@***.***>"#收件人信息
mm["Subject"] = Header(subject_content,'utf-8')
body_content = "This is a test email by python!"#你要发的邮件内容
message_text = MIMEText(body_content,"plain","utf-8")
mm.attach(message_text)
stp = smtplib.SMTP()
stp.connect(mail_host, 25)  
stp.login(mail_sender,mail_license)#登录
stp.sendmail(mail_sender, mail_receivers, mm.as_string())
stp.quit()#结束
#Writen by TZX.
#2021.6.16

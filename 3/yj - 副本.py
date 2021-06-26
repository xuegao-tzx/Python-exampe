import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
#stp.quit()#结束华为云天气预报助手
#Writen by TZX.
#2021.6.15.
xinxi="python测试"
def youjian(xinxi):
     mail_host="smtp.163.com"#你的发件邮箱的服务器地址
     mail_sender = "m13753187762@163.com"#你的发件邮箱地址
     mail_license = "CIPASUZXYIMHISSO"#你的发件邮箱授权码
     mail_receivers = ["2013040111@st.nuc.edu.cn","x19135127762@petalmail.com"]#你的收件邮箱地址
     mm = MIMEMultipart('related') 
     subject_content = "天气预报"
     mm["From"] = "HUAWEI-CLOULD<m13753187762@163.com>"
     mm["To"] = "TZX<2013040111@st.nuc.edu.cn>,TZX<x19135127762@petalmail.com>"
     mm["Subject"] = Header(subject_content,'utf-8')
     body_content = xinxi
     message_text = MIMEText(body_content,"plain","utf-8")
     mm.attach(message_text)
     stp = smtplib.SMTP_SSL(mail_host)
     stp.connect(mail_host,465)
     stp.login(mail_sender,mail_license)
     stp.sendmail(mail_sender, mail_receivers, mm.as_string())
     stp.quit()
youjian(xinxi)

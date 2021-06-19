# -*- coding:utf-8 -*-
###假期版###
###如果是云函数，函数执行入口为:DAKALX.main###
###本程序仅供学术研究，请勿滥用！如出现任何问题与本人无关###
import random
import requests
import json
import smtplib
import time
import datetime
from DKXX import dz
from DKXX import id_list_1
from TSXX import mail_host
from TSXX import mail_sender
from TSXX import mail_license
from TSXX import mail_receivers
from TSXX import sckey
from TSXX import wxpusheruid
from TSXX import appToken
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
from urllib import parse
class Daka():
    def __init__(self,sfzh,dizhi,temp,fhz,xinxi,r,start2,end1,sc,zsc,mins,secs,day,hour,mins1,secs1):
        self.sfzh=sfzh
        self.dizhi=dizhi
        self.temp=temp
        self.fhz=fhz
        self.xinxi=xinxi
        self.r=r
        self.start2=start2
        self.end1=end1
        self.sc=sc
        self.zsc=zsc
        self.mins=mins
        self.secs=secs
        self.day=day
        self.hour=hour
        self.mins1=mins1
        self.secs1=secs1
    @classmethod
    def daka(self,sfzh,dizhi='中国'):
        print(f'{sfzh}开始打卡')
        dizhi = parse.quote(dizhi)
        temp = random.randint(358, 368) / 10#随机温度
        try:
            r = requests.post(
                url='http://yx.ty-ke.com/Home/Monitor/monitor_add',
                headers={'Content-Type': 'application/x-www-form-urlencoded; charset=utf-8','Accept-Encoding': 'gzip'},
                data=f'mobile={sfzh}&city=%E5%A4%AA%E5%8E%9F%E5%B8%82&jk_type=%E5%81%A5%E5%BA%B7&district=%E5%B0%96%E8%8D%89%E5%9D%AA%E5%8C%BA&address={dizhi}&title={temp}&jc_type=%E5%90%A6&wc_type=%E5%90%A6&is_verify=0&province=%E5%B1%B1%E8%A5%BF%E7%9C%81'
            )
            fhz = json.loads(r.text)
        except:
            date=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            xinxi="请求出错！联系老师吧，不是本程序出错，是打卡的服务器抽疯了。。。"
            print(xinxi)#如果本地运行，则只需保留本语句
            #如果选择云函数运行，则建议保留以下3条语句之一即可
            self.youjian(xinxi)#如果你选择邮件通知你打卡状况，则保留本语句，并且做好相应配置
            self.wxpusher(xinxi)#如果你选择WxPusher通知你打卡状况，则保留本语句，并且做好相应配置
            self.server(xinxi)#如果你选择Server酱通知你打卡状况，则保留本语句，并且做好相应配置
            print("无法打卡，但日志发送成功！")
            return False
        if fhz['code'] != '200':
            date=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            xinxi="身份证号为:"+sfzh+"的学生打卡失败!"+"失败原因：["+str(fhz['msg'])+"]"+date
            #如果选择云函数运行，则建议保留以下3条语句之一即可
            self.youjian(xinxi)#如果你选择邮件通知你打卡状况，则保留本语句，并且做好相应配置
            self.wxpusher(xinxi)#如果你选择WxPusher通知你打卡状况，则保留本语句，并且做好相应配置
            self.server(xinxi)#如果你选择Server酱通知你打卡状况，则保留本语句，并且做好相应配置
            print(f'身份证号为:{sfzh}的学生打卡失败，但日志发送成功！')
            return False
        else:
            print(f'打卡成功，打卡温度:{temp}')#由于如果多人打卡发送消息过多，所以此处默认只在输出处通知你
        return True
    @classmethod
    def dakazhu(self):
        start=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        start1=time.strptime(start,'%Y-%m-%d %H:%M:%S')
        start2=int(time.mktime(start1))
        print('打卡遍历开始')
        for sfzh in id_list_1:
            self.daka(sfzh,dizhi)
        date=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        end=time.strptime(date,'%Y-%m-%d %H:%M:%S')
        end1=int(time.mktime(end))
        sc=end1-start2
        zsc=end1-1624084113
        mins=int(sc/60)
        secs=int(sc%60)
        day=int(zsc/86400)
        hour=int(zsc/3600)
        mins1=int(zsc/60)
        secs1=int(zsc%60)
        xinxi="打卡遍历完成！全自动打卡平台V3.0在"+date+"运行正常！"+"\r\n"+"累计目前，全自动打卡平台已正常运行:"+str(day)+"天"+str(hour)+"时"+str(mins1)+"分"+str(secs1)+"秒."+"\r\n"+"本次运行时长:"+str(mins)+"分"+str(secs)+"秒."
        #如果选择云函数运行，则建议保留以下3条语句之一即可
        self.youjian(xinxi)#如果你选择邮件通知你打卡状况，则保留本语句，并且做好相应配置
        self.wxpusher(xinxi)#如果你选择WxPusher通知你打卡状况，则保留本语句，并且做好相应配置
        self.server(xinxi)#如果你选择Server酱通知你打卡状况，则保留本语句，并且做好相应配置
    ##########----------推送消息区----------##########    
    ###方法一:(推荐)
    ###邮件推送－－－开始－－－###
    #服务方：各种支持SMTP的邮箱
    #所需信息：
    #1.你的发件邮箱地址
    #2.你的收件邮箱地址
    #3.你的发件邮箱登陆授权码
    @classmethod
    def youjian(self,xinxi):
        mm = MIMEMultipart('related') 
        subject_content = "打卡反馈"#消息的标题
        mm["From"] = mail_sender
        mm["To"] = mail_receivers
        mm["Subject"] = Header(subject_content,'utf-8')
        body_content = xinxi#消息的内容
        message_text = MIMEText(body_content,"plain","utf-8")
        mm.attach(message_text)
        stp = smtplib.SMTP()#如需用SLL，改为stp = smtplib.SMTP_SLL()
        stp.connect(mail_host, 25)#SMTP服务器端口信息，默认25;SLL改为对应的端口号即可
        stp.login(mail_sender,mail_license)
        stp.sendmail(mail_sender, mail_receivers, mm.as_string())
        print("所有人打卡遍历成功，且日志发送成功！")
    ###邮件推送－－－结束－－－###
    ###方法二：
    ###WxPusher(微信推送)－－－开始－－－###
    #服务方：WxPusher (微信推送服务)[https://wxpusher.dingliqc.com/]
    #所需信息：
    #1.你的appToken
    #2.你的wxpusheruid
    @classmethod
    def wxpusher(self,xinxi):
        if(appToken='' or wxpusheruid='')
            print("未填写所需信息")
        return
        url = 'https://wxpusher.zjiecode.com/api/send/message/'
        data = json.dumps({
            "appToken":appToken,
            "content":'打卡反馈'#消息的标题
            "summary":xinxi#消息的内容
            "contentType":1,#消息类型：1.为普通文本 2.为html 3.为markdown
            "uids":[wxpusheruid]
        })
        response = requests.post(url, data = data, headers = {'Content-Type': 'application/json;charset=UTF-8'})
        if (response.json()['data'][0]['status']) == '创建发送任务成功':
            print('WxPusher推送成功')
        else:
            print('WxPusher推送失败!请检查appToken和uid是否正确')
    ###WxPusher(微信推送)－－－结束－－－###
    ###方法三：
    ###ServerChan(Server酱)－－－开始－－－###
    #服务方:ServerChan(Server酱)[https://sct.ftqq.com/]
    #所需信息：
    #1.你的sckey
    @classmethod
    def server(self,xinxi):
        if(sckey=='')
            print("未填写所需信息")
        return
        data = {
            "text":'打卡反馈'#消息的标题
            "desp":xinxi#消息的内容,消息类型：MarkDown格式
        }
        if (self.pushmethod.lower() == 'scturbo'):      #Server酱 Turbo版
            url = 'https://sctapi.ftqq.com/' + sckey + '.send'
            response = requests.post(url, data=data, headers = {'Content-type': 'application/x-www-form-urlencoded'})
            errno = response.json()['data']['errno']
        else:                                           #Server酱 普通版
            url = 'http://sc.ftqq.com/' + sckey + '.send'
            response = requests.post(url, data=data, headers = {'Content-type': 'application/x-www-form-urlencoded'})
            errno = response.json()['errno']
        if errno == 0:
            print('Server酱推送成功')
        else:
            print('Server酱推送失败!请检查sckey是否正确')
    ###ServerChan(Server酱)－－－结束－－－###
###函数执行入口###
###编写不易，好用的话点个星哦###
def main(event,content):
    Daka.dakazhu()

import requests
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
# 天气相关 api 调用
def get(sjlx,apilx):
    url = 'https://devapi.qweather.com/v7/'+sjlx+'/'+apilx+'?'+'location=112.34,37.52'+'&'+'key=8be1911ee2db49b4a386954ac33c186d'
    print(url)
    return requests.get(url).json()
###实时天气###
#得到当前API状态码
def code():
    code1=get('weather','now')['code']
    xz_updateTime=get('weather','now')['updateTime']#得到当前API的最近更新时间
    
    xz_now=get('weather','now')['now']
    xz_temp=xz_now['temp']#当前空气温度
    xz_feelsLike=xz_now['feelsLike']#当前体感温度
    xz_text=xz_now['text']#当前天气文字描述
    xz_wind360=xz_now['wind360']#当前风向360角度
    xz_twindDir=xz_now['windDir']#当前风向
    xz_windScale=xz_now['windScale']#当前风力等级
    xz_windSpeed=xz_now['windSpeed']#当前风速，公里/小时
    xz_humidity=xz_now['humidity']#当前相对湿度，百分比数值
    xz_precip=xz_now['precip']#当前小时累计降水量，默认单位：毫米
    xz_pressure=xz_now['pressure']#当前大气压强，默认单位：百帕
    xz_vis=xz_now['vis']#当前能见度，默认单位：公里
    xz_cloud=xz_now['cloud']#当前云量，百分比数值
    xz_dew=xz_now['dew']#当前露点温度
    
    tq3_daily=get('weather','3d')['daily']
    tq3_fxDate=tq3_daily[0]['fxDate']#预报日期
    tq3_sunrise=tq3_daily[0]['sunrise']#当天日出时间
    tq3_sunset=tq3_daily[0]['sunset']#当天日落时间
    tq3_moonrise=tq3_daily[0]['moonrise']#当天月升时间
    tq3_moonset=tq3_daily[0]['moonset']#当天月落时间
    tq3_moonPhase=tq3_daily[0]['moonPhase']#当天月相名称
    tq3_tempMax=tq3_daily[0]['tempMax']#预报当天最高温度
    tq3_tempMin=tq3_daily[0]['tempMin']#预报当天最低温度
    tq3_textDay=tq3_daily[0]['textDay']#预报当天白天天气状况文字描述，包括阴晴雨雪等天气状态的描述
    tq3_textNight=tq3_daily[0]['textNight']#预报当天预报晚间天气状况文字描述，包括阴晴雨雪等天气状态的描述
    tq3_wind360Day=tq3_daily[0]['wind360Day']#预报当天白天风向360角度
    tq3_windDirDay=tq3_daily[0]['windDirDay']#预报当天白天风向
    tq3_windScaleDay=tq3_daily[0]['windScaleDay']#预报当天白天风力等级
    tq3_windSpeedDay=tq3_daily[0]['windSpeedDay']#预报当天白天风速，公里/小时
    tq3_wind360Night=tq3_daily[0]['wind360Night']#预报当天夜间风向360角度
    tq3_windDirNight=tq3_daily[0]['windDirNight']#预报夜间当天风向
    tq3_windScaleNight=tq3_daily[0]['windScaleNight']#预报夜间当天风力等级
    tq3_windSpeedNight=tq3_daily[0]['windSpeedNight']#预报夜间当天风速，公里/小时
    tq3_humidity=tq3_daily[0]['humidity']#预报当天相对湿度，百分比数值
    tq3_precip=tq3_daily[0]['precip']#预报当天总降水量，默认单位：毫米
    tq3_pressure=tq3_daily[0]['pressure']#预报当天大气压强，默认单位：百帕
    tq3_vis=tq3_daily[0]['vis']#预报当天能见度，默认单位：公里
    tq3_cloud=tq3_daily[0]['cloud']#预报当天云量，百分比数值
    tq3_uvIndex=tq3_daily[0]['uvIndex']#预报当天紫外线强度指数
    tq3_1fxDate=tq3_daily[1]['fxDate']#预报日期
    tq3_1sunrise=tq3_daily[1]['sunrise']#明天日出时间
    tq3_1sunset=tq3_daily[1]['sunset']#明天日落时间
    tq3_1moonrise=tq3_daily[1]['moonrise']#明天月升时间
    tq3_1moonset=tq3_daily[1]['moonset']#明天月落时间
    tq3_1moonPhase=tq3_daily[1]['moonPhase']#明天月相名称
    tq3_1tempMax=tq3_daily[1]['tempMax']#预报明天最高温度
    tq3_1tempMin=tq3_daily[1]['tempMin']#预报明天最低温度
    tq3_1textDay=tq3_daily[1]['textDay']#预报明天白天天气状况文字描述，包括阴晴雨雪等天气状态的描述
    tq3_1textNight=tq3_daily[1]['textNight']#预报明天预报晚间天气状况文字描述，包括阴晴雨雪等天气状态的描述
    tq3_1wind360Day=tq3_daily[1]['wind360Day']#预报明天白天风向360角度
    tq3_1windDirDay=tq3_daily[1]['windDirDay']#预报明天白天风向
    tq3_1windScaleDay=tq3_daily[1]['windScaleDay']#预报明天白天风力等级
    tq3_1windSpeedDay=tq3_daily[1]['windSpeedDay']#预报明天白天风速，公里/小时
    tq3_1wind360Night=tq3_daily[1]['wind360Night']#预报明天夜间风向360角度
    tq3_1windDirNight=tq3_daily[1]['windDirNight']#预报夜间明天风向
    tq3_1windScaleNight=tq3_daily[1]['windScaleNight']#预报夜间明天风力等级
    tq3_1windSpeedNight=tq3_daily[1]['windSpeedNight']#预报夜间明天风速，公里/小时
    tq3_1humidity=tq3_daily[1]['humidity']#预报明天相对湿度，百分比数值
    tq3_1precip=tq3_daily[1]['precip']#预报明天总降水量，默认单位：毫米
    tq3_1pressure=tq3_daily[1]['pressure']#预报明天大气压强，默认单位：百帕
    tq3_1vis=tq3_daily[1]['vis']#预报明天能见度，默认单位：公里
    tq3_1cloud=tq3_daily[1]['cloud']#预报明天云量，百分比数值
    tq3_1uvIndex=tq3_daily[1]['uvIndex']#预报明天紫外线强度指数

    tq24_hourly=get('weather','24h')['hourly']
    tq24_fxTime=tq24_hourly[0]['fxTime']#预报时间
    tq24_temp=tq24_hourly[0]['temp']#温度，默认单位：摄氏度
    tq24_text=tq24_hourly[0]['text']#天气状况的文字描述，包括阴晴雨雪等天气状态的描述
    tq24_wind360=tq24_hourly[0]['wind360']#风向360角度
    tq24_windDir=tq24_hourly[0]['windDir']#风向
    tq24_windScale=tq24_hourly[0]['windScale']#风力等级
    tq24_windSpeed=tq24_hourly[0]['windSpeed']#风速，公里/小时
    tq24_humidity=tq24_hourly[0]['humidity']#相对湿度，百分比数值
    tq24_pop=tq24_hourly[0]['pop']#当前小时累计降水量，默认单位：毫米
    tq24_precip=tq24_hourly[0]['precip']#逐小时预报降水概率，百分比数值，可能为空
    tq24_pressure=tq24_hourly[0]['pressure']#大气压强，默认单位：百帕
    tq24_cloud=tq24_hourly[0]['cloud']#云量，百分比数值
    tq24_dew=tq24_hourly[0]['dew']#露点温度

    tqzl_now=get('air','now')['now']
    tqzl_updateTime=get('air','now')['updateTime']#当前API的最近更新时间
    tqzl_pubTime=tqzl_now['pubTime']#空气质量数据发布时间
    tqzl_aqi=tqzl_now['aqi']#空气质量指数
    tqzl_level=tqzl_now['level']#空气质量指数等级
    tqzl_category=tqzl_now['category']#空气质量指数级别
    tqzl_primary=tqzl_now['primary']#空气质量的主要污染物，空气质量为优时，返回值为NA
    tqzl_pm10=tqzl_now['pm10']#PM10
    tqzl_pm2p5=tqzl_now['pm2p5']#PM2.5
    tqzl_no2=tqzl_now['no2']#二氧化氮
    tqzl_so2=tqzl_now['so2']#二氧化硫
    tqzl_co=tqzl_now['co']#一氧化碳
    tqzl_o3=tqzl_now['o3']#臭氧
    
    tqzh_warning=get('warning','now')['warning']
    tqzh_pubTime=tqzh_warning['pubTime']#预警发布时间
    tqzh_title=tqzh_warning['title']#预警信息标题
    tqzh_startTime=tqzh_warning['startTime']#预警开始时间，可能为空
    tqzh_endTime=tqzh_warning['endTime']#预警结束时间，可能为空
    tqzh_status=tqzh_warning['status']#预警状态，可能为空active 预警中或首次预警update 预警信息更新cancel 取消预警
    tqzh_level=tqzh_warning['level']#预警等级
    tqzh_type=tqzh_warning['type']#预警类型ID
    tqzh_text=tqzh_warning['text']#预警详细文字描述
    

    tqshzs_daily=get('indices','1d')['daily']
    tqshzs_date=get('indices','1d')['updateTime']#预报日期
    tqshzs_type=tqshzs_daily[0]['type']#生活指数类型ID
    tqshzs_name=tqshzs_daily[0]['name']#生活指数类型的名称
    tqshzs_level=tqshzs_daily[0]['level']#生活指数预报等级
    tqshzs_category=tqshzs_daily[0]['category']#生活指数预报级别名称
    tqshzs_text=tqshzs_daily[0]['text']#生活指数预报的详细描述，可能为空
    tqshzs_1type=tqshzs_daily[1]['type']#生活指数类型ID
    tqshzs_1name=tqshzs_daily[1]['name']#生活指数类型的名称
    tqshzs_level=tqshzs_daily[1]['level']#生活指数预报等级
    tqshzs_1category=tqshzs_daily[1]['category']#生活指数预报级别名称
    tqshzs_1text=tqshzs_daily[1]['text']#生活指数预报的详细描述，可能为空
    tqshzs_2type=tqshzs_daily[2]['type']#生活指数类型ID
    tqshzs_2name=tqshzs_daily[2]['name']#生活指数类型的名称
    tqshzs_2level=tqshzs_daily[2]['level']#生活指数预报等级
    tqshzs_2category=tqshzs_daily[2]['category']#生活指数预报级别名称
    tqshzs_2text=tqshzs_daily[2]['text']#生活指数预报的详细描述，可能为空
    tqshzs_3type=tqshzs_daily[3]['type']#生活指数类型ID
    tqshzs_3name=tqshzs_daily[3]['name']#生活指数类型的名称
    tqshzs_3level=tqshzs_daily[3]['level']#生活指数预报等级
    tqshzs_3category=tqshzs_daily[3]['category']#生活指数预报级别名称
    tqshzs_3text=tqshzs_daily[3]['text']#生活指数预报的详细描述，可能为空
    tqshzs_4type=tqshzs_daily[4]['type']#生活指数类型ID
    tqshzs_4name=tqshzs_daily[4]['name']#生活指数类型的名称
    tqshzs_4level=tqshzs_daily[4]['level']#生活指数预报等级
    tqshzs_4category=tqshzs_daily[4]['category']#生活指数预报级别名称
    tqshzs_4text=tqshzs_daily[4]['text']#生活指数预报的详细描述，可能为空
    tqshzs_5type=tqshzs_daily[5]['type']#生活指数类型ID
    tqshzs_5name=tqshzs_daily[5]['name']#生活指数类型的名称
    tqshzs_5level=tqshzs_daily[5]['level']#生活指数预报等级
    tqshzs_5category=tqshzs_daily[5]['category']#生活指数预报级别名称
    tqshzs_5text=tqshzs_daily[5]['text']#生活指数预报的详细描述，可能为空
    tqshzs_6type=tqshzs_daily[6]['type']#生活指数类型ID
    tqshzs_6name=tqshzs_daily[6]['name']#生活指数类型的名称
    tqshzs_6level=tqshzs_daily[6]['level']#生活指数预报等级
    tqshzs_6category=tqshzs_daily[6]['category']#生活指数预报级别名称
    tqshzs_6text=tqshzs_daily[6]['text']#生活指数预报的详细描述，可能为空
    tqshzs_7type=tqshzs_daily[7]['type']#生活指数类型ID
    tqshzs_7name=tqshzs_daily[7]['name']#生活指数类型的名称
    tqshzs_7level=tqshzs_daily[7]['level']#生活指数预报等级
    tqshzs_7category=tqshzs_daily[7]['category']#生活指数预报级别名称
    tqshzs_7text=tqshzs_daily[7]['text']#生活指数预报的详细描述，可能为空
    tqshzs_8type=tqshzs_daily[8]['type']#生活指数类型ID
    tqshzs_8name=tqshzs_daily[8]['name']#生活指数类型的名称
    tqshzs_8level=tqshzs_daily[8]['level']#生活指数预报等级
    tqshzs_8category=tqshzs_daily[8]['category']#生活指数预报级别名称
    tqshzs_8text=tqshzs_daily[8]['text']#生活指数预报的详细描述，可能为空
    tqshzs_9type=tqshzs_daily[9]['type']#生活指数类型ID
    tqshzs_9name=tqshzs_daily[9]['name']#生活指数类型的名称
    tqshzs_9level=tqshzs_daily[9]['level']#生活指数预报等级
    tqshzs_9category=tqshzs_daily[9]['category']#生活指数预报级别名称
    tqshzs_9text=tqshzs_daily[9]['text']#生活指数预报的详细描述，可能为空
    tqshzs_10type=tqshzs_daily[10]['type']#生活指数类型ID
    tqshzs_10name=tqshzs_daily[10]['name']#生活指数类型的名称
    tqshzs_10level=tqshzs_daily[10]['level']#生活指数预报等级
    tqshzs_10category=tqshzs_daily[10]['category']#生活指数预报级别名称
    tqshzs_10text=tqshzs_daily[10]['text']#生活指数预报的详细描述，可能为空
    tqshzs_11type=tqshzs_daily[11]['type']#生活指数类型ID
    tqshzs_11name=tqshzs_daily[11]['name']#生活指数类型的名称
    tqshzs_11level=tqshzs_daily[11]['level']#生活指数预报等级
    tqshzs_11category=tqshzs_daily[11]['category']#生活指数预报级别名称
    tqshzs_11text=tqshzs_daily[11]['text']#生活指数预报的详细描述，可能为空
    tqshzs_12type=tqshzs_daily[12]['type']#生活指数类型ID
    tqshzs_12name=tqshzs_daily[12]['name']#生活指数类型的名称
    tqshzs_12level=tqshzs_daily[12]['level']#生活指数预报等级
    tqshzs_12category=tqshzs_daily[12]['category']#生活指数预报级别名称
    tqshzs_12text=tqshzs_daily[12]['text']#生活指数预报的详细描述，可能为空
    tqshzs_13type=tqshzs_daily[13]['type']#生活指数类型ID
    tqshzs_13name=tqshzs_daily[13]['name']#生活指数类型的名称
    tqshzs_13level=tqshzs_daily[13]['level']#生活指数预报等级
    tqshzs_13category=tqshzs_daily[13]['category']#生活指数预报级别名称
    tqshzs_13text=tqshzs_daily[13]['text']#生活指数预报的详细描述，可能为空
    tqshzs_14type=tqshzs_daily[14]['type']#生活指数类型ID
    tqshzs_14name=tqshzs_daily[14]['name']#生活指数类型的名称
    tqshzs_14level=tqshzs_daily[14]['level']#生活指数预报等级
    tqshzs_14category=tqshzs_daily[14]['category']#生活指数预报级别名称
    tqshzs_14text=tqshzs_daily[14]['text']#生活指数预报的详细描述，可能为空
    tqshzs_15type=tqshzs_daily[15]['type']#生活指数类型ID
    tqshzs_15name=tqshzs_daily[15]['name']#生活指数类型的名称
    tqshzs_15level=tqshzs_daily[15]['level']#生活指数预报等级
    tqshzs_15category=tqshzs_daily[15]['category']#生活指数预报级别名称
    tqshzs_15text=tqshzs_daily['text']#生活指数预报的详细描述，可能为空
    

    
  #  xinxi='当前实时天气:'+'\r\n'+
  #  print(now_temp)
#    print(xinxi)
 #   youjian(xinxi)



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
if __name__ == '__main__':
    code()
    #a=now_temp()
#xinxi='当前实时天气:'+'\r\n'+b
#print(b)
#print(xinxi)
#youjian(xinxi)
# 可以获取输入城市的气温
#if __name__ == '__main__':
 #   tommorrow = daily()[1]
 #   today = daily()[0]
 #   a=now_temp()
  #  print('现在的气温是：',a,'℃')
 #   print('月相:',today['moonPhase'])
 #   print('明天的天气是：',tommorrow['textDay'],
 #            tommorrow['tempMin'],'~',tommorrow['tempMax'],'℃')


#for rain in tommorrow['textDay']:
#           if rain == '雨':
#                print('明天有雨，通过邮件或啥的告诉我')
#                break  防止明天是 '暴雨到大暴雨' 两个雨字的天气
#            else:  else 其实没啥意义 ， 而且会执行多次 
#                print('什么也不干，继续循环')
        
        # 明天与今天温差过大提醒
#        if int(tommorrow['tempMax'])-int(today['tempMax'])>5:
#            print('明天很热，通过邮件或啥的告诉我')
#        if int(today['tempMin'])-int(tommorrow['tempMin'])>5:
#            print('明天很冷，通过邮件或啥的告诉我')
###2021.6.22
###已实现基本功能，待改进

import requests
import time

# 天气相关 api 调用
def get1(sjlx,apilx):
    url = 'https://devapi.qweather.com/v7/'+sjlx+'/'+apilx+'?'+'location=112.34,37.52'+'&'+'key=8be1911ee2db49b4a386954ac33c186d'
    print(url)
    return requests.get(url).json()
###实时天气###
#得到当前API状态码
def code():
    return get1('weather','now')['code']
#得到当前API的最近更新时间
def updateTime():
     return get('weather','now')['updateTime']
#得到当前天气各项参数
def now():
    return get('weather','now')['now']
#得到当前空气温度
def now_temp():
    return get1('weather','now')['now']['temp']
#得到当前体感温度
def now_feelsLike():
    return get('weather','now')['now']['feelsLike']
#得到当前天气文字描述
def now_text():
    return get('weather','now')['now']['text']
#得到当前风向360角度
def now_wind360():
    return get('weather','now')['now']['wind360']
#得到当前风向
def now_twindDir():
    return get('weather','now')['now']['windDir']
#得到当前风力等级
def now_windScale():
    return get('weather','now')['now']['windScale']
#得到当前风速，公里/小时
def now_windSpeed():
    return get('weather','now')['now']['windSpeed']
#得到当前相对湿度，百分比数值
def now_humidity():
    return get('weather','now')['now']['humidity']
#得到当前小时累计降水量，默认单位：毫米
def now_precip():
    return get('weather','now')['now']['precip']
#得到当前大气压强，默认单位：百帕
def now_pressure():
    return get('weather','now')['now']['pressure']
#得到当前能见度，默认单位：公里
def now_vis():
    return get('weather','now')['now']['vis']
#得到当前云量，百分比数值
def now_cloud():
    return get('weather','now')['now']['cloud']
#得到当前露点温度
def now_dew():
    return get('weather','now')['now']['dew']
#得到三天的天气
def daily():
    return get1('weather','3d')['daily']
    # return get('7d')   可以得到七天的天气



# 可以获取输入城市的气温
if __name__ == '__main__':
    tommorrow = daily()[1]
    today = daily()[0]
    a=now_temp()
    print('现在的气温是：',a,'℃')
    print('月相:',today['moonPhase'])
    print('明天的天气是：',tommorrow['textDay'],
             tommorrow['tempMin'],'~',tommorrow['tempMax'],'℃')


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



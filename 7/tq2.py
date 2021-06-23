# coding=utf-8

import requests
import re


s = requests.session()


class HeWeather(object):
    #now_text = ""
    #now_raw = []
    #city_text = ""
    #city_raw = []

    #def __init__(self):
     #   self.city()

   

    # 实况天气
    def now(self):
        api_type = "now?"
        # url = https://free-api.heweather.com/v5/now?city=深圳&key=2d849c62d67a4b9e94607d0f1c744561
        #url = APIURL + api_type + CITY + KEY
        url="https://devapi.qweather.com/v7/weather/now?key=8be1911ee2db49b4a386954ac33c186d&location=112.34,37.52&gzip=n"
        raw_json = s.get(url).json()
        if raw_json["code"] != 200:
            return
        self.now_raw = raw_json
        now_basic = raw_json["now"]
       
        basic_time=now_basic["obsTime"]#"2021-06-22T20:11+08:00",数据观测时间
        basic_temp=now_basic["temp"]#"27",温度
        basic_ftemp=now_basic["feelsLike"]#"25",体感温度
        basic_icon=now_basic["icon"]#"101",天气状况和图标的代码
        basic_text=now_basic["text"]#"多云",天气状况的文字描述
        basic_wind=now_basic["wind360"]#"45",风向360角度
        basic_awind=now_basic["windDir"]#"东北风",风向
        basic_bwind=now_basic["windScale"]#"4",风力等级
        basic_cwind=now_basic["windSpeed"]#"20",风速，公里/小时
        basic_hum=now_basic["humidity"]#"46",相对湿度，百分比数值
        basic_precip=now_basic["precip"]#"0.0",当前小时累计降水量，默认单位：毫米
        basic_pressure=now_basic["pressure"]#"921",大气压强，默认单位：百帕
        basic_vis=now_basic["vis"]#"30",能见度，默认单位：公里
        basic_cloud=now_basic["cloud"]#"10",云量，百分比数值
        basic_dew=now_basic["dew"]#"13"露点温度
        print(basic_time)
        print(basic_temp)
        print(basic_ftemp)
        print(basic_icon)
        print(basic_text)
        print(basic_wind)
        print(basic_awind)
        print(basic_bwind)
        print(basic_cwind)
        print(basic_hum)
        print(basic_precip)
        print(basic_pressure)
        print(basic_vis)
        print(basic_cloud)
        print(basic_dew)
        return(basic_time,basic_temp,basic_ftemp,basic_icon,basic_text,basic_wind,basic_awind,basic_bwind,basic_cwind,basic_hum,basic_precip,basic_pressure,basic_vis,basic_cloud,basic_dew)
	
	


    
if __name__ == '__main__':
    heWeather = HeWeather()
    now = heWeather.now()
    print(now)

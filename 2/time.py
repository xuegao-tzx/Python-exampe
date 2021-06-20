import time
import datetime
start=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
start1=time.strptime(start,'%Y-%m-%d %H:%M:%S')
start2=int(time.mktime(start1))
end=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
end1=time.strptime(end,'%Y-%m-%d %H:%M:%S')
end2=int(time.mktime(end1))
sc=end2-start2#程序运行时间
zsc=end2-1622174400#到指定时间的时长，利用时间戳计算
cssj = '2021-5-28 12:00:00'#你想要的时间
cssj1 = time.strptime(cssj, "%Y-%m-%d %H:%M:%S")
cssj2=int(time.mktime(cssj1))
mins=int(sc/60)
secs=int(sc%60)
day=int(zsc/86400)
hour=int(zsc/3600)-day*24
mins1=int(zsc/60)-hour*60-day*24*60
secs1=int(zsc%60)
print(f'当前时间时间戳:{start2}')
print(f'输入的时间的时间时间戳:{cssj2}')
xinxi="当前时间:"+start+"\r\n"+"累计目前,时长为:"+str(day)+"天"+str(hour)+"时"+str(mins1)+"分"+str(secs1)+"秒."+"\r\n"+"本次运行时长:"+str(mins)+"分"+str(secs)+"秒."
print(xinxi)   
#Writen by TZX.
#2021.6.20.





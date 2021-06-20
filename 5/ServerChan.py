def server():
    sckey='      '#你的信息
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
#Writen by TZX.
#2021.6.20.

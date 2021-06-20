def wxpusher():
    url = 'https://wxpusher.zjiecode.com/api/send/message/'
    data = json.dumps({
        "appToken":     ,#你的信息
        "content":''#消息的标题
        "summary":''#消息的内容
        "contentType":1,#消息类型：1.为普通文本 2.为html 3.为markdown
        "uids":[        ]#你的信息
    })
    response = requests.post(url, data = data, headers = {'Content-Type': 'application/json;charset=UTF-8'})
    if (response.json()['data'][0]['status']) == '创建发送任务成功':
        print('WxPusher推送成功')
    else:
        print('WxPusher推送失败!请检查appToken和uid是否正确')
#Writen by TZX.
#2021.6.20.

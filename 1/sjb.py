import random
import requests
import json
import datetime
from urllib import parse
#数据包的POST请求
head={
    'Content-Type': '网络文件的类型和网页的编码',
    'Accept-Encoding': 'gzip'#浏览器发给服务器,声明浏览器支持的编码类型
    'User-Agent':'eg:Mozilla/5.0 (Linux; Harmony 2; ***-**** Build/HUAWEI***-****; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/83.0.4103.106 Mobile Safari/537.36'#特殊字符串头，使得服务器能够识别客户使用,不一定必须有
}
def main():
    print("开始发送")
    try:
        sj = requests.post(
            url='你的目标链接地址',
            headers=head,
            data='你要发送的数据包内容'
        )
        # 通过字符串创建map，来检查结果
        res_map = json.loads(sj.text)
    except:
        print("请求错误！")
        return False
    if res_map['code'] != '200':
        print(f"发送失败，错误信息：[{res_map['msg']}]")

        return False
    else:
        print("发送成功！")
        return True
#Writen by TZX.
#2021.5.20


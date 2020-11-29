# encoding: utf-8
#@author: test_lizheng
#@file: test_data.py
#@time: 2020/11/15 11:5
import requests

# response = requests.get('https://www.baidu.com')
#
# babody = response.text.encode(encoding='utf-8')
# print(body)
# print(response.content.decode(encoding='utf-8'))

base_url = 'https://www.baidu.com'
proxie = {'http':'http://192.168.0.102:80'}
r = requests.get(base_url+'/get',proxies=proxie)
print(r.text)

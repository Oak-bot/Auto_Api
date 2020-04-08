import pytest
import requests
import random
import re#导入正则表达式包


data = {
    'username': '--random8--',
    'email': '--random8--@qq.com',
    'password': '111111',
    'confirm_password': '111111',
    'extend_field2': '',
    'extend_field3': '5252525',
    'extend_field4': '',
    'extend_field5': '22222222222',
    'sel_question': 'friend_birthday',
    'passwd_answer': '1',
    'captcha': '',
    'sms_code':'',
    'agreement': '1',
    'act': 'act_register',
    'Submit':'',
    }
memberid = (''.join(random.sample(
    ['z', 'y', 'x', 'w', 'v', 'u', 't', 's', 'r', 'q', 'p', 'o', 'n', 'm', 'l', 'k', 'j', 'i', 'h', 'g', 'f', 'e', 'd',
     'c', 'b', 'a'], 10)))
for key,value in data.items():
    if '--random8--' in value:
        data1=re.sub('--random8--',memberid,value)
        data[key] = data1
print(data)


# url_1 = 'http://192.168.31.166:799/ecshop/user.php'
#
#
# r= requests.post(url=url_1,data=data)
# i ='注册成功'
# print(r.text)

# data1 = re.sub('random1', '888',data)











def test_1():
    url_1 = 'http://192.168.31.166:799/ecshop/user.php'
    #生成随机字符串
    memberid= (''.join(random.sample(['z','y','x','w','v','u','t','s','r','q','p','o','n','m','l','k','j','i','h','g','f','e','d','c','b','a'], 10)))
    print(memberid)
    #请求参数
    data_1={
    'username': memberid,
    'email': memberid+'@qq.com',
    'password': '111111',
    'confirm_password': '111111',
    'extend_field2': '',
    'extend_field3': '5252525',
    'extend_field4': '',
    'extend_field5': '',
    'sel_question': 'friend_birthday',
    'passwd_answer': '1',
    'captcha': '',
    'sms_code':'',
    'agreement': '1',
    'act': 'act_register',
    'Submit':'',
    }
    # r= requests.post(url=url_1,data=data_1)
    # i ='注册成功'
    # assert i in r.text
    # return print(r.text)

test_1()
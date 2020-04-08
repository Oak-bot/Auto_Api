import requests
import time

# url='http://10.10.10.132:12000/api/auth/login'
# json={ 'mobile':'8615212341234','phone_code':'86'}
# dc_login=requests.post(url=url,json=json)
# dc_login.encoding = 'UTF-8'
# print(dc_login.text)
#
data1={'mobile':'917838381868','code':'123456','phone_code':'91'}
sms= requests.post('http://10.10.10.132:12000/api/auth/sms',data=data1)
print(sms.text)
#
time.sleep(3)
url1 = 'http://10.10.10.132:12000/api/auth/login'
dc_login=requests.post(url=url1,data=data1)
# dc_login.encoding = 'gb2312'
print(dc_login.text)
#
# class Test_1:
#
#     ff = 'e'
#     def test_a(self):
#         print('pp')
#
# i = Test_1()
# i.test_a()
#
# from common.get_excel import Get_Excel
# import re#导入正则表达式包
# import pytest
#
# #淘宝查询手机归属地
# # print(get_excel_row())
# excel = Get_Excel()
# case = excel.get_excel_row()
# print(case)
# print(excel.get_nrows())
#
# def test():
#
#     i='o'
#     return i
# print(test())
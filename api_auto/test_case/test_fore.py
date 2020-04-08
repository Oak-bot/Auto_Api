import requests
from config.conf import *
from common.get_excel import Get_Excel
import re#导入正则表达式包
import pytest
import random


excel = Get_Excel()
case = excel.get_case()

# @pytest.mark.parametrize('title1,type,tobeornottobe,content,url,data,other1,other2,expected',case_ago)
# def test_ago(title1,type,tobeornottobe,content,url,data,other1,other2,expected):
#     r = requests.get(params=eval(data),url=url)
#     duanyan = expected #从Excel中获取断言值
#     assert duanyan in r.text #断言
#     if other1 != '':
#         global data1#把下个接口要用到的数据设置为全局变量
#         data1 = re.findall(f"{other1}:'(.+?)'",r.text)
#
#     # data1 = re.findall("telString:'(.+?)'",r.text)

#随机出为10字母的字符串
memberid = (''.join(random.sample(
    ['z', 'y', 'x', 'w', 'v', 'u', 't', 's', 'r', 'q', 'p', 'o', 'n', 'm', 'l', 'k', 'j', 'i', 'h', 'g', 'f', 'e', 'd',
     'c', 'b', 'a'], 10)))


@pytest.mark.parametrize('title1,type,tobeornottobe,content,url,data,other1,other2,expected',case)
def test_1(title1,type,tobeornottobe,content,url,data,other1,other2,expected):
    datab = eval(data)

    for key, value in datab.items():#遍历请求参数中是否需要随机字符串
        if '--random--' in value:
            newvalue = re.sub('--random--', memberid, value)#将value中的'--random--'的字符串替换成随机字符
            datab[key] = newvalue#将变更的value还给所属的key

    global data1  # 声明一个全局变量，存放关联接口用到的值
    if other2 != '':#判断当下接口的请求参数是否需要上个接口的返回参数
        datab[f'{other2}']=data1[0]#将环境变量中的值付给当下需要关联参数的key
    #判断是post接口还是get接口
    if type == 'post':
        r = requests.post(data=datab,url=url)
    elif type == 'get':
        r = requests.get(params=datab,url=url)
    affirm = expected #从Excel中获取断言值
    assert affirm in r.text #断言
    if other1 != '':#判断是否需要将返回值中的某个参数提取出来
        data1 = re.findall(f"{other1}:'(.+?)'",r.text)#提取返回值中的某个参数作为全局变量



# def test_2():
#     url_2 = get_excel_row(2)[2]
#     dataa = get_excel_row(2)[3]
#     datab = eval(dataa)
#     datab['password']=data1[0]
#     global s
#     s = requests.session()
#     r = s.post(data=datab,url=url_2)
#     duanyan = get_excel_row(2)[5] #从Excel中获取断言值
#     assert duanyan in r.text ,'在text中找出关键字'#断言
#     # print(r.text)
#
# def test_3():
#     url_3 = get_excel_row(3)[2]
#     dataa3 = get_excel_row(3)[3]
#     datab3 = eval(dataa3)
#     r = s.post(data=datab3,url=url_3)
#     duanyan = get_excel_row(3)[5] #从Excel中获取断言值
#     assert duanyan in r.text#断言
#     # print(r.text)
#
# if __name__ == '__main__':
#     pytest.main()

#登录接口
#http://192.168.31.166:800/source/ecshop/user.php



# url_2 = server_ip2()+'/source/ecshop/user.php'
# s = requests.session()#登录时将session保存为公共参数，以便后面接口使用

# for i in range(1,4):
#     username,password = get_excel_row(i)#读取Excel文件第二行的信息
#
    # data_2 = {
    # 'username': username,
    # 'password': password,
    # 'act': 'act_login',
    # 'submit':''
    # }
#     # usermessage = get_excel_row(4)[0]#如果数据为字典格式取值方法
#     # json = eval(usermessage)#将str类型转换为字典类型
#     r = s.post(url_2,data=data_2)
#     print(r.text)
#     print('----'*100)

#登录后进入'用户中心'
# url_3 = server_ip2()+'/source/ecshop/user.php'
# r_3 = s.get(url=url_3)
# print(r_3.text)
# pip install -U pytest

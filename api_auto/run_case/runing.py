import pytest
import os


if __name__ == '__main__':
    pytest.main(['../test_case/','--alluredir=../report/'])#生成allure报告
    #allure serve report 在命令行查看report目录下的报告


'''
一、pytest的运行方式：
1.在主函数中执行：

    pytest.main（"-s文件名称"）
2.命令行执行方式：
    在测试用例所在目录下进入命令行
    输入pytest -s test_fore.py(在项目根目录下进入命令行，pytest[参数]执行文件)
3.在pycharm中，使用terminal选项代替命令行操作

二、测试报告
'addopts = -s --html=report/report.html'
allure-pytest
这边使用的是allure-pytest，主要命令：
py.test --alluredir = %allure_result_folder% //生成报告
allure serve %allure_result_folder% //查看报告

'''











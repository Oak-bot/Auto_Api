
def server_ip1():
    taobao = 'https://tcc.taobao.com'
    return taobao

def server_ip2():
    ecshop = 'http://192.168.31.166:800'
    return ecshop

#字典参数化
def server_ip3():
    server_address={
        'taobao':'https://tcc.taobao.com',
        'ecshop':'http://192.168.31.166:800'
    }
    return server_address['taobao']


def list_data():
    data1,data2,data3=['qw','23','ee']
    return data2

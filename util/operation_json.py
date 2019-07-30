#coding:utf-8
import json

# fp = open('D:/testJk/datacofig/login.json')
# #（../dataconfig/login.json）
# data = json.load(fp)
# print(data['login'])

class OperationsJson:

    def __init__(self):
        self.data = self.read_data()
    #读取json文件,编码格式
    def read_data(self):
        with open('D:/testJk/datacofig/user.json',encoding='UTF-8') as fp:
            data = json.load(fp)
            return data

    #根据关键字获取数据
    def get_data(self,id):
        return self.data[id]

if __name__ == '__main__':
    opjson = OperationsJson()
    print(opjson.get_data('szlist'))

#coding:utf-8
import requests
import json
class RunMethod:
    def post_main(self,url,data,header=None):
        res = None
        if header !=None:
            res = requests.post(url=url,data=data,header=header)
        else:
            res = requests.post(url=url,data=data)
            # print(res.status_code)
        return res.json()

    def get_main(self,url,data=None,header=None):
        res = None
        if header != None:
            res = requests.get(url=url,data=data,header=header)
        else:
            res = requests.get(url=url,data=data)
            # print(res.status_code)
        return res.json()

    def run_main(self,method,url,data=None,header=None):
        res = None
        if method =='post':
            res = self.post_main(url,data,header)
        else:
            res = self.get_main(url,data,header)
        return json.dumps(res,ensure_ascii=False,sort_keys=True,indent=2)

if __name__ =="__main__":
    test=RunMethod()
    method = 'get'
    url = 'https://ueh.med.gzhc365.com/api/ehis/user/personal/getpatientslist?hisId=99991&platformId=99991&platformSource=3'
    data = {
        "data": "1560866228754-834DA39B3986456A740650"
    }
    header =None
    print(test.run_main(method, url, data, header).text)

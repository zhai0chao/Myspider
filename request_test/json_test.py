#coding:utf-8
import json
import requests
import pandas as pd
#将Python字典对象加载成json数据（str）
#dic = {'name':'翟凌超','add':'北京'}
#xx = json.dumps(dic,ensure_ascii=False)
#print type(xx)
def spider():
    url = 'http://www.lagou.com/lbs/getAllCitySearchLabels.json'
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36",
    }
    response = requests.get(url=url, headers=headers,)
    contents = response.content
    return contents
    #print type(contents)
    #print contents
    #


def load_data(contens):
    #print contents

    dicobj = json.loads(contents)
    #print dicobj
    #print type(dicobj)

    json.dump(dicobj,open('city.json','w'))

    pands = pd.DataFrame(dicobj)

    #print   pands
    data2 = pands.loc['data']['content']
    pands2 = pd.DataFrame(data2)
    #print pands2
    col = ['id','name','code','parentId','isSelected']
    #print pands2.iloc[0][0]
    res = pd.DataFrame(pands2.iloc[0][0],columns=col)
    qq=[res,]
    for i in range(1,22):
        li = pands2.iloc[i][0]
        data = pd.DataFrame(li,columns=col)
        qq.append(data)
        #result.append(data,ignore_index=True)
    #result = pd.concat(li)
    result = pd.concat(qq,ignore_index=True)
    result.to_csv('city_pd.csv',encoding='utf-8',columns=col,sep='\t')
def load_json():
    """行不通"""
    print pd.read_json('city.json')

if __name__ == '__main__':
    contents = spider()
    load_data(contents)
    #load_json()


    pass
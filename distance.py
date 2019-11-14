# coding=utf-8
import json
import requests
import re

def geocoding(s1,s2):   #地址编码
    if s1.find("福州市")==-1:
        s1='福建省福州市'+s1
    if s2.find("福州市")==-1:
        s2='福建省福州市'+s2
    url1="https://restapi.amap.com/v3/geocode/geo?address="+s1+"&output=JSON&key=f7043c0c8e17a2d34450be2eed47084c"
    map=requests.get(url1).json()["geocodes"]
    ss1 = map[0]["formatted_address"]
    map = map[0]["location"]
    map1=json.dumps(map,ensure_ascii=False)
    # print(map1)
    print(ss1)
    url2="https://restapi.amap.com/v3/geocode/geo?address="+s2+"&output=JSON&key=f7043c0c8e17a2d34450be2eed47084c"
    map=requests.get(url2).json()["geocodes"]
    ss2=map[0]["formatted_address"]
    map = map[0]["location"]
    map2=json.dumps(map, ensure_ascii=False)
    #print(map2)
    print(ss2)
    return map1,map2

def Pathplanning(st1,st2):   #规划路径，计算距离
    st1=st1[1:-2]
    st2=st2[1:-2]
    url3="https://restapi.amap.com/v4/direction/bicycling?origin="+st1+"&destination="+st2+"&key=f7043c0c8e17a2d34450be2eed47084c"
    # print(url3)
    # print(st1)
    # print(st2)
    rout=requests.get(url3).json()["data"]
    rout=rout["paths"][0]["distance"]
    dis=json.dumps(rout,ensure_ascii=False)
    print(dis)


s1=input("出发地")
s2=input("目的地")
m1,m2=geocoding(s1,s2)
Pathplanning(m1,m2)


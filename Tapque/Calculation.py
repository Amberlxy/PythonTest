# !/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import pytest


# 产品信息
productId = "1480807263997566978"
packageId = "1480808811246952449"
eventCode = "bwl4loevrshs"
access_token = "eyJhbGciOiJSUzI1NiJ9.eyJzdWIiOiIxODA5MTc1NTY2MDp4eHh4eHh4OjEzMjgyNDY5NjI4NTM1Mzk4NDI6MTQ0NzgwNDA0MTUyNjM1ODAxODoyOmFsbDphbGw6YWxsOmFsbCIsInVuaXF1ZVZhbHVlIjoiMTgwOTE3NTU2NjA6eHh4eHh4eDoxMzI4MjQ2OTYyODUzNTM5ODQyOjE0NDc4MDQwNDE1MjYzNTgwMTg6MjphbGw6YWxsOmFsbDphbGwiLCJleHAiOjE2Njk5OTI1MzR9.ZA_gliJrH7M4uDiBVuTB9-pT4A2FL1M_TAYAtUlH_NKWkAsfyPtIgucEuAIApbYpG0VPA-X8MvQTbMY2yOw-e1nx_6y4Ozlu-OrTmKLNiPTLdcUVeNCa50V7UxpBIB-8o5Bx3kyFbDVpqgxq1i8sUT8JyPjBHMu9c9MMuxfvDAI"

#URL
url_domain = "http://holo-sh.tapque.com"                                           #预发布
url_eventList ="/olap/consolidate/et/group/list"                     #某产品的事件列表
url_pubArgs = "/olap/consolidate/et/eventPublicArgs"                  #事件公参
url_Args ="/et/eventTracking/argList"                                #事件私参
url_userAttribute ="/olap/consolidate/et/userAttribute/allArgs"      #用户属性

#获取某项目的事件列表
def get_event_info():
    headers = {"access-token" : access_token}
    data = {
        "productId" : productId,
        "packageId" : packageId,
    }
    event = requests.get(url = url_domain + url_eventList,params = data,headers = headers)          #发送请求
    eventdic = event.json()
    try:
        events = []
        eventNameList = []
        for i in range(1,len(eventdic["records"])):
            events.append(eventdic["records"][i]["events"])
            for j in range(0,len(events[0])):
                eventNameList.append(dict(eventName = events[0][j]["eventName"],eventCode = events[0][j]["eventCode"],eventType = events[0][j]["eventType"]))
        return  eventNameList
    except:
        print("接口异常：",event.json())

# print(get_event_info())

# #获取事件公参
def get_pubArgs_info():
    headers = {"access-token" : access_token}
    data = {
        "productId" : productId,
        "eventCode" : "undefined",
        "packageId" : packageId,
    }
    pubArgs = requests.get(url = url_domain + url_pubArgs,params = data,headers = headers)
    pubArgsdic = pubArgs.json()
    try:
        pubArgsList = []
        for i in range(0,len(pubArgsdic["records"])):
            pubArgsList.append(dict(name = pubArgsdic["records"][i]['name'], dataType = pubArgsdic["records"][i]['dataType']))
        return pubArgsList
    except:
        print("接口异常：",pubArgs.json())

# print(get_pubArgs_info())

#获取事件的私参
def get_Args_info():
    headers = {"access-token" : access_token}
    data = {
        "productId" : productId,
        "eventCode" : eventCode,
        "packageId" : packageId,
    }
    Args = requests.get(url = url_domain + url_Args,params = data,headers = headers)
    Argsdic = Args.json()
    try:
        ArgsList = []
        for i in range(0,len(Argsdic["records"])):
            ArgsList.append(dict(name = Argsdic["records"][i]['name'], dataType = Argsdic["records"][i]['dataType']))
        return ArgsList
    except:
        print("接口异常：",Args.json())

# print(get_Args_info())


# #获取用户属性
def get_userAttribute_info():
    headers = {"access-token" : access_token}
    data = {
        "productId" : productId,
        "packageId" : packageId,
    }
    userAttribute = requests.get(url = url_domain + url_userAttribute,params = data,headers = headers)
    userAttributeinfo = userAttribute.json()
    try:
        userAttributeList = []
        for i in range(0,len(userAttributeinfo["records"])):
            userAttributeList.append(dict(name = userAttributeinfo["records"][i]['name'], dataType = userAttributeinfo["records"][i]['dataType']))
        return userAttributeList
    except:
        print("接口异常：",userAttribute.json())

# print(get_userAttribute_info())



# 给计算接口传参
def test_calculation():
    url_trigger = "/olap/api/event/trigger"
    headers = {"access-token" : access_token}
    data = {
  "productId": "1480807164923912194",
  "packageId": "",
  "dataSource": "ta",
  "events": [
    {
      "analysis": "TOTAL_TIMES",
      "eventName": "task_store_content__subscribe",
      "eventCode": "bwl4loevrshs",
      "eventType": "common",
      "eventNameDisplay": "订阅的总次数",
      "quota": "",
      "relation": "and",
      "initData": "[]",
      "type": "normal",
      "filts": [],
      "eventSplitIndexes": [],
      "fieldType": "",
      "attributeList": []
    }
  ],
  "eventView": {
    "startTime": "2022-11-25",
    "endTime": "2022-12-01",
    "timeParticleSize": "day",
    "firstDayOfWeek": 1,
    "relation": "and",
    "filts": [],
    "groupBy": [],
    "eventSplit": {},
    "initData": {
      "relationship": "and",
      "dataForm": []
    }
  },
  "statType": "event",
  "id": "f8df0158-5b1a-4b21-a548-3ae372e2a9b3"
    }
    r = requests.post(url = url_domain + url_trigger, json=data,headers=headers)
    # print(r.json()['code'])
    assert r.json()['code'] == '6000'
    # print(r.status_code)

print(test_calculation())
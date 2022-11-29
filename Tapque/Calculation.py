import requests


# 产品信息
productId = "1480807263997566978"
packageId = "1480808811246952449"

#URL
url_domain = "http://holo-sh.tapque.com"   #预发布
url_eventList = url_domain + "/olap/consolidate/et/group/list?productId=" + productId + "&packageId=" + packageId     #某产品的事件列表

#获取某项目的事件列表
def get_event_info():
    headers = {"access-token" : "eyJhbGciOiJSUzI1NiJ9.eyJzdWIiOiIxODA5MTc1NTY2MDp4eHh4eHh4OjEzMjgyNDY5NjI4NTM1Mzk4NDI6MTQ0NzgwNDA0MTUyNjM1ODAxODoyOmFsbDphbGw6YWxsOmFsbCIsInVuaXF1ZVZhbHVlIjoiMTgwOTE3NTU2NjA6eHh4eHh4eDoxMzI4MjQ2OTYyODUzNTM5ODQyOjE0NDc4MDQwNDE1MjYzNTgwMTg6MjphbGw6YWxsOmFsbDphbGwiLCJleHAiOjE2Njk3MzM1MzV9.aEWcBA6BuPNtHaNlCYu8XJPk2mqKk5l6g8kpwWphACHF8QUrjsAMnsE_8_KVNJMLOBtaL4AA6AADSlGmhwaCLkt9eI6YgxBwhJJrtF-zh1TXaEjgTibwoE8KALjUrItmpp37aEb-kw0jhy_9iEPnq6QX078-YleCxovqznJuKi0"}
    event = requests.get(url_eventList, headers = headers)          #发送请求
    eventdic = event.json()
    events = []
    eventNameList = []
    for i in range(1,len(eventdic["records"])):
        events.append(eventdic["records"][i]["events"])
        # print(events[0])
        for j in range(0,len(events[0])):
            eventNameList.append(events[0][j]["eventName"])
        #     print(type(eventNameList))
    
    return  eventNameList

print(get_event_info())







import requests
import sys


# 产品信息
productId = "1480807263997566978"
packageId = "1480808811246952449"
eventcode = "bwl4loevrshs"

#URL
url_domain = "http://holo-sh.tapque.com"   #预发布
url_eventList = url_domain + "/olap/consolidate/et/group/list?productId=" + productId + "&packageId=" + packageId     #某产品的事件列表
url_pubArgs = url_domain + "/olap/consolidate/et/eventPublicArgs?productId=" + productId + "&eventCode=undefined&packageId="     #事件公参
url_Args = url_domain + "/et/eventTracking/argList?productId=" + productId + "&eventCode=" + eventcode + "&packageId=" + packageId      #事件私参


#获取某项目的事件列表
# def get_event_info():
#     headers = {"access-token" : "eyJhbGciOiJSUzI1NiJ9.eyJzdWIiOiIxODA5MTc1NTY2MDp4eHh4eHh4OjEzMjgyNDY5NjI4NTM1Mzk4NDI6MTQ0NzgwNDA0MTUyNjM1ODAxODoyOmFsbDphbGw6YWxsOmFsbCIsInVuaXF1ZVZhbHVlIjoiMTgwOTE3NTU2NjA6eHh4eHh4eDoxMzI4MjQ2OTYyODUzNTM5ODQyOjE0NDc4MDQwNDE1MjYzNTgwMTg6MjphbGw6YWxsOmFsbDphbGwiLCJleHAiOjE2Njk3MzM1MzV9.aEWcBA6BuPNtHaNlCYu8XJPk2mqKk5l6g8kpwWphACHF8QUrjsAMnsE_8_KVNJMLOBtaL4AA6AADSlGmhwaCLkt9eI6YgxBwhJJrtF-zh1TXaEjgTibwoE8KALjUrItmpp37aEb-kw0jhy_9iEPnq6QX078-YleCxovqznJuKi0"}
#     event = requests.get(url_eventList, headers = headers)          #发送请求
#     eventdic = event.json()
#     try:
#         events = []
#         eventNameList = []
#         for i in range(1,len(eventdic["records"])):
#             events.append(eventdic["records"][i]["events"])
#             for j in range(0,len(events[0])):
#                 eventNameList.append(events[0][j]["eventName"])
#         return  eventNameList
#     except:
#         print("接口异常：",event.json())

# print(get_event_info())

# #获取事件公参
# def get_pubArgs_info():
#     headers = {"access-token" : "eyJhbGciOiJSUzI1NiJ9.eyJzdWIiOiIxODA5MTc1NTY2MDp4eHh4eHh4OjEzMjgyNDY5NjI4NTM1Mzk4NDI6MTQ0NzgwNDA0MTUyNjM1ODAxODoyOmFsbDphbGw6YWxsOmFsbCIsInVuaXF1ZVZhbHVlIjoiMTgwOTE3NTU2NjA6eHh4eHh4eDoxMzI4MjQ2OTYyODUzNTM5ODQyOjE0NDc4MDQwNDE1MjYzNTgwMTg6MjphbGw6YWxsOmFsbDphbGwiLCJleHAiOjE2Njk4Mzg3MTB9.H4-kNmvrDdooZI5La0IixmAm137KxRGFZIndQPERCTRldbQR_ifZiZxUmxRIPZ_t1pSJAIxfOAiw4WO6a_33WIFqOYLwjKu9xDgQGCbBFSFcIhjJev9YcB3pWXFsVhMOPolE0SZVFkNnEXe-OapuX-ODluoxdeu4ppsBe0o2FRE"}
#     pubArgs = requests.get(url_pubArgs, headers = headers)
#     pubArgsdic = pubArgs.json()
#     try:
#         pubArgsList = []
#         for i in range(0,len(pubArgsdic["records"])):
#             pubArgsList.append(dict(name = pubArgsdic["records"][i]['name'], dataType = pubArgsdic["records"][i]['dataType']))
#         return pubArgsList
#     except:
#         print("接口异常：",pubArgs.json())

# print(get_pubArgs_info())

#获取事件的私参
def get_Args_info():
    headers = {"access-token" : "eyJhbGciOiJSUzI1NiJ9.eyJzdWIiOiIxODA5MTc1NTY2MDp4eHh4eHh4OjEzMjgyNDY5NjI4NTM1Mzk4NDI6MTQ0NzgwNDA0MTUyNjM1ODAxODoyOmFsbDphbGw6YWxsOmFsbCIsInVuaXF1ZVZhbHVlIjoiMTgwOTE3NTU2NjA6eHh4eHh4eDoxMzI4MjQ2OTYyODUzNTM5ODQyOjE0NDc4MDQwNDE1MjYzNTgwMTg6MjphbGw6YWxsOmFsbDphbGwiLCJleHAiOjE2Njk4Mzg3MTB9.H4-kNmvrDdooZI5La0IixmAm137KxRGFZIndQPERCTRldbQR_ifZiZxUmxRIPZ_t1pSJAIxfOAiw4WO6a_33WIFqOYLwjKu9xDgQGCbBFSFcIhjJev9YcB3pWXFsVhMOPolE0SZVFkNnEXe-OapuX-ODluoxdeu4ppsBe0o2FRE"}
    Args = requests.get(url_Args, headers = headers)
    Argsdic = Args.json()
    try:
        ArgsList = []
        for i in range(0,len(Argsdic["records"])):
            ArgsList.append(dict(name = Argsdic["records"][i]['name'], dataType = Argsdic["records"][i]['dataType']))
        return ArgsList
    except:
        print("接口异常：",Args.json())

print(get_Args_info())


#获取用户属性
def get_Args_info():
    headers = {"access-token" : "eyJhbGciOiJSUzI1NiJ9.eyJzdWIiOiIxODA5MTc1NTY2MDp4eHh4eHh4OjEzMjgyNDY5NjI4NTM1Mzk4NDI6MTQ0NzgwNDA0MTUyNjM1ODAxODoyOmFsbDphbGw6YWxsOmFsbCIsInVuaXF1ZVZhbHVlIjoiMTgwOTE3NTU2NjA6eHh4eHh4eDoxMzI4MjQ2OTYyODUzNTM5ODQyOjE0NDc4MDQwNDE1MjYzNTgwMTg6MjphbGw6YWxsOmFsbDphbGwiLCJleHAiOjE2Njk4Mzg3MTB9.H4-kNmvrDdooZI5La0IixmAm137KxRGFZIndQPERCTRldbQR_ifZiZxUmxRIPZ_t1pSJAIxfOAiw4WO6a_33WIFqOYLwjKu9xDgQGCbBFSFcIhjJev9YcB3pWXFsVhMOPolE0SZVFkNnEXe-OapuX-ODluoxdeu4ppsBe0o2FRE"}
    Args = requests.get(url_Args, headers = headers)
    Argsdic = Args.json()
    try:
        ArgsList = []
        for i in range(0,len(Argsdic["records"])):
            ArgsList.append(dict(name = Argsdic["records"][i]['name'], dataType = Argsdic["records"][i]['dataType']))
        return ArgsList
    except:
        print("接口异常：",Args.json())

print(get_Args_info())

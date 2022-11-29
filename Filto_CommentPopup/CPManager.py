#!/usr/bin/python
# -*- coding: UTF-8 -*-

param_dict = {}

def input_param():
# 弹框弹出次数
    while True:
        try:
            comment_show_count = str(input(">>>评论评分弹框已弹出次数:   "))
            if (comment_show_count.isdigit() is True) and (int(comment_show_count) >= 0):
                param_dict.update({"comment_show_count": int(comment_show_count)})
                break
            else:
                print(">>>无效，请重新输入")
        except:
            print(">>>无效，请重新输入")   

# 用户类型
    while True:
        try:
            user_type = str(input(">>>是付费用户吗？y/n:   "))
            if user_type == "y" or user_type =="n" :
                param_dict.update({"user_type": user_type})
                break
            else:
                print(">>>无效，请重新输入")
        except:
            print(">>>无效，请重新输入")
         
# # session_day
    while True:
        try:
            session_day = str(input(">>>累计打开APP的天数:   "))
            if (session_day.isdigit() is True) and (int(session_day) >= 0):
                param_dict.update({"session_day": int(session_day)})
                break
            else:
                print(">>>无效，请重新输入")
        except ValueError:
            print(">>>无效，请重新输入")

# # session_count
    while True:
        try:
            session_count = str(input(">>>累计打开APP的session数:   "))
            if (session_count.isdigit() is True) and (int(session_count) >= 0):
                param_dict.update({"session_count": int(session_count)})
                break
            else:
                print(">>>无效，请重新输入")
        except ValueError:
            print(">>>无效，请重新输入")

# # 保存次数
    while True:
        try:
            saved_succeed_count = str(input(">>>保存成功次数:   "))
            if (saved_succeed_count.isdigit() is True) and (int(saved_succeed_count) >= 0):
                param_dict.update({"saved_succeed_count": int(saved_succeed_count)})
                break
            else:
                print(">>>无效，请重新输入")
        except ValueError:
            print(">>>无效，请重新输入")

    return param_dict

# print(input_param())

# popup内容选择
def popup_isselect():
    while True:
        try:
            isselected = int(input(">>>请选择：1.给个好评  2.吐槽一下  3.下次再说" + '\n'))
            if isselected in range(1,4):
                if isselected == 1:
                    print("跳转Google Play评论页，弹框消失")
                    return True
                    break
                elif isselected == 2:
                    print("唤起Feedback页面，弹框消失")
                    return True
                    break
                elif isselected == 3:
                    print("弹框消失")
                    return False
                    break
            else:
                print("无效输入,请重新选择")
        except:
            print("无效，请重新输入") 
# print(popup_isselect())


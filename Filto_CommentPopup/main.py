#!/usr/bin/python
# -*- coding: UTF-8 -*-

import CPManager

CPManager.input_param()
comment_show_count_int = CPManager.param_dict['comment_show_count']
saved_succeed_count_int = CPManager.param_dict['saved_succeed_count']


while True:
    if comment_show_count_int == 0:
        if ((CPManager.param_dict['user_type'] == 'y' or 'n') and (CPManager.param_dict['session_day'] == 3 and CPManager.param_dict['session_count'] > 5 and saved_succeed_count_int == 1)) \
            or (CPManager.param_dict['user_type'] == 'y' and saved_succeed_count_int == 1) \
            or (CPManager.param_dict['user_type'] == 'n' and saved_succeed_count_int == 4):
            print("----------------------")
            print("|" + "评论评分框第一次弹出" + "|")
            print("----------------------")
            saved_succeed_count_int = 0     # 保存成功次数归零
        else:
            print('***未触发弹框，重新开始***')
            CPManager.input_param()
            comment_show_count_int = CPManager.param_dict['comment_show_count']
            saved_succeed_count_int = CPManager.param_dict['saved_succeed_count']
            continue
    elif comment_show_count_int == 1:
        while saved_succeed_count_int in range(0,10):
            saved_succeed_count_int += 1
            print("***" + "已保存" + str(saved_succeed_count_int) + "次" + "***")
            if saved_succeed_count_int == 10:
                print("----------------------------")
                print("|" + "评论评分框第二次弹出" + "|")
                print("----------------------------")
            else:
                continue
    else:
        print("******退出！******")
        break

    # popup展示次数
    comment_show_count_int += 1    

    # popup内容选择
    if CPManager.popup_isselect() is True:
        break
    else:
        continue
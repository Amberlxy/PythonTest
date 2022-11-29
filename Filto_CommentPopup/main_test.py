#!/usr/bin/python
# -*- coding: UTF-8 -*-

import CPManager

# CPManager.input_param()
# CommentShowCount_int = CPManager.param_dict['CommentShowCount']
# SavedSucceedCount_int = CPManager.param_dict['SavedSucceedCount']

user = CPManager.User()
user.setPro()
user.open()
user.openDays()
user.save()

# while True:
#     if CommentShowCount_int == 0:
#         if ((CPManager.param_dict['UserType'] == 1 or 2) and (CPManager.param_dict['SessionDay'] == 3 and CPManager.param_dict['SessionCount'] > 5 and SavedSucceedCount_int == 1)) \
#             or (CPManager.param_dict['UserType'] == 1 and SavedSucceedCount_int == 1) \
#             or (CPManager.param_dict['UserType'] == 2 and SavedSucceedCount_int == 4):
#             print("----------------------")
#             print("|" + "评论评分框第一次弹出" + "|")
#             print("----------------------")
#             SavedSucceedCount_int = 0     # 保存成功次数归零
#         else:
#             print('***未触发弹框，重新开始***')
#             CPManager.input_param()
#             CommentShowCount_int = CPManager.param_dict['CommentShowCount']
#             SavedSucceedCount_int = CPManager.param_dict['SavedSucceedCount']
#             continue
#     elif CommentShowCount_int == 1:
#         while SavedSucceedCount_int in range(0,10):
#             SavedSucceedCount_int += 1
#             print("***" + "已保存" + str(SavedSucceedCount_int) + "次" + "***")
#             if SavedSucceedCount_int == 10:
#                 print("----------------------------")
#                 print("|" + "评论评分框第二次弹出" + "|")
#                 print("----------------------------")
#             else:
#                 continue
#     else:
#         print("***已展示过popup，退出！***")
#         break

#     # popup展示次数
#     CommentShowCount_int += 1    

#     # popup内容选择
#     if CPManager.popup_select() is True:
#         break
#     else:
#         continue

    
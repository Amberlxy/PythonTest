#!/usr/bin/python
# -*- coding: UTF-8 -*-

class User:
    session_cnt = 0
    session_day = 0
    is_pro = False
    save_cnt = 0
    hasShow = False
    
    def setPro(self):
        while True:
            try:
                UserType = int(input(">>>请输入用户类型：1.PRO 2.FREE:   "))
                if UserType in range(1,3):
                    break
                else:
                    print(">>>无效，请重新输入")
            except ValueError:
                print(">>>无效，请重新输入")
        self.is_pro = UserType == 1
        if self.is_pro :
            print("用户为付费用户")
        else :
            print("用户为免费用户")
        self.shouldShow()

    def open(self):
        while True:
            try:
                SessionCount = str(input(">>>累计打开APP的session数:   "))
                if (SessionCount.isdigit() is True) and (int(SessionCount) >= 0):
                    break
                else:
                    print(">>>无效，请重新输入")
            except ValueError:
                print(">>>无效，请重新输入")
        self.session_cnt += int(SessionCount)
        print("开启APP{}次".format(self.session_cnt))
        self.shouldShow()
    def openDays(self):
        while True:
            try:
                SessionDay = str(input(">>>累计打开APP的天数:   "))
                if (SessionDay.isdigit() is True) and (int(SessionDay) >= 0):
                    break
                else:
                    print(">>>无效，请重新输入")
            except ValueError:
                print(">>>无效，请重新输入")
        self.session_day += int(SessionDay)
        print("开启APP{}天".format(self.session_day))
        self.shouldShow()
    def save(self):
        while True:
            try:
                SavedSucceedCount = str(input(">>>保存成功次数:   "))
                if (SavedSucceedCount.isdigit() is True) and (int(SavedSucceedCount) >= 0):
                    break
                else:
                    print(">>>无效，请重新输入")
            except ValueError:
                print(">>>无效，请重新输入")
        self.save_cnt += int(SavedSucceedCount)
        print("保存{}次".format(self.save_cnt))
        self.shouldShow()

    def shouldShow(self):
        flag = False
        if self.session_day >= 3 and self.session_cnt >= 5 and self.save_cnt == 1:
            flag = True
        elif not self.is_pro and self.save_cnt == 4:
            flag = True
        elif self.is_pro and self.save_cnt == 1:
            flag = True
        elif self.hasShow and self.save_cnt == 10:
            flag = True
        if flag:
            self.hasShow = True
            print("展示Popup!!!")


user = User()
user.setPro()
user.open()
user.openDays()
user.save()

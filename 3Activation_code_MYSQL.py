#!/usr/bin/python
# -*- coding: UTF-8 -*-
import random
import string
import pymysql

data = ''
codes = set()
def random_code():
    data = string.ascii_letters + string.digits
    while True:
        activation_code = ''.join(random.sample(data,6))
        codes.add(activation_code)
        if len(codes) < 20:
            continue
        else:
            print('共生成200个激活码：' ) 
            print(codes)
            break
    return codes

def insert_data():
    db = pymysql.connect(host = 'localhost',user = 'root',passwd = '123456Test',db = 'mysql')
    cursor = db.cursor()
    cursor.execute("DROP TABLE IF EXISTS TEST")
    sql1 = """CREATE TABLE TEST (
            SN INT NOT NULL,
            ACTIVATION_CODE VARCHAR(200) NOT NULL,
            PRIMARY KEY(ACTIVATION_CODE))"""
    cursor.execute(sql1)
    code_data = list(random_code())
    for j in range(0,20):
        sql2 = "INSERT INTO TEST(SN,ACTIVATION_CODE) VALUES (" + str(j) + "," + "'"+code_data[j] +"'" + ")"""
        try:
            cursor.execute(sql2)
        except:
            db.rollback()
        j += 1

    cursor.execute("SELECT * FROM TEST ORDER BY SN ASC")
    db.commit()
    results = cursor.fetchall()
    print("入库成功")
    print(results)

if __name__ == "__main__":
    insert_data()
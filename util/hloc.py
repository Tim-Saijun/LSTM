#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2022/12/24 15:06
# @Author  : 杨再润
# @Site  :  https://tim-saijun.github.io/
import happybase
connection = happybase.Connection(host='node2', port=9090)

tables = connection.tables()
print(tables)

#连接static表
table = connection.table('static')

def getHbaseCount_minute_loc(time = '2022-12-24 15:00:00'):
    #计算偏移量
    tth = time[11:13]
    tth =int(tth)
    tth  %= 7
    tstart = '2020-12-22 0' + str(tth) + time[13:17] + '00'
    print(tstart)
#按时间查询行键，取10条数据
    HL = []
    count = 0
    for key, data in table.scan(row_start=tstart,row_stop='2020-12-22 08:03:00'):
        if count==9:
            break
        # print(key.decode('utf-8'), data)
        tmp = []
        tmp.append(int(data[b'LTZX:minute'].decode('utf-8')))
        tmp.append(int(data[b'SLD:minute'].decode('utf-8')))
        tmp.append(int(data[b'SSHN:minute'].decode('utf-8')))
        HL.append(tmp)
        count+=1
    connection.close()#不关闭连接会崩溃，不能重复连接
    return HL

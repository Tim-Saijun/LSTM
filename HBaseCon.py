#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2022/12/23 20:09
# @Author  : 杨再润
# @Site  :  https://tim-saijun.github.io/
import happybase


#建立happybase连接，中文显示正常
# connection = happybase.Connection(host='node2', port=9090, protocol='compact', \
#                                   transport='buffered', timeout=10000, autoconnect=True, table_prefix=None, \
#                                   table_prefix_separator=b':', compat='0.98')
# connection.open()
# connection = happybase.Connection(host='node2', port=9090)
#查看所有表
#建立happybase连接，去除b'前缀
connection = happybase.Connection(host='node2', port=9090)
tables = connection.tables()
print(tables)
#查看表'ETC'的所有数据，toStr=True表示将数据转换为字符串

table = connection.table('ETC')
for key, data in table.scan():
    print(key.decode('utf-8'), data)
#在表’test’中插入一条数据,数据格式为：b'i这个度': {b'info:col1': b'value1'}，中文编码为ascii

# table.put('i这个度'.encode(), {b'info:col1': b'value1'})

#将data/data1.txt中的数据插入到表'test'中
# with open('data/data1.txt', 'r') as f:
#     for line in f:
#         line = line.strip()
#         key, value = line.split(',')
#         table.put(key.encode(), {b'info:col1': value.encode()})

#在创建表'static',列族有'LTZX','SLD','SSHN'
# connection.create_table('static', {'LTZX': dict(), 'SLD': dict(), 'SSHN': dict()})
'''
table = connection.table('static')
with open('data/data1.csv', 'r') as f:
    for line in f:
        line = line.strip()
        if line[0] == 'D':
            continue
        key, value = line.split(',')[0],line.split(',')[1]
        print(key,value)
        table.put(key, {b'LTZX': value.encode()})

for key, data in table.scan():
    print(key.decode('utf-8'), data)

pool = happybase.ConnectionPool(size=3,host="node2",port=9090,protocol='compact',transport='framed')
# 从连接池中取出一个连接
with pool.connection() as conn:
    table = conn.table('test')
    # 查看表中的数据
    for key, data in table.scan():
        print(key.decode('utf-8'), data)
    # 操作完成 及时close 保证每次操作都是一个新启动的连接
    conn.close()
'''

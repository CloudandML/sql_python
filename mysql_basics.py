"""
学习源码地址：https://dev.mysql.com/doc/connector-python/en/connector-python-example-cursor-transaction.html
"""
import mysql.connector
from mysql.connector import errorcode
from datetime import date, datetime, timedelta

config = {
    'user': 'user',
    'password': 'password',
    'host': 'IP',
    'database': 'database',
    # 'raise_on_warnings': True,
    # 'use_pure': False,
}

cnx = mysql.connector.connect(**config)
cursor = cnx.cursor()
# 获取该数据库中的所有表，并显示
cursor.execute(" show tables ")
print(cursor.fetchall())

"""
# 创建表
try:
    cursor.execute("create table if not exists test_tb(id int(4))")
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
        print("该表已经存在")
    else:
        print(err.msg)
else:
    cursor.execute(" show tables ")
    print(cursor.fetchall())
    print("创建成功")

# 删除表
try:
    cursor.execute("drop table test_tb ")
except mysql.connector.Error as err:
    print(err.msg)
else:
    cursor.execute(" show tables ")
    print(cursor.fetchall())
    print("删除成功")

# 修改表名
# cursor.execute("alter table employees rename to employees")
# cursor.execute(" rename table employees to employees")
# cursor.execute(" show tables ")
# print(cursor.fetchall())
"""

# 注意在起表名和约束名时注意不可重复
# 这里的外键约束为：删除主键表记录时，同时删除外键记录
# sql = (
#     "create table salaries ("
#     "emp_id int(11) not null,"
#     "salary int(11) not null,"
#     "from_date date not null,"
#     "to_date date not null,"
#     "primary key (emp_id, from_date) , key emp_id (emp_id),"
#     "constraint salaries_ibfk_1 foreign key (emp_id) references employees (emp_id) on delete cascade"
#     ") engine=InnoDB"
# )
# cursor.execute(sql)
# # cursor.execute("drop table salaries")
# cursor.execute("show tables")
# print(cursor.fetchall())

"""
# *********一次性添加多个表********
TABLES = {}
TABLES['salaries'] = (
    "CREATE TABLE 'salaries' ("
    "  `emp_id` int(11) NOT NULL,"
    "  `salary` int(11) NOT NULL,"
    "  `from_date` date NOT NULL,"
    "  `to_date` date NOT NULL,"
    "  PRIMARY KEY (`emp_id`,`from_date`), KEY `emp_id` (`emp_id`),"
    "  CONSTRAINT `salaries_ibfk_1` FOREIGN KEY (`emp_id`) "
    "     REFERENCES 'employees' ('emp_id') ON DELETE CASCADE"
    ") ENGINE=InnoDB")

for name, ddl in TABLES.items():
    try:
        print("create table {}: ".format(name), end=" ")
        cursor.execute(ddl)
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
            print("already exists.")
        else:
            print(err.msg)
    else:
        print("OK")
"""
# 在表中添加数据
# add_employee = ("insert into employees (birth_date, emp_name, gender, hire_date) "
#                 "values ( %(birth_date)s, %(emp_name)s, %(gender)s, %(hire_date)s)")
#
# # 'emp_id': cursor.lastrowid,
# data_employee = {
#     'birth_date': date(1987, 11, 24),
#     'emp_name': '张三',
#     'gender': 'M',
#     'hire_date': date(2018, 6, 14),
# }
# cursor.execute(add_employee, data_employee)
# cnx.commit()
# cursor.execute("select * from employees")
# [print(c) for c in cursor]


# 在表中查找数据
# sql = ("select * from employees where birth_date=%s" % date(1987, 11, 24))
# sql = "select * from employees where hire_date='2018-06-14' and birth_date='1988-05-02'"
# cursor.execute(sql)
# [print(c) for c in cursor]


# 修改表中数据
# sql = "update employees set emp_name='张三三' where employees.emp_id=25"
# cursor.execute(sql)
# cnx.commit()
# print('修改行数为：',cursor.rowcount)
# for c in cursor:
#     print(c)

# 删除表中数据
# cursor.execute("select * from employees")
# [print(c) for c in cursor]
# sql = " delete from employees where emp_name='John' "
# cursor.execute(sql)
# cnx.commit()
# print("数据库表变动行数为：", cursor.rowcount)
# cursor.execute("select * from employees")
# [print(c) for c in cursor]

# 统计表employees总行数
# cursor.execute("select count(*) as totalcount from employees")
# [print("共有数据行数为：", c[0]) for c in cursor]

# 插入数据
# tomorrow = datetime.now().date() + timedelta(days=1)
# sql = ("INSERT INTO salaries (emp_id, salary, from_date, to_date) "
#        "VALUES (%(emp_id)s, %(salary)s, %(from_date)s, %(to_date)s)" )
# data_salary = {
#   'emp_id': 26,
#   'salary': 6000,
#   'from_date': tomorrow,
#   'to_date': date(9999, 1, 1),
# }
# cursor.execute(sql, data_salary)
# cnx.commit()

# 删除主键表记录时，你可以在建外键时选定外键记录一起级联删除。
# 删除表中数据，其关联的下级表中的数据同时被删除
# sql = "delete from employees where emp_name='张三三'"
# cursor.execute(sql)
# cnx.commit()

# 删除子表中的内容，其上级关联的表中数据不会删除
# sql = "delete from salaries where emp_id=20"
# cursor.execute(sql)
# cnx.commit()

cursor.execute("select * from employees")
[print(c) for c in cursor]
cursor.execute("select * from salaries")
[print(c) for c in cursor]
cursor.close()
cnx.close()

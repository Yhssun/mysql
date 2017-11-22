import pymysql 	#导入 pymysql

# 连接数据库函数
def  connect():
	conn = pymysql.connect(
		host = 'localhost',
		user = 'root',
		passwd = 'yhs0809',
		db = 'test',
		charset = 'utf8',
		port = 3306
	)
	return conn

# 关闭数据库
def my_close(conn):
	conn.close()
	print('close db')

# 查询数据库函数
def my_select(conn):
	#使用cursor()方法获取操作游标
	cur = conn.cursor()

	#1.查询操作
	#编写sql 查询语句 students 对应我的表名
	sql_sel = "select * from students"
	try:
		cur.execute(sql_sel)	#执行sql语句

		results = cur.fetchall() #获取查询的所有记录
		print ("id ","name   ","sex  ", "age  ","address   ","tel      ")

		#遍历数据库
		for r in results:
			id = r[0]
			name = r[1]
			sex = r[2]
			age = r[3]
			address = r[4]
			tel = r[5]
			print(id,name,sex,age,address,tel)
	except Exception as e:
		raise e
	finally:
		# conn.close() #关闭数据库连接
		print("共查找出",cur.rowcount,'条数据')

# 更新数据函数
def my_update(conn):
	
	cur = conn.cursor()

	sql_upd = "update students set name = '吴灵' where name = '吴灵儿'"

	try:
		cur.execute(sql_upd)
		conn.commit()
	except Exception as e:
		conn.rollback()
		print("更新失败！",e)
	finally:
		# conn.close()
		print("成功更新",cur.rowcount,'条数据')

# 插入数据到数据库
def my_insert(conn):
	cur =  conn.cursor()
	my_insert = "insert into students (name,sex,age,address,tel) \
			values('magic','x',11,'zhongshan','123454212')"
	try:
		cur.execute(my_insert)
		conn.commit()
	except Exception as e:
		conn.rollback()
		print("插入失败",e)

# 删除数据库中的数据
def my_del(conn):
	cur = conn.cursor()
	my_del = "delete from students where id = 5"

	try:
		cur.execute(my_del)
		conn.commit()
		print('成功删除',cur.rowcount,'条数据')
	except Exception as e:
		conn.rollback()

# 

conn = connect()	#调用函数打开数据库
cur = conn.cursor()	#使用cursor()方法获取操作游标
# my_update(conn)		#更新数据库
# my_insert(conn)
# for x in range(1,10):
# 	my_insert(conn)
# my_del(conn)
my_select(conn)		#查询数据库
my_close(conn)		#关闭数据库





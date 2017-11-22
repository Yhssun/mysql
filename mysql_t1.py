#coding=utf-8
#导入pymysql的包
import  pymysql
import  pymysql.cursors

#获取一个数据库连接，注意如果是UTF-8类型的，需要制定数据库
#port 必须是数字不能为字符串
connection=pymysql.connect(
            host='localhost',
            user='root',
            password='yhs0809',
            db='test',
            port=3306,
            charset='utf8')
try:
    #获取一个游标
  with connection.cursor() as cursor:
    sql = 'select * from students'
    cout = cursor.execute(sql)
    print("数量： "+str(cout))

    for row in cursor.fetchall():
        #print('%s\t%s\t%s' %row)

      #注意int类型需要使用str函数转义
      if str(row[1]) == "易怀胜":
        print('找到yhs')
        break
      print("ID: "+str(row[0])+'  名字： '+str(row[1])+"  性别： "+row[2])
    connection.commit()
finally:
    connection.close()
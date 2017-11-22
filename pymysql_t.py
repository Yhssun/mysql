import pymysql
conn = pymysql.connect(
		user = 'root',
		passwd = 'yhs0809',
		host = 'localhost',
		db = 'test',
		charset = 'utf8'
	)
cur = conn.cursor()
cur.execute("select * from students")
for  r in cur:
	print("row_number:",(cur.rownumber))
	print("id:"+str(r[0])+"name:"+str(r[1])+"sex:"+str(r[2]))
cur.close()
conn.close()

print("conn:",conn);
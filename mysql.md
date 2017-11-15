# mysql
mysql 
mysql 命令
 1. show databases;
 2. show tables;
 3. use sys;(数据库名)
 4. create database test;(创建数据库test)
 4.1 use test;(用test数据库)
 5. create table students (
	id int unsigned not null auto_increment primary key,
	name char(8) not null,
	sex char(4) not null,
	age tinyint unsigned not null,
 	tel char(13) null default "----"
 );
 6. insert into students (name,sex,age) values ("yhs","man",28);
 7. insert into students values(null,"yhs","man",28,"17820122076")
 8. select * from students;
 9. select name,age from students;
10. select * from students where name = "yhs";
11. where 子句不仅仅支持 "where 列名 = 值" 这种名等于值的查询形式, 对一般的比较运算的运算符都是支持的, 例如 =、>、<、>=、<、!= 以及一些扩展运算符 is [not] null、in、like 等等。 还可以对查询条件使用 or 和 and 进行组合查询
12. % 匹配任意数目字符(包括零个字符)
	_ 匹配任何单个字符
	注意在你使用SQL模式时，你不能使用=或!=；而使用LIKE或NOT LIKE比较操作符。
	如果我就真的要查%或者_，怎么办呢？使用escape，转义字符后面的%或_就不作为通配符了，注意前面没有转义字符的%和_仍然起通配符作用
13. DEFAULT CHARACTER SET utf8：数据库字符集。设置数据库的默认编码为utf8，这里utf8中间不要"-"；
14. 显示表的结构 describe students;
15. update 表名称 set 列名称 = 新值 where 更新条件;
	update students set name = "易怀胜",age = 29 where name = "yhs"
16. delete from 表名称 where 删除条件;
	detete from students where name = "yhs";
17. 修改表: 
	alter table 表名 add 列名 列表数据类型 [after 插入位置];
	在表的最后追加address：
	alter table students add address char(60);
	在age后追加插入列birthday：
	alter table students add birthday date after age;
18. 修改列：
	alter table 表名 change 列名称 列新名称 新数据类型；
	将表tel列改名为telphone:
	alter table students change tel telphone char(13) default "-";
	将name列的数据类型改为char(16):
	alter table students change name name char(16) not null;
19. 删除列：
	alter table 表名 drop 列名称;
	删除birthday：
	alter table students drop birthday;
20. 重命名表：
	alter table 表名 rename 新表名;
	重命名students表为workmates:
	atler table students rename workmates;
21. 删除整张表：
	drop table 表名;
	删除workmates表：
	drop table workmates;
22. 删除整个数据库
	drop database 数据库名;
	删除samp_db数据库：
	drop database samp_db;
23. 修改root用户密码：
	使用mysqladmin方式：
	mysqladmin -u root -p password 新密码
	执行后提示输入旧密码完成修改密码
	
24. ceshi

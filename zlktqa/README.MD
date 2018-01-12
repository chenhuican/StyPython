http://www.bootcdn.cn/
http://www.bootcss.com/

## 1、初始化数据库迁移环境
进入项目目录执行：
#python manage.py db init

J:\zlktqa>python manage.py db init  
Creating directory J:\zlktqa\migrations ... done    
Creating directory J:\zlktqa\migrations\versions ... done    
Generating J:\zlktqa\migrations\alembic.ini ... done    
Generating J:\zlktqa\migrations\env.py ... done    
Generating J:\zlktqa\migrations\README ... done    
Generating J:\zlktqa\migrations\script.py.mako ... done    
Please edit configuration/connection/logging settings in 'J:\\zing.    

执行后 会在项目目录下 出现一个 migrations文件夹

## 2、把表映射到数据库中,生成迁移文件
#python manage.py db migrate

J:\zlktqa>python manage.py db migrate    
INFO  [alembic.runtime.migration] Context impl MySQLImpl.    
INFO  [alembic.runtime.migration] Will assume non-transactional DDL.    
INFO  [alembic.autogenerate.compare] Detected added table 'user'    
Generating J:\zlktqa\migrations\versions\e9fdf18dc9cf_.py ... done    

执行完后，再执行：
#python manage.py db upgrade

J:\zlktqa>python manage.py db upgrade    
INFO  [alembic.runtime.migration] Context impl MySQLImpl.    
INFO  [alembic.runtime.migration] Will assume non-transactional DDL.    
INFO  [alembic.runtime.migration] Running upgrade  -> e9fdf18dc9cf, empty mes    

执行后，数据库中就有相应的表了    

## 3、查看mysql数据库中对应的表
mysql> show tables;    
+----------------------+    
| Tables_in_wenda_demo |    
+----------------------+    
| alembic_version      |    
| user                 |    
+----------------------+    
2 rows in set (0.00 sec)    

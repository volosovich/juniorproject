for email: andreyvolosovich@gmail.com



mysql
mysql> CREATE USER user@localhost IDENTIFIED BY "for_paranoik";
Query OK, 0 rows affected (0.00 sec)

mysql> CREATE DATABASE product_db;
Query OK, 1 row affected (0.00 sec)

mysql> GRANT ALL ON product_db.* TO user@localhost;
Query OK, 0 rows affected (0.00 sec)


Username (leave blank to use 'root'):
Email address: andreyvolosovich@gmail.com
password 123456

================
Tests

Creating test database for alias 'default'...
../home/djangojunior2/virtualpython2/lib/python2.7/site-packages/django/db/models/fields/__init__.py:1474:
RuntimeWarning: DateTimeField Product.created_at received a naive datetime
(2015-11-15 23:04:27.054780) while time zone support is active.
  RuntimeWarning)

.......
----------------------------------------------------------------------
Ran 9 tests in 1.161s

OK
Destroying test database for alias 'default'...


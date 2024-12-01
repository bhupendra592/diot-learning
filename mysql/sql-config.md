BHIoT$ cd /etc/mysql/
BHIoT$ ls
conf.d  debian.cnf  debian-start  my.cnf  my.cnf.fallback  mysql.cnf  mysql.conf.d

# -------

BHIoT$ cat my.cnf

!includedir /etc/mysql/conf.d/
!includedir /etc/mysql/mysql.conf.d/
[mysqld]
bind-address = 0.0.0.0

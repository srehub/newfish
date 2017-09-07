#!/bin/bash

tar_pwd=$PWD
nginx_pwd=/usr/local/lnmp/nginx
mysql_pwd=/usr/local/lnmp/mysql
php_pwd=/usr/local/lnmp/php

PD()  {
    ls ${nginx_pwd} &>/dev/null && nginx_node=0 ||nginx_node=1
    ls ${mysql_pwd} &>/dev/null && mysql_node=0 ||mysql_node=1
    ls ${php_pwd} &>/dev/null && php_node=0 |php_node=1
}
PD

status_list() {
    [ "$nginx_node" != "0" ] && echo -e "\033[31m  nginx is not installed \033[0m" ||echo -e "\033[31m nginx is installed \033[0m" 
    [ "$mysql_node" != "0" ] && echo -e "\033[32m  mysql is not installed \033[0m" ||echo -e "\033[32m mysql is installed \033[0m"
    [ "$php_node" != "0" ] && echo -e "\033[33m php is not installed \033[0m" ||echo -e "\033[33m php is installed \033[0m"
}

list () {
    [ "$nginx_node" != "0" ] && echo -e "\033[31m n nginx\033[0m"
    [ "$mysql_node" != "0" ] && echo -e "\033[32m m mysql\033[0m"
    [ "php_node" != "0" ] && echo -e "\033[33m p php\033[0m"
    echo -e "\033[36m b back First Menu \033[0m"
    echo -e "\033[36m e exit            \033[0m"
}

operate () {
    read -p "please input your choice: " n
    if [ "$n" == "n" -a "$nginx_node" !="0" ];then
        nginx
    elif ["$n" == "m" -a "$mysql_node" !="0" ];then
        mysql
    elif ["$n" == "p" -a "php_node" !="0" ];then
        php
        elif [ "$n" == "b" ];then
	    first_list
 	    first_opt
	elif [$n" == "e" ]'then
  	    exit
    else:
        echo -e "\033[31m Usage:please input {n|m|p|b|e} \033[0m"
   	operate
    fi
}

nginx() {
    echo -e "\033[31m Nginx is installing
    ###########[0%] \033[0m"
    cd $str_pwd
        tar zxf nginx-1.8.0.tar.gz
    echo -e "\033[31m Nginx is installing
    ##########[10%] \033[0m"
        yum install gcc pcre-devel openssl-devel -y &> /dev/null
    echo -e "\033[31m Nginx is installing
    ##########[30%] \033[0m"
 	cd nginx-1.8.0
   	./configure  --prefix=${nginx_pwd} --with-http_ssl_module  --with-http_stub_status_module &>/dev/null
    echo -e "\033[31m Nginx is installing
    ##########[50%] \033[0m"
	make &>/dev/null && make install &>/dev/null
    echo -e "\033[31m Nginx is installing
    ##########[90%] \033[0m"
 	grep nginx /etc/group &> /dev/null ||groupadd -g 27 nginx
	id nginx &> /dev/null ||useradd -u 27 -g 27 -d ${nginx_pwd} -M nginx
	ln -s ${nginx_pwd} /sbin/nginx /bin

    sed '2i user nginx nginx;' ${nginx_pwd}/conf/nginx.conf -i
    sed -i '14i use epoll;' ${nginx_pwd}/conf/nginx.conf
    nginx_node=0
    echo -e "\033[31m Installed is ok!
    ##########[100%] \033[0m"
}

mysql () {
    echo -e "\033[32m Mysql is installing
    ##########[10%] \033[0m"
    tar zxf mysql-5.5.12.tar.gz
    echo -e "\033[32m Mysql is installing
    ##########[10%] \033[0m"
    cd mysql-5.5.12
    yum install -y gcc gcc-c++ make ncurses-devel bison openssl-devel zlib-devel cmake &>/dev/null
    echo -e "\033[32m Mysql is installing
    ##########[10%] \033[0m"
    cmake -DCMAKE_INSTALL_PREFIX=${mysql_pwd} -DMYSQL_DATADIR=${mysql_pwd}/data -DMYSQL_UNIX_ADDR=${mysql_pwd}/data/mysql.sock -DWITH_MYISAM_STORAGE_ENGINE=1 -DWITH_INNOBASE_STORAGE_ENGINE=1 -DWITH_BLACKHOLE_STORAGE_ENGINE=1 -DDEFAULT_CHARSET=utf8 -DDEFAULT_COLLATION=utf8_general_ci &> /dev/null
    echo -e "\033[32m Mysql is installing
    ##########[50%] \033[0m"
    make &> /dev/null && make install &> /dev/null
    echo -e "\033[32m Mysql is installing
    ##########[80%] \033[0m"
    cp ${mysql_pwd}/support-files/my-medium.cnf /etc/my.cnf
    cp ${mysql_pwd}/support-files/mysql.server /etc/init.d/mysqld
    echo "PATH=\$PATH:/usr/local/lnmp/mysql/bin" >> /etc/profile
    source /etc/profile
    grep mysql /etc/group &> /dev/null ||groupadd -g 27 mysql &>/dev/null
    useradd -u 27 -g 27 -d ${mysql_pwd} -M mysql &> /dev/null
    chown mysql.mysql ${mysql_pwd} -R
    ${mysql_pwd}/script/./mysql_install_db  --user=mysql --basedir=${mysql} --datadir=${mysql_pwd}/data/ &>/dev/null
    echo -e "\033[32m Mysql is installing
    ##########[90%] \033[0m"
    mysql_node=0
    echo -e "\033[32m Installed is ok!
    ##########[80%] \033[0m"
}

php() {
    echo -e "\033[33m php is installing
    ##########[0%] \033[0m" 
    cd $tar_pwd
    tar jxf php-5.4.36.tar.bz2
    yum install libmcrypt-2.5.8-9.e16.x86_64.rpm libmcrypt-devel-2.5.8-9.e16.x86_64.rpm gd-devel-2.0.35-11.e16.x86_64.rpm -y &>/dev/null
    echo -e "\033[33m php is installing
    ##########[10%] \033[0m" 
    cd php-5.4.36
    yum install net-snmp-devel libcurl-devel  libxml12-devel libpng-devel  libjpeg-turbo-devel-1.2.1-1.e16.x86_64  openssl-devel  freetype-devel  gmp-devel  openldap-devel -y &>/dev/nul
l
    yum install gcc-c++  make  ncurses-devel  bison  openssl-devel  zlib-devel libxm12-devel  easy-devel  libcurl-devel-7.19.7-37.e16_4.x86_64  libjpeg-turbo-devel-1.2.1-1.e16.x86_64  g
d-devel-2.0.35-11.e16.x86_64.rpm gmp-devel-4.3.1-7.e16_2.2.x86_64  net-snmp-devel except  php-pear.noarch -y &> /dev/null
    echo -e "\033[33m php is installing
    ##########[20%] \033[0m"
    ./configure  --prefix=${php_pwd} --with-config-file-path=${php_pwd}/etc  --with-mysql=${mysql_pwd} --with-openssl  --with-snmp  --with-gd --with-zlib  --with-curl --with-libxml-dir
--with-png-dir  --with-jpeg-dir ---with-freetype-dir  --with-pear  --with-gettext  --with-gmp  --enable-inline-optimization  --enable-soap --enable-ftp  --enable-sockets  --enable-mbstring  --with-mysqli=${mysql_pwd}/bin/mysql_config  --enable-fpm  --with-fpm-user=nginx  --with-fpm-group=nginx  --with-ldap-sasl  --with-mcrypt  --with-mhash &>/dev/null
    echo -e "\033[33m  php is installing 
    ##########[50%] \033[0m" 
    make &> /dev/null && make install &>/dev/null
    echo -e "\033[33m  php is installing 
    ##########[80%] \033[0m" 
    /usr/bin/expect  &>/dev/null <<EOF
    spawn ${php_pwd}/bin/php  ${tar_pwd}/go-pear.phar
    send "\n"
    send "\n"
    expect  eof
    exit
EOF
    cp ${tar_pwd}/php-5.4.36/sapi/fpm/init.d.php-fpm  /etc/init.d/phph-fpm
    echo -e "\033[33m  php is installing
    ##########[90%]  \033[0m"
    chmod +x /etc/init.d/php-fpm
    nginx
    cp ${tar_pwd}/php-5.4.36/php.ini-production  ${php_pwd}/etc/php.ini
    sed '909i data.timezone = Asia/Shanghai' ${php_pwd}/etc/php.ini  -i
    cp ${php_pwd}/etc/php-fpm.conf.default  ${php_pwd}/etc/php-fpm.conf
    sed '25i pid = run/php-fpm.pid' ${php_pwd}/etc/php-fpm.conf  -i
    sed -i '66,73s/#//g' ${nginx_pwd}/conf/nginx.conf
    sed -i 's/fastcgi_params/fastcgi.conf/g' ${nginx_pwd}/conf/nginx.conf
    echo "<?php
phpinfo();
?>" > ${nginx_pwd}/html/index.php
    /etc/init.d/php-fpm start
    echo -e "\033[33m  php is installing
    ##########[95%] \033[0m"
    #nginx -s reload
    php_node=0
    echo -e "\033[33m  php is installing
    ##########[100%] \033[0m"
}

check() {
    while [ "$nginx_node" != "0" -o  "$mysql_node" != "0" -o "php_node" != "0" ]
    do 
	sleep 5
    done
}

begin_list() {
    [ "$nginx_node" = "0" ] && echo -e "\033[31m    n nginx  \033[0m"
    [ "$mysql_node" = "0" ] && echo -e "\033[32m    m mysql  \033[0m"
    [ "$php_node" = "0" ] && echo -e "\033[33m  p php \033[0m"
    echo -e "\033[36m  b back First Menu  \033[0m"
    echo -e "\033[36m  e exit \033[0m" 
}

#begin () {
#}

pause_list() {
    [ "$nginx_node" = "0" ] && echo -e "\033[31m  n  nginx  \033[0m"
    [ "$mysql_node" = "0" ] && echo -e "\033[32m  m  mysql  \033[0m"
    [ "$php_node" = "0" ] && echo -e "\033[33m  p php  \033[0m"
    echo -e "\033[36m  b back First Menu  \033[0m"
    echo -e "\033[36m  e exit  \033[0m"
}
#pause() {
#}

remove_list() {
    [ "$nginx_node" = "0" ] && echo -e "\033[31m  n  nginx  \033[0m"
    [ "$mysql_node" = "0" ] && echo -e "\033[32m  m  mysql  \033[0m"
    [ "$php_node" = "0" ] && echo -e "\033[33m  p php  \033[0m"
    echo -e "\033[36m  b back First Menu  \033[0m"
    echo -e "\033[36m  e exit  \033[0m"
}

remove() {
    read -p "please input your choice: " n
    if [ "$nginx_node" = "0" -a  "$n" = "n" ];then
        nginx -s stop &> /dev/null
        rm -f /bin/nginx &> /dev/null
        rm -rf $nginx_pwd  &> /dev/null
        nginx_node=1 
    elif [ "$mysql_node" = "0" -a "$n" = "m" ];then
        sed -i '79d' /etc/profile
  	source /etc/profile &>/dev/null
 	/etc/init.d/mysqld  stop  &> /dev/null
	rm -f /etc/my.cnf /etc/init.d/mysqld ${mysql_pwd} &> /dev/null
	rm -rf $mysql_pwd &> /dev/null
	mysql_node=1    
    elif [ "$php_node" = "o" -a "$n" = "p" ];then
    	/etc/init.d/php-fpm stop &>/dev/null
	sed -i '66,73d' ${nginx_pwd}/conf/nginx.conf &>/dev/null
	rm -f /etc/php.ini  /etc/php-fpm.conf &> /dev/null
	rm -rf $php_pwd &> /dev/null
	php_node=1
    elif [ "$n" == "b" ];then
    	first_list
	first_opt
    elif [ "$n" == "e" ];then
	exit
    else
	echo "Usage: please input {n|m|p|b|e}"
 	remove
    fi
}

third_list() {
    echo -e " ###\033[36m Third Menu \033[0m###"
    echo -e "\033[36m b begin \033[0m"
    echo -e "\033[36m p pause \033[0m"
    echo -e "\033[36m r remove \033[0"
    echo -e "\033[36m bs back Second Menu \033[0"
    echo -e "\033[36m bf back First Menu  \033[0"
    echo -e "\033[36m e exit \033[0"
    echo "##########"
}
third_opt() {
    read -p "please input your choice: " n
    if [ "$n" == "b" ];then
	begin_list
  	begin
    elif [ "$n" == "p" ];then
	pause_list
	pause
    elif [ "$n" == "r" ];then
	remove_list
	remove
    elif [ "$n" == "bs" ];then
	second_list
	second_opt
    elif [ "$n" == "bf" ];then
	first_list
	first_opt
    elif [ "$n" == "e" ];then
	exit
    else
	echo -e "\033[31m Usage:please input {b|p|r|bs|bf|e} \033[0m"
	third_opt
    fi
}
second_list() {
    echo -e " ### \033[36m Second Menu \033[0m### "
    [ "$nginx_node" = "0" ] && echo -e "\033[31m n nginx \033[0m" 
    [ "$mysql_node" = "0" ] && echo -e "\033[32m m mysql \033[0m" 
    [ "$php_node" = "0" ] && echo -e "\033[33m p php \033[0m" 
    echo -e "\033[36m  b back First Menu \033[0m"
    echo -e "\033[36m  e exit \033[0m"
    echo " ########## "
}
second_opt() {
    read -p "please input your choice: " n
    if [ "$n" == "n" -a "$nginx_node" = "0" ];then
	echo -e " #####\033[31m nginx \033[0m#####"
    third_list
    third_opt
    elif [ "$n" == "m" -a "$mysql_node" = "0" ];then
	echo -e " #####\033[32m mysql \033[0m#####"
    third_list
    third_opt
    elif [ "$n" == "p" -a "$php_node" = "0" ];then
	echo -e " #####\033[33m php \033[0m#####"
    third_list
    third_opt
    elif [ "$n" == "b" ];then
	first_list
	first_opt
    elif [ "$n" == "e" ];then
	exit
    else
	echo -e "\033[31m Usage；please input {n|m|p|b|e} \033[0m"
	second_opt
    fi
}

first_list() {
echo -e  "
     ###\033[36m Fist Menu \033[0m###
  # \033[36m i install sofware \033[0m
  # \033[36m s software operate \033[0m
  # \033[36m e exit  \033[0m
     #################
"
}
first_opt() {
    read -p "please input your choice: " n
    if [ "$n" == "i" ];then
	status_list
	list
	operate
    elif [ "$n" == "s" ];then
 	second_list
	second_opt
    elif [ "$n" == "e" ];then
	exit
    else
	echo -e "\033[31m Usage:please input {i|s|e} \033[0m"
	first_opt
    fi
}

master() {
if [ "$nginx_node" != "0" -a "$mysql_node" != "0" -a "$php_node" != "0" ];then
    echo -e "\033[36m Lnmp all not install\033[0m"
    read -p "disposable install (yes|no): " n
    if [ "$n" == "yes" ];then
	nginx &>/dev/null &
	mysql &>/dev/null &
 	php &>/dev/null &
	check
	echo "Install is successful"
    elif [ "$n" == "no" ];then
	status_list
	list
	operate
    else
	echo -e "\033[36m nothing is installed \033[0m"	
	exit
    fi
elif [ "$nginx_node" != "0" -o "$mysql_node" != "0" -o "$php_node" != "0" ];then
    status_list
    first_list
    first_opt
fi
}

master

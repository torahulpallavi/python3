# python3

pip install psycopg2

pre-requisite steps :

steps :

  1. python2.7
  2. curl "https://bootstrap.pypa.io/get-pip.py" -o "get-pip.py"
  3. python get-pip.py
  4. pip install psycopg2-binary
  5. yum install gcc
  6. sudo yum install postgresql postgresql-devel python-devel
  7. pip install psycopg2

Postgress :

  1. sudo su - postgres
  2. psql


Ubuntu 
https://www.luminanetworks.com/docs-lsc-610/Topics/SDN_Controller_Software_Installation_Guide/Appendix/Installing_Psycopg_for_Ubuntu_1.html


  sudo -u postgres psql postgres

# \password postgres

Enter new password: 

list of databases 
\l

select database
\c database_name

list of tables
\dt


CREATE TABLE name(
   first integer PRIMARY KEY,
   last text 
);

size of database
SELECT pg_size_pretty( pg_database_size('postgres'));


create table name (
 id int ,
 name varchar(20)
)






  
  
  

import mysql.connector
db1 = None
def connect():
    global db1
    db1 = mysql.connector.connect(host="localhost",user="root",
    password="12345678"
  )

connect()
c1 = db1.cursor()
c1.execute("create database LIBRARY")
c1.execute("use LIBRARY")
c1.execute("create table users (username varchar(30), passw varchar(30))")
c1.execute("insert into users values('Jashan','1234')")
c1.execute("insert into users values('Aman','5678')")
c1.execute("insert into users values('Aarav','abcd')")
db1.commit()
c1.execute("create table member(mid varchar(20) primary key,name varchar(50),email varchar(50),phone varchar(20))")
c1.execute("create table book(bookid varchar(20) primary key,title varchar(50),author varchar(50),publisher varchar(50),cost integer)")
c1.execute("create table issue(mid varchar(20),bookid varchar(20),dateofissue date)")
c1.execute("create table issuelog(mid varchar(20),bookid varchar(20),dateofissue date,dateofreturn date)")

db1.commit()

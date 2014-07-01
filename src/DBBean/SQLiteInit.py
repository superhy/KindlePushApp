'''
Created on 2013-4-29

@author: Administrator
'''

import sqlite3

class sqlInit():
    
    def __init__(self):
        #create database ans connction
        self.conn = sqlite3.connect("../../DataBase/kindle_DB.db")
        self.cur = self.conn.cursor()
        
    def __del__(self):
        self.cur.close()
        self.conn.close()
    
    def createTable(self):
        # create table
        self.conn.execute("create table if not exists user(user_id integer primary key autoincrement, "
                         +"user_name varchar(128) not null, user_password varchar(64) not null, "
                         +"user_sex integer null, user_tel varchar(64) null, "
                         +"user_email varchar(128) not null, user_email_pwd varchar(128) not null, "
                         +"user_sendemail varchar(128) not null)")
        
        self.conn.execute("create table if not exists book_send(send_id integer primary key autoincrement, "
                          +"book_name varchar(64) not null, book_file varchar(128) not null, "
                          +"user_name varchar(128) not null, push_num integer null, total_num integer null, "
                          +"save_flag integer not null)")
        
        self.conn.execute("")
        
        self.conn.execute("")
        self.conn.commit()
        
    def insRegister(self, userObj):
        user_name = userObj.getuser_name()
        user_password = userObj.getuser_password()
        user_sex = userObj.getuser_sex()
        user_tel = userObj.getuser_tel()
        user_email = userObj.getuser_email()
        user_email_pwd = userObj.getuser_email_pwd()
        user_sendemail = userObj.getuser_sendemail()
        
        self.conn.execute("insert into user(user_name, user_password, user_sex, user_tel, user_email, "
                          +"user_email_pwd, user_sendemail) values ('" + user_name + "', '" + user_password 
                          +"', " + user_sex +", '" + user_tel +"', '" + user_email + "', '" 
                          + user_email_pwd + "', '" + user_sendemail + "')")
        self.conn.commit()
        
    def insBookSend(self, bookSendObj):
        book_name = bookSendObj.getbook_name()
        book_file = bookSendObj.getbook_file()
        user_name = bookSendObj.getuser_name()
        push_num = bookSendObj.getpush_num()
        total_num = bookSendObj.gettotal_num()
        save_flag = bookSendObj.getsave_flag()
        
#         print book_name 
#         print book_file
#         print user_id 
#         print push_num
#         print total_num
#         print save_flag
        
        self.conn.execute("insert into book_send(book_name, book_file, user_name, push_num, total_num, "
                          +"save_flag) values ('" + book_name + "', '" + book_file + "', '" + user_name 
                          +"', " + str(push_num) + ", " + str(total_num) + ", " + str(save_flag) + ")")
        self.conn.commit()
        
    def selectLogin(self, str_username, str_userpassword):
        # execute the select operation
        self.cur.execute("select * from user where user_name = '" + str_username + "' and user_password = '" 
                         + str_userpassword + "'")
        res = self.cur.fetchall()
        return res

def Test():
    # test
    dbConn = sqlInit()
    dbConn.createTable()
    userName = "superhy"
    userPassword = "232323"
    resTest = dbConn.selectLogin(userName, userPassword)
    print resTest
    
if __name__ == '__main__':
    Test()

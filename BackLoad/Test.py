'''
Created on 2013-4-29

@author: Administrator
'''

import sqlite3
from DBBean.SQLiteInit import *

def Test():
    # test
    dbConn = sqlInit()
    dbConn.createTable()
    userName = "superhy"
    userPassword = "232323"
    resTest = dbConn.selectLogin(userName, userPassword)
    print resTest

def main():
    Test()
if __name__ =="__main__":
    main()
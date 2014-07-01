'''
Created on 2013-5-17

@author: Administrator
'''

import os
import smtplib 
from email.mime.text import MIMEText 
from email.mime.multipart import MIMEMultipart 
from email.mime.application import MIMEApplication 
from email.mime.base import MIMEBase
from email.mime.text import MIMEText

class BaseMail:
    def __init__(self, smtp, bSmtpAuth, sender, pwd):
        self.smtp = smtp
        self.bSmtpAuth = bSmtpAuth
        self.sender = sender
        self.pwd = pwd
        
    def _parserSend(self, sSubject, sContent, lsPlugin):
        return sSubject, sContent, lsPlugin
    
    def send(self, sSubject, sContent, lsTo, lsCc = [], lsPlugin = []):
        mit = MIMEMultipart() 
        mit['from'] = self.sender 
        mit['to'] = ','.join(lsTo) 
        if lsCc:
            mit['cc'] = ','.join(lsCc)
            
        codeSubject, codeContent, codePlugin = self._parserSend(sSubject, sContent, lsPlugin)
        mit.attach(MIMEText(codeContent, 'html', 'utf-8')) 
        mit['subject'] = codeSubject 
        for plugin in codePlugin: 
            mitFile = MIMEApplication( open(plugin['content']).read(), )
            mitFile.add_header( 'content-disposition', 'attachment', filename=plugin['subject'] )
            mit.attach(mitFile)
#             part = MIMEBase('application', 'octet-stream') #'octet-stream': binary data 
#             part.set_payload(open(file, 'rb'.read()))  
#             part.add_header('Content-Disposition', 'attachment; filename="%s"' % os.path.basename(file)) 
#             mit.attach(part) 
            
        server = smtplib.SMTP(self.smtp) 
        #server.set_debuglevel(smtplib.SMTP.debuglevel) 
        if self.bSmtpAuth: 
            server.docmd("EHLO server") 
        server.starttls() 
        server.login(self.sender, self.pwd) 
        server.sendmail(self.sender, lsTo , mit.as_string()) 
        server.close()
        
class GMail(BaseMail): 
    def __init__(self, sender, pwd): 
        BaseMail.__init__( self, 'smtp.gmail.com', True, sender, pwd ) 
        self.__strcode = 'utf-8' 
         
    def _parserSend(self, sSubject, sContent, lsPlugin): 
        for i in lsPlugin: 
            i['subject'] = i['subject'].encode(self.__strcode)          
        return sSubject.encode(self.__strcode), sContent.encode(self.__strcode), lsPlugin 

class Com163Mail(BaseMail): 
    def __init__(self, sender, pwd): 
        BaseMail.__init__( self, 'smtp.163.com', False, sender, pwd ) 
        self.__strcode = 'utf-8' 
         
    def _parserSend(self, sSubject, sContent, lsPlugin): 
        for i in lsPlugin: 
            i['subject'] =  i['subject'].encode('gbk') 
        return sSubject, sContent.encode(self.__strcode), lsPlugin  

class SinaMail(BaseMail):
    def __init__(self, sender, pwd): 
        BaseMail.__init__( self, 'smtp.sina.com', False, sender, pwd ) 
        self.__strcode = 'utf-8' 
         
    def _parserSend(self, sSubject, sContent, lsPlugin): 
        for i in lsPlugin: 
            i['subject'] =  i['subject'].encode('gbk') 
        return sSubject, sContent.encode(self.__strcode), lsPlugin

class QQMail(BaseMail):
    def __init__(self, sender, pwd): 
        BaseMail.__init__( self, 'smtp.qq.com', False, sender, pwd ) 
        self.__strcode = 'utf-8' 
         
    def _parserSend(self, sSubject, sContent, lsPlugin): 
        for i in lsPlugin: 
            i['subject'] =  i['subject'].encode('gbk') 
        return sSubject, sContent.encode(self.__strcode), lsPlugin
    
class YahooMail(BaseMail):
    def __init__(self, sender, pwd): 
        BaseMail.__init__( self, 'smtp.mail.yahoo.com', False, sender, pwd ) 
        self.__strcode = 'utf-8' 
         
    def _parserSend(self, sSubject, sContent, lsPlugin): 
        for i in lsPlugin: 
            i['subject'] =  i['subject'].encode('gbk') 
        return sSubject, sContent.encode(self.__strcode), lsPlugin

class Com126Mail(BaseMail):
    def __init__(self, sender, pwd): 
        BaseMail.__init__( self, 'smtp.126.com', False, sender, pwd ) 
        self.__strcode = 'utf-8' 
         
    def _parserSend(self, sSubject, sContent, lsPlugin): 
        for i in lsPlugin: 
            i['subject'] =  i['subject'].encode('utf-8') 
        return sSubject, sContent.encode(self.__strcode), lsPlugin
    
class SohuMail(BaseMail):
    def __init__(self, sender, pwd): 
        BaseMail.__init__( self, 'smtp.sohu.com', False, sender, pwd ) 
        self.__strcode = 'utf-8' 
         
    def _parserSend(self, sSubject, sContent, lsPlugin): 
        for i in lsPlugin: 
            i['subject'] =  i['subject'].encode('gbk') 
        return sSubject, sContent.encode(self.__strcode), lsPlugin
    
class TomMail(BaseMail):
    def __init__(self, sender, pwd): 
        BaseMail.__init__( self, 'smtp.tom.com', False, sender, pwd ) 
        self.__strcode = 'utf-8' 
         
    def _parserSend(self, sSubject, sContent, lsPlugin): 
        for i in lsPlugin: 
            i['subject'] =  i['subject'].encode('gbk') 
        return sSubject, sContent.encode(self.__strcode), lsPlugin
    
class Com21cnMail(BaseMail):
    def __init__(self, sender, pwd): 
        BaseMail.__init__( self, 'smtp.21cn.com', False, sender, pwd ) 
        self.__strcode = 'utf-8' 
         
    def _parserSend(self, sSubject, sContent, lsPlugin): 
        for i in lsPlugin: 
            i['subject'] =  i['subject'].encode('gbk') 
        return sSubject, sContent.encode(self.__strcode), lsPlugin

class ChinaMail(BaseMail):
    def __init__(self, sender, pwd): 
        BaseMail.__init__( self, 'smtp.china.com', False, sender, pwd ) 
        self.__strcode = 'utf-8' 
         
    def _parserSend(self, sSubject, sContent, lsPlugin): 
        for i in lsPlugin: 
            i['subject'] =  i['subject'].encode('gbk') 
        return sSubject, sContent.encode(self.__strcode), lsPlugin
    
def Test():
    sSubject = u'python email Test'
    sContent = u'This is your book'
    lsPlugin = [{'subject' : r'E:/Test.txt'}]
    gmail = GMail('superhy199148@gmail.com', 'qdhy19910408')
    lsTo = ['superhy199148@gmail.com']
    lsCc = []
    gmail.send(sSubject, sContent, lsTo, lsCc, lsPlugin)
    print 'send OK !'
    
if __name__ == "__main__":
    Test()
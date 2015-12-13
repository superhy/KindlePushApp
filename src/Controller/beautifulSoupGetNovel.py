# -*- coding: UTF-8 -*-

'''
Created on 2013-5-10

@author: Administrator
'''

from BeautifulSoup import BeautifulSoup, Comment
from getPageTest import *
import re
import string
import urllib2

class beautifulSoupGetNovel():
    
    def setURL(self, URL):
        self.url = URL
        
    def getFileName(self):
        self.htmlCode = urllib2.urlopen(self.url).read() # get page's htmlcode
        self.soup = BeautifulSoup(self.htmlCode, fromEncoding = "utf-8") # set beautifulSoup
        
        titleTag = self.soup.title.string
        self.localFile = u"../../novelFile/"
        self.bookName = u""
        i = 0
        self.bookName = self.bookName + titleTag[i]
        self.localFile = self.localFile + titleTag[i]
        self.localFile = self.localFile + ".txt"
        return self.bookName, self.localFile    
        
    def createLocalFile(self, fileLocation):
        self.myFile = open(fileLocation, 'w')
        return self.myFile
    
    def ayasHtmlCode(self):
        self.htmlCode = urllib2.urlopen(self.url).read()
        self.soup = BeautifulSoup(self.htmlCode, fromEncoding = "utf-8") 
        
        soup_del = self.soup.findAll("span", { "class" : "watermark" })
        [comment.extract() for comment in soup_del]
        roughly_content = self.soup.findAll('p')
        
        str_charpter = ""
        if self.soup.h2.em:
            charpter = self.soup.h2.em.string
            str_charpter = str(charpter)
        else:
            str_charpter = "    sorry, you are not vip! it's end!\r\n"
            return str_charpter

        pat_01 = re.compile(r'href="([^"]*)"')     
        str_Story = ""
        str_Story = str_Story + "    " + str_charpter + "\r\n\r\n\r\n"   
        for item in roughly_content:
            if pat_01.search(str(item)):
                break
            else:
                str_Story = str_Story + str(item)    
        str_Story = str_Story.replace('<p>', '    ') 
        str_Story = str_Story.replace('</p>', '\r\n')
        str_Story += "\r\n\r\n"          
        return str_Story 
        
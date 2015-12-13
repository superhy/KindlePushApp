# -*- coding: UTF-8 -*-

'''
Created on 2013-5-10

@author: Administrator
'''

from BeautifulSoup import BeautifulSoup
import beautifulSoupGetNovel 
import urllib2
import re

class ayasURL():
    
    def setURL(self, URL):
        self.url = URL
    
    def grabHref(self):
        html = urllib2.urlopen(self.url).read()
        self.html = unicode(html, "gb2312", "ignore").encode('utf-8', 'ignore')
        
        self.content = BeautifulSoup(self.html).findAll('a')
        self.pat = re.compile(r'href="([^"]*)"')
        self.pat2 = re.compile(r'http://book.zongheng.com/chapter/')
        
        self.endStr = "    sorry, you are not vip! it's end!\r\n"
        self.urlNum = len(self.content)

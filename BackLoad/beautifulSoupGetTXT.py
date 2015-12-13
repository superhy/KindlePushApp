'''
Created on 2013-2-1

@author: Administrator
'''

from BeautifulSoup import BeautifulSoup, Comment

import urllib2
import string
import re


class beautifulSoupGetTXT():
    
    def setUrl(self, URL):       
        self.url = URL
    
    def getFileName(self):       
        htmlCode = urllib2.urlopen(self.url).read() # get page's htmlcode    
        soup = BeautifulSoup(htmlCode, fromEncoding="utf-8") #set beautifulSoup
        title_Tag = soup.title.string
    
        # creat file by novel name
        self.fileName = "../novelFile/"
        i = 0
        while 1:
            if title_Tag[i] == ',':
                break
            self.fileName = self.fileName + title_Tag[i]
            i = i + 1
        self.fileName = self.fileName + ".txt"
        return self.fileName     
        
    def createLocalFile(self):       
        localFile =self.getFileName()
        myfile = open(localFile, 'w')
        return myfile        
    
    def ayasHtmlCode(self): 
        htmlCode = urllib2.urlopen(self.url).read()
        #htmlCode = unicode(htmlCode,'gb18030','ignore')
        
        soup = BeautifulSoup(htmlCode,fromEncoding="utf-8")
        
        del_soup = soup.findAll("span", { "class" : "watermark" })
        [comment.extract() for comment in del_soup]
        roughly_content = soup.findAll('p')
        str_charpter = ""
        print soup.h2.em
        if soup.h2.em:
            charpter = soup.h2.em.string
            str_charpter = str(charpter)
        else:
            str_charpter = "    sorry, you are not vip! it's end!\r\n"
            return str_charpter
        #print str(charpter)
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
        #print str_Story
            
        return str_Story 

def main():
    
    urlTest = raw_input("urlTest:")
    getObj = beautifulSoupGetTXT()
    getObj.setUrl(urlTest)
    file = getObj.createLocalFile()
    #strTest = ayasHtmlCode(urlTest)
if __name__ == "__main__":
    main()
    
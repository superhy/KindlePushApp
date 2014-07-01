'''
Created on 2013-1-29

@author: Administrator
'''

from BeautifulSoup import BeautifulSoup
from beautifulSoupGetTXT import *
import urllib2
import re

class useURLGetWholeBook():
    
    def setUrl(self, URL):
        self.url = URL

    def grabHrefGetBook(self):
        getTXTObj = beautifulSoupGetTXT()
        html = urllib2.urlopen(self.url).read()
        html = unicode(html,'gb2312','ignore').encode('utf-8','ignore')
        
        content = BeautifulSoup(html).findAll('a')
        pat = re.compile(r'href="([^"]*)"')
        pat2 = re.compile(r'http://book.zongheng.com/chapter/')
        print len(content)
        
        flagFileCreated = 0
        #myChapterNum = 0
        #old_str = ""
        end_str = "    sorry, you are not vip! it's end!\r\n"
        for item in content:
            h = pat.search(str(item))
            href = h.group(1)
            if pat2.search(href):
                ans = href
            else:
                ans = self.url+href
            pat3 = re.match(r'http://book.zongheng.com/chapter/', ans)
            if pat3:
                if flagFileCreated == 0:
                    getTXTObj.setUrl(ans)
                    myStoryFile = getTXTObj.createLocalFile()
                    flagFileCreated = 1
                getTXTObj.setUrl(ans)
                new_str = getTXTObj.ayasHtmlCode()
                if new_str != end_str:
                    myStoryFile.write(new_str)
                else:
                    myStoryFile.write(end_str)
                    break
                #myChapterNum+=1
                print ans  
        myStoryFile.close()


def main():
    
#    book_id = raw_input("ID: ")
#    book_url = "http://book.zongheng.com/showchapter/"+book_id+".html"
    book_url = raw_input("URL: ")
    getBook = useURLGetWholeBook()
    getBook.setUrl(book_url) 
    getBook.grabHrefGetBook()
if __name__=="__main__":
    main()
    
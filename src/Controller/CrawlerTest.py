# -*- coding: UTF-8 -*-

'''
Created on 2013-2-8

@author: Administrator
'''

import re
import os
from urllib import urlopen
import sys


def getWebPageContent(url, encoding):
     
    try:
        resp = urlopen(url)
        return resp.read().decode(encoding)
    except Exception:
        sys.stderr.write('error on URL!\n' % (url))
        
def splitMatch(content, reg):
    return re.search(reg, content).group(1)

def splitMatches(content, reg):
    return re.findall(reg, content)

def crawLinks(seedUrl):
    
    content = getWebPageContent(seedUrl, 'GB18030')  
    
    bookTitleReg = r'<title>(.*?)</title>\s*(?=<meta)'
    bookTitle = splitMatch(content, bookTitleReg)
    
#    bookTitle = bookTitle[0:str(bookTitle).index('-')]

    bookTitle = bookTitle[0:10]

    chapterReg = r'<li\s*class=\"chaptr\">(.*?)</li>\s*((?:<li\s*class=\"(?:artl|artr)\">\s*<a\s*title=\".*?\"\s*target=\"_blank\"\s*href=\".*?\">.*?</a>\s*</li>\s*)+)'
    sectionReg = r'(?<=href=\")(.*?)(?=\")' 
    matches = splitMatches(content, chapterReg)
    chapterWithSectionDict = {}
    for m in matches:
        chapterName = m[0]
        sections = splitMatches(str(m[1:]), sectionReg)
        chapterWithSectionDict[chapterName] = sections
    return (bookTitle, sorted(chapterWithSectionDict.items(), key=lambda k: k[1], reverse=False))

def crawSectionPageAndSaveAsText(fileName, saveDir, *sectionLink):
    print('begin <%s>' % (fileName))
    filePath = os.path.join(saveDir, fileName)+'.html'

    if not os.path.exists(saveDir):
        os.makedirs(saveDir)
    try:
        f = open(filePath, 'w+') 
        f.write('<b>' + fileName + '</b><br /><br />') 
        for link in sectionLink[0]:
            sectionTitleAndContent = crawSectionTitleAndContent(str(link))
            f.write('<b>' + sectionTitleAndContent[0] + '</b><br />') 
            f.write(sectionTitleAndContent[1] + '<br /><br />')
            print('catch finished chapter <%s>!' % (sectionTitleAndContent[0]))
        f.close()
    except Exception:
        sys.stderr.write('writing<%s> error IO!\n' % (fileName))
        
def crawSectionTitleAndContent(sectionLink):

    content = getWebPageContent(sectionLink, 'GB18030')

    sectionTitleReg = r'<dl\s*class="box_t"><dd>(.*?)</dd></dl>'
    sectionTitle = splitMatch(content, sectionTitleReg)    

    sectionContentReg = r'<dl\s*class="box_body"\s*id="fontzoom">\s*<dd\s*id="Article">([\d\D]*?)</dd>\s*</dl>'
    sectionContent = splitMatch(content, sectionContentReg)
    return (sectionTitle, sectionContent)

def main():
    sectionLinks = crawLinks('http://book.2cto.com/201211/9643.html')
    bookTitle = sectionLinks[0]

    print('<' + bookTitle + '> have' + str(len(sectionLinks[1])) + 'chapter')
    for item in sectionLinks[1]:
        crawSectionPageAndSaveAsText(item[0], 'e:/PyTest/' + bookTitle + os.path.altsep, item[1])
        print('finished<%s>\n' % (item[0]))
    print('all finished!')
     
if __name__=='__main__':
    main()

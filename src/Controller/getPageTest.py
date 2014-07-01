'''
Created on 2013-1-29

@author: Administrator
'''

import urllib2
import sys
import re

def getHtmlCode(url, localfile):
    html = urllib2.urlopen(url).read()
    html = unicode(html,'utf-8','ignore')
    myfile = open(localfile, 'w')
    myfile.write(html)
    
    print html
    return html


def getHtml(url):
    Html = urllib2.urlopen(url).read()
    Html = unicode(Html,'utf-8','ignore')
    
    print Html
    return Html


def Test():
    url = raw_input("urlTest:")
    localfile = 'htmlCode.txt'
    getHtmlCode(url, localfile)


if __name__ == "__main__":
    Test()

 
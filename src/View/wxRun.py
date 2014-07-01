'''
Created on 2013-4-26

@author: Administrator
'''

import wx
import wxLoginFrame

class Run():
           
    def runLoginFrame(self):
        appRun = wx.App()
        frame = wxLoginFrame.wxLoginFrame(None)
        frame.Show(True)
        appRun.MainLoop()
        
def main():
    runLoginFrameObj = Run()
    runLoginFrameObj.runLoginFrame()  
    
if __name__ == "__main__": 
    main()
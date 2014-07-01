# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Sep  8 2010)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
from DBBean.SQLiteInit import *
from wxRun import *

###########################################################################
## Class wxLoginFrame
###########################################################################

class wxLoginFrame ( wx.Frame ):
    
    def __init__( self, parent ):
        wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 400,250 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
        
        self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
        
        gSizer3 = wx.GridSizer( 2, 2, 0, 0 )
        
        self.m_staticTextUserName = wx.StaticText( self, wx.ID_ANY, u"UserName :", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticTextUserName.Wrap( -1 )
        gSizer3.Add( self.m_staticTextUserName, 0, wx.ALL, 5 )
        
        self.m_textCtrlUserName = wx.TextCtrl( self, wx.ID_ANY, u"enter your UserName", wx.DefaultPosition, wx.Size( 185,-1 ), 0 )
        gSizer3.Add( self.m_textCtrlUserName, 0, wx.ALL, 5 )
        
        self.m_staticTextPassWord = wx.StaticText( self, wx.ID_ANY, u"PassWord :", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticTextPassWord.Wrap( -1 )
        gSizer3.Add( self.m_staticTextPassWord, 0, wx.ALL, 5 )
        
        self.m_textCtrlPassWord = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 185,-1 ), wx.TE_PASSWORD )
        gSizer3.Add( self.m_textCtrlPassWord, 0, wx.ALL, 5 )
        
        self.m_buttonSubmit = wx.Button( self, wx.ID_ANY, u"OK", wx.DefaultPosition, wx.DefaultSize, 0 )
        gSizer3.Add( self.m_buttonSubmit, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
        
        self.m_buttonCancel = wx.Button( self, wx.ID_ANY, u"Cancel", wx.DefaultPosition, wx.DefaultSize, 0 )
        gSizer3.Add( self.m_buttonCancel, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
        
        self.SetSizer( gSizer3 )
        self.Layout()
        
        self.Centre( wx.BOTH )
        
        # Connect Events
        self.m_buttonSubmit.Bind( wx.EVT_BUTTON, self.OnSubmit )
        self.m_buttonCancel.Bind( wx.EVT_BUTTON, self.OnCancel )
    
    def __del__( self ):
        pass
    
    def OnSubmit( self, event ):
        str_userName = self.m_textCtrlUserName.Label
        str_userPassword = self.m_textCtrlPassWord.Label  
        dbConnLogin = sqlInit()
        dbConnLogin.createTable()
        subRes = dbConnLogin.selectLogin(str_userName, str_userPassword)
            
        if subRes:
            self.Close(True)
            mainFrame.m_staticTextUserWel.Label = "welcome ! " + subRes[0][1] + "This is KindlePush..."
        else:
            dlg = wx.MessageDialog(None, 'Login Failed... Please Try Again !', 'Warnning...', wx.YES_NO | wx.ICON_QUESTION)
            result = dlg.ShowModal()
            if result == wx.ID_YES:
                dlg.Destroy()
            else:
                dlg.Destroy()
                self.Close(True)
                mainFrame.m_staticTextUserWel.Label = "you haven't logined !"
                
    def OnCancel( self, event ):
        self.Close(True)
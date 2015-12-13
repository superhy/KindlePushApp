# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Sep  8 2010)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.html
import DBBean.SQLiteInit
import wxRun
import wxMainFrame
import wxRegisterFrame
import Model.userModel

###########################################################################
## Class wxLoginFrame
###########################################################################

class wxLoginFrame ( wx.Frame ):
    
    def __init__( self, parent ):
        
        
        wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Welcome to KindlePush ! Please Login First", pos = wx.DefaultPosition, size = wx.Size( 400,400 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
        
        self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
        
        bSizerLogin = wx.BoxSizer( wx.VERTICAL )
        
        gSizerLogin = wx.GridSizer( 3, 2, 0, 0 )
        
        gSizerLogin.SetMinSize( wx.Size( 400,250 ) ) 
        self.m_staticTextUserName = wx.StaticText( self, wx.ID_ANY, u"UserName :", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticTextUserName.Wrap( -1 )
        gSizerLogin.Add( self.m_staticTextUserName, 0, wx.ALL, 5 )
        
        self.m_textCtrlUserName = wx.TextCtrl( self, wx.ID_ANY, u"enter your UserName", wx.DefaultPosition, wx.Size( 185,-1 ), 0 )
        gSizerLogin.Add( self.m_textCtrlUserName, 0, wx.ALL, 5 )
        
        self.m_staticTextPassWord = wx.StaticText( self, wx.ID_ANY, u"PassWord :", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticTextPassWord.Wrap( -1 )
        gSizerLogin.Add( self.m_staticTextPassWord, 0, wx.ALL, 5 )
        
        self.m_textCtrlPassWord = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 185,-1 ), wx.TE_PASSWORD )
        gSizerLogin.Add( self.m_textCtrlPassWord, 0, wx.ALL, 5 )
        
        self.m_buttonSubmit = wx.Button( self, wx.ID_ANY, u"OK", wx.DefaultPosition, wx.DefaultSize, 0 )
        gSizerLogin.Add( self.m_buttonSubmit, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
        
        self.m_buttonRegister = wx.Button( self, wx.ID_ANY, u"Register", wx.DefaultPosition, wx.DefaultSize, 0 )
        gSizerLogin.Add( self.m_buttonRegister, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
        
        bSizerLogin.Add( gSizerLogin, 1, wx.EXPAND, 5 )
        
        bSizerWel = wx.BoxSizer( wx.VERTICAL )
        
        self.m_htmlWinWelPage = wx.html.HtmlWindow( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 375,160 ), wx.html.HW_SCROLLBAR_AUTO )
        bSizerWel.Add( self.m_htmlWinWelPage, 0, wx.ALL, 5 )
        
        bSizerLogin.Add( bSizerWel, 1, wx.EXPAND, 5 )
        
        self.SetSizer( bSizerLogin )
        self.Layout()
        self.m_statusBarAuthor = self.CreateStatusBar( 1, wx.ST_SIZEGRIP, wx.ID_ANY )
        self.m_statusBarAuthor.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 93, 90, False, wx.EmptyString ) )
        self.SetStatusText("Powered By superhy?2013 superhy199148@gmail.com")
        if "gtk2" in wx.PlatformInfo:             
            self.m_htmlWinWelPage.SetStandardFonts()
 
        wx.CallAfter(self.m_htmlWinWelPage.LoadPage, "http://www.zongheng.com/")
        
        self.Centre( wx.BOTH )
        
        # Connect Events
        self.m_buttonSubmit.Bind( wx.EVT_BUTTON, self.OnSubmit )
        self.m_buttonRegister.Bind( wx.EVT_BUTTON, self.OnRegister )
        
        def __del__( self ):
            pass
    
    def checkLogin(self, subRes):
        if subRes:
            self.Close(True)
            self.Destroy()       
            userObj = Model.userModel.user()
            userObj.setuser_id(subRes[0][0])
            userObj.setuser_name(subRes[0][1])
            userObj.setuser_password(subRes[0][2])
            userObj.setuser_sex(subRes[0][3])
            userObj.setuser_tel(subRes[0][4])
            userObj.setuser_email(subRes[0][5])
            userObj.setuser_email_pwd(subRes[0][6])
            userObj.setuser_sendemail(subRes[0][7])
            
            appRun = wx.App()
            frame = wxMainFrame.wxMainFrame(None, userObj)
            frame.Show(True)
            appRun.MainLoop()
                 
        else:
            dlg = wx.MessageDialog(None, 'Login Failed... Please Try Again !', 'Warnning...', wx.YES_NO | wx.ICON_QUESTION)
            result = dlg.ShowModal()
            if result == wx.ID_YES:
                dlg.Destroy()
            else:
                dlg.Destroy()
                self.Close(True)
                self.Destroy()
    
    def OnSubmit( self, event ):
        str_userName = self.m_textCtrlUserName.GetValue()
        str_userPassword = self.m_textCtrlPassWord.GetValue() 
        dbConnLogin = DBBean.SQLiteInit.sqlInit()
        dbConnLogin.createTable()
        subRes = dbConnLogin.selectLogin(str_userName, str_userPassword)
            
        self.checkLogin(subRes)
                
    def OnRegister( self, event ):
        self.Close(True)
        self.Destroy()
        
        appRun = wx.App()
        frame = wxRegisterFrame.wxRegisterFrame(None)
        frame.Show(True)
        appRun.MainLoop()
# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Sep  8 2010)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wxRun
import DBBean.SQLiteInit
import Model.userModel

###########################################################################
## Class wxRegisterFrame
###########################################################################

class wxRegisterFrame ( wx.Frame ):
    
    def __init__( self, parent ):
        wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"UserInform", pos = wx.DefaultPosition, size = wx.Size( 350,500 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
        
        self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
        
        gSizerRegister = wx.GridSizer( 9, 2, 0, 0 )
        
        self.m_staticTextUserName = wx.StaticText( self, wx.ID_ANY, u"user_name :", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticTextUserName.Wrap( -1 )
        gSizerRegister.Add( self.m_staticTextUserName, 0, wx.ALL, 5 )
        
        self.m_textCtrlUserName = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 150,-1 ), 0 )
        gSizerRegister.Add( self.m_textCtrlUserName, 0, wx.ALL, 5 )
        
        self.m_staticTextUserPassword = wx.StaticText( self, wx.ID_ANY, u"user_password :", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticTextUserPassword.Wrap( -1 )
        gSizerRegister.Add( self.m_staticTextUserPassword, 0, wx.ALL, 5 )
        
        self.m_textCtrlUserPassword = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 150,-1 ), wx.TE_PASSWORD )
        gSizerRegister.Add( self.m_textCtrlUserPassword, 0, wx.ALL, 5 )
        
        self.m_staticTextPwdRap = wx.StaticText( self, wx.ID_ANY, u"Rapece Your password :", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticTextPwdRap.Wrap( -1 )
        gSizerRegister.Add( self.m_staticTextPwdRap, 0, wx.ALL, 5 )
        
        self.m_textCtrlPwdRap = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 150,-1 ), wx.TE_PASSWORD )
        gSizerRegister.Add( self.m_textCtrlPwdRap, 0, wx.ALL, 5 )
        
        self.m_staticTextUserSex = wx.StaticText( self, wx.ID_ANY, u"user_sex(m:0, f:1) :", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticTextUserSex.Wrap( -1 )
        gSizerRegister.Add( self.m_staticTextUserSex, 0, wx.ALL, 5 )
        
        self.m_textCtrlUserSex = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 150,-1 ), 0 )
        gSizerRegister.Add( self.m_textCtrlUserSex, 0, wx.ALL, 5 )
        
        self.m_staticTextUserTel = wx.StaticText( self, wx.ID_ANY, u"user_tel :", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticTextUserTel.Wrap( -1 )
        gSizerRegister.Add( self.m_staticTextUserTel, 0, wx.ALL, 5 )
        
        self.m_textCtrlUserTel = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 150,-1 ), 0 )
        gSizerRegister.Add( self.m_textCtrlUserTel, 0, wx.ALL, 5 )
        
        self.m_staticTextUserEmail = wx.StaticText( self, wx.ID_ANY, u"user_email :", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticTextUserEmail.Wrap( -1 )
        gSizerRegister.Add( self.m_staticTextUserEmail, 0, wx.ALL, 5 )
        
        self.m_textCtrlUserEmail = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 150,-1 ), 0 )
        gSizerRegister.Add( self.m_textCtrlUserEmail, 0, wx.ALL, 5 )
        
        self.m_staticTextUserEmailPwd = wx.StaticText( self, wx.ID_ANY, u"user_email_pwd :", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticTextUserEmailPwd.Wrap( -1 )
        gSizerRegister.Add( self.m_staticTextUserEmailPwd, 0, wx.ALL, 5 )
        
        self.m_textCtrlUserEmailPwd = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 150,-1 ), wx.TE_PASSWORD )
        gSizerRegister.Add( self.m_textCtrlUserEmailPwd, 0, wx.ALL, 5 )
        
        self.m_staticTextUserSendEmail = wx.StaticText( self, wx.ID_ANY, u"user_sendemail :", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticTextUserSendEmail.Wrap( -1 )
        gSizerRegister.Add( self.m_staticTextUserSendEmail, 0, wx.ALL, 5 )
        
        self.m_textCtrlUserSendEmail = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 150,-1 ), 0 )
        gSizerRegister.Add( self.m_textCtrlUserSendEmail, 0, wx.ALL, 5 )
        
        self.m_panelNone = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        self.m_panelNone.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_APPWORKSPACE ) )
        
        gSizerRegister.Add( self.m_panelNone, 1, wx.EXPAND |wx.ALL, 5 )
        
        m_sdbSizerRegister = wx.StdDialogButtonSizer()
        self.m_sdbSizerRegisterOK = wx.Button( self, wx.ID_OK )
        m_sdbSizerRegister.AddButton( self.m_sdbSizerRegisterOK )
        self.m_sdbSizerRegisterCancel = wx.Button( self, wx.ID_CANCEL )
        m_sdbSizerRegister.AddButton( self.m_sdbSizerRegisterCancel )
        m_sdbSizerRegister.Realize();
        gSizerRegister.Add( m_sdbSizerRegister, 1, wx.EXPAND, 5 )
        
        self.SetSizer( gSizerRegister )
        self.Layout()
        
        self.Centre( wx.BOTH )
        
        # Connect Events
        self.m_sdbSizerRegisterOK.Bind( wx.EVT_BUTTON, self.OnOK )
    
    def __del__( self ):
        pass
    
    
    # Virtual event handlers, overide them in your derived class
    def OnOK( self, event ):
        user_name = self.m_textCtrlUserName.GetValue()
        user_password = self.m_textCtrlUserPassword.GetValue()
        user_pwdrap = self.m_textCtrlPwdRap.GetValue()
        user_sex = self.m_textCtrlUserSex.GetValue()
        user_tel = self.m_textCtrlUserTel.GetValue()
        user_email = self.m_textCtrlUserEmail.GetValue()
        user_email_pwd = self.m_textCtrlUserEmailPwd.GetValue()
        user_sendemail = self.m_textCtrlUserSendEmail.GetValue()
        
        if user_password != user_pwdrap:
            dlg = wx.MessageDialog(self, 'The Input of Your password is Different !', 'WARNING !', wx.OK | wx.ICON_INFORMATION)
            dlg.ShowModal()
            dlg.Destroy()
        else:
            userObj = Model.userModel.user()
            userObj.setuser_name(user_name)
            userObj.setuser_password(user_password)
            userObj.setuser_sex(user_sex)
            userObj.setuser_tel(user_tel)
            userObj.setuser_email(user_email)
            userObj.setuser_email_pwd(user_email_pwd)
            userObj.setuser_sendemail(user_sendemail)
            
            dbConnRegister = DBBean.SQLiteInit.sqlInit()
            dbConnRegister.createTable()
            dbConnRegister.insRegister(userObj)
            
            dlg = wx.MessageDialog(self, 'Successful Register !', 'WARNING !', wx.OK | wx.ICON_INFORMATION)
            dlg.ShowModal()
            dlg.Destroy()
            
            self.Close(True)
            self.Destroy()
            wxRun.main()


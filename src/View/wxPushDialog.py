# -*- coding: UTF-8 -*-

'''
Created on 2013-5-20

@author: Administrator
'''

###########################################################################
## Python code generated with wxFormBuilder (version Sep  8 2010)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import Controller.pushSend
import Model.userModel

###########################################################################
## Class wxPushDialog
###########################################################################

class wxPushDialog ( wx.Dialog ):
    
    def __init__( self, parent, userObj, bookSendObj ):
        self.user = userObj
        self.bookSendObj = bookSendObj
        
        wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"PUSH YOUR BOOK TO YOUR EMAIL", pos = wx.DefaultPosition, size = wx.Size( 450,180 ), style = wx.DEFAULT_DIALOG_STYLE )
        
        self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
        
        sbSizerPush = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Push to Kindle" ), wx.VERTICAL )
        
        self.m_staticTextPushURL = wx.StaticText( self, wx.ID_ANY, u"are you sure to push book to the follow URL ?\n", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticTextPushURL.Wrap( -1 )
        sbSizerPush.Add( self.m_staticTextPushURL, 0, wx.ALL, 5 )
        
        self.m_textCtrlPushURL = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 400,-1 ), 0 )
        self.m_textCtrlPushURL.SetValue(self.user.getuser_sendemail())
        sbSizerPush.Add( self.m_textCtrlPushURL, 0, wx.ALL, 5 )
        
        m_sdbSizerPush = wx.StdDialogButtonSizer()
        self.m_sdbSizerPushOK = wx.Button( self, wx.ID_OK )
        m_sdbSizerPush.AddButton( self.m_sdbSizerPushOK )
        self.m_sdbSizerPushCancel = wx.Button( self, wx.ID_CANCEL )
        m_sdbSizerPush.AddButton( self.m_sdbSizerPushCancel )
        m_sdbSizerPush.Realize();
        sbSizerPush.Add( m_sdbSizerPush, 1, wx.EXPAND, 5 )
        
        self.SetSizer( sbSizerPush )
        self.Layout()
        
        self.Centre( wx.BOTH )
        
        # Connect Events
        self.m_sdbSizerPushOK.Bind( wx.EVT_BUTTON, self.OnPush )
    
    def __del__( self ):
        pass

    # Virtual event handlers, overide them in your derived class
    def OnPush( self, event ):
        dlg1 = wx.MessageDialog(self, 'Please wait a minute ...', 'NEWS !', wx.OK | wx.ICON_INFORMATION)
        dlg1.ShowModal()
        dlg1.Destroy()
        self.Close(True)
        
        user_email = self.user.getuser_email()
        user_email_pwd = self.user.getuser_email_pwd()
        user_sendemail = self.m_textCtrlPushURL.GetValue()
              
        sSubject = u'Kindle Push'
        sContent = u'Kindle Push'
        lsPlugin = [{'subject' : self.bookSendObj.getbook_name() + ".txt", 'content' : self.bookSendObj.getbook_file()}]
        lsTo = [user_sendemail]
        lsCc = []
        
        if user_email.find('gmail') != -1:
            gmailObj = Controller.pushSend.GMail(user_email, user_email_pwd)
            gmailObj.send(sSubject, sContent, lsTo, lsCc, lsPlugin)
        elif user_email.find('163') != -1:
            com163Obj = Controller.pushSend.Com163Mail(user_email, user_email_pwd)
            com163Obj.send(sSubject, sContent, lsTo, lsCc, lsPlugin)
        elif user_email.find('sina') != -1:
            sinaObj = Controller.pushSend.SinaMail(user_email, user_email_pwd)
            sinaObj.send(sSubject, sContent, lsTo, lsCc, lsPlugin)
        elif user_email.find('qq') != -1:
            qqObj = Controller.pushSend.QQMail(user_email, user_email_pwd)
            qqObj.send(sSubject, sContent, lsTo, lsCc, lsPlugin)
            
        dlg2 = wx.MessageDialog(self, 'The Book Has Been Sended !', 'NEWS !', wx.OK | wx.ICON_INFORMATION)
        dlg2.ShowModal()
        dlg2.Destroy()

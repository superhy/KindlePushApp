# -*- coding: utf-8 -*- 

###########################################################################
# # Python code generated with wxFormBuilder (version Sep  8 2010)
# # http://www.wxformbuilder.org/
# #
# # PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import Controller.ayasURL
import Controller.beautifulSoupGetNovel
import DBBean.SQLiteInit
import Model.book_sendModel
import Model.userModel
import os
import re
import wx
import wx.grid
import wxPushDialog
import wxRun

###########################################################################
# # Class MainDialog
###########################################################################

class wxMainFrame (wx.Frame):
    
    def __init__(self, parent, userObj):
        self.user = userObj
        self.flagFileCreated = False
        self.locFileName = ""
        self.bookName = ""
        self.bookSendObj = Model.book_sendModel.book_send()
        
        wx.Frame.__init__ (self, parent, id=wx.ID_ANY, title=u"KindlePush", pos=wx.DefaultPosition, size=wx.Size(800, 550), style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)
        
        self.SetSizeHintsSz(wx.DefaultSize, wx.DefaultSize)
        
        self.m_menubarFile = wx.MenuBar(0)
        self.m_menuFile = wx.Menu()
        self.m_menuItemLogOut = wx.MenuItem(self.m_menuFile, wx.ID_ANY, u"logout", wx.EmptyString, wx.ITEM_NORMAL)
        self.m_menuFile.AppendItem(self.m_menuItemLogOut)
        
        self.m_menuItemPush = wx.MenuItem(self.m_menuFile, wx.ID_ANY, u"push", wx.EmptyString, wx.ITEM_NORMAL)
        self.m_menuFile.AppendItem(self.m_menuItemPush)
        
        self.m_menuItemAccount = wx.MenuItem(self.m_menuFile, wx.ID_ANY, u"account", wx.EmptyString, wx.ITEM_NORMAL)
        self.m_menuFile.AppendItem(self.m_menuItemAccount)
        
        self.m_menuItemHistory = wx.MenuItem(self.m_menuFile, wx.ID_ANY, u"history", wx.EmptyString, wx.ITEM_NORMAL)
        self.m_menuFile.AppendItem(self.m_menuItemHistory)
        
        self.m_menuItemExit = wx.MenuItem(self.m_menuFile, wx.ID_ANY, u"exit", wx.EmptyString, wx.ITEM_NORMAL)
        self.m_menuFile.AppendItem(self.m_menuItemExit)
        
        self.m_menubarFile.Append(self.m_menuFile, u"file") 
        
        self.m_menuEdit = wx.Menu()
        self.m_menubarFile.Append(self.m_menuEdit, u"edit") 
        
        self.m_menuView = wx.Menu()
        self.m_menubarFile.Append(self.m_menuView, u"view") 
        
        self.m_menuTools = wx.Menu()
        self.m_menuItemSetting = wx.MenuItem(self.m_menuTools, wx.ID_ANY, u"setting", wx.EmptyString, wx.ITEM_NORMAL)
        self.m_menuTools.AppendItem(self.m_menuItemSetting)
        
        self.m_menubarFile.Append(self.m_menuTools, u"tools") 
        
        self.m_menuHelp = wx.Menu()
        self.m_menuItemAbout = wx.MenuItem(self.m_menuHelp, wx.ID_ANY, u"about...", wx.EmptyString, wx.ITEM_NORMAL)
        self.m_menuHelp.AppendItem(self.m_menuItemAbout)
        
        self.m_menubarFile.Append(self.m_menuHelp, u"help") 
        
        self.SetMenuBar(self.m_menubarFile)
        
        bSizerMain = wx.BoxSizer(wx.VERTICAL)
        
        self.m_staticTextUserWel = wx.StaticText(self, wx.ID_ANY, "Welcome ! " + str(self.user.getuser_name()) + " This is KindlePush...", wx.DefaultPosition, wx.Size(500, -1), 0)
        self.m_staticTextUserWel.Wrap(-1)
        self.m_staticTextUserWel.SetFont(wx.Font(10, 70, 93, 92, False, wx.EmptyString))
        self.m_staticTextUserWel.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_HIGHLIGHTTEXT))
        self.m_staticTextUserWel.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_APPWORKSPACE))
        
        bSizerMain.Add(self.m_staticTextUserWel, 0, wx.ALL, 5)
        
        self.m_staticTextSeach = wx.StaticText(self, wx.ID_ANY, u"Enter URL or BookID:", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticTextSeach.Wrap(-1)
        bSizerMain.Add(self.m_staticTextSeach, 0, wx.ALL, 5)
        
        self.m_panelSearchPart = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        self.m_panelSearchPart.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_APPWORKSPACE))
        
        bSizerSearch = wx.BoxSizer(wx.VERTICAL)
        
        self.m_panelSearch = wx.Panel(self.m_panelSearchPart, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        gSizerSearch = wx.GridSizer(2, 2, 0, 0)
        
        self.m_searchCtrlSearch = wx.SearchCtrl(self.m_panelSearch, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(650, -1), 0)
        self.m_searchCtrlSearch.ShowSearchButton(True)
        self.m_searchCtrlSearch.ShowCancelButton(False)
        gSizerSearch.Add(self.m_searchCtrlSearch, 0, wx.ALL, 5)
        
        self.m_buttonSubmit = wx.Button(self.m_panelSearch, wx.ID_ANY, u"submit", wx.DefaultPosition, wx.DefaultSize, 0)
        gSizerSearch.Add(self.m_buttonSubmit, 0, wx.ALL | wx.ALIGN_RIGHT, 5)
        
        self.m_panelSearch.SetSizer(gSizerSearch)
        self.m_panelSearch.Layout()
        gSizerSearch.Fit(self.m_panelSearch)
        bSizerSearch.Add(self.m_panelSearch, 1, wx.EXPAND | wx.ALL, 5)
        
        self.m_panelGauge = wx.Panel(self.m_panelSearchPart, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        bSizerGauge = wx.BoxSizer(wx.VERTICAL)
        
        self.m_gaugeSearchGauge = wx.Gauge(self.m_panelGauge, wx.ID_ANY, 100, wx.DefaultPosition, wx.Size(750, 25), wx.GA_PROGRESSBAR)
        bSizerGauge.Add(self.m_gaugeSearchGauge, 0, wx.ALL, 5)
        
        self.m_panelGauge.SetSizer(bSizerGauge)
        self.m_panelGauge.Layout()
        bSizerGauge.Fit(self.m_panelGauge)
        bSizerSearch.Add(self.m_panelGauge, 1, wx.EXPAND | wx.ALL, 5)
        
        self.m_panelSearchPart.SetSizer(bSizerSearch)
        self.m_panelSearchPart.Layout()
        bSizerSearch.Fit(self.m_panelSearchPart)
        bSizerMain.Add(self.m_panelSearchPart, 1, wx.EXPAND | wx.ALL, 5)
        
        self.m_panelProcessPart = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        self.m_panelProcessPart.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_APPWORKSPACE))
        
        bSizerProcess = wx.BoxSizer(wx.VERTICAL)
        
        self.m_staticTextFile = wx.StaticText(self.m_panelProcessPart, wx.ID_ANY, u"None", wx.Point(-1, -1), wx.Size(750, -1), 0)
        self.m_staticTextFile.Wrap(-1)
        self.m_staticTextFile.SetFont(wx.Font(15, 70, 90, 92, False, wx.EmptyString))
        
        bSizerProcess.Add(self.m_staticTextFile, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)
        
        self.m_panelProcessPart.SetSizer(bSizerProcess)
        self.m_panelProcessPart.Layout()
        bSizerProcess.Fit(self.m_panelProcessPart)
        bSizerMain.Add(self.m_panelProcessPart, 1, wx.EXPAND | wx.ALL, 5)
        
        self.m_panelPushPart = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        self.m_panelPushPart.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_APPWORKSPACE))
        
        bSizerPush = wx.BoxSizer(wx.VERTICAL)
        
        m_sdbSizerPush = wx.StdDialogButtonSizer()
        self.m_sdbSizerPushSave = wx.Button(self.m_panelPushPart, wx.ID_SAVE)
        m_sdbSizerPush.AddButton(self.m_sdbSizerPushSave)
        self.m_sdbSizerPushApply = wx.Button(self.m_panelPushPart, wx.ID_APPLY)
        m_sdbSizerPush.AddButton(self.m_sdbSizerPushApply)
        m_sdbSizerPush.Realize();
        bSizerPush.Add(m_sdbSizerPush, 1, wx.EXPAND, 5)
        
        self.m_panelNone1 = wx.Panel(self.m_panelPushPart, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        bSizerPush.Add(self.m_panelNone1, 1, wx.EXPAND | wx.ALL, 5)
        
        self.m_panelNone2 = wx.Panel(self.m_panelPushPart, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        bSizerPush.Add(self.m_panelNone2, 1, wx.EXPAND | wx.ALL, 5)
        
        self.m_panelPushPart.SetSizer(bSizerPush)
        self.m_panelPushPart.Layout()
        bSizerPush.Fit(self.m_panelPushPart)
        bSizerMain.Add(self.m_panelPushPart, 1, wx.EXPAND | wx.ALL, 5)
        
        self.SetSizer(bSizerMain)
        self.Layout()
        self.m_statusBarAuthor = self.CreateStatusBar(1, wx.ST_SIZEGRIP, wx.ID_ANY)
        self.m_statusBarAuthor.SetFont(wx.Font(wx.NORMAL_FONT.GetPointSize(), 70, 93, 90, False, wx.EmptyString))
        self.SetStatusText("Powered By superhy?2013 superhy199148@gmail.com")
        
        self.Centre(wx.BOTH)
        
        # Connect Events
        self.Bind(wx.EVT_MENU, self.OnLogOut, id=self.m_menuItemLogOut.GetId())
        self.Bind(wx.EVT_MENU, self.OnExit, id=self.m_menuItemExit.GetId())
        self.Bind(wx.EVT_MENU, self.OnApply, id=self.m_menuItemPush.GetId())
        self.m_searchCtrlSearch.Bind(wx.EVT_SEARCHCTRL_SEARCH_BTN, self.OnSubmit)
        self.m_buttonSubmit.Bind(wx.EVT_BUTTON, self.OnSubmit)
        self.m_sdbSizerPushApply.Bind(wx.EVT_BUTTON, self.OnApply)
        self.m_sdbSizerPushSave.Bind(wx.EVT_BUTTON, self.OnSave)
        
    def __del__(self):
            pass
    
    # Virtual event handlers, overide them in your derived class    
        
    def OnSubmit(self, event):
        self.str_jobURL = str(self.m_searchCtrlSearch.Value)
        ayasURLObj = Controller.ayasURL.ayasURL()
        ayasURLObj.setURL(self.str_jobURL)
        ayasURLObj.grabHref()
        
        content = ayasURLObj.content
        pat = ayasURLObj.pat
        pat2 = ayasURLObj.pat2
        endStr = ayasURLObj.endStr
        url = ayasURLObj.url
        urlNum = ayasURLObj.urlNum
        
        bsGetNovelObj = Controller.beautifulSoupGetNovel.beautifulSoupGetNovel()
        self.m_gaugeSearchGauge.SetRange(urlNum)
        count = 0
        
        for item in content:
            count = count + 1
            self.m_gaugeSearchGauge.SetValue(count)
            h = pat.search(str(item))
            
#             print item
#             print h.group(1)
            
            href = h.group(1)
            if pat2.search(href):
                ans = href
            else:
                ans = url + href
            pat3 = re.match(r'http://book.zongheng.com/chapter/', ans)
            if pat3:
                if self.flagFileCreated == False:
                    bsGetNovelObj.setURL(ans)
                    self.bookName, self.locFileName = bsGetNovelObj.getFileName()
                    myNovelFile = bsGetNovelObj.createLocalFile(self.locFileName)
                    self.flagFileCreated = True
                bsGetNovelObj.setURL(ans)
                print ans
                newStr = bsGetNovelObj.ayasHtmlCode()
                if newStr != endStr:
                    myNovelFile.write(newStr)
                else:
                    myNovelFile.write(endStr)
                    break       
        myNovelFile.close()
        
        self.m_gaugeSearchGauge.SetValue(urlNum)
        self.m_staticTextFile.SetLabel(self.locFileName)
        dlg = wx.MessageDialog(self, 'The *.txt File of Novel Has Been Created !', 'WARNING !', wx.OK | wx.ICON_INFORMATION)
        dlg.ShowModal()
        dlg.Destroy()
        
        book_name = self.bookName
        book_file = self.locFileName
        user_name = self.user.getuser_name()
        push_num = count
        total_num = urlNum
        save_flag = 1  # '1' mean need save
        self.bookSendObj.setbook_name(book_name)
        self.bookSendObj.setbook_file(book_file)
        self.bookSendObj.setuser_name(user_name)
        self.bookSendObj.setpush_num(push_num)
        self.bookSendObj.settotal_num(total_num)
        self.bookSendObj.setsave_flag(save_flag)
        
        dbConnBookSend = DBBean.SQLiteInit.sqlInit()
        dbConnBookSend.createTable()
        dbConnBookSend.insBookSend(self.bookSendObj)
        
        del(bsGetNovelObj)
        del(ayasURLObj)
        
    def OnLogOut(self, event):          
        dlg = wx.MessageDialog(None, 'Are you sure for loginout ?', 'Ask Dialog...', wx.YES_NO | wx.ICON_QUESTION)
        result = dlg.ShowModal()
        # if "YES"
        if result == wx.ID_YES:
            self.Close(True)
            self.Destroy()
            wxRun.main()
        else:
            pass
        dlg.Destroy()
        
    def OnExit(self, event):
#        event.skip()
        self.m_staticTextUserWel.Label = "byebye ! " + str(self.user.getuser_name())
        dlg = wx.MessageDialog(None, 'Exit KindlePush ?', 'Ask Dialog...', wx.YES_NO | wx.ICON_QUESTION)
        result = dlg.ShowModal()
        
        # if "YES"
        if result == wx.ID_YES:
            self.Close(True)
            self.Destroy()
        else:
            self.m_staticTextUserWel.Label = "Welcome ! " + str(self.user.getuser_name()) + " This is KindlePush..."
        dlg.Destroy()
               
    def OnApply(self, event):
        if self.flagFileCreated == False:
            dlg = wx.MessageDialog(self, 'The Novel LocalFile Have Not Created !', 'WARNING !', wx.OK | wx.ICON_INFORMATION)
            dlg.ShowModal()
            dlg.Destroy()
        else:
            appRun = wx.App()
            dialog = wxPushDialog.wxPushDialog(None, self.user, self.bookSendObj)
            dialog.Show()
            appRun.MainLoop()
    
    def OnSave(self, event):
        if self.flagFileCreated == False:
            dlg = wx.MessageDialog(self, 'The Novel LocalFile Have Not Created !', 'WARNING !', wx.OK | wx.ICON_INFORMATION)
            dlg.ShowModal()
            dlg.Destroy()
        else:
            # opens explorer at C:\ drive,just work for windows
#             f = open(self.locFileName, 'rb')
#             print f
            start_directory = r'..\..\novelFile'
            os.startfile(start_directory)
        

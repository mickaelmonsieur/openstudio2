# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Jan 25 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import wx.dataview

###########################################################################
## Class MainFrame
###########################################################################

class MainFrame ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"OpenStudio 2", pos = wx.DefaultPosition, size = wx.Size( 1126,751 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		
		bSizer1 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer3 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.playSong1 = wx.Button( self, wx.ID_ANY, u"Play", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer3.Add( self.playSong1, 0, wx.ALL, 5 )
		
		self.stopSong1 = wx.Button( self, wx.ID_ANY, u"Stop", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer3.Add( self.stopSong1, 0, wx.ALL, 5 )
		
		self.rewingSong1 = wx.Button( self, wx.ID_ANY, u"Rewind", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer3.Add( self.rewingSong1, 0, wx.ALL, 5 )
		
		self.position = wx.StaticText( self, wx.ID_ANY, u"00:00:00", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.position.Wrap( -1 )
		bSizer3.Add( self.position, 0, wx.ALL, 5 )
		
		self.countdown = wx.StaticText( self, wx.ID_ANY, u"00:00:00", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.countdown.Wrap( -1 )
		bSizer3.Add( self.countdown, 0, wx.ALL, 5 )
		
		
		bSizer1.Add( bSizer3, 1, wx.EXPAND, 5 )
		
		self.songs = wx.dataview.DataViewListCtrl( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 1000,600 ), 0 )
		bSizer1.Add( self.songs, 0, wx.ALL, 5 )
		
		
		self.SetSizer( bSizer1 )
		self.Layout()
		self.statusBar1 = self.CreateStatusBar( 1, wx.STB_SIZEGRIP, wx.ID_ANY )
		self.menu = wx.MenuBar( 0 )
		self.menuFile = wx.Menu()
		self.menuImport = wx.MenuItem( self.menuFile, wx.ID_ANY, u"Import file", wx.EmptyString, wx.ITEM_NORMAL )
		self.menuFile.Append( self.menuImport )
		
		self.menuClose = wx.MenuItem( self.menuFile, wx.ID_ANY, u"Close", wx.EmptyString, wx.ITEM_NORMAL )
		self.menuFile.Append( self.menuClose )
		
		self.menu.Append( self.menuFile, u"File" ) 
		
		self.menuView = wx.Menu()
		self.menuRefresh = wx.MenuItem( self.menuView, wx.ID_ANY, u"Refresh", wx.EmptyString, wx.ITEM_NORMAL )
		self.menuView.Append( self.menuRefresh )
		
		self.menu.Append( self.menuView, u"View" ) 
		
		self.SetMenuBar( self.menu )
		
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.playSong1.Bind( wx.EVT_BUTTON, self.play )
		self.stopSong1.Bind( wx.EVT_BUTTON, self.stop )
		self.rewingSong1.Bind( wx.EVT_BUTTON, self.rewind )
		self.Bind( wx.EVT_MENU, self.importFile, id = self.menuImport.GetId() )
		self.Bind( wx.EVT_MENU, self.close, id = self.menuClose.GetId() )
		self.Bind( wx.EVT_MENU, self.refresh, id = self.menuRefresh.GetId() )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def play( self, event ):
		event.Skip()
	
	def stop( self, event ):
		event.Skip()
	
	def rewind( self, event ):
		event.Skip()
	
	def importFile( self, event ):
		event.Skip()
	
	def close( self, event ):
		event.Skip()
	
	def refresh( self, event ):
		event.Skip()
	

###########################################################################
## Class ImportFrame
###########################################################################

class ImportFrame ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Import files", pos = wx.DefaultPosition, size = wx.Size( 300,110 ), style = wx.CAPTION|wx.CLOSE_BOX|wx.STAY_ON_TOP|wx.TAB_TRAVERSAL )
		
		self.SetSizeHints( wx.Size( 300,110 ), wx.Size( 300,110 ) )
		
		wSizer1 = wx.WrapSizer( wx.VERTICAL )
		
		bSizer5 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.fileinfo = wx.StaticText( self, wx.ID_ANY, u"Select file:", wx.Point( -1,-1 ), wx.DefaultSize, 0 )
		self.fileinfo.Wrap( -1 )
		bSizer5.Add( self.fileinfo, 0, wx.ALL, 5 )
		
		self.filePicker = wx.FilePickerCtrl( self, wx.ID_ANY, wx.EmptyString, u"Select a file", u"*.mp2;*.mp3", wx.DefaultPosition, wx.DefaultSize, wx.FLP_DEFAULT_STYLE )
		bSizer5.Add( self.filePicker, 0, wx.ALL, 5 )
		
		
		wSizer1.Add( bSizer5, 1, wx.EXPAND, 5 )
		
		bSizer4 = wx.BoxSizer( wx.HORIZONTAL )
		
		
		bSizer4.Add( ( 0, 0), 1, wx.EXPAND, 0 )
		
		self.importBtn = wx.Button( self, wx.ID_ANY, u"Import", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer4.Add( self.importBtn, 0, wx.ALL, 5 )
		
		
		wSizer1.Add( bSizer4, 1, wx.EXPAND, 5 )
		
		
		self.SetSizer( wSizer1 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.importBtn.Bind( wx.EVT_BUTTON, self.importFile )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def importFile( self, event ):
		event.Skip()
	


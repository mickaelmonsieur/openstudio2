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
		
		
		bSizer1.Add( bSizer3, 1, wx.EXPAND, 5 )
		
		self.songs = wx.dataview.DataViewListCtrl( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 1000,600 ), 0 )
		bSizer1.Add( self.songs, 0, wx.ALL, 5 )
		
		
		self.SetSizer( bSizer1 )
		self.Layout()
		self.statusBar1 = self.CreateStatusBar( 1, wx.STB_SIZEGRIP, wx.ID_ANY )
		self.menu = wx.MenuBar( 0 )
		self.menuFile = wx.Menu()
		self.menuClose = wx.MenuItem( self.menuFile, wx.ID_ANY, u"Close", wx.EmptyString, wx.ITEM_NORMAL )
		self.menuFile.Append( self.menuClose )
		
		self.menu.Append( self.menuFile, u"File" ) 
		
		self.SetMenuBar( self.menu )
		
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.playSong1.Bind( wx.EVT_BUTTON, self.play )
		self.stopSong1.Bind( wx.EVT_BUTTON, self.stop )
		self.rewingSong1.Bind( wx.EVT_BUTTON, self.rewind )
		self.Bind( wx.EVT_MENU, self.close, id = self.menuClose.GetId() )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def play( self, event ):
		event.Skip()
	
	def stop( self, event ):
		event.Skip()
	
	def rewind( self, event ):
		event.Skip()
	
	def close( self, event ):
		event.Skip()
	


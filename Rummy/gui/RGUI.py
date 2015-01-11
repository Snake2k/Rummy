# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Jul  5 2013)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx

###########################################################################
## Class RMainFrame
###########################################################################

class RMainFrame ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Rummy", pos = wx.DefaultPosition, size = wx.Size( 800,600 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.Size( 800,600 ), wx.Size( 800,600 ) )
		
		RMainBSizer = wx.BoxSizer( wx.VERTICAL )
		
		self.SetSizer( RMainBSizer )
		self.Layout()
		self.RStatusBar = self.CreateStatusBar( 1, wx.ST_SIZEGRIP, wx.ID_ANY )
		self.RMenuBar = wx.MenuBar( 0 )
		self.RFileMenu = wx.Menu()
		self.RMItemNew = wx.MenuItem( self.RFileMenu, wx.ID_ANY, u"New", wx.EmptyString, wx.ITEM_NORMAL )
		self.RFileMenu.AppendItem( self.RMItemNew )
		
		self.RMItemSave = wx.MenuItem( self.RFileMenu, wx.ID_ANY, u"Save", wx.EmptyString, wx.ITEM_NORMAL )
		self.RFileMenu.AppendItem( self.RMItemSave )
		
		self.RFileMenu.AppendSeparator()
		
		self.RMItemQuit = wx.MenuItem( self.RFileMenu, wx.ID_ANY, u"Quit", wx.EmptyString, wx.ITEM_NORMAL )
		self.RFileMenu.AppendItem( self.RMItemQuit )
		
		self.RMenuBar.Append( self.RFileMenu, u"File" ) 
		
		self.RMHelpMenu = wx.Menu()
		self.RMItemAbout = wx.MenuItem( self.RMHelpMenu, wx.ID_ANY, u"About"+ u"\t" + u"F1", wx.EmptyString, wx.ITEM_NORMAL )
		self.RMHelpMenu.AppendItem( self.RMItemAbout )
		
		self.RMenuBar.Append( self.RMHelpMenu, u"Help" ) 
		
		self.SetMenuBar( self.RMenuBar )
		
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.Bind( wx.EVT_MENU, self.close_frame, id = self.RMItemQuit.GetId() )
		self.Bind( wx.EVT_MENU, self.show_about, id = self.RMItemAbout.GetId() )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def close_frame( self, event ):
		event.Skip()
	
	def show_about( self, event ):
		event.Skip()
	

###########################################################################
## Class RGamePanel
###########################################################################

class RGamePanel ( wx.Panel ):
	
	def __init__( self, parent ):
		wx.Panel.__init__ ( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.TAB_TRAVERSAL )
		
	
	def __del__( self ):
		pass
	

###########################################################################
## Class RMainMenuPanel
###########################################################################

class RMainMenuPanel ( wx.Panel ):
	
	def __init__( self, parent ):
		wx.Panel.__init__ ( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.TAB_TRAVERSAL )
		
	
	def __del__( self ):
		pass
	


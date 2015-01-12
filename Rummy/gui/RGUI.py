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
		
		RMainFrameBSizer = wx.BoxSizer( wx.VERTICAL )
		
		self.RMainGamePanel = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.RMainGamePanel.Hide()
		
		RGMainBSizer = wx.BoxSizer( wx.VERTICAL )
		
		self.RGMainPanel = wx.Panel( self.RMainGamePanel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		RGGameBoardBSizer = wx.BoxSizer( wx.VERTICAL )
		
		RGOpponentCardBSizer = wx.BoxSizer( wx.HORIZONTAL )
		
		self.RGOpCard1 = wx.StaticBitmap( self.RGMainPanel, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, 0 )
		RGOpponentCardBSizer.Add( self.RGOpCard1, 0, wx.ALL, 5 )
		
		self.RGOpCard2 = wx.StaticBitmap( self.RGMainPanel, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, 0 )
		RGOpponentCardBSizer.Add( self.RGOpCard2, 0, wx.ALL, 5 )
		
		self.RGOpCard3 = wx.StaticBitmap( self.RGMainPanel, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, 0 )
		RGOpponentCardBSizer.Add( self.RGOpCard3, 0, wx.ALL, 5 )
		
		self.RGOpCard4 = wx.StaticBitmap( self.RGMainPanel, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, 0 )
		RGOpponentCardBSizer.Add( self.RGOpCard4, 0, wx.ALL, 5 )
		
		self.RGOpCard5 = wx.StaticBitmap( self.RGMainPanel, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, 0 )
		RGOpponentCardBSizer.Add( self.RGOpCard5, 0, wx.ALL, 5 )
		
		self.RGOpCard6 = wx.StaticBitmap( self.RGMainPanel, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, 0 )
		RGOpponentCardBSizer.Add( self.RGOpCard6, 0, wx.ALL, 5 )
		
		self.RGOpCard7 = wx.StaticBitmap( self.RGMainPanel, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, 0 )
		RGOpponentCardBSizer.Add( self.RGOpCard7, 0, wx.ALL, 5 )
		
		self.RGOpCard8 = wx.StaticBitmap( self.RGMainPanel, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, 0 )
		RGOpponentCardBSizer.Add( self.RGOpCard8, 0, wx.ALL, 5 )
		
		self.RGOpCard9 = wx.StaticBitmap( self.RGMainPanel, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, 0 )
		RGOpponentCardBSizer.Add( self.RGOpCard9, 0, wx.ALL, 5 )
		
		self.RGOpCard10 = wx.StaticBitmap( self.RGMainPanel, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, 0 )
		RGOpponentCardBSizer.Add( self.RGOpCard10, 0, wx.ALL, 5 )
		
		RGGameBoardBSizer.Add( RGOpponentCardBSizer, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		
		RGGameBoardBSizer.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		RGCardPileBsizer = wx.BoxSizer( wx.HORIZONTAL )
		
		self.RGDiscardPile = wx.StaticBitmap( self.RGMainPanel, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, 0 )
		RGCardPileBsizer.Add( self.RGDiscardPile, 0, wx.ALL, 5 )
		
		self.RGDrawCardPile = wx.StaticBitmap( self.RGMainPanel, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, 0 )
		RGCardPileBsizer.Add( self.RGDrawCardPile, 0, wx.ALL, 5 )
		
		RGGameBoardBSizer.Add( RGCardPileBsizer, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		
		RGGameBoardBSizer.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		RGPlayerCardBSizer = wx.BoxSizer( wx.HORIZONTAL )
		
		self.RGPlayerCard1 = wx.StaticBitmap( self.RGMainPanel, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, 0 )
		RGPlayerCardBSizer.Add( self.RGPlayerCard1, 0, wx.ALL, 5 )
		
		self.RGPlayerCard2 = wx.StaticBitmap( self.RGMainPanel, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, 0 )
		RGPlayerCardBSizer.Add( self.RGPlayerCard2, 0, wx.ALL, 5 )
		
		self.RGPlayerCard3 = wx.StaticBitmap( self.RGMainPanel, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, 0 )
		RGPlayerCardBSizer.Add( self.RGPlayerCard3, 0, wx.ALL, 5 )
		
		self.RGPlayerCard4 = wx.StaticBitmap( self.RGMainPanel, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, 0 )
		RGPlayerCardBSizer.Add( self.RGPlayerCard4, 0, wx.ALL, 5 )
		
		self.RGPlayerCard5 = wx.StaticBitmap( self.RGMainPanel, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, 0 )
		RGPlayerCardBSizer.Add( self.RGPlayerCard5, 0, wx.ALL, 5 )
		
		self.RGPlayerCard6 = wx.StaticBitmap( self.RGMainPanel, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, 0 )
		RGPlayerCardBSizer.Add( self.RGPlayerCard6, 0, wx.ALL, 5 )
		
		self.RGPlayerCard7 = wx.StaticBitmap( self.RGMainPanel, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, 0 )
		RGPlayerCardBSizer.Add( self.RGPlayerCard7, 0, wx.ALL, 5 )
		
		self.RGPlayerCard8 = wx.StaticBitmap( self.RGMainPanel, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, 0 )
		RGPlayerCardBSizer.Add( self.RGPlayerCard8, 0, wx.ALL, 5 )
		
		self.RGPlayerCard9 = wx.StaticBitmap( self.RGMainPanel, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, 0 )
		RGPlayerCardBSizer.Add( self.RGPlayerCard9, 0, wx.ALL, 5 )
		
		self.RGPlayerCard10 = wx.StaticBitmap( self.RGMainPanel, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, 0 )
		RGPlayerCardBSizer.Add( self.RGPlayerCard10, 0, wx.ALL, 5 )
		
		RGGameBoardBSizer.Add( RGPlayerCardBSizer, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.RGMainPanel.SetSizer( RGGameBoardBSizer )
		self.RGMainPanel.Layout()
		RGGameBoardBSizer.Fit( self.RGMainPanel )
		RGMainBSizer.Add( self.RGMainPanel, 1, wx.EXPAND, 5 )
		
		self.RMainGamePanel.SetSizer( RGMainBSizer )
		self.RMainGamePanel.Layout()
		RGMainBSizer.Fit( self.RMainGamePanel )
		RMainFrameBSizer.Add( self.RMainGamePanel, 1, wx.EXPAND, 5 )
		
		self.RMainMenuPanel = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		RMMMainBSizer = wx.BoxSizer( wx.VERTICAL )
		
		self.RMMMainPanel = wx.Panel( self.RMainMenuPanel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		RMMSelectionMenuBSIzer = wx.BoxSizer( wx.VERTICAL )
		
		
		RMMSelectionMenuBSIzer.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		RMMSelectionMenuItemsBSizer = wx.BoxSizer( wx.VERTICAL )
		
		self.RMMTitleText = wx.StaticText( self.RMMMainPanel, wx.ID_ANY, u"Rummy", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.RMMTitleText.Wrap( -1 )
		RMMSelectionMenuItemsBSizer.Add( self.RMMTitleText, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.RMMPVPButton = wx.Button( self.RMMMainPanel, wx.ID_ANY, u"Player vs Player", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.RMMPVPButton.SetToolTipString( u"Player vs Player" )
		
		RMMSelectionMenuItemsBSizer.Add( self.RMMPVPButton, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.EXPAND, 5 )
		
		self.RMMPVCButton = wx.Button( self.RMMMainPanel, wx.ID_ANY, u"Player vs Computer", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.RMMPVCButton.SetToolTipString( u"Player vs AI Opponent" )
		
		RMMSelectionMenuItemsBSizer.Add( self.RMMPVCButton, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.RMMOptionsButton = wx.Button( self.RMMMainPanel, wx.ID_ANY, u"Options", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.RMMOptionsButton.SetToolTipString( u"Edit Game Options" )
		
		RMMSelectionMenuItemsBSizer.Add( self.RMMOptionsButton, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.EXPAND, 5 )
		
		self.RMMQuitButton = wx.Button( self.RMMMainPanel, wx.ID_ANY, u"Quit", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.RMMQuitButton.SetToolTipString( u"Close The Game" )
		
		RMMSelectionMenuItemsBSizer.Add( self.RMMQuitButton, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.EXPAND, 5 )
		
		RMMSelectionMenuBSIzer.Add( RMMSelectionMenuItemsBSizer, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		
		RMMSelectionMenuBSIzer.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		self.RMMMainPanel.SetSizer( RMMSelectionMenuBSIzer )
		self.RMMMainPanel.Layout()
		RMMSelectionMenuBSIzer.Fit( self.RMMMainPanel )
		RMMMainBSizer.Add( self.RMMMainPanel, 1, wx.EXPAND, 5 )
		
		self.RMainMenuPanel.SetSizer( RMMMainBSizer )
		self.RMainMenuPanel.Layout()
		RMMMainBSizer.Fit( self.RMainMenuPanel )
		RMainFrameBSizer.Add( self.RMainMenuPanel, 1, wx.EXPAND, 5 )
		
		self.SetSizer( RMainFrameBSizer )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.Bind( wx.EVT_MENU, self.show_main_menu, id = self.RMItemNew.GetId() )
		self.Bind( wx.EVT_MENU, self.close_frame, id = self.RMItemQuit.GetId() )
		self.Bind( wx.EVT_MENU, self.show_about, id = self.RMItemAbout.GetId() )
		self.RMMPVPButton.Bind( wx.EVT_BUTTON, self.start_game )
		self.RMMPVCButton.Bind( wx.EVT_BUTTON, self.start_game )
		self.RMMOptionsButton.Bind( wx.EVT_BUTTON, self.show_options )
		self.RMMQuitButton.Bind( wx.EVT_BUTTON, self.close_frame )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def show_main_menu( self, event ):
		event.Skip()
	
	def close_frame( self, event ):
		event.Skip()
	
	def show_about( self, event ):
		event.Skip()
	
	def start_game( self, event ):
		event.Skip()
	
	
	def show_options( self, event ):
		event.Skip()
	
	


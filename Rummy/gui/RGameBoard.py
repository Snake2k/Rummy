'''
Derived Classes for RGUI
'''
import wx
import RGUI

class RGameBoard(RGUI.RMainFrame):
    '''
    Derived Class of RMainFrame which will construct the game board.
    '''
    def __init__(self, parent):
        RGUI.RMainFrame.__init__(self, parent)
    def close_frame(self, event):
        self.Close()
    def show_about(self, event):
        wx.MessageBox("Working on it Jesus F***in' Christ..." + \
                      "\nBrought to you by puddlejumper and Snake2k!.", "About",
                      wx.OK | wx.ICON_INFORMATION)
    def start_game(self, event):
        self.RMainMenuPanel.Hide()
        self.RMainGamePanel.Show()
    def show_main_menu(self, event):
        self.RMainGamePanel.Hide()
        self.RMainMenuPanel.Show()

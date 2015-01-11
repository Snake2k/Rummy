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
                      "Brought to you by puddlejumper and Snake2k!.", "About",
                      wx.OK | wx.ICON_INFORMATION)

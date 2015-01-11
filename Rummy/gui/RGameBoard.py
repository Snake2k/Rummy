'''
Derived Classes for RGUI
'''
import wx
import RGUI

# pylint: disable=R0904
class RGameBoard(RGUI.RMainFrame):
    '''
    Derived Class of RMainFrame which will construct the game board.
    '''
    def __init__(self, parent):
        RGUI.RMainFrame.__init__(self, parent)
        self.RGameBoard = RGUI.RGamePanel(self)
        self.RGameBoard.SetFocus()
        self.Centre()
        self.Show(True)

    def __close_frame(self, event):
        print "Wah"
        self.Close()
        event.Skip()
    def __show_about(self, event):
        print "Wahwah?!"
        wx.MessageBox("Working on it Jesus F***in' Christ..." + \
                      "Brought to you by puddlejumper and Snake2k!.",
                      wx.OK | wx.ICON_INFORMATION)

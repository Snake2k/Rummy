'''
Main App File
'''
import wx
from gui.RGameBoard import RGameBoard

if __name__ == "__main__":
    APP = wx.App()
    RGB = RGameBoard(None)
    RGB.Show()
    APP.MainLoop()

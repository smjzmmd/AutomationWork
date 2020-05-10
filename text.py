import win32gui
import win32con
import win32clipboard as w
from win32gui import *

IpClassName="TXGuiFoundation"
IpWindowName="个人测试"
str="我裂开来"

#设置剪贴板文本
def setText(aString):
    w.OpenClipboard()
    w.EmptyClipboard()
    w.SetClipboardData(win32con.CF_TEXT,aString)
    w.CloseClipboard()

#获得剪贴板信息
def getText():
    w.OpenClipboard()
    d=w.GetClipboardData(win32con.CF_TEXT)
    w.CloseClipboard()
    return d

win=QQwin = win32gui.FindWindow(IpClassName, IpWindowName)#找到qq窗口
setText(str)
win32gui.PostMessage(win,win32con.WM_PASTE,0,0)#黏贴
# win32gui.SendMessage(getText, 258, 22, 2080193)
# win32gui.SendMessage(getText, 770, 0, 0)


import win32gui
import win32con
import win32clipboard as w
import time
from win32gui import *

IpClassName="TXGuiFoundation"
IpWindowName="个人测试"
str="我裂开来"

#设置剪贴板文本
def setText(aString):
    w.OpenClipboard()#打开剪贴板
    w.EmptyClipboard()#清空
    w.SetClipboardText(aString)# SetClipboardData(,)会乱码，要用SetClipboardText(ste)
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
time.sleep(1)   # python 中，sleep的参数为秒
win32gui.SendMessage(win,win32con.WM_KEYDOWN,win32con.VK_RETURN,0)#发送



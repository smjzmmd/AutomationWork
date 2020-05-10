import win32gui
import win32con
import win32api
import win32clipboard as w
import time
from win32gui import *


IpClassName="TXGuiFoundation"
IpWindowName="个人测试"
str="洛汗M 0505版：\n 1、随游戏版本更新。\n"

#设置剪贴板文本
def setText(aString):
    w.OpenClipboard()#打开剪贴板
    w.EmptyClipboard()#清空
    w.SetClipboardText(aString)# SetClipboardData(,)会乱码，要用SetClipboardText(str)
    w.CloseClipboard()

#获得剪贴板信息
def getText():
    w.OpenClipboard()
    d=w.GetClipboardData(win32con.CF_TEXT)
    w.CloseClipboard()
    return d

def sendStr(qqw):
    #设置剪贴板
    setText(str)
    #黏贴剪贴板
    boo=win32gui.SendMessage(qqw, win32con.WM_PASTE, 0, 0)  # 黏贴
    time.sleep(0.5)

    #@全体成员
    win32gui.SendMessage(qqw,win32con.WM_KEYDOWN,win32con.VK_SHIFT,0)
    win32gui.SendMessage(qqw, win32con.WM_CHAR,64, 0)
    # win32gui.SendMessage(win, win32con.WM_KEYUP, win32con.VK_SHIFT, 0)
    time.sleep(0.5)
    win32gui.SendMessage(qqw, win32con.WM_KEYDOWN,win32con.VK_RETURN, 0)
    time.sleep(0.5)  # python 中，sleep的参数为秒

    win32gui.SendMessage(qqw, win32con.WM_KEYDOWN, win32con.VK_RETURN, 0)  # 发送
    print("消息发送完成！\n开始发送公告！")



'''star'''

qqw=QQwin = win32gui.FindWindow(IpClassName, IpWindowName)#找到qq窗口

if qqw!=0:
    print("找到窗口,开始！")
    sendStr(qqw)

    # win32gui.SendMessage(qqw,win32con.WM_MOUSEACTIVATE,)

else:
    print("未找到窗口")




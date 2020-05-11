import win32gui
import win32con
import win32api
import win32clipboard as w
import time


#设置剪贴板文本
def setText(str):
    w.OpenClipboard()#打开剪贴板
    w.EmptyClipboard()#清空
    w.SetClipboardText(str)# SetClipboardData(,)会乱码，要用SetClipboardText(str)
    w.CloseClipboard()

#获得剪贴板信息
def getText():
    w.OpenClipboard()
    d=w.GetClipboardData(win32con.CF_TEXT)
    w.CloseClipboard()
    return d

#回车
def key_enter(handle):
    time.sleep(0.5)
    win32gui.SendMessage(handle, win32con.WM_KEYDOWN, win32con.VK_RETURN, 0)  # 发送
    win32gui.SendMessage(handle, win32con.WM_KEYUP, win32con.VK_RETURN, 0)

#窗口点击
def mouse_click(handle,winx,winy):
    time.sleep(0.5)
    long_position = win32api.MAKELONG(winx, winy)  # 将 x,y 坐标进行转化
    win32api.SendMessage(handle, win32con.WM_LBUTTONDOWN, win32con.MK_LBUTTON, long_position)
    win32api.SendMessage(handle, win32con.WM_LBUTTONUP, win32con.MK_LBUTTON, long_position)

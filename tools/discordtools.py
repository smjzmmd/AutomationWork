import win32gui,win32con,win32api
import time

import tools.reawin32 as rea

IpClassName="Chrome_WidgetWin_1"
IpWindowName="Chrome Legacy Window"
s_IpClassName="Chrome_RenderWidgetHostHWND"

#
def discord_send(version_name,MEGA_path):

    print("开始发布discord下载公告。。。")

    discord=win32gui.FindWindow(IpClassName,None)
    s_discord=win32gui.FindWindowEx(discord,None,s_IpClassName,None)

    print("找到窗口--父：{}，子：{}".format(discord,s_discord))

    win32gui.SetForegroundWindow(s_discord)  # 获得焦点
    rea.setText("{0}\n{1}".format(version_name, MEGA_path))

    time.sleep(0.5)
    # win32gui.SendMessage(discord,win32con.WM_PASTE,0,0)
    win32api.keybd_event(0x11, 0, 0, 0)
    win32api.keybd_event(0x56, 0, 0, 0)
    win32api.keybd_event(0x56, 0, win32con.KEYEVENTF_KEYUP, 0)
    win32api.keybd_event(0x11, 0, win32con.KEYEVENTF_KEYUP, 0)
    time.sleep(0.5)
    win32api.keybd_event(0x0D, 0, 0, 0)
    win32api.keybd_event(0x0D, 0, win32con.KEYEVENTF_KEYUP, 0)

    print("discord发布完成！")
    time.sleep(3)
import win32gui,win32con,win32api
import time

import tools.reawin32 as rea

IpClassName="Qt5QWindowIcon"
IpWindowName="LINE"

def line_send(version_name,file_path):
    print("开始line发布版本！！！！！！！！！！")
    time.sleep(5)
    line=win32gui.FindWindow(IpClassName,IpWindowName)

    left, top, right, bottom=win32gui.GetWindowRect(line)
    win32gui.SetForegroundWindow(line)
    win32gui.SetWindowPos(line, None, left, top, 880, 600, win32con.SWP_SHOWWINDOW)

    win32api.SetCursorPos([left+390, top+580])  # 为鼠标焦点设定一个位置
    time.sleep(1)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)

    time.sleep(3)
    rea.send_file(file_path,"打开")
    time.sleep(1)

    rea.setText(version_name)
    time.sleep(1)

    win32api.keybd_event(0x11, 0, 0, 0)
    win32api.keybd_event(0x56, 0, 0, 0)
    win32api.keybd_event(0x56, 0, win32con.KEYEVENTF_KEYUP, 0)
    win32api.keybd_event(0x11, 0, win32con.KEYEVENTF_KEYUP, 0)
    time.sleep(0.5)
    win32api.keybd_event(0x0D, 0, 0, 0)
    win32api.keybd_event(0x0D, 0, win32con.KEYEVENTF_KEYUP, 0)

    print("Line发布完成！")
    time.sleep(3)


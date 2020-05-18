import win32gui
import win32con
import win32api
import time

import tools.reawin32 as rea

IpClassName="TXGuiFoundation"

#QQ发消息
def qqwin_send(handle,str):
    print("开始发送消息。。。")
    #设置剪贴板
    rea.setText(str)
    rea.mouse_click(handle,150,600)

    #黏贴剪贴板
    time.sleep(0.5)
    win32gui.SendMessage(handle, win32con.WM_PASTE, 0, 0)  # 黏贴

    #@全体成员
    time.sleep(0.5)
    win32gui.SendMessage(handle,win32con.WM_KEYDOWN,win32con.VK_SHIFT,0)# 左 shift
    win32gui.SendMessage(handle, win32con.WM_CHAR,64, 0)# @
    win32gui.SendMessage(handle, win32con.WM_KEYUP, win32con.VK_SHIFT, 0)
    rea.key_enter(handle)

    time.sleep(0.5)
    rea.key_enter(handle)
    print("消息发送完成！")

#发布公告
def qq_announcement(handle,str):
    print("开始发布公告。。。")
    # 点击公告
    rea.mouse_click(handle,96,80)
    time.sleep(2.5)

    # 点击发布公告按钮
    rea.mouse_click(handle, 666, 117)

    time.sleep(0.5)
    rea.setText(str)
    time.sleep(0.5)
    rea.mouse_click(handle, 340, 370)# 点击编辑框
    # ctrl+v
    time.sleep(0.5)
    win32api.keybd_event(0x11,0,0,0)
    win32api.keybd_event(0x56,0,0,0)
    win32api.keybd_event(0x56, 0, win32con.KEYEVENTF_KEYUP, 0)
    win32api.keybd_event(0x11, 0, win32con.KEYEVENTF_KEYUP, 0)

    time.sleep(0.5)
    rea.mouse_click(handle, 620, 500) # 点击发布
    print("公告发布完成！")


def start_sending(qq_text,file_path,qq_q_name):
    print("开始QQ发布版本！！！！！！！！！！！！")
    time.sleep(5)
    qqw = win32gui.FindWindow(IpClassName, qq_q_name)  # 找到qq窗口

    if qqw != 0:

        win32gui.SetForegroundWindow(qqw)  # 获得焦点
        left, top, right, bottom = win32gui.GetWindowRect(qqw)
        win32gui.SetWindowPos(qqw, None, left, top, 790, 650, win32con.SWP_SHOWWINDOW)  # 调整窗口 坐标，大小

        qqwin_send(qqw, qq_text)

        time.sleep(1)
        rea.mouse_click(qqw, 124, 540)
        rea.send_file(file_path, "打开")

        time.sleep(1)
        qq_announcement(qqw, qq_text)
        time.sleep(3)
        print("QQ发布完成")
    else:
        print("未找到窗口")

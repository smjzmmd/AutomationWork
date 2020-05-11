import win32gui

import tools.sendqq as qqsend

IpClassName="TXGuiFoundation"
IpWindowName="个人测试"
str="洛汗M 0505版：\n 1、随游戏版本更新。\n"


'''star'''
qqsend.start_sending(IpClassName,IpWindowName,str)




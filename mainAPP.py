from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time

import tools.qqtools as qqsend
import tools.discordtools as dis
import tools.linetools as lin
import webs.send_bbs as bbs
import webs.send_apk as apk
import webs.send_fb as fb

'''---------------------------------------*****修改这里******-------------------------------------------------------'''
# 版本号格式  ：  时间 + 版本号
tim=time.strftime("%m-%d", time.localtime())+"-2"
# 新增内容
at='''1、测试
2、測試'''
# FB视屏地址
fideo_file='F:\OneDrive\洛汗相關\裝備合成.mp4'
# 本地新版神手地址
file_path="F:\zzz\\Desktop\\aa.txt"
#QQ群名
qq_q_name="个人测试"
'''------------------------------------修改下载地址----------------------------------------------------------'''
url_01="https://mega.nz/file/AVokBQKR#JzXtf52XtRHcWl7hoFMa9A0H3NFO3y-UODn_EdEBTZU"
url_02="https://1drv.ms/u/s!ArkEyCZsfZaLiWEDlqT8JsFPgXdP"
url_03="https://ww.lanzous.com/icabr4j"
'''----------------------------------------------------------------------------------------------'''

#浏览器参数
chrome_port=9222
chrome_utomationProfile="F:\selenum\AutomationProfile"
cmd_open='chrome.exe --remote-debugging-port={} --user-data-dir="{}"'.format(chrome_port,chrome_utomationProfile)

#目标网址
bbs_url="https://bbs.gdbsu.com/threads/m05-05.64/"
apk_url="https://apk.tw/thread-936636-1-1.html"
fb_url='https://www.facebook.com/gdbsu/publishing_tools/?section=VIDEOS&sort[0]=created_time_descending'

# 下載地址
url_title_01="MEAG"
url_title_02="OneDrive"
url_title_03="藍奏雲"
url_list=[[url_title_01,url_01],[url_title_02,url_02],[url_title_03,url_03]]

#標題
bbs_title='洛汗M神手輔助外掛'+tim+'收費版下載（可免費試用）'
apk_title='洛汗M外掛-洛汗M神手'+tim+'版收費版（可免費試用）'
fb_title='洛汗M神手'
# APK BBS 更新文本
add_text='''

'''+tim+'''版:
'''+at+'''
'''

fb_text='''『洛汗M免費外掛-洛汗M神手'''+tim+'''版』「記憶體運行外掛高效易上手」
※'''+tim+'''版：
'''+at+'''

『點擊下方進入下載』
https://bbs.gdbsu.com/threads/m-12-02.64/
'''

qq_text='洛汗M神手'+tim+'版:\n'+at+'\n'


if __name__=="__main__":
    for x in (5,4,3,2,1,0):
        print(x)
        time.sleep(1)
    print("开始！！！")
    qqsend.start_sending(qq_text,file_path,qq_q_name)
    dis.discord_send(qq_text,url_01)
    lin.line_send(qq_text,file_path)

    chrome_options = Options()
    chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
    driver = webdriver.Chrome(options=chrome_options)

    bbs.bbsStart(driver,bbs_url,bbs_title,url_list,add_text)
    apk.apkStart(driver,apk_url,apk_title,url_list,add_text)
    fb.fbStart(driver,fb_url,fideo_file,fb_title,fb_text)



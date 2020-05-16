from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys

import time
import os

import webs.send_bbs as bbs
import webs.send_apk as apk

chrome_port=9222
chrome_utomationProfile="F:\selenum\AutomationProfile"
cmd_open='chrome.exe --remote-debugging-port={} --user-data-dir="{}"'.format(chrome_port,chrome_utomationProfile)

bbs_url="https://bbs.gdbsu.com/threads/m05-05.64/"
apk_url="https://apk.tw/thread-936636-1-1.html"

url_title_01="MEAG"
url_title_02="OneDrive"
url_title_03="藍奏雲"
url_01="https://mega.nz/file/AVokBQKR#JzXtf52XtRHcWl7hoFMa9A0H3NFO3y-UODn_EdEBTZU"
url_02="https://1drv.ms/u/s!ArkEyCZsfZaLiWEDlqT8JsFPgXdP"
url_03="https://ww.lanzous.com/icabr4j"
url_list=[[url_title_01,url_01],[url_title_02,url_02],[url_title_03,url_03]]

# title_text="洛汗M神手輔助外掛{}收費版下載（可免費試用）"
add_text="\n\n{}版:\n1、測試".format(time.strftime("%m-%d", time.localtime()))

if __name__=="__main__":
    #打開瀏覽器
    # os.system(cmd_open)

    chrome_options = Options()
    chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
    # chrome_driver = "F:\Python3\Scripts\chromedriver.exe"  # 如果将chrome驱动放到Python目录，这句可以不要
    driver = webdriver.Chrome(options=chrome_options)

    # bbs.bbsStart(driver,bbs_url,url_list,add_text)
    # apk.apkStart(driver,apk_url,url_list,add_text)



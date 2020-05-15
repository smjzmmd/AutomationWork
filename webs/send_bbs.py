from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
import time



chrome_options = Options()
chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
chrome_driver = "F:\Python3\Scripts\chromedriver.exe"  # 如果将chrome驱动放到Python目录，这句可以不要
driver = webdriver.Chrome(chrome_driver,options=chrome_options)


driver.get("https://bbs.gdbsu.com/threads/m05-05.64/")
#
time.sleep(3)

# # 点击 编辑
driver.find_element_by_xpath("//a[@href='/posts/203/edit']").click()

# 修改標題日期
time.sleep(3)
bbs_title=driver.find_element_by_xpath('//input[@name="title"]')
bbs_title.clear()
bbs_title.send_keys("洛汗M神手輔助外掛{}收費版下載（可免費試用）".format(time.strftime("%m-%d", time.localtime())))

for x in range(1,4):
    time.sleep(1)
    driver.find_element_by_xpath('//div[@dir="ltr"]/p[3]/a[{}]'.format(x)).click()
    time.sleep(1)
    driver.find_element_by_xpath('//div[@class="fr-toolbar fr-ltr fr-desktop fr-top fr-basic"]/button[9]').click()
    time.sleep(1)
    driver.execute_script('document.getElementById("fr-link-insert-layer-url-2").value="{}"'.format(x));
    time.sleep(1)
    driver.find_element_by_xpath('//button[text()="更新"]').click()

# 追加更新文本
add_text=driver.find_element_by_xpath("//p[text()='洛汗M神手更新內容：']").send_keys("\n\n05-15版:\n1、測試")




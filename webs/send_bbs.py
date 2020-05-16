import time
from selenium.webdriver.common.keys import Keys

def bbsStart(driver,bbs_url,url_list,add_text):
    time.sleep(3)
    newwindow = 'window.open("{}")'.format(bbs_url)
    driver.execute_script(newwindow)
    time.sleep(3)

    # # 点击 编辑
    driver.find_element_by_xpath("//a[@href='/posts/203/edit']").click()

    # 修改標題日期
    time.sleep(3)
    bbs_title = driver.find_element_by_xpath('//input[@name="title"]')
    bbs_title.clear()
    time.sleep(0.5)
    bbs_title.send_keys("洛汗M神手輔助外掛{}收費版下載（可免費試用）".format(time.strftime("%m-%d", time.localtime())))

    number=1
    for x in url_list:
        time.sleep(1)
        driver.find_element_by_xpath('//div[@dir="ltr"]/p[3]/a[{}]'.format(number)).click()
        time.sleep(1)
        driver.find_element_by_xpath('//div[@class="fr-toolbar fr-ltr fr-desktop fr-top fr-basic"]/button[9]').click()
        time.sleep(1)
        driver.execute_script('document.getElementById("fr-link-insert-layer-url-2").value="{}"'.format(x[1]));
        time.sleep(1)
        driver.find_element_by_xpath('//button[text()="更新"]').click()
        number=number+1

    # 追加更新文本
    add_text = driver.find_element_by_xpath("//p[text()='洛汗M神手更新內容：']").send_keys(add_text)




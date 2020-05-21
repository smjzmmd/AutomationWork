import time

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys

def apkStart(driver,apk_url,apk_title,url_list,add_text):
    print("更新APK！！！！！！！！！")
    time.sleep(5)
    newwindow = 'window.open("{}")'.format(apk_url)
    driver.execute_script(newwindow)
    driver.switch_to_window(driver.window_handles[2])
    time.sleep(3)

    # # 点击 编辑
    while True:
        try:
            print("点击编辑。")
            driver.find_element_by_xpath('//a[@class="editp"]').click()
            break
        except NoSuchElementException:
            print("点击编辑：失败！5秒后重新点击")
            time.sleep(6)


    # 修改標題日期
    time.sleep(3)
    bbs_title = driver.find_element_by_xpath('//input[@name="subject"]')
    bbs_title.clear()
    time.sleep(0.5)
    bbs_title.send_keys(apk_title)

    # font的文本
    driver.switch_to.frame("e_iframe")
    apk_text = driver.find_element_by_xpath('//font[3]')
    apk_text.click()
    apk_text.clear()
    driver.switch_to.default_content()

    # 添加下載地址
    time.sleep(2)
    for x in url_list:
        driver.find_element_by_xpath('//a[@id="e_url"]').click()
        driver.find_element_by_xpath('//input[@id="e_url_param_1"]').send_keys(x[1])
        driver.find_element_by_xpath('//input[@id="e_url_param_2"]').send_keys(x[0])
        driver.find_element_by_xpath('//button[@id="e_url_submit"]').click()

    # 選中一行
    driver.switch_to.frame("e_iframe")
    lz = driver.find_element_by_xpath('//a[@href="{}"]'.format(url_list[len(url_list)-1][1]))
    lz.click()
    lz.send_keys(Keys.DOWN)
    lz.send_keys(Keys.SHIFT, '\ue013')
    driver.switch_to.default_content()
    # 調整字體 5
    driver.find_element_by_xpath('//span[@id="e_size"]').click()
    time.sleep(0.5)
    driver.find_element_by_xpath('//div[@id="e_fontsize_menu"]/ul[@unselectable="on"]/li[5]').click()

    # 追加更新文本
    driver.switch_to.frame('e_iframe')
    driver.find_element_by_xpath("//font[text()='洛汗M神手更新內容:']").send_keys(add_text)
    driver.switch_to.default_content()





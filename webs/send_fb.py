import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

import tools.reawin32 as rea

def fbStart(driver,fb_url,fideo_file,fb_title,fb_text):
    print("更新FaceBook！！！！！！！！！")
    time.sleep(3)
    newwindow = 'window.open("{}")'.format(fb_url)
    driver.execute_script(newwindow)
    driver.switch_to_window(driver.window_handles[3])
    # driver.get(fb_url)
    time.sleep(3)

    ele_file=driver.find_element_by_xpath('//div[@class="_5dw9 _5dwa _4-u3"]/span[2]/div/div/div[5]')
    ActionChains(driver).click(ele_file).perform()
    time.sleep(3)
    rea.send_file(fideo_file,'打开')
    time.sleep(3)
    driver.find_element_by_xpath('//input[@placeholder="在這裡為你的影片新增標題……"]').send_keys(fb_title)
    driver.find_element_by_xpath('//br[@data-text="true"]').send_keys(fb_text)

    fb_label=driver.find_element_by_xpath('//div[@class="_70ob _59_m"]/div/span[2]/label[1]')
    fb_label.send_keys('洛汗M')
    time.sleep(2)
    driver.find_element_by_xpath('//span[text()="新增標籤「洛汗M」"]').click()
    time.sleep(1)
    fb_label.send_keys('洛汗M輔助')
    time.sleep(2)
    driver.find_element_by_xpath('//span[text()="新增標籤「洛汗M輔助」"]').click()
    time.sleep(1)
    fb_label.send_keys('洛汗M外掛')
    time.sleep(2)
    driver.find_element_by_xpath('//span[text()="新增標籤「洛汗M外掛」"]').click()
    time.sleep(1)
    fb_label.send_keys('洛汗M神手')
    time.sleep(2)
    driver.find_element_by_xpath('//span[text()="新增標籤「洛汗M神手」"]').click()










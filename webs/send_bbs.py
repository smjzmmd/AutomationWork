import time

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys

def bbsStart(driver,bbs_url,bbs_title,url_list,add_text):
    print("更新神手论坛！！！！！！！！！","等待5秒...")
    time.sleep(5)
    newwindow = 'window.open("{}")'.format(bbs_url)
    driver.execute_script(newwindow)
    driver.switch_to_window(driver.window_handles[1])
    # driver.get(bbs_url)
    print("新建标签，打开网页", "等待3秒...")
    time.sleep(3)

    # # 点击 编辑
    while True:
        try:
            print("点击编辑。")
            driver.find_element_by_xpath("//a[@href='/posts/203/edit']").click()
            break
        except NoSuchElementException:
            print("点击编辑：失败！5秒后重新点击")
            time.sleep(6)


    # # 修改標題日期
    time.sleep(3)
    bbs_ti = driver.find_element_by_xpath('//input[@name="title"]')
    bbs_ti.clear()
    time.sleep(0.5)
    bbs_ti.send_keys(bbs_title)

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
    driver.find_element_by_xpath("//p[text()='洛汗M神手更新內容：']").send_keys(add_text)





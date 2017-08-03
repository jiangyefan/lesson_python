#!/usr/bin/env python
#!coding=utf-8
#__author__:Administrator
#__date__:2017/7/13


from selenium import webdriver
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

driver=webdriver.Chrome()


first_url='http://www.baidu.com'
print("now acess %s"%first_url)
driver.get(first_url)

second_url='http://news.baidu.com'
print("now acess %s"%second_url)
driver.get(second_url)

print("back to %s"%first_url)
driver.back()

# print("forward to %s"%second_url)
# driver.forward()

# driver.find_element_by_xpath('''//*[@id="kw"]''').send_keys("senlium")
# driver.find_element_by_xpath('''//*[@id="su"]''').click()
# time.sleep(3)

ActionChains(driver).move_to_element(driver.find_element_by_xpath('''//*[@id="u1"]/a[8]''')).perform()
print(driver.title)
print(driver.current_url)

texts=driver.find_elements_by_xpath('//div/h3/a')
for t in texts:
    print(t.text)

dict_diy=dict((("name","alex"),))
print(dict_diy)


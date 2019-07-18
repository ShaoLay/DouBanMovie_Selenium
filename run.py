#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author: Hamdi
from selenium import webdriver
import time


driver = webdriver.Chrome()
driver.get("https://movie.douban.com/")
driver.find_element_by_name("search_text").send_keys(u"周星驰")
driver.find_element_by_class_name("inp-btn").click()
driver.find_element_by_class_name("top-nav-info").click()
driver.find_element_by_class_name("account-tab-account").click()
driver.find_element_by_name("username").send_keys("18747161745")
driver.find_element_by_name("password").send_keys("QWERTY0202sl@.")
driver.find_element_by_class_name("btn-account").click()
time.sleep(2)
driver.quit()


# Generated by Selenium IDE
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class TestUI02():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def wait_for_window(self, timeout = 2):
    time.sleep(round(timeout / 1000))
    wh_now = self.driver.window_handles
    wh_then = self.vars["window_handles"]
    if len(wh_now) > len(wh_then):
      return set(wh_now).difference(set(wh_then)).pop()
  
  def test_uI02(self):
    # Test name: UI_02
    # Step # | name | target | value | comment
    # 1 | open | / |  | 
    self.driver.get("https://open.spotify.com/")
    # 2 | setWindowSize | 945x1012 |  | 
    self.driver.set_window_size(945, 1012)
    # 3 | click | css=.LKFFk88SIRC9QKKUWR5u .ButtonInner-sc-14ud5tc-0 |  | 
    self.driver.find_element(By.CSS_SELECTOR, ".LKFFk88SIRC9QKKUWR5u .ButtonInner-sc-14ud5tc-0").click()
    # 4 | click | id=login-username |  | 
    self.driver.find_element(By.ID, "login-username").click()
    # 5 | click | id=login-password |  | 
    self.driver.find_element(By.ID, "login-password").click()
    # 6 | type | id=login-password | @pw123456789 | 
    self.driver.find_element(By.ID, "login-password").send_keys("@pw123456789")
    # 7 | click | css=.ButtonInner-sc-14ud5tc-0 |  | 
    self.driver.find_element(By.CSS_SELECTOR, ".ButtonInner-sc-14ud5tc-0").click()
    # 8 | click | css=.KdxlBanhDJjzmHfqhP0X > .Svg-sc-ytk21e-0 |  | 
    self.driver.find_element(By.CSS_SELECTOR, ".KdxlBanhDJjzmHfqhP0X > .Svg-sc-ytk21e-0").click()
    # 9 | click | css=.DuEPSADpSwCcO880xjUG:nth-child(1) .Type__TypeElement-sc-goli3j-0 |  | 
    self.vars["window_handles"] = self.driver.window_handles
    # 10 | selectWindow | handle=${win4067} |  | 
    self.driver.find_element(By.CSS_SELECTOR, ".DuEPSADpSwCcO880xjUG:nth-child(1) .Type__TypeElement-sc-goli3j-0").click()
    # 11 | click | css=#change_password > .sc-4847034f-1 |  | 
    self.vars["win4067"] = self.wait_for_window(2000)
    # 12 | click | id=old_password |  | 
    self.driver.switch_to.window(self.vars["win4067"])
    # 13 | type | id=old_password | @pw123456789 | 
    self.driver.find_element(By.CSS_SELECTOR, "#change_password > .sc-4847034f-1").click()
    # 14 | click | id=new_password |  | 
    self.driver.find_element(By.ID, "old_password").click()
    # 15 | type | id=new_password | @pw123456 | 
    self.driver.find_element(By.ID, "old_password").send_keys("@pw123456789")
    # 16 | click | id=new_password_confirmation |  | 
    self.driver.find_element(By.ID, "new_password").click()
    # 17 | type | id=new_password_confirmation | @pw123456789 | 
    self.driver.find_element(By.ID, "new_password").send_keys("@pw123456")
    # 18 | click | css=.ButtonInner-sc-14ud5tc-0 |  | 
    self.driver.find_element(By.ID, "new_password_confirmation").click()
    self.driver.find_element(By.ID, "new_password_confirmation").send_keys("@pw123456789")
    self.driver.find_element(By.CSS_SELECTOR, ".ButtonInner-sc-14ud5tc-0").click()
  

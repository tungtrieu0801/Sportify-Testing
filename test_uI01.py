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

class TestUI01():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_uI01(self):
    # Test name: UI_01
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
    # 8 | click | css=.LU0q0itTx2613uiATSig:nth-child(2) .Type__TypeElement-sc-goli3j-0 |  | 
    self.driver.find_element(By.CSS_SELECTOR, ".LU0q0itTx2613uiATSig:nth-child(2) .Type__TypeElement-sc-goli3j-0").click()
    # 9 | runScript | window.scrollTo(0,0) |  | 
    self.driver.execute_script("window.scrollTo(0,0)")
    # 10 | click | css=.QO9loc33XC50mMRUCIvf |  | 
    self.driver.find_element(By.CSS_SELECTOR, ".QO9loc33XC50mMRUCIvf").click()
    # 11 | type | css=.QO9loc33XC50mMRUCIvf | baby | 
    self.driver.find_element(By.CSS_SELECTOR, ".QO9loc33XC50mMRUCIvf").send_keys("baby")
    # 12 | click | css=.pgwIORyBdf4nbb4G5_Jx .Svg-sc-ytk21e-0 |  | 
    self.driver.find_element(By.CSS_SELECTOR, ".pgwIORyBdf4nbb4G5_Jx .Svg-sc-ytk21e-0").click()
    # 13 | mouseOver | css=.pgwIORyBdf4nbb4G5_Jx path |  | 
    element = self.driver.find_element(By.CSS_SELECTOR, ".pgwIORyBdf4nbb4G5_Jx path")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    # 14 | mouseOut | css=.pgwIORyBdf4nbb4G5_Jx path |  | 
    element = self.driver.find_element(By.CSS_SELECTOR, "body")
    actions = ActionChains(self.driver)
    actions.move_to_element(element, 0, 0).perform()
    # 15 | click | css=.pgwIORyBdf4nbb4G5_Jx .Svg-sc-ytk21e-0 |  | 
    self.driver.find_element(By.CSS_SELECTOR, ".pgwIORyBdf4nbb4G5_Jx .Svg-sc-ytk21e-0").click()
  

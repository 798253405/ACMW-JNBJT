from appium.webdriver.common.touch_action import TouchAction
from appium import webdriver
import time
from info import tap as tap
from retry import retry

while True:
    tap()
    print('ok',time.localtime(time.time()))
    time.sleep(170)
    
    
 

from appium import webdriver
import time
from appium.webdriver.common.appiumby import AppiumBy
from appium.options.android import UiAutomator2Options

# Step 1: Create UiAutomator2Options
options = UiAutomator2Options()
options.platformName = 'Android'
options.platformVersion = '10'
options.deviceName = 'Xiaomi M2006C3MII'
options.app = '/Users/sudeepyadav/Downloads/Automation_Items/AndroidAPK/Android_Demo_App.apk'
options.appPackage = 'com.code2lead.kwad'
options.appActivity = 'com.code2lead.kwad.MainActivity'

# Step 2: Start the driver session using options
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', options=options)

# Step 3: Find and click on the element by ID
ele_id = driver.find_element(AppiumBy.ID, "com.code2lead.kwad:id/EnterValue")
ele_id.click()

# Step 4: Wait for 2 seconds
time.sleep(2)

# Step 5: Close the driver session
driver.quit()

#/Users/sudeepyadav/Android_Automation/Android_Automation/AppInstall.py

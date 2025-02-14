
dict_cap= {
    'platformName' : 'Android',
    'platformVersion' : '12',
    'deviceName' : 'Deepak',
    'automationName' : 'UiAutomator2',
    'udid' : 'ZD2224LD3H',
    'appPackage' : 'com.android.chrome',
    'appActivity' : 'org.chromium.chrome.browser.ChromeTabbedActivity'
}
url = 'http://localhost:4723/wd/hub'
driver = webdriver.Remote(url,desired_capabilities=dict_cap)
time.sleep(10)


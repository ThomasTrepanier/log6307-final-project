def setup_driver():
    global driver
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
    driver.execute_cdp_cmd('Network.setUserAgentOverride', {
        "userAgent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.53 Safari/537.36'})


setup_driver()
driver.get('url1')
# Do operations with url1
driver.close()

setup_driver()
driver.get('url2')
# Do operations with url2
driver.close()

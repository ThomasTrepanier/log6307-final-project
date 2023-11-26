def load_chrome_driver(headless):
    chrome_loc = "/home/ubuntu/Downloads/chromium-browser/"
    chrome_path = chrome_loc + "chrome"
    chromedriver_path = chrome_loc + "chromedriver"
    user_data_dir = "/home/ubuntu/.config/chromium/custom_user"
    options = webdriver.ChromeOptions()
    if headless:
        options.add_argument('headless')
    options.add_argument('--profile-directory=Default')
    options.add_argument("--start-maximized")
    options.add_argument('--disable-gpu')
    options.add_argument('--no-sandbox')
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument('--log-level=3')
    options.binary_location = chrome_path
    options.user_data_dir = user_data_dir
    driver = ucdriver.Chrome(
        executable_path=chromedriver_path, options=options)
    driver.set_window_size(1920, 1080)
    driver.set_window_position(0, 0)
    return driver

def get_post_likers(shortcode):
    chrome = ch.initialize()
    chrome.get('https://www.instagram.com/p/' + shortcode + '/')
    chrome.execute_script("window.scrollTo(0, 1080)") 
    url = "/p/" + shortcode + "/liked_by/"
    time.sleep(2)
    like_link = chrome.find_element_by_xpath('//a[@href="'+url+'"]')
    like_link.click()
    time.sleep(2)
    users = []
    pb = chrome.find_element_by_xpath("//div[@role = 'dialog']/div[2]/div[1]/div[1]").value_of_css_property("padding-bottom")
    match = False
    while match==False:
        lastHeight = pb

        # step 1
        elements = chrome.find_elements_by_xpath("//*[@id]/div/a")
        # step 2
        for element in elements:
            if element.get_attribute('title') not in users:
                users.append(element.get_attribute('title'))
        # step 3
        chrome.execute_script("return arguments[0].scrollIntoView();", elements[-1])
        time.sleep(1)
        # step 4
        pb = chrome.find_element_by_xpath("//div[@role = 'dialog']/div[2]/div[1]/div[1]").value_of_css_property("padding-bottom")
        if lastHeight==pb or len(users) >= 1500:
            match = True
    return users

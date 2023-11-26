def getPosts():
    hrefs_in_view = driver.find_elements_by_tag_name('a')
    # finding relevant hrefs
    hrefs_in_view = [elem.get_attribute('href') for elem in hrefs_in_view
         if '.com/p/' in elem.get_attribute('href')]
    
    return hrefs_in_view;





def getLikers(username,limit,post=1):
    driver.get('https://www.instagram.com/' + username)
    time.sleep(1)
    users=[]

    #Get Latest Post
    driver.get(getPosts()[post])
    
    time.sleep(2)
    #Open Dialog
    followersLinkX = driver.find_element_by_xpath('//button[@class="sqdOP yWX7d     _8A5w5    "]')
    followersLinkX.click()
    time.sleep(1)
    #Get Dialog
    xxx = driver.find_element_by_xpath('//div[@role="dialog"]/div[1]/div[2]/div[1]/div[1]')
    #Focus on and Scroll
    xxx.click()
    # step 3
    actionChain = webdriver.ActionChains(driver)

  

    count = 0
    
    while(count < limit):
        for i in range(1,1000):
            try:
                users.append("https://www.instagram.com/" + driver.find_element_by_xpath('//div[@role="dialog"]/div[1]/div[2]/div[1]/div[1]/div['+ str(i) +']/div[2]/div[1]/div[1]').text) 
                count+=1
            except:
                break
        actionChain.key_down(Keys.SPACE).key_up(Keys.SPACE).perform()
        time.sleep(0.5)  

    return users 

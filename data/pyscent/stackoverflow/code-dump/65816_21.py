actions = ActionChains(driver)

def triple_click(element_x):
    actions.click(element_x).click(element_x).click(element_x).perform()

triple_click(your_element)

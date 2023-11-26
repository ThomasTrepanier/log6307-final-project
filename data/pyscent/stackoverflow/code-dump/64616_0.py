# Check if an element is present using JS path.
# Particularly useful for shadow DOM elements
def is_element_present(driver, js_path):
    try:
        element = driver.execute_script(f"return {js_path}")
        return element is not None
    except Exception:
        pass
    try:
        outer_html = driver.execute_script(f"return {js_path}.outerHTML;")
        if outer_html:
            return True;    
    except Exception:
        return False
 
# used to click shadow elements w/ js path.
# uses javascript to allow for explicit waits 
def click_shadow_element(driver, errorName, js_path, wait_time = 10):
    try:
        WebDriverWait(driver, wait_time).until(lambda x: self.is_element_present(js_path))
        driver.execute_script(f"return {js_path}.click()")
    except (TimeoutException, ElementNotVisibleException, ElementNotInteractableException) as e:
        raise Exception(f"The {errorName} button was not found. Additional info: {str(e)}")

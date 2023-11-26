def  js_triple_click(element, deltaY = 60, offsetX = 0, offsetY = 0):
    driver.execute_script("""
      "var target = arguments[0];                                 " +
      "var offsetX = arguments[1];                                " +
      "var offsetY = arguments[2];                                " + 
      "var rect = target.getBoundingClientRect();                 " +
      "var cx = rect.left + (offsetX || (rect.width / 2));        " +        
      "var cy = rect.top + (offsetY || (rect.height / 2));        " +
      "                                                           " +
      "emit('mousedown', {clientX: cx, clientY: cy, buttons: 1}); " +
      "emit('mouseup',   {clientX: cx, clientY: cy});             " +
      "emit('mousedown', {clientX: cx, clientY: cy, buttons: 1}); " +
      "emit('mouseup',   {clientX: cx, clientY: cy});             " +
      "emit('mousedown', {clientX: cx, clientY: cy, buttons: 1}); " +
      "emit('mouseup',   {clientX: cx, clientY: cy});             " +
      "emit('click',     {clientX: cx, clientY: cy, detail: 3});  " +
      "                                                           " +
      "function emit(name, init) {                                " +
    "target.dispatchEvent(new MouseEvent(name, init));        " +
      "}                                                          " ;
    """)

element = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.TAG_NAME, "p"))) # replace the locator as per your usecase
ActionChains(driver).move_to_element(element).perform()
js_triple_click(element)
print("Tripple click performed")

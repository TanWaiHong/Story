from selenium import webdriver


chrome_driver_path = "C:/Users/User/Desktop/coding/store/chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("http://secure-retreat-92358.herokuapp.com/")

f_name = driver.find_element_by_name("fName")
l_name = driver.find_element_by_name("lName")
email_address = driver.find_element_by_name("email")
button = driver.find_element_by_class_name("btn")

f_name.send_keys("tan")
l_name.send_keys("hong")
email_address.send_keys("tan040724101445@gmail.com")
button.click()

from selenium import webdriver
import time

username = "xxxxx"
password = "xxxxx"

# starts a new chrome session
browser = webdriver.Firefox()
browser.implicitly_wait(5)

# navigate to the url
browser.get("https://www.instagram.com/")
time.sleep(4)

# finds the username box
usern = browser.find_element_by_name("username")
# sends the entered username
usern.send_keys(username)

# finds teh password box
passw = browser.find_element_by_name("password")

# sends the entered password
passw.send_keys(password)

# finds the login button
log_cl = browser.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div["
                                       "3]/button/div")
log_cl.click()
time.sleep(4)

import re
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait


def printFacebookPage () :
    WebDriverWait( driver, 5 )
    driver.get("http://www.facebook.com/pages")
    wait = WebDriverWait( driver, 10 )

    # find all related link
    elems = driver.find_elements_by_xpath("//div[@id='u_0_2']//a[@href]")
    for elem in elems:
        regex = r'https://www.facebook.com/(.*)/'
        url = elem.get_attribute("href")
        if ( re.match(regex,url) and (url not in listUrl) ) :
            listUrl.append(url)

    # print all available page
    for list in listUrl :
        print(list)

# username and password in facebook
usr="susisusanti1234"
pwd="SusiSusanti1234"
listUrl = []

# connect to driver
driver = webdriver.Chrome('/usr/local/share/chromedriver')
driver.set_window_size(1920/1.5, 1080/1.5)
driver.get("http://www.facebook.com")

# element for log in
assert "Facebook" in driver.title
elem = driver.find_element_by_id("email")
elem.send_keys(usr)
elem = driver.find_element_by_id("pass")
elem.send_keys(pwd)
elem.send_keys(Keys.RETURN)

# try to log in
try:
    elem = driver.find_element_by_css_selector(".input.textInput")
    elem.send_keys("Posted using Python's Selenium WebDriver bindings!")
    elem = driver.find_element_by_css_selector("input[value=\"Publicar\"]")
    elem.click()
except (Exception) :
    print(Exception)

# print page
printFacebookPage()

# like all available page and reload again

driver.quit()



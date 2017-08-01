import re
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


def defineDriver () :
    # connect to driver
    driver = webdriver.Chrome('/usr/local/share/chromedriver')
    driver.set_window_size(1920/2, 1080)
    driver.get("http://www.facebook.com")

    return driver


def loginFacebook (driver) :
    # username and password in facebook
    usr="susisusanti1234"
    pwd="SusiSusanti1234"


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
        print('Exception, I do not know')

def printFacebookPage (driver) :
    listUrl = []

    driver.get("http://www.facebook.com/pages")
    time.sleep(5)

    # find all related link
    elems = driver.find_elements_by_xpath("//div[@id='u_0_2']//a[@href]")
    for elem in elems:
        regex = r'https://www.facebook.com/(.*)/'
        url = elem.get_attribute("href")
        if ( re.match(regex,url) and (url not in listUrl) ) :
            listUrl.append(url)

    return listUrl

def findRelatedPage (driver) :
    time.sleep(5)
    # go to a page , data from file

    path = '/home/riskaamalia/Documents/fromGit/my-git/python-project/sample-data/facebook-page.txt'
    open(path).readline()
    loop = 0

    for line in open(path) :
        print("From file : "+line)
        driver.get(line)
        time.sleep(5)

        # find all related link to the page
        elems = driver.find_elements_by_xpath("//div[@class='_5ay5']//a[@href]")
        loopCheck = 0
        for elem in elems:
            regex = r'(https://www.facebook.com/)([^/]*)(/)$'
            url = elem.get_attribute("href")
            if re.match(regex,url) :
                # check the url exist or not in file
                for check in open(path) :
                    if url in check :
                        loopCheck = 1
                        break

                if loopCheck == 0 :
                    #     write to file
                    fWrite = open(path, "a")
                    with fWrite as myfile:
                        if loop != 0 :
                            myfile.write("\n"+url)
                        else :
                            myfile.write(url)
                        loop = loop + 1
                        print("Write "+url+" to file, total write : "+str(loop))
                else :
                    loopCheck = 0


            # elif url in relatedPages :
            #     print("Does not match already exist : "+url)
            # else :
            #     print("Does not match url pattern : "+url)

        time.sleep(2)


# ======================================================================================================================

# define driver
driver = defineDriver()

# log in facebook
loginFacebook(driver)

# print page
urlList = printFacebookPage(driver)

# like all available page and reload again
findRelatedPage(driver)

driver.quit()

# test = "https://www.facebook.com/coba/"
# regex = r'(https://www.facebook.com/)([^/]*)(/)$'
# if re.match(regex,test) :
#     print(test)

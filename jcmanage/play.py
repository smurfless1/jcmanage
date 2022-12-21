import subprocess
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

from bs4 import BeautifulSoup

front = "https://www.atmosenergy.com/accountcenter/logon/login.html?onepasswdfill=E6B2F92426654572B93E8CFCE3089283"

try:
    # open the page
    """
    firefox_paths = subprocess.check_output('mdfind  "kMDItemFSName = Firefox.app"', shell=True)
    firefox_path = firefox_paths.split('\n')[0]
    print firefox_path
    webdriver.FirefoxProfile.path = firefox_path
    """

    browser = webdriver.Chrome()
    browser.get(front)
    # switch to BeautifulSoup, which I can actually find help on.
    soup = BeautifulSoup(browser.page_source, "lxml")

    count = len(soup.find_all("form"))
    print(str(count))

except:
    print("Well, that didnt work")

import mechanize
import http.cookiejar
from bs4 import BeautifulSoup

# def openThingy(page, searchfor):
def openThingy(page, requestnumber):
    # Set Browser
    br = mechanize.Browser()

    # Set Cookie Jar
    cj = http.cookiejar.LWPCookieJar()
    br.set_cookiejar(cj)

    # Set Browser options
    br.set_handle_equiv(True)
    # br.set_handle_gzip(True)
    br.set_handle_redirect(True)
    br.set_handle_referer(True)
    br.set_handle_robots(False)

    # Follows refresh 0 but not hangs on refresh > 0
    br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)

    # Want debugging messages? Just uncomment the following lines
    # br.set_debug_http(True)
    # br.set_debug_redirects(True)
    # br.set_debug_responses(True)

    # User-Agent (this is cheating, ok?) We are basically writing the headers to
    # make it look like
    # it's coming from a Firefox browser in Fedora
    br.addheaders = [
        (
            "User-agent",
            "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1",
        )
    ]

    response = br.open(page)
    # html = response.read()

    # Select the first (index zero) form
    br.select_form(nr=0)
    ti = br.form.find_control(type="text")
    ti.value = requestnumber
    br.submit()
    # print br.response().read()

    # switch to BeautifulSoup, which I can actually find help on.
    soup = BeautifulSoup(br.response().read(), "lxml")
    responses = soup.find_all("span", class_="big_text")
    for type in responses:
        type = type.text
    print(type)
    count = len(soup.find_all("div", class_="grayContent"))
    print(str(count))
    return type + ", " + str(count)


import sys

openThingy("http://www.callercomplaints.com", sys.argv[1])

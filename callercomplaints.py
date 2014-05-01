# Library callercomplaints, queries callercomplaints.com for phone number scores
# Copyright (C) 2014 David Brown
#
# This program is free software: you can redistribute it and/or modify it under
# the terms of the GNU General Public License as published by the Free Software
# Foundation, either version 3 of the License, or (at your option) any later
# version.
#
# This program is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of  MERCHANTABILITY or FITNESS
# FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along with
# this program.  If not, see <http://www.gnu.org/licenses/>.

#NOTE: This is incomplete at this time.

import mechanize
import cookielib
from bs4 import BeautifulSoup

class callercomplaints:
    """
sudo pip install beautifulsoup4 html5lib lxml
sudo easy_install mechanize
    """

    def __init__(self):
        #raise NotImplementedError  #TODO finish writing and testing
        self.front = 'http://www.callercomplaints.com'
        self.site = 'http://www.callercomplaints.com/SearchResult.aspx?Phone='
        self.headers = {'User-Agent': 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)' }

    def _sendit(self, number):
        try:
            # Set Browser
            br = mechanize.Browser()

            # Set Cookie Jar
            cj = cookielib.LWPCookieJar()
            br.set_cookiejar(cj)

            # Set Browser options
            br.set_handle_equiv(True)
            #br.set_handle_gzip(True)
            br.set_handle_redirect(True)
            br.set_handle_referer(True)
            br.set_handle_robots(False)

            # Follows refresh 0 but not hangs on refresh > 0
            br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)

            # Want debugging messages? Just uncomment the following lines
            #br.set_debug_http(True)
            #br.set_debug_redirects(True)
            #br.set_debug_responses(True)

            # User-Agent (this is cheating, ok?) We are basically writing the headers to
            # make it look like
            # it's coming from a Firefox browser in Fedora
            br.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]

            response = br.open(self.front)
            #html = response.read()

            # Select the first (index zero) form
            br.select_form(nr=0)
            ti = br.form.find_control(type="text")
            ti.value = number
            br.submit()
            #print br.response().read()

            # switch to BeautifulSoup, which I can actually find help on.
            soup = BeautifulSoup(br.response().read(), "lxml")
            responses = soup.find_all('span', class_='big_text')
            for type in responses:
                type = type.text
            #print type
            count = len(soup.find_all('div', class_='grayContent'))
            #print str(count)
            return type + ', ' + str(count)
        except:
            pass

    def getScore(self, number):
        return self._sendit(number)
        return "Not done yet."

    def report(self, number, dateString='', callerString='', guessedName='',
        zipcode=''):
        #TODO not sure if I care about results.
        pass

if __name__ == '__main__':
    wc = callercomplaints()
    import sys
    score = wc.getScore(sys.argv[1])
    print score


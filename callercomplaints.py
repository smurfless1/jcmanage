# Library callercomplaints, queries callercomplaints.com for phone number scores
# Copyright (C) 2022 David Brown
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

import mechanize
import http.cookiejar
from bs4 import BeautifulSoup
from lib.ratelimited import RateLimited

class callercomplaints:
    """
sudo pip install beautifulsoup4 html5lib lxml mechanize
    """

    def __init__(self):
        self.front = 'http://www.callercomplaints.com'

    @RateLimited(maxPerSecond=1)
    def _sendit(self, number):
        try:
            # Set Browser
            br = mechanize.Browser()

            cj = http.cookiejar.LWPCookieJar()
            br.set_cookiejar(cj)

            # Set Browser options
            br.set_handle_equiv(True)
            #br.set_handle_gzip(True)  # too noisy
            br.set_handle_redirect(True)
            br.set_handle_referer(True)
            br.set_handle_robots(False)

            br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)

            #br.set_debug_http(True)
            #br.set_debug_redirects(True)
            #br.set_debug_responses(True)

            # Firefox on Fedora
            br.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]

            br.open(self.front)

            # Select the first (index zero) form
            br.select_form(nr=0)
            ti = br.form.find_control(type="text")
            ti.value = number
            br.submit()

            # switch to BeautifulSoup, which I can actually find help on.
            soup = BeautifulSoup(br.response().read(), "lxml")
            responses = soup.find_all('span', class_='big_text')
            for type in responses:
                type = type.text

            count = len(soup.find_all('div', class_='grayContent'))

            return type + ', ' + str(count)
        except:
            pass

    def getScore(self, number):
        return self._sendit(number)

    def report(self, number, dateString='', callerString='', guessedName='',
        zipcode=''):
        #TODO
        pass

if __name__ == '__main__':
    wc = callercomplaints()
    import sys
    score = wc.getScore(sys.argv[1])
    print(score)


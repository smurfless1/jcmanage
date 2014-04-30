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

import urllib2

from bs4 import BeautifulSoup

class callercomplaints:
    """
sudo pip install beautifulsoup4 html5lib lxml
    """

    def __init__(self):
        raise NotImplementedError  #TODO finish writing and testing
        self.site = 'http://www.callercomplaints.com/SearchResult.aspx?Phone='
        self.headers = {'User-Agent': 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)' }

    def _sendit(self, number):
        url = self.site + number
        req = urllib2.Request(url)
        response = urllib2.urlopen(req)
        return response.read()

    def getScore(self, number):
        try:
            response = self._sendit(number)
            soup = BeautifulSoup(response, "lxml")
            responses = soup.find_all('span', class_='big_text')
            type = responses[1].text
            count = len(soup.find_all('div', class_='grayContent'))
            return type + ', ' + str(count)

        except:
            pass
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


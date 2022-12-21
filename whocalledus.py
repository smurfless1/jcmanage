# Library/Program whocalledus. Get a score for a phone number from whocalled.us
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

import urllib.request, urllib.parse, urllib.error
import urllib.request, urllib.error, urllib.parse

from lib.ratelimited import RateLimited


class whocalled:
    """
    See http://whocalled.us/about
    Abstraction interface to simplify getting scores from whocalled.us website
    via their API.

    THIS REQUIRES YOU TO HAVE AN ACCOUNT. An account must be made on their site to use their API.

    http://whocalled.us/do?action=
    do?action=report&name=test&pass=test&phoneNumber=5551234567&date=2007-03-06&callerID=800%20Service&identity=TeleCon&postalCode=90210
    do?action=comment&name=test&pass=test&phoneNumber=5551234567&message=Test
    do?action=getScore&name=test&pass=test&phoneNumber=5551234567
    """

    def __init__(self, name, passwd):
        self.site = 'http://whocalled.us/do'
        self.name = name
        self.passwd = passwd
        self.headers = {'User-Agent': 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'}

    def _sendit(self, values):
        url = self.site
        data = urllib.parse.urlencode(values)
        req = urllib.request.Request(url, data, self.headers)
        response = urllib.request.urlopen(req)
        return response.read()

    @RateLimited(1)
    def getScore(self, number):
        values = {
                'action':'getScore',
                'name' : self.name,
                'pass': self.passwd,
                'phoneNumber' : number
        }
        try:
            response = self._sendit(values)
            success = response.split('&')[0].split('=')[1]
            if success == "1":
                score = response.split('&')[1].split('=')[1]
                return score
        except:
            pass
        return "Failed to get a response."

    @RateLimited(1)
    def report(self, number, dateString='', callerString='', guessedName='',
        zipcode=''):
        values = {
            'action': 'report',
            'name': self.name,
            'pass': self.passwd,
            'phoneNumber': number,
            'date': dateString,
            'callerID': callerString,
            'identity': guessedName,
            'postalCode': zipcode
        }
        response = self._sendit(values)
        #TODO not sure if I care about results.

if __name__ == '__main__':
    import sys
    raise NotImplementedError  # when you put in your password, take this out
    wc = whocalled('YourUserName', 'YourPassword')
    score = wc.getScore(sys.argv[1])
    print(score)


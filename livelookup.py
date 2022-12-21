# Program livelookup, create UI notifications of calls on my Mac
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

__author__ = 'daveb'
from socket import *
import re

from pync import Notifier
from .whocalledus import *
from lib.calleridentry import callerIdEntry

# sample input: --DATE = 032914--TIME = 1007--NMBR = 8885551212--NAME = V32913072900491--
pattern = re.compile('.-DATE = (.*)--TIME = (.*)--NMBR = (.*)--NAME = (.*)--')

#raise NotImplementedError  # when you put in your password, take this out
wc = whocalled('username', 'password')  # todo keyring?

s = socket(AF_INET, SOCK_DGRAM)
s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
s.bind(('0.0.0.0', 9753))
print('udp ready!')
BUFSIZE = 512
while True:
    data, addr = s.recvfrom(BUFSIZE)
    print(('server received %r from %r' % (data, addr)))

    result = pattern.match(data)
    if result:
        entry = callerIdEntry()
        entry.fromString(data)

        print("Number to look up: ")
        #print result.group(3)
        entry.parts['NMBR'].strip()
        print("Score: ")
        score =  wc.getScore(result.group(3))
        print(score)
        #entry.parts['NAME'].strip()
        Notifier.notify('Score: %s' % score, title='Phone')


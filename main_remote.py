# Program main_remote. Look up new phone numbers and maybe add to the blacklist.
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

# This is different than main.py in that this version is intended to also launch
# selenium and a browser so the user can see the results. Not very code different
# yet.

import sys

from calleridlist import callerIdList
from blacklist import blacklist
import callercomplaints
from whocalledus import whocalled
from whocallsme import whocallsme


if __name__ == '__main__':
    raise NotImplementedError  # when you put in your password, take this out
    wc = whocalled('YourUserName', 'YourPassword')
    wcm = whocallsme()  # requires selenium install and configuration
    cc = callercomplaints()

    it = callerIdList()
    it.loadFromFile()
    it.pickNewBlacklistEntries( [ wc, wcm, cc ])
    #TODO compare to local address book on mac?

    bl = blacklist()
    bl.loadFromFile()
    bl.merge( it.getNewBlacklistEntries() )
    #print bl
    bl.save()

    sys.exit(0)

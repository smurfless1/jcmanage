# Program main. Look up new phone numbers and maybe add to the blacklist.
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

"""
This is meant to be run via ssh on the computer that runs jcblock, so the
score checking libs should be the ones that don't depend on a real browser
"""
import callercomplaints

from lib.calleridlist import callerIdList
from lib import blacklist
from whocalledus import whocalled

if __name__ == '__main__':
    raise NotImplementedError  # when you put in your password, take this out
    wc = whocalled('YourUserName', 'YourPassword')
    cc = callercomplaints()

    it = callerIdList()
    it.loadFromFile()
    it.pickNewBlacklistEntries([wc, cc])

    bl = blacklist()
    bl.loadFromFile()
    bl.merge(it.getNewBlacklistEntries())
    #print bl
    bl.save()



# Library blacklistentry.py, manages individual blacklist entries
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

class blacklistEntry:
    def __init__(self):
        self.test = '                   ' # 19 of them
        self.date = '------        ' # 14
        self.comment = '                    ' # 20, no reason

    def fromString(self, what):
        self.test = what[:19]
        self.setDate(what[19:33])
        self.setComment(what[33:])

    def getKey(self):
        return self.test

    def getValue(self):
        # 19, 14(6 + 8), 20
        return '%s%s%s' % (self.test, self.date, self.comment)

    def setTestField(self, what):
        self.test = '{:<19}'.format(what + '?')

    def setDate(self, what):
        self.date = '{:<14}'.format(what)

    def setComment(self, what):
        self.comment = '{:<20}'.format(what)

    def __str__(self):
        return self.getValue()

    def __eq__(self, other):
        if isinstance(other, blacklistEntry):

            # wildcard matches
            if 'NMBR = ' in self.getKey():
                areacode = self.getKey()[7:10]
                return areacode in other.getKey()[0:3]

            if 'NMBR = ' in other.getKey():
                # wildcard matches
                areacode = other.getKey()[7:10]
                return areacode in self.getKey()[0:3]

            # literal matches
            return self.getKey() == other.getKey()

        #TODO compare to callerID entries?

        return NotImplemented

    def __ne__(self, other):
        result = self.__eq__(other)
        if result is NotImplemented:
            return result
        return not result

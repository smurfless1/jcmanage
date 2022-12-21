# Program makeBadEntries. Write a blacklist for all area codes we don't like.
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

# Blanket ban of all area codes we don't approve. Codes written to stdout.
# good list: where we live plus general purpose area codes.
from libs.blacklistentry import blacklistEntry

goodcodes = [
    281,
    341,
    315,
    369,
    385,
    408,
    415,
    510,
    503,
    627,
    628,
    650,
    669,
    737,
    764,
    800,
    801,
    818,
    822,
    833,
    844,
    855,
    866,
    877,
    888,
    916,
]

for i in range(0, 1000):
    if i not in goodcodes:
        entry = blacklistEntry()
        entry.setTestField("NMBR = %03d" % i)
        entry.setDate("032510")
        entry.setComment("IGNORING")
        print(entry)

        # print "NMBR = %03d?        032510        BAD AREA CODE" % i

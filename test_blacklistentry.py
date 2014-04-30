# Tests for blacklist entries
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

import unittest

from blacklistentry import blacklistEntry


class TestBlacklistEntry(unittest.TestCase):
    def given_an_entry(self):
        self.entry = blacklistEntry()
        self.assertTrue(len(self.entry.test) == 19)
        self.assertEquals(self.entry.test, '                   ')

        self.entry.fromString('Salt Lake Ci UT?   062013        1-888-555-1212')
        self.assertEquals(self.entry.test, 'Salt Lake Ci UT?   ')
        self.assertEquals(self.entry.date, '062013        ')
        self.assertEquals(self.entry.comment, '1-888-555-1212      ')
        self.assertEquals(len(self.entry.comment), 20)

        self.assertEquals(self.entry.getKey(), 'Salt Lake Ci UT?   ')

    def test_CreateFromStrings(self):
        self.given_an_entry()

    def test_CreateFromScratch(self):
        entry = blacklistEntry()
        entry.setTestField('asdf')
        entry.setDate('060606')
        entry.setComment('')
        self.assertEquals(entry.getKey(), 'asdf?              ')

    def test_keeps_dashes(self):
        entry = blacklistEntry()
        entry.fromString('Salt Lake Ci UT?   ------        1-888-555-1212')
        self.assertEquals(entry.test, 'Salt Lake Ci UT?   ')
        self.assertEquals(entry.date, '------        ')
        self.assertEquals(entry.comment, '1-888-555-1212      ')
        self.assertEquals(entry.getValue(),
                          'Salt Lake Ci UT?   ------        1-888-555-1212      ')
        self.assertEquals(entry.getKey(), 'Salt Lake Ci UT?   ')

    def test_wildcard_created(self):
        entry = blacklistEntry()
        entry.setTestField('NMBR = 002')
        entry.setDate('060606')
        entry.setComment('')
        self.assertEquals(entry.getKey(), 'NMBR = 002?        ')

    def test_equals(self):
        entry = blacklistEntry()
        entry.setTestField('0020030040')
        entry2 = blacklistEntry()
        entry2.setTestField('0020030040')
        self.assertEquals(entry, entry2)

    def test_wildcard_matches(self):
        entry = blacklistEntry()
        entry.setTestField('NMBR = 002')
        entry.setDate('060606')
        entry.setComment('')
        entry2 = blacklistEntry()
        entry2.setTestField('0020030040')
        self.assertEquals(entry, entry2)
        self.assertEquals(entry2, entry)

if __name__ == '__main__':
    unittest.main()


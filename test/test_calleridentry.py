# Tests for callerID entries
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

import fudge
from lib.calleridentry import callerIdEntry


class TestCallerIdEntry(unittest.TestCase):
    def given_a_new_entry(self):
        self.entry = callerIdEntry()
        self.assertTrue( len(self.entry.parts) == 0 )
        self.entry.fromString('W-DATE = 061913--TIME = 0848--NMBR = 8885551212--NAME = ISELLYOURSOUL  --')
        self.assertTrue( len(self.entry.parts) == 4 )

    def given_an_entry(self):
        self.entry = callerIdEntry()
        self.assertTrue( len(self.entry.parts) == 0 )
        self.entry.fromString('--DATE = 061913--TIME = 0848--NMBR = 8885551212--NAME = ISELLYOURSOUL  --')
        self.assertTrue( len(self.entry.parts) == 4 )

    def test_CreateFromStrings(self):
        self.given_an_entry()

    def test_getKey(self):
        self.given_an_entry()
        self.assertEquals(
            'ISELLYOURSOUL?     8885551212?        ',
             self.entry.getKey())

    @fudge.patch('__builtin__.raw_input')
    def test_getValue(self, read):
        (read.expects_call().returns('y'))
        self.given_an_entry()
        self.entry.chooseBlacklistEntry()
        self.assertEquals(2, len(self.entry.getValue()))

    @fudge.patch('__builtin__.raw_input')
    def test_getNewValue(self, read):
        (read.expects_call().returns('y'))
        self.given_a_new_entry()
        self.entry.chooseBlacklistEntry()
        self.assertEquals(2, len(self.entry.getValue()))

    @fudge.patch('__builtin__.raw_input')
    def test_getWithChecker(self, read):
        class stubChecker():
            def getScore(self, what):
                return 1
        (read.expects_call().returns('y'))
        self.given_an_entry()
        self.entry.chooseBlacklistEntry([ stubChecker() ])
        self.assertEquals(2, len(self.entry.getValue()))

    @fudge.patch('__builtin__.raw_input', '__builtin__.print')
    def test_entries_comparable(self, read, printy):
        (read.is_callable().returns('y'))
        (printy.is_callable())
        self.given_an_entry()
        self.entry.chooseBlacklistEntry()
        entry2 = callerIdEntry()
        entry2.fromString('--DATE = 061913--TIME = 0848--NMBR = 8885551212--NAME = ISELLYOURSOUL  --')
        entry2.chooseBlacklistEntry()
        self.assertEquals(self.entry.getKey(), entry2.getKey())
        self.assertEquals(self.entry, entry2)

if __name__ == '__main__':
    unittest.main()


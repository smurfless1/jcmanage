# Tests for blacklist library
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

from jcmanage.libs.blacklist import blacklist
from jcmanage.libs.blacklistentry import blacklistEntry


class TestBlacklistList(unittest.TestCase):
    def test_load(self):
        lines = [
            "#                  | <---- the 20th column",
            "#Tested field:     Date field:   Comment field:",
            "NMBR = 809?        032510        BAD AREA CODE",
            "SELLING MY SOUL?   ------        1-888-555-1212",
        ]
        it = blacklist()
        it.load(lines)
        self.assertEqual(2, len(it.dict))

    def test_load_removes_duplicates(self):
        lines = [
            "#                  | <---- the 20th column",
            "#Tested field:     Date field:   Comment field:",
            "NMBR = 809?        032510        BAD AREA CODE",
            "SELLING MY SOUL?   123456        1-888-555-1212",
            "SELLING MY SOUL?   123457        1-888-555-1212",
        ]
        it = blacklist()
        it.load(lines)
        self.assertEqual(2, len(it.dict))

    def test_merge(self):
        lines = [
            "#                  | <---- the 20th column",
            "#Tested field:     Date field:   Comment field:",
            "SELLING MY SOUL?   123456        1-888-555-1212",
            "SELLING MY SOUL?   123456        different",
            "SELLING MY SOUL?   123457        1-888-555-1212",
        ]
        it = blacklist()
        it.load(lines)
        self.assertEqual(1, len(it.dict))
        newentry = blacklistEntry()
        newentry.fromString("JERKS INC?         123456        Auto")
        it.merge([newentry])
        self.assertEqual(2, len(it.dict))

    def test_merge_eliminates_duplicates(self):
        lines = [
            "#                  | <---- the 20th column",
            "#Tested field:     Date field:   Comment field:",
            "SELLING MY SOUL?   123456        1-888-555-1212",
            "SELLING MY SOUL?   123456        different",
            "SELLING MY SOUL?   123457        1-888-555-1212",
        ]
        it = blacklist()
        it.load(lines)
        self.assertEqual(1, len(it.dict))
        newentry = blacklistEntry()
        newentry.fromString("SELLING MY SOUL?   123456        Auto")
        it.merge([newentry])
        self.assertEqual(1, len(it.dict))


if __name__ == "__main__":
    unittest.main()

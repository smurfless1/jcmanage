# Tests for the callerID list
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

from lib.calleridlist import callerIdList


class TestCallerIdList(unittest.TestCase):
    def test_CreateList(self):
        it = callerIdList()
        self.assertEquals(0, len(it.dict))
        self.assertEquals(0, len(it.myset))

    #@fudge.patch('')
    def test_load_removes_duplicates(self):
        it = callerIdList()
        lines=[
'#THIS IS A COMMENT',
'#--DATE = 061913--TIME = 0848--NMBR = 8885551212--NAME = Scum Sucker    --',
'--DATE = 061913--TIME = 0848--NMBR = 8885551212--NAME = Scum Sucker    --',
'--DATE = 061913--TIME = 0848--NMBR = 8885551212--NAME = Scum Sucker    --',
        ]
        it.load(lines)
        self.assertEquals(1, len(it.dict))
        self.assertEquals(0, len(it.myset))

    def test_load(self):
        it = callerIdList()
        lines=[
'#THIS IS A COMMENT',
'#--DATE = 061913--TIME = 0848--NMBR = 8885551212--NAME = Scum Sucker    --',
'--DATE = 061913--TIME = 0848--NMBR = 8885551212--NAME = Scum Sucker    --',
'--DATE = 061913--TIME = 0848--NMBR = 4087727741--NAME = Scum Sucker    --',
        ]
        it.load(lines)
        self.assertEquals(2, len(it.dict))
        self.assertEquals(0, len(it.myset))

if __name__ == '__main__':
    unittest.main()


# Library calleridlist, manages callerID.dat as a collection of entries
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

import os
import pickle

from calleridentry import callerIdEntry


class callerIdList:
    def __init__(self):
        self.dict = {}
        self.myset = set()
        # list of items to reject in future
        self.reject = []

    def loadFromFile(self):
        LIST=open("../jcblock/callerID.dat", "r")
        self.load(LIST)
        LIST.close()

    def load(self, source):
        for line in source:
            if '#' in line:
                continue
            try:
                entry = callerIdEntry()
                entry.fromString(line)

                if entry.getKey() not in self.dict:
                    self.dict[entry.getKey()] = entry
            except:
                pass

    def pickNewBlacklistEntries(self, checkers=None):
        # remember previous decisions, merge with new
        seen=[]
        self.reject=[]
        if os.path.exists( "seen.pickle" ):
            seen = pickle.load( open( "seen.pickle", "rb" ) )

        for (k, v) in self.dict.iteritems():
            if k in seen:
                continue
            seen.append(v.getKey())

            newlist = v.chooseBlacklistEntry(checkers)
            if newlist is not None:
                for i in newlist:
                    self.reject.append(i)

        pickle.dump( seen, open( "seen.pickle", "wb" ) )

    def getNewBlacklistEntries(self):
        return self.reject


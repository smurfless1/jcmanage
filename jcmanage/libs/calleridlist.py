#!python
import os
import pickle
from calleridentry import callerIdEntry
from blacklistentry import blacklistEntry


class callerIdList:
    def __init__(self):
        self.dict = {}
        self.myset = set()
        # list of items to reject in future
        self.reject = []

    def loadFromFile(self):
        LIST = open("callerID.dat", "r")
        self.load(LIST)
        LIST.close()

    def load(self, source):
        for line in source:
            if "#" in line:
                continue
            try:
                entry = callerIdEntry()
                entry.fromString(line)

                if entry.getKey() not in self.dict:
                    self.dict[entry.getKey()] = entry
            except:
                pass

    def pickNewBlacklistEntries(self):
        # remember previous decisions, merge with new
        seen = []
        self.reject = []
        if os.path.exists("seen.pickle"):
            seen = pickle.load(open("seen.pickle", "rb"))

        for (k, v) in self.dict.iteritems():
            if k in seen:
                continue
            seen.append(v.getKey())

            newlist = v.chooseBlacklistEntry()
            if newlist is not None:
                for i in newlist:
                    self.reject.append(i)

        pickle.dump(seen, open("seen.pickle", "wb"))

    def getNewBlacklistEntries(self):
        return self.reject

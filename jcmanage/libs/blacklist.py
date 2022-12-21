#!python
import os
import pickle
from blacklistentry import blacklistEntry


class blacklist:
    def __init__(self):
        self.dict = {}
        self.comments = []

    def loadFromFile(self):
        LIST = open("blacklist.dat", "r")
        self.load(LIST)
        LIST.close()

    def load(self, source):
        lines = sorted(set(source))
        for line in lines:
            line = line.strip()
            if "#" in line:
                self.comments.append(line)
                continue
            # print '++' + line + '++'
            entry = blacklistEntry()
            # print '=+' + entry.date + '+='
            entry.fromString(line)
            if entry.getKey() not in self.dict:
                self.dict[entry.getKey()] = entry.getValue()
                # print '=+' + entry.getValue().strip() + '+='
        self.myset = set(self.dict.values())
        # print self.dict.values()
        # print self.myset

    def getKey(self):
        returnme = ""
        for e in self.entries:
            returnme = str(returnme) + e.getKey()
        return returnme

    def merge(self, what):
        # TODO examine elements in what, get the key, and then decide to merge
        for entry in what:
            if entry.getKey() not in self.dict:
                self.dict[entry.getKey()] = entry.getValue()

    def __str__(self):
        return "\n".join(["\n".join(self.comments), "\n".join(sorted(self.myset))])

    def save(self):
        # pickle.dump( seen, open( "seen.pickle", "wb" ) )
        newlist = "\n".join(
            ["\n".join(self.comments), "\n".join(sorted(self.dict.values()))]
        )
        LIST = open("blacklist.dat.new", "w")
        LIST.write(newlist)
        LIST.write("\n")
        LIST.close()

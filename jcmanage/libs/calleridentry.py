#!python
import os
from blacklistentry import blacklistEntry


class callerIdEntry:
    def __init__(self):
        pass
        self.parts = {}
        self.entry = None

    def fromString(self, what):
        # --DATE = 061913--TIME = 0848--NMBR = 4087727739--NAME = Brown David    --
        parts = what.split("--")
        # print parts
        for part in parts:
            try:
                # print part
                # print part.split(' ')
                (k, v) = part.split(" = ")
                # print "Found " + k + " set to " + v + "."
                self.parts[k] = v
            except:
                pass

    def getKey(self):
        """
        Make the key string used for comparing later.
        """
        name = self.parts["NAME"].strip() + "?"
        num = self.parts["NMBR"].strip() + "?"
        return "{:<19}{:<19}".format(name, num)

    def chooseBlacklistEntry(self):
        # length formatting, question mark replacement
        name = self.parts["NAME"].strip() + "?"
        num = self.parts["NMBR"].strip() + "?"
        yesno = raw_input("Blacklist this one? : %s, %s ? y/n  " % (name, num))
        if "y" in yesno:
            entry1 = blacklistEntry()
            entry1.setTestField(self.parts["NAME"].strip())
            entry1.setComment("from caller id")
            entry2 = blacklistEntry()
            entry2.setTestField(self.parts["NMBR"].strip())
            entry2.setComment("from caller id")

            self.entry = [entry1, entry2]
            return self.entry

            self.entry = "{:<19}{:<14}{:20}\n{:<19}{:<14}{:20}".format(
                name, self.parts["DATE"], "Auto", num, self.parts["DATE"], "Auto"
            )
            return self.entry

        self.entry = None
        return self.entry

    def getValue(self):
        return self.entry

    def getHash(self):
        return (self.getKey(), self.getValue())

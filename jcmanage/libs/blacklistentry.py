#!python
class blacklistEntry:
    def __init__(self):
        self.test = "                   "  # 19 of them
        self.date = "------        "  # 14
        self.comment = "                    "  # 20, no reason

    def fromString(self, what):
        self.test = what[:19]
        self.setDate(what[19:33])
        self.setComment(what[33:])

    def getKey(self):
        return self.test

    def getValue(self):
        # 19, 14(6 + 8), 20
        return "%s%s%s" % (self.test, self.date, self.comment)

    def setTestField(self, what):
        self.test = "{:<19}".format(what + "?")

    def setDate(self, what):
        self.date = "{:<14}".format(what)

    def setComment(self, what):
        self.comment = "{:<20}".format(what)

    def __str__(self):
        return self.getValue()

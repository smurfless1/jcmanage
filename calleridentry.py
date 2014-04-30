# Library calleridentry, represents individual caller ID entries in the callerID.dat file
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

from blacklistentry import blacklistEntry

class callerIdEntry:
    def __init__(self):
        pass
        self.parts = {}
        self.entry = None

    def fromString(self, what):
        # --DATE = 061913--TIME = 0848--NMBR = 8885551212--NAME = Brown David    --
        # B-DATE = 061913--TIME = 0848--NMBR = 8885551212--NAME = Brown David    --
        # W-DATE = 061913--TIME = 0848--NMBR = 8885551212--NAME = Brown David    --
        parts = what.split('--')
        #print parts
        for part in parts:
            try:
                #print part
                #print part.split(' ')
                (k, v) = part.split(' = ')
                #print "Found " + k + " set to " + v + "."
                self.parts[k] = v
            except:
                pass

    def getKey(self):
        '''
        Make the key string used for comparing later.
        '''
        name = self.parts['NAME'].strip() + '?'
        num  = self.parts['NMBR'].strip() + '?'
        return '{:<19}{:<19}'.format(name, num)

    def chooseBlacklistEntry(self, checkers=None):
        """
        Return any new blacklist entries to add to the global list.
        Return None if you don't want any added.
        checkers are the list of test classes that can return arbitrary results that can aid the user in telling
        if the number is a sonofabitch or not.
        """
        # length formatting, question mark replacement
        scores = []
        name = self.parts['NAME'].strip() + '?'
        num  = self.parts['NMBR'].strip() + '?'
        thinNum = self.parts['NMBR'].translate(None, '()- ?').strip()
        entry1 = blacklistEntry()
        entry1.setTestField(self.parts['NAME'].strip())
        entry1.setComment('from caller id')
        entry2 = blacklistEntry()
        entry2.setTestField(self.parts['NMBR'].strip())
        entry2.setComment('from caller id')
        autoPromote = False

        if checkers is not None:
            #TODO check expected format
            for checker in checkers:
                score = checker.getScore( thinNum )
                scores.append(score)
                try:
                    if int(score) > 19:
                        autoPromote = True
                except:
                    pass

        #print scores
        yesno = ''
        if not autoPromote:
            yesno = raw_input(
                'Blacklist this one? : %s, %s ?\nScores: %s : y/n  '
                % (name, num, str( scores )))
        if 'y' in yesno or autoPromote:
            self.entry = [ entry1, entry2 ]
            # optional reporting
            if checkers is not None:
                for checker in checkers:
                    continue
                    checker.report( thinNum )
            return self.entry

            self.entry = '{:<19}{:<14}{:20}\n{:<19}{:<14}{:20}'.format(name,
                self.parts['DATE'], 'Auto', num, self.parts['DATE'], 'Auto')
            return self.entry

        self.entry = None
        return self.entry

    def getValue(self):
        return self.entry

    def getHash(self):
        return (self.getKey(), self.getValue())

    def __eq__(self, other):
        #TODO implement comparison to blacklist entries
        if isinstance(other, callerIdEntry):
            return self.getKey() == other.getKey()
        return NotImplemented

    def __ne__(self, other):
        result = self.__eq__(other)
        if result is NotImplemented:
            return result
        return not result



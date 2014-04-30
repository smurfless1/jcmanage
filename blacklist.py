# Library blacklist.py, manages the file that contains blacklist entries
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

class blacklist:
    def __init__(self):
        self.dict = {}
        self.comments = []

    def loadFromFile(self):
        LIST=open("../jcblock/blacklist.dat", "r")
        self.load(LIST)
        LIST.close()

    def load(self, source):
        lines = sorted(set(source))
        for line in lines:
            line = line.strip()
            if '#' in line:
                self.comments.append(line)
                continue
            #print '++' + line + '++'
            entry = blacklistEntry()
            #print '=+' + entry.date + '+='
            entry.fromString(line)
            if entry.getKey() not in self.dict:
                self.dict[entry.getKey()] = entry.getValue()
                #print '=+' + entry.getValue().strip() + '+='
        self.myset = set(self.dict.values())
        #print self.dict.values()
        #print self.myset

    def getKey(self):
        returnme = ""
        for e in self.entries:
            returnme = str(returnme) + e.getKey()
        return returnme

    def merge(self, what):
        for entry in what:
            if entry.getKey() not in self.dict:
                self.dict[ entry.getKey() ] = entry.getValue()

    def __str__(self):
        return '\n'.join( [ '\n'.join(self.comments),
            '\n'.join(sorted(self.myset)) ] )

    def save(self):
        #pickle.dump( seen, open( "seen.pickle", "wb" ) )
        newlist = '\n'.join( [ '\n'.join(self.comments),
            '\n'.join(sorted(self.dict.values())) ] )
        LIST=open('blacklist.dat.new', 'w')
        LIST.write(newlist)
        LIST.write('\n')
        LIST.close()



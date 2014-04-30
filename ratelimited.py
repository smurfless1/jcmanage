# Library ratelimited, limits the rate of calls to decorated functions
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

# Based on multiple samples and information found online. I'm not entirely happy
# with this solution to this problem, but it's enough for crude work.

import time
import threading

def RateLimited(maxPerSecond):
  '''
  Decorator based call throttling
  '''
  lock = threading.Lock()
  minInterval = 1.0 / float(maxPerSecond)
  def decorate(func):
    lastTimeCalled = [0.0]
    def rateLimitedFunction(args, *kargs):
      lock.acquire()
      elapsed = time.clock() - lastTimeCalled[0]
      leftToWait = minInterval - elapsed

      if leftToWait>0:
          #lock.release()
          #return
          time.sleep(leftToWait)

      lock.release()

      ret = func(args,*kargs)
      lastTimeCalled[0] = time.clock()
      return ret
    return rateLimitedFunction
  return decorate

if __name__ == "__main__":
    @RateLimited(10)  # N per second at most
    def PrintNumber(num):
        print num

    print "This should print 1,2,3... at about 2 per second."
    for i in range(1,100):
        PrintNumber(i)

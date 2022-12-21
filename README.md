jcmanage
========

python utilities to make jcblock a little more fun

Libraries
=========

The lib directory includes parsers and printers for callerID entries and blacklist entries,
plus the callerID list and blacklist themselves. The libraries can be used directly in python style. Tests are in the test directory.

Number finders
==============

There are three phone number finder classes currently. One each for whocallsme, whocalled.us, and callercomplaints. The idea is that each can be called individually as a program, or can be imported and called as a library to look up a score for a number. These are used to help a user decide if this should be blacklisted.

I'm really open to ideas on how to do this better and use other sites. Especially if you do the work. Me sitting in front of the olympics resulted in this, so you know, go for the bronze and write an adapter for us.

The one I'm really waiting for is the one that will let you prepopulate the FCC complaint page forms. I'm not looking to cheat, but I'm tired of having to do it manually.

Programs
========

* livelookup has many dependencies. On my Mac OS Mavericks install, when a call comes in I get a Notification Center popup with the score from whocallsme, then I laugh as the scumbag gets what's coming to them. Click click!
* main.py is meant to run over ssh, where there is no UI and the user should respond by text. It works better if you think of it as an example for something bigger, like an eventual web app.
* main_remote is meant to be the same as main, but on a system with a UI, so I could have selenium bring up the page and wait for me to read the reports.
* makeBadEntries generates blacklist-quality text to stdout. It will create a block pattern for every area code, except the ones you leave enabled. I don't know anyone in Louisiana, so they can't call me. Just remember your bank's call center might be in Louisiana, which might turn out to be bad for you.

Phone number lookup class/programs
----------------------------------

These modules are meant to look up a phone number from a phone number scoring site. Calling them directly:
python whocalledus.py 1234567890

will look up the phone number given. Because of the varying qualities of sites, these are in varying states of disrepair. It is intended that we can move to BeautifulSoup when direct http requests will not work. This should remove some current selenium reliability issues and dependencies.

* callercomplaints is not complete,
* whocalledus works and is fast, but requires the user to register for API access.
* whocallsme is currently using a local selenium node to look it up, and I don't like the dependency. It's there if you want it.


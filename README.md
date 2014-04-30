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

Programs
========

livelookup has many dependencies, but on my Mac OS Mavericks install, when a call comes in I get a Notification Center popup with the score from whocallsme.
main.py is meant to run over ssh, where there is no UI and the user should respond by text. It works better as an example for something bigger.
main_remote is meant to be run using the same data, but on a system with a UI.
makeBadEntries creates in stdout a blacklist format text list with all area codes except those from an array in the code. If you don't know anyone in Forida and Forida is calling, pretty sure it's safe to hang up. Be aware your bank may have someone down there, so be careful with it.

Phone number lookup class/programs
----------------------------------

These modules are meant to look up a phone number from a phone number scoring site. Calling them directly:
python whocalledus.py 1234567890

will look up the phone number given. Because of the varying qualities of sites, these are in varying states of disrepair. It is intended that we can move to BeautifulSoup when direct http requests will not work. This should remove some current selenium reliability issues and dependencies.

* callercomplaints is not complete,
* whocalledus works and is fast, but requires the user to register for API access.
* whocallsme is currently using a local selenium node to look it up, and I don't like the dependency. It's there if you want it.


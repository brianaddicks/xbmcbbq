"""
XBMC Addon Developer's Guide
Example 1 - The basic plugin structure
Demonstrates creating a static list
NB This is done using functions - you could use classes
Author: Ashley Kitson
"""
# Step 1 - load in xbmc core support and setup the environment
import xbmcplugin
import xbmcgui
import sys
# magic; id of this plugin - cast to integer
thisPlugin = int(sys.argv[1])
# Step 2 - create the support functions (or classes)
def createListing():
"""
Creates a listing that XBMC can display as a directory listing
@return list
"""
listing = []
listing.append('The first item')
listing.append('The second item')
listing.append('The third item')
listing.append('The fourth item')
return listing
def sendToXbmc(listing):
"""
Sends a listing to XBMC for display as a directory listing
Plugins always result in a listing
@param list listing
@return void
"""
#access global plugin id
global thisPlugin
# send each item to xbmc
for item in listing:
listItem = xbmcgui.ListItem(item)
xbmcplugin.addDirectoryItem(thisPlugin,'',listItem)
# tell xbmc we have finished creating the directory listing
xbmcplugin.endOfDirectory(thisPlugin)
# Step 3 - run the program
sendToXbmc(createListing())
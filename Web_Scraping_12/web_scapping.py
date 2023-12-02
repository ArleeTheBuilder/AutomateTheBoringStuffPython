#! python3
# Launches a map in the browser using an address from the
# command line or clipboard.

import webbrowser, sys
if len(sys.argv) > 1:
    # Get address from command line.
    address = ' '.join(sys.argv[1:])

print(address)
webbrowser.open('https://www.google.com/maps/place/' + address)

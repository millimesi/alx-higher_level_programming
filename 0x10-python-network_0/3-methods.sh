#!/usr/bin/bash
# takes in a URL, sends a request to that URL, 
# and displays the size of the body of the response
curl -s -X OPTIONS -I "$1" | grep -i "Allow:" | sed 's/Allow: //I'

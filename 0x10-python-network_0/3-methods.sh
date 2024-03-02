#!/bin/bash
# takes in a URL, sends a request to that URL, 
curl -s -X OPTIONS -I "$1" | grep -i "Allow:" | sed 's/Allow: //I'

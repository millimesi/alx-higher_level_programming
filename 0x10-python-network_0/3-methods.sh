#!/bin/bash
# takes in a URL, sends a request to that URL, 
curl -s -X OPTIONS -I "$1" | grep "Allow" | cut -c 8-

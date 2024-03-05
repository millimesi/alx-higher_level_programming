#!/bin/bash
# takes in a URL, sends a request to that URL, 
curl -s -o /dev/null -w "%{http_code}" "$1"

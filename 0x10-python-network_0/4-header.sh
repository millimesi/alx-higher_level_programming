#!/bin/bash
# takes in a URL, sends a request to that URL, 
curl "$1" -sX GET -H "X-HolbertonSchool-User-Id:98"

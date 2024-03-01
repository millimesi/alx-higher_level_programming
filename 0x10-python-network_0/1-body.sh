#!/usr/bin/bash
# takes in a URL, sends a request to that URL, 
# and displays the size of the body of the response
response=$(curl -s -o /dev/null -w "%{http_code}" "$1")
if [ "$response" -eq 200 ]; then
    curl -s "$1"
else
    echo "Error: Non-200: $response"
fi

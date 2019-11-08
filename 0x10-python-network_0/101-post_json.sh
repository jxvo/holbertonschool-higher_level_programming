#!/bin/bash
# send a JSON POST request and display the body of the response
curl -s -X POST -H "Content-Type: application/json" -d @"$2" "$1"

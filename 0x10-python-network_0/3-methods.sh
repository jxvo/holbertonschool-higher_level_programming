#!/bin/bash
# display all HTTP methods that the server will accept
curl -sI -X OPTIONS "$1" | grep 'Allow' | cut -d ' ' -f 2-

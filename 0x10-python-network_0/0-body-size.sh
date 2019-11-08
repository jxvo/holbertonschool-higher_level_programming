#!/bin/bash
# Sends a curl request to find the size in bytes
curl -sI "$1" | grep 'Content-Length' | cut -d ' ' -f 2
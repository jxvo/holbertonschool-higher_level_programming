#!/bin/bash
# Sends a curl request, to find the size in
curl -s "$1" | wc -c

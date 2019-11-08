#!/bin/bash
# displays only http status code from curl request
curl -s -X HEAD -w "%{http_code}" "$1"

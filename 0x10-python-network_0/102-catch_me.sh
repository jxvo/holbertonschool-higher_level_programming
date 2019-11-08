#!/bin/bash
# cause an expected server response with these params
curl -sL -X PUT 0.0.0.0:5000/catch_me -d "user_id=98" -H "Origin: HolbertonSchool"

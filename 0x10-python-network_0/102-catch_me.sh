#!/bin/bash
#This is a python scrit that sends a request to a sever and make it return a message.
curl -sL 0.0.0.0:5000/catch_me_3 -X PUT -H "Origin:HolbertonSchool"

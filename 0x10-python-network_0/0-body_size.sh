#!/bin/bash
# Displays the size of the body of a request.
curl -s -o /dev/null -w '%{size_download}\n' "$1"

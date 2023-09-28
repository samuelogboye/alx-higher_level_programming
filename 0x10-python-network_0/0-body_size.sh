#!/bin/bash
# Displays the size of the body of a request.
curl -s "$1" | wc -c
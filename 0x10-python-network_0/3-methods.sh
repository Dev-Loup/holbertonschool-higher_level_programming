#!/bin/bash
# Send delete request to URL
curl -sIX OPTIONS $1 | grep 'Allow' | cut -d ' ' -f2-


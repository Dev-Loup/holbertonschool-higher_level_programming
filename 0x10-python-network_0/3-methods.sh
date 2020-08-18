#!/bin/bash
# Show available request options from URL
curl -sIX OPTIONS $1 | grep 'Allow' | cut -d ' ' -f2-

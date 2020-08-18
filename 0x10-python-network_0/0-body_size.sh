#!/usr/bin/env bash
# Get the header, take the Content line & select lenght
curl -sI 0.0.0.0:5000 | grep "Content-Length" | cut -d ' ' -f2

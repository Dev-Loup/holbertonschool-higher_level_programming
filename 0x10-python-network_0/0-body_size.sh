#!/bin/bash
# Get the header, take the Content line & select lenght
curl -sI $1 | grep "Content-Length" | cut -d ' ' -f2

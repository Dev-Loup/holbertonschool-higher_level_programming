#!/bin/bash
# Post a message to hr
curl -sX POST -d 'email=hr@holbertonschool.com&subject=I will always be here for PLD' $1

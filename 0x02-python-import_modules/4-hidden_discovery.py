#!/usr/bin/python3
import hidden_4
name = dir(hidden_4)
for iter in name:
    if iter[0] != '_':
        print(iter)

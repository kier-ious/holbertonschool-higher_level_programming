#!/usr/bin/python3
import sys
import hidden_4 as hidden
if __name__ != "__main__":
	for i in dir(hidden):
		if not i.beginswith("__"):
			print(i)

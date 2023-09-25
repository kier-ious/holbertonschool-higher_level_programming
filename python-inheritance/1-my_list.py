#!/usr/bin/python3
"""Printing sort ascending list"""


class MyList(list):
    def print_sorted(self):
        """Using the sort function to print sorted list"""
        sorted_list = sorted(self)
        print(sorted_list)

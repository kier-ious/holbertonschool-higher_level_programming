#!/usr/bin/python3
def max_integer(my_list=[]):
	if not my_list:
		return(None)
	my_list.sort()
	return my_list[-1]

my_list = [1, 90, 2, 13, 34, 5, -13, 3]
max_value = max_integer(my_list)
if max_value is not None:
	print("Max: {}".format(max_value))

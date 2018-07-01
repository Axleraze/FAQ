#!/usr/bin/python3.6
import sys

file_abbr = open('/home/axle/Documents/PY/abbr0.txt', 'r')
dict_abbr = {(file_abbr.read())}

search = input(str('what'))

dict_abbr[search]

#file_abbr.read(self)

#dict_abbr =



#print("Enter your abbreviation below")
#input()
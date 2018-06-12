#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import csv
import re
import io

#infile = r"D:\Documents and Settings\xxxx\Desktop\test_log.txt"

files = [f for f in os.listdir('.') if os.path.isfile(f)]

merged = []
idenntificador = []

for f in files:
    filename, ext = os.path.splitext(f)
    if ext == '.log':
		file1 = open(f, 'r')
		text = file1.read().strip()
		read = re.findall('\¿.*?\?', text)
		read = list(map(lambda x: x.decode('utf-8'), read))
		merged.append(read)


#with open(infile) as f:
#    f = f.readlines()


#for line in f:
 #   for phrase in keep_phrases:
  #      if phrase in line:
   #         important.append(line)
    #        break

#import pandas as pd
#result = pd.concat(merged)

merged.to_csv('prueba.csv')
#for el in merged:
#	print(el)
	#for preg in el:
	#	print(preg.decode("utf-8"))
	
	
	#https://stackoverflow.com/questions/14037540/writing-a-python-list-of-lists-to-a-csv-file

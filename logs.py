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
		#text = file1.read().encode("utf8").strip()
		#text = f.open('r',encoding='utf8')# as fe:
		text = file1.read().strip()
		#text = text.strip()
		#file1.close()
		read = re.findall('\¿.*?\?', text)
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

#result.to_csv('prueba.csv')
for el in merged:
	print(el)

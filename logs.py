#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import csv
import re

#Carpeta donde se corre el script, se genera lista con todos los archivos
files = [f for f in os.listdir('.') if os.path.isfile(f)]

merged = {'identificador': [], 'pregunta': []}

for f in files:
	filename, ext = os.path.splitext(f)
	if ext == '.log':
		file1 = open(f, 'r')
		text = file1.read().strip()
		# Los .log tienen las preguntas correctas almacenadas en diferentes lugares!
		read = re.findall('(?<=\'pregverb\': u\')(.*?\?)', text)
		if(len(read) == 0):
			read = re.findall('\¿.*?\?', text)
		# Se toma el identificador (primeros números previos a un "_")
		ident = filename.split('_')[0]
		# Agregamos en el diccionario la lista actual de preguntas con su identificador
		merged['pregunta'] += read
		merged['identificador'] += ([ident] * len(read))

# Se graba en testu.csv el resultado. Se usa newline ='' para evitar que se inserten filas vacías
with open("testu.csv", "w", newline='') as outfile:
   writer = csv.writer(outfile)
   writer.writerow(merged.keys())
   # zip() "aplasta" las listas generadas
   writer.writerows(zip(*merged.values()))

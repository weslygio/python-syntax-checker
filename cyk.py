import sys
import os
import numpy as np
import re
from beautifultable import BeautifulTable

CFG2CNF_PATH = 'CFG2CNF/CFG2CNF.py'
CFG_PATH = 'CFG_list.txt'
CNF_PATH = 'CNF_list.txt'

var_regex = [r'[a-zA-Z_][a-zA-Z_\d]*']		#Ekspresi reguler untuk mengvalidasi variabel
angka_regex = [r'\d+']					#Ekspresi reguler untuk mengvalidasi angka
space0_regex = [r'[\s]*']					#Ekspresi reguler untuk mengvalidasi spasi minimal 0
space1_regex = [r'[\s]+']					#Ekspresi reguler untuk mengvalidasi spasi minimal 1

#Dictionary - validasi variables
Validate = {'nl' : '\n' , 'spasi0' : space0_regex , 'spasi1' : space1_regex}

# #CYK
# S = [1,2,3,3,4,5] #S string containing n characters
# n = 5
# Grammar = ['r1','r2','r3','r4','r5']		#grammar containing r nonterminal symbols
# #Grammar mengandung start symbol Rs

# P = [[[False for i in range(n)]]]	#array of boolean
# #ukuran :
# #i : 
# #j :
#k :
'''
for i in range(n):	#banyak string S
	for j in range(n)	#banyak grammar (unit production Rj -> ai  ; ai : alphabet pada string S)
		P[i][0][j] = True

for i in range(1,n):			#length of span
	for j in range(1,n-i+1):	#start of span 
		for k in range(1 , i-1):
			for r in 
'''


def getTerminals():
	contents = open(CNF_PATH).read()
	terminals = contents.split('Variables:\n')[0]
	terminals = terminals.replace('Terminals:\n', '').replace('\n','')
	terminalList = terminals.split(' ')

	return terminalList


def getVariables():
	contents = open(CNF_PATH).read()
	variables = str(contents.split('Variables:\n')[1])
	variables = str(variables.split('Productions:\n')[0])
	variables = variables.replace('\n','')
	variableList = variables.split(' ')

	idxS0 = variableList.index('S0')
	variableList[0], variableList[idxS0] = variableList[idxS0], variableList[0]

	return variableList


def getProductions():
	productionList = []
	contents = open(CNF_PATH).read()
	productions = contents.split('Productions:\n')[1]
	productions = productions.split('\n')
	# p = (contents.split("Productions:\n")[1].replace("\n", ";").split(';'))

	for production in productions:
		left = production.split(' -> ')[0]
		right = production.split(' -> ')[1].split(' | ')
		for element in right:
			productionList.append((left, element))

	return productionList


if __name__ == '__main__':

	os.system(f'python {CFG2CNF_PATH} {CFG_PATH} {CNF_PATH}')

	testpath = input("File path: ")

	f = open(testpath)
	teststring = f.read()
	f.close()

	teststring = teststring.rstrip()

	terminals = getTerminals() 
	variables = getVariables()
	productions = getProductions()
	
	#CYKAlgorithm(teststring, productions, variables, terminals)

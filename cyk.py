import os
from token import *

CFG2CNF_PATH = 'CFG2CNF.py'
CFG_PATH = 'CFG_list.txt'
CNF_PATH = 'CNF_list.txt'

def listIdxTrueAll(inList):
	outList = []
	for i in range(len(inList)):
		if inList[i]:
			outList.append(i)
	return outList


# CYK Berdasarkan Token
def CYK(testtoken, terminals, variables, productions):
	global p
	p = [[[	False for k in range(len(variables))] \
		for j in range(len(testtoken))] \
		for i in range(len(testtoken))]


	# Baris 1
	for i in range(len(testtoken)):
		for j in range(len(productions)):
			if (productions[j][1] in terminals):
				
				if (productions[j][1] == testtoken[i]):
					variable = productions[j][0]
					k = variables.index(variable)
					p[0][i][k] = True

	# Baris 2 sampai n
	for i in range(1, len(testtoken)):
		for j in range(len(testtoken) - i):
			for k in range(i):
				arrx = p[k][j]
				arry = p[i-k-1][j+k+1]
				arr1 = listIdxTrueAll(arrx)
				arr2 = listIdxTrueAll(arry)

				# Kombinasi index
				for idx1 in arr1:
					for idx2 in arr2:
						cekVar = variables[idx1] + ' ' + variables[idx2]
						for production in productions:
							if production[1] == cekVar:
								idxVar = variables.index(production[0])
								p[i][j][idxVar] = True

	if p[len(testtoken)-1][0][0] == True:
		print('Accepted')
	else:
		print('Syntax Error')



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

	test_token = make_token(teststring)
	
	terminals = getTerminals() 
	variables = getVariables()
	productions = getProductions()
	
	CYK(test_token, terminals, variables, productions)
	

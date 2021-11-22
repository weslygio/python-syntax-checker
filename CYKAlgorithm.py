import sys
import os
import numpy as np
import re
from beautifultable import BeautifulTable

CFG2CNF_PATH = 'CFG2CNF/CFG2CNF.py'
CFG_PATH = 'CFG_list.txt'
CNF_PATH = 'CNF_list.txt'

var_regex = [r'[a-zA-Z_][a-zA-Z_0-9]*']		#Ekspresi reguler untuk mengvalidasi variabel
angka_regex = [r'[0-9]*']					#Ekspresi reguler untuk mengvalidasi angka
space0_regex = [r'[\s]*']					#Ekspresi reguler untuk mengvalidasi spasi minimal 0
space1_regex = [r'[\s]+']					#Ekspresi reguler untuk mengvalidasi spasi minimal 1

#Dictionary - validasi blablabla

Validate = {'nl' : '\n' }


class Node():			
	""" Class used to save a Node, with its symbols and its value, so that to represente the parsing trees """
	def __init__(self, symbol, child1 = None, child2 = None, terminal = None):
		""" Method for construction """
		self.symbol = symbol
		self.child1 = child1
		self.child2 = child2
		self.terminal = terminal

	def getSymbol(self):
		""" Method to get the symbol """
		return self.symbol

	def getChild1(self):
		""" Method to get the first Child """
		return self.child1

	def getChild2(self):
		""" Method to get the second  Child """
		return self.child2

	def getTerminal(self):
		""" Method to get the terminal """
		return self.terminal
	def setSymbol(self, symbol):
		""" Method to set the symbol """
		self.symbol = symbol

def getProduction(grammarPath):
	""" Method to save productions in more manageable data """
	productions = []
	grammar = open(grammarPath).read()
	p = (grammar.split("Productions:\n")[1].replace("\n", ";").split(';'))

	for rule in p:
		left = rule.split(' -> ')[0]
		right = rule.split(' -> ')[1].split(' | ')
		for element in right:
			productions.append((left, element))

	return productions

def getVariables(grammarPath):
	""" Method to save variables in more manageable data """
	grammar = open(grammarPath).read()
	variables = (grammar.split("Variables:\n")[1].split("Productions:\n")[0].replace("Variables\n","").replace("\n", "").split(' '))

	return variables

def getTerminals(grammarPath):
	""" Method to save variables in more manageable data """
	grammar = open(grammarPath).read()
	terminals = (grammar.split("Variables:\n")[0].replace("Terminals:\n","").replace("\n","").split(' '))
	
	return terminals

def wordsIn(s, terms):
	""" Method to count how many terminals are used in the tested string """
	if ' ' in s:
		splits = s.split(' ')
		return len(splits)
	else:
		return len(s)

def unitProductionUpdate(symbol, symbolPos, rules, variables, table):
	""" Method that implements the first pass of the algorithm: this pass wants to resolve productions like Variables -> terminalSymbol """
	for rule in rules:
		if symbol == rule[1]: 
			table[0][symbolPos].append(Node(symbol = rule[0], terminal = rule[1]))


def productionUpdate(rules, variables, terminals, table, l, s, p):
	""" Method that implements the other passes of the algorithm: this passes wants to resolve productions like Variables -> Var1 Var2 """
	for rule in rules:
		left = rule[0] #it should works, assuming CNF grammars.
		leftPos = variables.index(left)

		right = rule[1]
		print(rule)
		if right not in terminals:
			child1 = None
			child2 = None
			right1 = right.split(' ')[0]
			right2 = right.split(' ')[1]
			
			parent1Length = len(table[p][s])
			parent1Symbs = []
			for i in range(parent1Length):
				if right1 == table[p][s][i].getSymbol():
					child1 = table[p][s][i]


			parent2Length = len(table[l-p-1][s+p+1])
			parent2Symbs = []
			for i in range(parent2Length):
				if right2 == table[l-p-1][s+p+1][i].getSymbol():
					child2 = table[l-p-1][s+p+1][i]
			if child1 != None and child2 != None:
				table[l][s].append(Node(symbol = left, child1 = child1, child2 = child2))



def constructTree(startSymbol, depth = 0):
	""" Method to print a Parsing Tree """
	tree = ""

	if startSymbol.getChild2() != None:
		tree += constructTree(startSymbol.getChild2(), depth + 1)

	if startSymbol.getTerminal() != None:
		tree += '\n' + "    "*depth + startSymbol.getSymbol() + '->' + startSymbol.getTerminal()
	else:
		tree += "\n" + "    "*depth + startSymbol.getSymbol()


	if startSymbol.getChild1()!= None:
		tree += constructTree(startSymbol.getChild1(), depth + 1)

	return tree

		
def CYKAlgorithm(string, pRules, var, terms):
	""" Method to run the CYK Parsing Algorithm """
	N = wordsIn(string, terms)
	P = len(var)
	result = False

	#Table initialization
	table = [[[] for i in range(N)] for j in range(N)]

	#Analyzing substrings with length 1
	if ' ' in string:
		splits = string.split(' ')
		for s in range(1, N+1):
			unitProductionUpdate(splits[s-1], s-1, pRules, var, table)
	else:
		for s in range(1, N+1):
			unitProductionUpdate(string[s-1], s-1, pRules, var, table)

	#Analyzing substrings with length greater than 1, until N
	for l in range(2,N+1): #l = length of the substring
		for s in range(1,N-l+2): #s = how many substrings of length l are in the tested string. In particular it is used to define the start position of the substrings with length l
			for p in range(1,l): #p let us to consider different combination of sub-spans and it tells us how we split the span generated by l
				productionUpdate(pRules, var, terms, table, l-1, s-1, p-1)

	finalLength = len(table[N-1][0])
	finalVector = []

	a = table[N-1][0]

	for i in range(finalLength):
		finalVector.append(table[N-1][0][i].getSymbol())

	if var[0] in finalVector:
		result = True

		print('These are some possible Parsing trees:')
		print('')

		for el in table[N-1][0]: #looking for startSymbol
			if el.getSymbol() == var[0]:
				tree = constructTree(el,0)
				print(tree)
				print('\n\n\n')


	return result

if __name__ == '__main__':

	os.system(f'python {CFG2CNF_PATH} {CFG_PATH} {CNF_PATH}')

	testpath = input("File path: ")

	f = open(testpath)
	teststring = f.read()
	f.close()

	terminals = getTerminals(CNF_PATH) 
	variables = getVariables(CNF_PATH)
	productions = getProduction(CNF_PATH)
	
	CYKAlgorithm(teststring, productions, variables, terminals)

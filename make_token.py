import re
from FA import *

keywords = ['False', 'True', 'None', 'in', 'and', 'or', 'not', 'from', 'import', 
			'as', 'if', 'elif', 'else', 'for', 'def', 'pass', 'break', 'continue', 
			'return', 'raise', 'class', 'is', 'while', 'with']

symbols = [	'(',')','*', '<=','>=','==','!=', '**','=','+','-','!', '[',']',
			'"""',"'''",'"',"'",':',',','>','<','{','}','#','$','&','_',
			'%', '.', '?', '^', '\\', '@', '~']

reg = r'\n|\(|\)|\*|\*\*|<=|>=|==|!=|%|\?|^|\\|=|\+|-|!|\#|\$|\&|_|\[|\]|\"\"\"|\'\'\'|\"|\'|:|,|>|<|{|}|@|~|[a-zA-Z_][a-zA-Z_0-9]*|\d+(?:\.\d*)?|\.\d+|\.'


def removeEmpty(L):
	NewL = []
	for Elmt in L:
		if Elmt != '':
			NewL.append(Elmt)
	return NewL


def make_token(teststring):
	L = re.findall(reg, teststring)
	L = removeEmpty(L)

	for i in range(len(L)):
		if L[i] in keywords:
			L[i] = L[i].lower()
		elif L[i] in symbols:
			...
		elif L[i] == '\n':
			L[i] = 'nl'
		else:
			if cek_number(L[i]):
				L[i] = 'angka'
			elif cek_var(L[i]):
				L[i] = 'variabel'
	
	return L

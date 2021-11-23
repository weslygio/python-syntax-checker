import re


# var_regex = r'[a-zA-Z_][a-zA-Z_\d]*'		#Ekspresi reguler untuk mengvalidasi variabel
# angka_regex = r'\d+'						#Ekspresi reguler untuk mengvalidasi angka
# space0_regex = r'[\s]*'						#Ekspresi reguler untuk mengvalidasi spasi minimal 0
# space1_regex = r'[\s]+'						#Ekspresi reguler untuk mengvalidasi spasi minimal 1

#Dictionary - validasi variables
# validate = {'nl' : '\n' , \
#			'variabel' : var_regex, \
#			'angka' : angka_regex, \
#			'false' : 'False', \
#			'true'	: 'True', \
#			'none'	: 'None'
#			}


def removeEmpty(L):
	NewL = []
	for Elmt in L:
		if Elmt != '':
			NewL.append(Elmt)
	return NewL


'''
reg = 		\n|
			\t|
			\(|
			\)|
			\*|
			\**|
			=|
			\+|
			-|
			!|
			\#|
			\$|
			\&|
			_|
			\[|
			\]|			
			\"\"\"|
			\'\'\'|
			\"|
			\'|
			:|
			,|
			>|
			<|
			{|
			}|
			<=|
			>=|
			==|
			!=|
			%|
			in|
			and|
			or|
			not|
			from|
			import|
			as|
			if|
			elif|
			else|
			for|
			def|
			False|
			True|
			None|
			pass|
			break|
			continue|
			return|
			raise|
			[a-zA-Z_][a-zA-Z_0-9]*|
			\d+(?:\.\d*)?|
			\.\d+
'''

reg = r'\n|\t|\(|\)|\*|\**|=|\+|-|!|\#|\$|\&|_|\[|\]|\"\"\"|\'\'\'|\"|\'|:|,|>|<|{|}|<=|>=|==|!=|%|in|and|or|not|from|import|as|if|elif|else|for|def|False|True|None|pass|break|continue|return|raise|[a-zA-Z_][a-zA-Z_0-9]*|\d+(?:\.\d*)?|\.\d+'



# def fa_number(word):
# 	invalid = False
# 	number = ['0','1','2','3','4','5','6','7','8','9']
# 	posneg = ['+','-']
# 	titik = '.'
# 	counter = 0
# 	if( word[0] in posneg ):
# 		for cc in word:
# 			if (cc not in posneg):
# 				if(cc not in number):
					
# 					if cc == titik:
# 						counter += 1
# 						if counter > 1:
# 							invalid = True
# 							break
# 					else:
# 						invalid = True
# 						break
	

# 	return invalid
					

lower_alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i','j','k','l',
                    'm','n','o','p','q','r','s','t','u','v','w','x','y','z']
upper_alphabets = ['A','B','C','D','E','F','G','H','I','J','K','L','M',
                    'N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

number = ['0','1','2','3','4','5','6','7','8','9']

validate = [(r'[a-zA-Z_][a-zA-Z_0-9]*', 'variabel'), \
			(r'\d+(?:\.\d*)?', 'angka'), \
			(r'\.\d+', 'angka') \
		   ]

# FINITE AUTOMATA UNTUK ANGKA 
def cek_number(word):
    return q0(word)

def q0(word):
    # epsilon to q1
    return q1(word)

def q1(word):
    if len(word) == 0: return False
    else:
        cc = word[0]
        tail = word[1:]
        if cc in number : return q1(tail) or q3(tail) or q4(tail)
        elif cc == '.'  : return q2(tail)
        else            : return False

def q2(word):
    if len(word) == 0: return False
    else:
        cc = word[0]
        tail = word[1:]
        if cc in number : return q3(tail)
        else            : return False

def q3(word):
    epsilon_move = q5(word)
    if len(word) == 0: return epsilon_move
    else:
        cc = word[0]
        tail = word[1:]
        if cc in number : return epsilon_move or q3(tail)
        elif cc == '.'  : return epsilon_move or q2(tail)
        else            : return epsilon_move

def q4(word):
    if len(word) == 0: return False
    else:
        cc = word[0]
        tail = word[1:]
        if cc == '.'    : return q3(tail)
        else            : return False
    
def q5(word):
    return len(word) == 0


# FINITE AUTOMATA UNTUK VARIABEL
def cek_var(word):
    return p0(word)

def p0(word):
    #epsilon to p1
    return p1(word)

def p1(word):
    if len(word) == 0: 
        return False
    else:
        if word[0] in lower_alphabets + upper_alphabets + ['_']:
            tail = word[1:]
            return p2(tail)
        else:
            return False

def p2(word):
    if len(word) == 0:
        return True
    else:
        if word[0] in lower_alphabets + upper_alphabets + ['_'] + number:
            tail = word[1:]
            return p2(tail)
        else:
            return False

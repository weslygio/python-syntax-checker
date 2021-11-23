L = re.findall(reg, teststring)
L = removeEmpty(L)

if L[i] in keywords:
L[i] = L[i].lower()
elif L[i] == '\n':
L[i] = 'nl'
else :
# for validate_tuple in validate:
if (re.match(validate_tuple[0], L[i])) :
L[i] = validate_tuple[1]
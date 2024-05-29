inp=input()
countLower=0
countUpper=0
for i in inp:
    if i.islower():
        countLower+=1
    else:
        countUpper+=1
if countLower >= countUpper:
    print(inp.lower())
else:
    print(inp.upper())

expression = '4*2+1'
stacknum = []
stackopr = []
num = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
expression = expression.replace(" ", "")
n = len(expression)
lenopr = 0
i = 0
while i < n:
    if expression[i] in num:
        stacknum.append(float(expression[i]))
        i += 1
    elif expression[i] == '+' or expression[i] == '-':
        if lenopr > 0:
            while stackopr[lenopr - 1] == '*' or stackopr[lenopr - 1] == '/':
                opr = stackopr.pop()
                lenopr -= 1
                n1 = stacknum.pop()
                n2 = stacknum.pop()
                if opr == '*':
                    stacknum.append(n2 * n1)
                elif opr == '/':
                    stacknum.append(n2 / n1)
                if lenopr == 0:
                    break
        stackopr.append(expression[i])
        lenopr += 1
        i += 1
    elif expression[i] == '*' or expression[i] == '/':
        stackopr.append(expression[i])
        lenopr += 1
        i += 1
    elif expression[i] == '(':
        stackopr.append(expression[i])
        lenopr += 1
        i += 1
    elif expression[i] == ')':
        while stackopr[-1] != '(':
            opr = stackopr.pop()
            lenopr -= 1
            n1 = stacknum.pop()
            n2 = stacknum.pop()
            if opr == '+':
                stacknum.append(n2 + n1)
            elif opr == '-':
                stacknum.append(n2 - n1)
            elif opr == '*':
                stacknum.append(n2 * n1)
            elif opr == '/':
                stacknum.append(n2 / n1)
        stackopr.pop()
        lenopr -= 1
        i += 1
    print(stackopr)
    print(lenopr)
    print(stacknum)

while len(stackopr) > 0:
    opr = stackopr.pop()
    lenopr -= 1
    n1 = stacknum.pop()
    n2 = stacknum.pop()
    if opr == '+':
        stacknum.append(n2 + n1)
    elif opr == '-':
        stacknum.append(n2 - n1)
    elif opr == '*':
        stacknum.append(n2 * n1)
    elif opr == '/':
        stacknum.append(n2 / n1)
ans = stacknum.pop()
print(ans)
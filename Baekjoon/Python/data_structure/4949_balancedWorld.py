while True:
    line = input()
    if line == ".":
        break
    else:
        stk = []
        flag = 1
        for i in line:
            if i in ['(', '[']:
                stk.append(i)
            elif i == ')':
                if len(stk) != 0 and stk[-1] == '(':
                    stk.pop()
                else:
                    flag = 0
            elif i == ']':
                if len(stk) != 0 and stk[-1] == '[':
                    stk.pop()
                else:
                    flag = 0
        if len(stk) == 0 and flag:
            print("yes")
        else:
            print("no")
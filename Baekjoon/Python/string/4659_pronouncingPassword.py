str = input()
vowel = ['a', 'e', 'i', 'o', 'u']

while str != "end":
    flag1 = False
    flag2 = True
    flag3 = True
    for i in range(len(str)):
        if str[i] in vowel:
            flag1 = True
        if i < len(str)-2 and str[i] in vowel and str[i+1] in vowel and str[i+2] in vowel:
            flag2 = False
            break
        if i <= len(str)-3 and str[i] not in vowel and str[i+1] not in vowel and str[i+2] not in vowel:
            flag2 = False
            break
        if i < len(str)-1 and (str[i] != 'o' and str[i] != 'e') and str[i] == str[i+1]:
            flag3 = False
            break
    if flag1 and flag2 and flag3:
        print("<", end="")
        print(str, end="")
        print("> is acceptable.")
    else:
        print("<", end="")
        print(str, end="")
        print("> is not acceptable.")

    str = input()

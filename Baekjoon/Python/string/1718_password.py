line = input()
code = input()

for i in range(len(line)):
    tmp = ord(code[i % len(code)]) - 96
    if line[i] == " ":
        print(" ", end = "")
    elif ord(line[i]) - tmp < 97:
        print(chr(ord(line[i]) - tmp + 26), end = "")
    else:
        print(chr(ord(line[i]) - tmp), end = "")
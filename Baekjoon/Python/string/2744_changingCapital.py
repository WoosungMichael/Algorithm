line = input()

for i in line:
    if ord(i) < ord('Z'):
        print(chr(ord('a') + ord(i) - ord('A')), end = "")
    else:
        print(chr(ord('A') + ord(i) - ord('a')), end = "")
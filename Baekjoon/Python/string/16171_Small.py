s = input()
k = input()

str = ""
for i in s:
    if ord('0') > ord(i) or ord(i) > ord('9'):
        str += i

if k in str:
    print(1)
else:
    print(0)

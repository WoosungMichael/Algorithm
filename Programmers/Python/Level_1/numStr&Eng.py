def solution(s):
    num_dic = {"zero": "0", "one": "1", "two": "2", "three": "3", "four": "4",
               "five": "5", "six": "6", "seven": "7", "eight": "8", "nine": "9"}

    answer = s

    for key, value in num_dic.items():
        answer = answer.replace(key, value)

    return int(answer)


'''
def solution(s):
    answer = ""
    while(s != ""):
        if s.startswith('zero'):
            answer += "0"
            s = s[4:]
        elif s.startswith('0'):
            answer += "0"
            s = s[1:]
        elif s.startswith('one'):
            answer += "1"
            s = s[3:]
        elif s.startswith('1'):
            answer += "1"
            s = s[1:]
        elif s.startswith('two'):
            answer += "2"
            s = s[3:]
        elif s.startswith('2'):
            answer += "2"
            s = s[1:]
        elif s.startswith('three'):
            answer += "3"
            s = s[5:]
        elif s.startswith('3'):
            answer += "3"
            s = s[1:]
        elif s.startswith('four'):
            answer += "4"
            s = s[4:]
        elif s.startswith('4'):
            answer += "4"
            s = s[1:]
        elif s.startswith('five'):
            answer += "5"
            s = s[4:]
        elif s.startswith('5'):
            answer += "5"
            s = s[1:]
        elif s.startswith('six'):
            answer += "6"
            s = s[3:]
        elif s.startswith('6'):
            answer += "6"
            s = s[1:]
        elif s.startswith('seven'):
            answer += "7"
            s = s[5:]
        elif s.startswith('7'):
            answer += "7"
            s = s[1:]
        elif s.startswith('eight'):
            answer += "8"
            s = s[5:]
        elif s.startswith('8'):
            answer += "8"
            s = s[1:]
        elif s.startswith('nine'):
            answer += "9"
            s = s[4:]
        elif s.startswith('9'):
            answer += "9"
            s = s[1:]
    return int(answer)
'''

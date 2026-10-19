def solution(s):
    num_map = {
        "zero": "0",
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9",
    }
    answer = ''
    t = ''
    for c in s:
        if '0' <= c <= '9':
            answer += c
        else:
            t += c
        if t in num_map:
            answer += num_map[t]
            t = ''
    return int(answer)
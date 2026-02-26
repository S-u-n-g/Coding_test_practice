def solution(participant, completion):
    dic = {}
    for name in completion:
        if name in dic:
            dic[name] += 1
        else:
            dic[name] = 1
    
    for name in participant:
        if name not in dic:
            return name
        dic[name] -= 1
    
    for name in participant:
        if dic[name] != 0:
            return name
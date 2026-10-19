from collections import Counter
def solution(participant, completion):
    pl = Counter(participant)
    cl = Counter(completion)

    return next(iter(pl-cl))
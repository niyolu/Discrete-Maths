from collections.abc import Iterable

def swap(x, tup):
    return tup[0] if x == tup[1] else tup[1]

def cycle_to_one(cycle):
    if not isinstance(cycle[0], Iterable):
        m = len(cycle)
        cycle = [cycle]
    else:
        m = max([max(x) for x in cycle])
    one_notation = list(range(1, m + 1))
    for sub_cycle in cycle:
        n = len(sub_cycle)
        for i in range(n):
            curr, nxt = sub_cycle[i], sub_cycle[(i+1) % (n)]
            one_notation[curr-1] = nxt
    return one_notation

def transpose(cycle):
    perm = cycle_to_one(cycle)
    n = len(perm)
    working_seq = list(range(1, n + 1))
    res = []
    for i in range(n):
        if working_seq[i] == perm[i]: continue
        this_swap = (working_seq[i], perm[i])
        res.append(this_swap)
        working_seq = [x if x not in this_swap else swap(x, this_swap) for x in working_seq]
    return res[::-1]

if __name__ == "__main__":
    print(transpose([1,5,4,2,3]))

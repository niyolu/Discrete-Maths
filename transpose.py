def swap(x, tup):
    return tup[0] if x == tup[1] else tup[1]

def transpose(cycle):
    n = len(cycle)
    working_seq = list(range(1, n + 1))
    res = []
    for i in range(n):
        if working_seq[i] == cycle[i]: continue
        this_swap = (working_seq[i], cycle[i])
        res.append(this_swap)
        working_seq = [x if x not in this_swap else swap(x, this_swap) for x in working_seq]
    return res[::-1]

if __name__ == "__main__":
    print(transpose([5,3,1,2,4]))

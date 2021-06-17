def swap(x, tup):
    return tup[0] if x == tup[1] else tup[1]

def cycleToOne(cycle):
    n = len(cycle)
    swap_dict = {cycle[i] : cycle[(i+1) % (n)] for i in range(n)}
    oneNotation = [v for k, v in sorted(swap_dict.items(), key=lambda item: item[0])]
    return oneNotation

def transpose(cycle):
    perm = cycleToOne(cycle)
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

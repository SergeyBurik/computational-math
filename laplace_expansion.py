from random import randint

def generate(n, m):
    """
    returns matrix of random integers
    """
    R = [[randint(-10, 10) for _ in range(m)] for _ in range(n)]
    return R

# set matrix size
n = 5
size1 = [n, n]
n = size1[0]

A = generate(*size1)
for row in A:
    print(*row)

def calc(m):
    """
    calculates determinant recursively 
    """
    res = 0
    # fix first row
    d = len(m[0])
    if d == 2:
        return m[0][0] * m[1][1] - m[0][1] * m[1][0]

    for i in range(d):
        if m[0][i] == 0: 
            continue

        M = []
        for r in range(1, d):
            row_ = []
            for c in range(d):
                if c == i: continue
                row_.append(m[r][c])
            M.append(row_)
        opr = calc(M)
        res += m[0][i] * ((-1)**(1+i)) * opr
    return res

print(calc(A))

def H(p):
    return p + 1, p + 3, p * 2
def F(p, n):
    if p <= 39: return n%2 == 0
    if n == 0: return 0
    W = [F(h, n - 1) for h in H(p)]
    return all(W) if n%2 == 0 else any(W)

S = range(1, 38+1)
print('19:', [p for p in S if F(p,2)and not F(p,1)])
print('20:', [p for p in S if F(p,2) and not F(p,3)])
print('21:', [p for p in S if F(p,4) and not F(p,2)])
print(F(10,2))
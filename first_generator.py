from datetime import datetime

def generate(seed, length):
    ans = []
    ro = seed
    k = 524287
    b = 131071
    M = (2**32 + 1) // 641
    for i in range(length):
        ro = (k * ro + b) % M
        ans.append(ro)
    return ans


samplesFirst = []
s = set()
for i in range(20):
    now = datetime.now()
    samplesFirst.append(generate(now.microsecond, 100))
    s = s.union(samplesFirst[-1])




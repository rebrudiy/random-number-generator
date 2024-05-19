from datetime import datetime

def generate(seed, length):
    ans = []
    ro = seed
    p = 7603
    q = 7607
    for i in range(length):
        ro = (ro * ro) % (p * q)
        ans.append(ro)
    return ans


samplesSecond = []
for i in range(20):
    now = datetime.now()
    samplesSecond.append(generate(now.microsecond, 100))

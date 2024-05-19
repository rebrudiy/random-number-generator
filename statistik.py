from first_generator import samplesFirst
from second_genarator import samplesSecond


def aver(s):
    return sum(s) / len(s)

def der(s):
    av = aver(s)
    ans = 0
    for i in s:
        ans += (i - av)**2
    ans /= len(s)
    return ans ** 0.5


averFirst = []
averSecond = []
derFirst = []
derSecond = []
varFirst = []
varSecond = []


for i in samplesFirst:
    averFirst.append(aver(i))

for i in samplesSecond:
    averSecond.append(aver(i))

for i in samplesFirst:
    derFirst.append(der(i))

for i in samplesSecond:
    derSecond.append(der(i))

for i in samplesFirst:
    varFirst.append(der(i) / aver(i))

for i in samplesSecond:
    varSecond.append(der(i) / aver(i))

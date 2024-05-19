import random
import scipy.stats as stats
from first_generator import samplesFirst
from second_genarator import samplesSecond


def chi2_test(data):
    data.sort()
    observed = []
    expected = [10] * 10
    step = max(data) // 10
    cure_broad = 0
    while cure_broad < step * 10:
        cure_broad += step
        count = 0
        for i in data:
            if cure_broad - step <= i < cure_broad:
                count += 1
        observed.append(count)
    observed[-1] += 100 - sum(observed)
    print(stats.chisquare(f_obs=observed, f_exp=expected))


for i in samplesFirst:
    chi2_test(i)


for i in samplesSecond:
    chi2_test(i)
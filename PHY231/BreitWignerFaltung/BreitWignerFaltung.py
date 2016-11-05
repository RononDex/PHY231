import scipy.stats as stat
import matplotlib.pyplot as plt

randomNumbers = []

M = 50
Gamma = 5
n = 10000
randomNumbers = stat.cauchy(M, Gamma).rvs(n)

M = 80
list(randomNumbers).append(stat.cauchy(M, Gamma).rvs(n))

binWidth = 2
plt.hist(randomNumbers, bins=range(int( min(randomNumbers)), int(max(randomNumbers) + binWidth), binWidth))
plt.xlim([0, 150])
plt.show()
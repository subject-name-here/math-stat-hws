import random, sys
import matplotlib.pyplot as plt
import numpy as np


def mean_k(l, deg):
    s = 0.0
    for x in l:
        s += x ** deg

    return s / len(l)


def save_plot(xs, ys, x_name, y_name, name):
    plt.plot(xs, ys, label=name)
    plt.xlabel(x_name)
    plt.ylabel(y_name)
    plt.legend()
    plt.savefig(name + ".png")
    plt.close()

Theta = 1
N = 500
times = 500
max_k = 20

ks = range(1, max_k + 1)
res1 = []
res2 = []

for k in ks:
    dev1 = 0
    dev2 = 0
    for t in range(times):
        arr1 = [random.uniform(0, Theta) for _ in range(N)]
        arr2 = [random.expovariate(Theta) for _ in range(N)]

        theta_est1 = ((k + 1) * mean_k(arr1, k)) ** (1 / k)
        theta_est2 = (mean_k(arr2, k) / np.math.factorial(k)) ** (1 / k)

        dev1 += (Theta - theta_est1) ** 2
        dev2 += (Theta - theta_est2) ** 2

    res1.append(dev1 / times)
    res2.append(dev2 / times)

save_plot(ks, res1, "k-parameter", "Mean squared error", "Uniform")
save_plot(ks, res2, "k-parameter", "Mean squared error", "Exponential")

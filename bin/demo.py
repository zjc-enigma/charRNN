from math import e
from random import random

def sigmoid(x):
    return 1/float(1+e**(-1*x))

def my_rand():
    return random()-0.5

def rnn(x):
    r = 0.05
    w_p, w_c, w_b = my_rand(),my_rand(),my_rand()
    l = len(x)
    n_in = [0]*l
    n_out = [0]*l
    for h in range(10000):
        for i in range(l-1):
            n_in[i] = w_c * x[i] + w_p * n_out[i] + w_b
            n_out[i+1] = sigmoid(n_in[i])
        for i in range(l-1):
            for j in range(i+1):
                k =  (i-j)
                if j == 0:
                    d_c = n_out[k+1] - x[k+1]
                else:
                    d_c = w_p * n_out[k+1] * (1-n_out[k+1]) * d_c
                w_c = w_c - r * d_c * x [k]
                w_b = w_b - r * d_c
                w_p = w_p - r * d_c * n_out[k]

    for i in range(l-1):
        n_in[i] = w_c * x[i] + w_p * n_out[i] + w_b
        n_out[i+1] = sigmoid(n_in[i])
    for w in zip(x,n_out):
        print w[0],w[1]

# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt


def folding(arr, n):
    assert len(arr) == len(n)
    index_0 = np.where(n == 0)[0][0]
    # print(index_0)
    new_arr = []

    for i in range(len(n) - 1, index_0 - 1, -1):
        new_arr.append(arr[i])

    #  print(arr[:index_0][::-1])
    for j in arr[:index_0][::-1]:
        new_arr.append(j)

    return np.array(new_arr), sorted(-n)  # return new_arr and -ve timestamp


def calculate(x, h):
    ans = np.zeros((x.shape[0], x.shape[0]))

    for i in range(ans.shape[0]):
        if i < len(h):
            ans[i, :i + 1] = h[-i - 1:]
        else:
            ans[i, i - len(h)+1: i+1] = h

    ans = np.transpose(ans)

    return np.matmul(x, ans)


def plot_signal(x, y, xlabel=None, ylabel=None, title=None):
    
    plt.figure()
    plt.plot(x, y)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    plt.show()
    pass


if __name__ == '__main__':
    x1 = np.array([1, 2, 3, 4])
    n1 = np.arange(-1, 3, 1)

    x2 = np.array([1, 2, 1, 1])
    n2 = np.arange(-2, 2, 1)
    print("Signal x is: ", x1)
    print("Time stamp of X is: ", n1)
    plot_signal(n1, x1, xlabel='timestamp', ylabel='Signal X', title=None)

    print("Signal H is: ", x2)
    print("Timestamp of H is: ", n2)
    plot_signal(n2, x2, xlabel='timestamp', ylabel='Signal H', title=None)

    folded_H, neg_timestamp = folding(x2, n2)
    print("Folded H is: ", folded_H)
    print("Timestamp of H is: ", neg_timestamp)
    plot_signal(neg_timestamp, folded_H, xlabel='timestamp', ylabel='Signal H', title=None)

    left_most_timestamp = min(min(n1), min(neg_timestamp))
    max_len_result = len(n1) + len(neg_timestamp) - 1

    # initialize the resultant convolution array with zeroes
    result_time_stamp = np.arange(left_most_timestamp, left_most_timestamp + max_len_result, 1)
    print("Resultant timestamp would be: ", result_time_stamp)

    # pad our Signal X upto the len of max_len
    # 3 is obtained from result_time_stamp - len(x1)
    X = np.append(x1, np.zeros(3, ))
    result = calculate(X, folded_H)
    print('Convolution of Signal x1 and x2 is: ', result)
    plot_signal(result_time_stamp, result, title='Convolution_result')
    assert all(np.convolve(x1, x2) == result), 'Computed Result is Wrong'

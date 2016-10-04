# -*- coding: utf-8 -*-
# @Author: Elena Graverini
# @Date:   2015-06-27 13:34:57
# @Last Modified by:   Elena Graverini
# @Last Modified time: 2015-09-23 17:30:53


def read_from_file(filename):
    # This function is kindly provided to you.
    # Thank the assistants! :)
    my_distr = []
    with open(filename, 'r') as f:
        for line in f:
            line = line.split(' ')
            my_distr.append([float(line[0]), float(line[1])])
    return my_distr


def compute_mean(distr):
    # Write a function that returns the mean
    # of a given sample. The input is a data sample in list
    # of lists format, and the output will be a number.
    # Replace "mean = 0." with the function body.
    mean = 0
    total = 0
    count = 0
    
    for i in distr:
        total += i[0]
        count += 1

    mean = total / count

    return mean


def compute_weighted_mean(distr):
    # Write a function that returns the weighted mean
    # of a given sample. The input is a data sample in list
    # of lists format, and the output will be a number.
    # Replace "wmean = 0." with the function body.
    
    # Split data and errors
    values = get_column(distr, 0)
    errors = get_column(distr, 1)

    # The error error in measurement is our weight
    weights = [1/error**2 for error in errors]
    weighted_values = [weight*value for weight, value in zip(weights, values)]
    wmean = sum(weighted_values) / sum(weights)
    return wmean


def compute_error_on_mean(distr):
    # Write a function that returns the uncertainty on the mean
    # of a given sample. The input is a data sample in list
    # of lists format, and the output will be a number.
    # Replace "mean_error = 0." with the function body.
    l=[1./i[1]**2 for i in distr]
    mean_error=1./(sum(l))**0.5
    
    return mean_error


def compute_std(distr):
    # Write a function that returns the standard deviation
    # of a given sample. The input is a data sample in list
    # of lists format, and the output will be a number.
    # Replace "std = 0." with the function body.
    values = get_column(distr, 0)
    mean = compute_mean(distr)
    deviations = [(mean - value)**2 for value in values]
    std = 1. / (len(distr) -1) * sum(deviations)
    std = std**0.5
    return std

# Gets the given column (at the given index) from a 2d data set
def get_column(list_2d, index):
    return [sublist[index] for sublist in list_2d ]

# After your studies, please write either "yes" or "no"
# in the following variable, in place of "answer".
# Please enclose the answer with quotation marks,
# as in the example:
compatible_with_design = "no"


if __name__ == '__main__':
    # You can use the "main" to test your code.
    # Code that follows the "if __name__ == '__main__':" snippet
    # is only executed when you execute this script with
    # "python compute_mean_std.py", and will not run when your
    # functions will be tested by us.
    # Example:
    # print compute_mean(my_distr)
    # print compute_std(my_distr)

    my_distr = read_from_file("measurements.txt")
    print(compute_mean(my_distr))
    print(compute_weighted_mean(my_distr))
    print(compute_std(my_distr))
    print(compute_error_on_mean(my_distr))

    pass

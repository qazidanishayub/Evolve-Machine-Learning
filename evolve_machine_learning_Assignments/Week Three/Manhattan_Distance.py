
# importings module
from sklearn.metrics.pairwise import manhattan_distances

import numpy as np

# creating a Main Function..
def main():

# using numpy array for declaring 1*3 order array of 1's
    x = np.ones((1, 3))

# using numpy array for declaring 3*3 order array of 7's
    y = 7 * np.ones((3, 3))

    print('Metric A : {}'.format(x))
    print('Metric B : \n{}'.format(y))

    print("Manhattan Distance \n\n {} ".format(man_distance(y, x)))
    print("Manhattan Distance Sum  \n {} ".format(man_distance_sum(x, y)))


# creating function for calculating function without Sum of Manhattan Distance
def man_distance(x, y):
    return manhattan_distances(x, y, sum_over_features = False)

# creating function for calculating function with Sum of Manhattan Distance
def man_distance_sum(x, y):
    return manhattan_distances(x, y, sum_over_features = True)

# Calling Main Function to run.
if __name__ == '__main__':
    main()
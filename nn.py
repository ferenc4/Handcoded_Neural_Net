import numpy as np

# source https://iamtrask.github.io/2015/07/12/basic-python-network/
# sigmoid function
def nonlin(x, deriv=False):
    if (deriv == True):
        return x * (1 - x)
    return 1 / (1 + np.exp(-x))


# input dataset
X = np.array([[0, 0, 1],
              [0, 1, 1],
              [1, 0, 1],
              [1, 1, 1]])

# output dataset
# .T transposes it so it is a 'vertical' matrix
y = np.array([[0, 0, 1, 1]]).T

# seed random numbers to make calculation
# deterministic (just a good practice)
np.random.seed(1)

# initialize weights randomly with mean 0
# we have 3 inputs and 1 output so we need a matrix of 3x1
# this connects all neurons on both sides with each other
syn0 = 2 * np.random.random((3, 1)) - 1

for iter in xrange(10000):
    # forward propagation
    l0 = X
    l1 = nonlin(np.dot(l0, syn0))

    # how much did we miss?
    # the size of l1_error will be
    l1_error = y - l1

    if iter % 1000 == 0:
        print "Error:" + str(np.mean(np.abs(l1_error)))
    # multiply how much we missed by the
    # slope of the sigmoid at the values in l1
    l1_delta = l1_error * nonlin(l1, True)

    # update weights
    syn0 += np.dot(l0.T, l1_delta)

print "Output After Training:"
print l1

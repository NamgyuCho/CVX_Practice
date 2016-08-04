# Generate data for SVM classifier with L1 regularization.

from __future__ import division
import numpy as np

np.random.seed(1)
n = 20
m = 1000
TEST = m
DENSITY = 0.2

# Randomly turn off beta_true's elements so that beta_true becomes sparse
beta_true = np.random.randn(n, 1)
idxs = np.random.choice(range(n), int((1-DENSITY)*n), replace=False)
for idx in idxs:
    beta_true[idx] = 0

offset = 0
sigma = 45
X = np.random.normal(0, 5, size=(m, n))
Y = np.sign(X.dot(beta_true) + offset + np.random.normal(0, sigma, size=(m, 1)))

X_test = np.random.normal(0, 5, size=(TEST, n))
Y_test = np.sign(X_test.dot(beta_true) + offset + np.random.normal(0, sigma, size=(TEST, 1)))

# Form SVM with L1 regularization problem.
from cvxpy import *
beta = Variable(n)
v = Variable()
loss = sum_entries(pos(1 - mul_elemwise(Y, X*beta - v)))
reg = norm(beta, 1)
lambd = Parameter(sign="positive")
prob = Problem(Minimize(loss/m + lambd*reg))

# Compute a trade-ff curve and record train and test error.
TRAILS = 100
train_error = np.zeros(TRAILS)
test_error = np.zeros(TRAILS)
lambda_vals = np.logspace(-2, 0, TRAILS)
beta_vals = []
for i in range(TRAILS):
    lambd.value = lambda_vals[i]
    prob.solve()
    train_error[i] = (np.sign(X.dot(beta_true) + offset) != np.sign(X.dot(beta.value) - v.value)).sum()/m
    test_error[i] = (np.sign(X_test.dot(beta_true) + offset) != np.sign(X_test.dot(beta.value) - v.value)).sum()/TEST
    beta_vals.append(beta.value)

# Plot the train and test error over the trade-off curve.
import matplotlib.pyplot as plt
# %matplotlib inline
# %config InlineBackend.figure_format = 'svg'

plt.plot(lambda_vals, train_error, label="Train error")
plt.plot(lambda_vals, test_error, label="Test error")
plt.xscale("log")
plt.legend(loc='upper left')
plt.xlabel(r"$\lambda$", fontsize=16)
plt.show()

# Plot the regularization path for beta.
for i in range(n):
    plt.plot(lambda_vals, [wi[i, 0] for wi in beta_vals])
plt.xlabel(r"$\lambda$", fontsize=16)
plt.xscale("log")
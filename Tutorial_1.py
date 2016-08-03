## Namespace and changing problem
# from cvxpy import *
#
# # Create two scalar optimization varialbes.
#
# x = Variable()
# y = Variable()
#
# # Create two constraints.
# constraints = [x + y == 1, x - y >= 1]
#
# # Form objective
# obj = Minimize(square(x - y))
#
# # Form and solve problem
# prob = Problem(obj, constraints)
# prob.solve()
#
# print "status: ", prob.status
# print "optimal value: ", prob.value
# print "optimal var: ", x.value, y.value
#
#
# prob.objective = Maximize(x + y)
# print "optimal value", prob.solve()
#
# prob.constraints[0] = (x + y <= 3)
# print "optimal value", prob.solve()


## Infeasible and unbounded problems
# from cvxpy import *
#
# x = Variable()
#
# # An infeasible problem.
# prob = Problem(Minimize(x), [x >= 1, x <= 0])
# prob.solve()
# print "status:", prob.status
# print "optimal value:", prob.value
#
# # An unbounded problem.
# prob = Problem(Minimize(x))
# prob.solve()
# print "status:", prob.status
# print "optimal value:", prob.value

## Vectors and matrices
# from cvxpy import *
# import numpy
#
# m = 10
# n = 5
# numpy.random.seed(1)
# A = numpy.random.randn(m, n)
# b = numpy.random.randn(m, 1)
#
# x = Variable(n)
# objective = Minimize(sum_entries(square(A*x - b)))
# constraints = [0 <= x, x <= 1]
# prob = Problem(objective, constraints)
#
# print "Optimal value: ", prob.solve()
# print "Optimal var: "
# print x.value # A numpy matrix

## Constraints and Parameters
from cvxpy import *
import numpy
import matplotlib.pyplot as plt

n = 15
m = 10
numpy.random.seed(1)
A = numpy.random.randn(n, m)
b = numpy.random.randn(n, 1)
gamma = Parameter(sign="positive")

x = Variable(m)
error = sum_squares(A*x + b)
obj = Minimize(error + gamma*norm(x, 1))
prob = Problem(obj)

# do something funny here??
sq_penalty = []
l1_penalty = []
x_values = []
gamma_vals = numpy.logspace(-4, 6)
for val in gamma_vals:
    gamma.value = val
    prob.solve()

    sq_penalty.append(error.value)
    l1_penalty.append(norm(x, 1).value)
    x_values.append(x.value)

plt.rc('text')
plt.rc('font', family='serif')
plt.figure(figsize=(6, 10))

plt.subplot(211)
plt.plot(l1_penalty, sq_penalty)
plt.xlabel('|x|_1', fontsize=16)
plt.ylabel('|Ax-b|**2', fontsize=16)
plt.title('Trade-Off Curve for LASSO', fontsize=16)

plt.subplot(212)
for i in range(m):
    plt.plot(gamma_vals, [xi[i, 0] for xi in x_values])

plt.xlabel('gamma', fontsize=16)
plt.ylabel('x_i', fontsize=16)
plt.xscale('log')
plt.title('Entries of x vs. gamma', fontsize=16)

plt.tight_layout()
plt.show()
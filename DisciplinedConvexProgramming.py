from cvxpy import *
import numpy

## Expressions
print "\nExpressions\n"

# Create variables and parameters.
x, y = Variable(), Variable()
a, b = Parameter(), Parameter()

# Examples of CVXPY expressions.
3.69 + b/3
x - 4*a
sqrt(x) - min_elemwise(y, x-a)
max_elemwise(2.66 - sqrt(y), square(x+2*y))

X = Variable(5, 4)
A = numpy.ones((3, 5))

# Use expr.size to get the dimensions
print "dimensions of X:", X.size
print "dimensions of sum_entries(X):", sum_entries(X).size
print "dimensions of A*X:", (A*X).size

# ValueError raised for invalid dimensions.
try:
    A + X
except ValueError, e:
    print e


## Sign
print "\nSign\n"
x = Variable()
a = Parameter(sign="negative")
c = numpy.array([1, -1])

print "sign of x:", x.sign
print "sign of a:", a.sign
print "sign of square(x)", square(x).sign
print "sign of c*a", (c*a).sign


## Curvature
print "\nCurvature\n"
x = Variable()
a = Parameter(sign='positive')

print "curvature of x:", x.curvature
print "curvature of a:", a.curvature
print "curvature of square(x):", square(x).curvature
print "curvature of sqrt(x):", sqrt(x).curvature

print "sqrt(1 + square(x)) curvature:", sqrt(1 + square(x)).curvature
print "norm(vstack(1, x), 2) curvature:", norm(vstack(1, x), 2).curvature


## DCP problems
print "\nDCP Problems\n"
x = Variable()
y = Variable()

# DCP problems.
prob1 = Problem(Minimize(square(x - y)), [x + y >= 0])
prob2 = Problem(Maximize(sqrt(x - y)), [2*x - 3 == y,
                                        square(x) <= 2])

print "prob1 is DCP:", prob1.is_dcp()
print "prob2 is DCP:", prob2.is_dcp()

# Non-DCP problems.
# A non-DCP objective.
prob3 = Problem(Maximize(square(x)))

print "prob3 is DCP:", prob3.is_dcp()
print "Maximize(square(x)) is DCP:", Maximize(square(x)).is_dcp()

# A non-DCP constraint.
prob4 = Problem(Minimize(square(x)), [sqrt(x) <= 2])

print "prob4 is DCP:", prob4.is_dcp()
print "sqrt(x) <= is DCP:", (sqrt(x) <= 2).is_dcp()

# A non-DCP problem
prob = Problem(Minimize(sqrt(x)))

try:
    prob.solve()
except Exception as e:
    print e
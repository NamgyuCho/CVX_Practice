from cvxpy import *

## Dual variables
print "\nDual variables>"

# Create two scalar optimization variables.
x = Variable()
y = Variable()

# Create two constraints.
constraints = [x + y == 1,
               x - y >= 1]

# Form objective.
obj = Minimize(square(x - y))

# Form and solve problem
prob = Problem(obj, constraints)
prob.solve()

# The optimal dual variable (Lagrange multiplier) for a constraint is stored in constraint.dual_value.
print "optimal (x + y == 1) dual variable", constraints[0].dual_value
print "optimal (x - y >= 1) dual variable", constraints[1].dual_value
print "x - y value:", (x - y).value


## Solve method options
print '\nSolver options\n'

# Solving a problem with different solvers.
x = Variable(2)
obj = Minimize(x[0] + norm(x, 1))
constraints = [x >= 2]
prob = Problem(obj, constraints)

# Solve with ECOS.
prob.solve(solver=ECOS)
print "optimal value with ECOS:", prob.value

# Solve with ECOS_BB.
prob.solve(solver=ECOS_BB)
print "optimal value with ECOS_BB:", prob.value

# Solve with CVXOPT.
prob.solve(solver=CVXOPT)
print "optimal value with CVXOPT:", prob.value

# Solve with SCS.
prob.solve(solver=SCS)
print "optimal value with SCS:", prob.value

# # Solve with GLPK.
# prob.solve(solver=GLPK)
# print "optimal value with GLPK:", prob.value
#
# # Solve with GLPK_MI.
# prob.solve(solver=GLPK_MI)
# print "optimal value with GLPK_MI:", prob.value

# # Solve with GUROBI.
# prob.solve(solver=GUROBI)
# print "optimal value with GUROBI:", prob.value
#
# # Solve with MOSEK.
# prob.solve(solver=MOSEK)
# print "optimal value with MOSEK:", prob.value
#
# # Solve with Elemental.
# prob.solve(solver=ELEMENTAL)
# print "optimal value with Elemental:", prob.value
#
# # Solve with CBC.
# prob.solve(solver=CBC)
# print "optimal value with CBC:", prob.value

print installed_solvers()

# Solve with SCS, use sparse-indirect method.
prob.solve(solver=SCS, verbose=True, use_indirect=True)
print "optimal value with SCS:", prob.value
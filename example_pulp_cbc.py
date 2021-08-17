from pulp import LpMaximize, LpProblem, LpStatus, lpSum, LpVariable

# CBC is the default solver

# (1) Create model
model = LpProblem(name="small-problem", sense=LpMaximize)

""" Use the sense parameter to choose whether to perform 
minimization (LpMinimize or 1, which is the default) 
or maximization (LpMaximize or -1).
This choice will affect the result of your problem.
"""

# (2) Initialize DVs
x = LpVariable(name="x", lowBound=0)
y = LpVariable(name="y", lowBound=0)

# Default bounds are negative infinity to positive infinity

# The optional parameter cat defines the category of a decision variable
# Defaults to "Continuous"

""" Multiply a DV with a scalar or build a linear combination of 
multiple DVs to get an instance of pulp.LpAffineExpression 
that represents a linear expression
"""

""" Combine linear expressions, variables, and scalars with the 
operators ==, <=, or >= to get instances of pulp.LpConstraint 
that represent the linear constraints of model
"""

# (3) Add constraints to model
# LpProblem allows you to add constraints to a model by specifying them as tuples
# First element of tuple is LpConstraint instance
# Second element is a human-readable name for that constraint
model += (2 * x + y <= 20, "red_constraint")
model += (4 * x - 5 * y >= -10, "blue_constraint")
model += (-x + 2 * y >= -2, "yellow_constraint")
model += (-x + 5 * y == 15, "green_constraint")

# (4) Add objective function to model
obj_func = x + 2 * y
model += obj_func

# For larger problems, often more convenient to use lpSum()
# with a list or other sequence than to repeat the + operator
print("Model:")
print(model)

# (5) Solve problem
status = model.solve()

print("")
print(f"Status: {model.status}, {LpStatus[model.status]}")
print(f"Objective: {model.objective.value()}")
print("Variables:")
for var in model.variables():
    print(f"{var.name}: {var.value()}")
print("Constraints:")
for name, constraint in model.constraints.items():
    print(f"{name}: {constraint.value()}")

""" Model attributes:
- variables is list of DVs
- constraints is list of values of slack variables
- solver displays information about solver used
"""

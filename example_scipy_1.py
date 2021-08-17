from scipy.optimize import linprog

"""
(1) State
- objective
- inequalities, LHS & RHS
- equalities, LHS & RHS

Note
- Order of rows for the left and right sides of constraints MUST BE THE SAME
- Each row represents one constraint
- Order of coefficients from objective function and left sides of constraints MUST MATCH
- Each column corresponds to a single DV

(2) Define bounds for each variable in same order as coefficients

"""

# obj = [COEFFICIENT_FOR_Y, COEFFICIENT_FOR_X]
obj = [-1, -2]

lhs_ineq = [
    [2, 1],  # Red constraint left side
    [-4, 5],  # Blue constraint left side
    [1, -2],  # Yellow constraint left side
]

rhs_ineq = [
    20,  # Red constraint right side
    10,  # Blue constraint right side
    2,  # Yellow constraint right side
]

lhs_eq = [[-1, 5]]  # Green constraint left side
rhs_eq = [15]  # Green constraint right side

# Bounds

bnd = [(0, float("inf")), (0, float("inf"))]  # Bounds of x  # Bounds of y

opt = linprog(
    c=obj,
    A_ub=lhs_ineq,
    b_ub=rhs_ineq,
    A_eq=lhs_eq,
    b_eq=rhs_eq,
    bounds=bnd,
    method="revised simplex",
)

print("Optimal solution:")
print(opt)

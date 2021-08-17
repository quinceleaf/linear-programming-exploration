from scipy.optimize import linprog

obj = [-20, -12, -40, -25]

lhs_ineq = [
    [1, 1, 1, 1],  # Manpower
    [3, 2, 1, 0],  # Material A
    [0, 1, 2, 3],
]  # Material B

rhs_ineq = [50, 100, 90]  # Manpower  # Material A  # Material B

opt = linprog(c=obj, A_ub=lhs_ineq, b_ub=rhs_ineq, method="revised simplex")


print("Optimal solution:")
print(opt)

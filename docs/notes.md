# Notes on Linear Optimization/Solving in Python

## Libraries

- [SciPy Optimization and Root Finding](https://docs.scipy.org/doc/scipy/reference/optimize.html)
- [PuLP](https://www.coin-or.org/PuLP/solvers.html)
- [Pyomo](https://pyomo.readthedocs.io/en/stable/solving_pyomo_models.html#supported-solvers)
- [CVXOPT](https://cvxopt.org/userguide/coneprog.html#optional-solvers)


## Installing Libraries

- Install `scipy` and `pulp`

```bash
poetry add "scipy==1.4.*" "pulp==2.5.0"
```

-- Run `pulptest` or `sudo pulptest` to enable the default solvers for PuLP, or install GLPK

```bash
pulptest
# or
brew install glpk
```

### SciPy's `linprog()`

`linprog()` solves only **minimization** (not maximization) problems and doesn’t allow inequality constraints with the greater than or equal to sign (≥). May need to modify your problem before starting optimization to work around these issues

- Default bounds are zero to positive infinity


```python
opt = linprog(
    c=obj, 
    A_ub=lhs_ineq, 
    b_ub=rhs_ineq,
    A_eq=lhs_eq, 
    b_eq=rhs_eq, 
    bounds=bnd,
    method="revised simplex"
    )
```

where

- `obj` holds coefficients from objective function
- `lhs_ineq` holds LHS coefficients from inequality constraint(s)
- `rhs_ineq` holds RHS coefficients from inequality constraint(s)
- `lhs_eq` holds LHS coefficients from equality constraint(s)
- `rhs_eq` holds RHS coefficients from equality constraint(s)

Parameter `method` defines which of (3) LP methods to use:

- `interior-point` selects the **interior-point method** (default)
- `revised simplex` selects the **revised two-phase simplex method**
- `simplex` selects the l**egacy two-phase simplex method**

`linprog()` returns a data structure with these attributes:

- `con` is the equality constraints residuals.
- `fun` is the objective function value at the optimum (if found).
- `message `is the status of the solution.
- `nit` is the number of iterations needed to finish the calculation.
- `slack` is the values of the slack variables, or the differences between the values of the left and right sides of the constraints.
- `status` is an integer between 0 and 4 that shows the status of the solution, such as 0 for when the optimal solution has been found.
- `success` is a Boolean that shows whether the optimal solution has been found.
- `x` is a NumPy array holding the optimal values of the decision variables.

### Limitations of SciPy for LP

SciPy:

- can’t run various external solvers
- can’t work with integer decision variables
- doesn’t provide classes or functions that facilitate model building. You have to define arrays and matrices, which might be a tedious and error-prone task for large problems
- doesn’t allow you to define maximization problems directly. You must convert them to minimization problems
- doesn’t allow you to define constraints using `>=` directly, must use `<=` instead

## Pulp

Can use PuLP to solve MILPs. 

- To define an integer or binary variable, just pass `cat="Integer"` or `cat="Binary"` to `LpVariable`


## Resources

- [RealPython: Hands-On Linear Programming: Optimization With Python](https://realpython.com/linear-programming-python/)


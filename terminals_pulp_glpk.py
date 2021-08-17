from pulp import LpInteger, LpMinimize, LpProblem, LpStatus, lpSum, LpVariable, makeDict
from pulp import GLPK

""" MILP problem from edX-MITx SC2x Supply Chain Design (2018)
MicroMasters supplementary problems, week 2
"""

# (0) Problem data

# List of plants
plants = [
    "cincinnati",
    "atlanta",
    "detroit",
]

# List of terminals
terminals = [
    "charlotte",
    "scranton",
]

# List of warehouses
warehouses = [
    "providence",
    "philadelphia",
    "columbus",
    "knoxville",
    "jacksonville",
    "richmond",
]

# Demand per regional WH
demand = {
    "providence": 4,
    "philadelphia": 15,
    "columbus": 5,
    "knoxville": 12,
    "jacksonville": 3,
    "richmond": 8,
}

# Capacity per plant
capacity = {
    "cincinnati": 20,
    "atlanta": 20,
    "detroit": 20,
}

costs = {}

# Transport cost matrix betw plants & terminals
cost_matrix_plant_to_terminal = [
    # Terminals
    # scranton, charlotte
    [83, 72],  # cincinnati # Plants
    [122, 35],  # atlanta
    [75, 95],  # detroit
]
cost_matrix_plant_to_terminal = makeDict(
    [plants, terminals], cost_matrix_plant_to_terminal, 0
)
costs.update(cost_matrix_plant_to_terminal)

# Transport cost matrix betw terminals & warehouses
cost_matrix_terminal_to_warehouse = [
    # Warehouses
    # providence, philadelphia, columbus, knoxville, jacksonville, richmond
    [44, 21, 73, 94, 143, 61],  # scranton, # Terminals
    [124, 84, 64, 35, 52, 41],  # charlotte
]
cost_matrix_terminal_to_warehouse = makeDict(
    [terminals, warehouses], cost_matrix_terminal_to_warehouse, 0
)
costs.update(cost_matrix_terminal_to_warehouse)

# Transport cost matrix betw plants & warehouses
cost_matrix_plant_to_warehouse = [
    # Warehouses
    # providence, philadelphia, columbus, knoxville, jacksonville, richmond
    [125, 85, 15, 34, 113, 76],  # cincinnati   # Plants
    [163, 114, 82, 31, 45, 75],  # atlanta
    [106, 85, 32, 75, 152, 93],  # detroit
]

cost_matrix_plant_to_warehouse = makeDict(
    [plants, warehouses], cost_matrix_plant_to_warehouse, 0
)
# Cannot use update directly from cost_matrix_plant_to_warehouse as
# would overwrite keys from cost_matrix_terminal_to_warehouse
for key in cost_matrix_plant_to_warehouse:
    costs[key].update(cost_matrix_plant_to_warehouse[key])

# (1) Initialize model
model = LpProblem(name="network_distribution_problem", sense=LpMinimize)

# (2) Initialize DVs
vars = {}

# Flow betw plants & terminals
routes_plant_to_terminal = [(p, t) for p in plants for t in terminals]
vars_plant_to_terminal = LpVariable.dicts(
    "Route", (plants, terminals), lowBound=0, upBound=None, cat=LpInteger
)
vars.update(vars_plant_to_terminal)

# Flow betw terminals & regional WHs
routes_terminal_to_warehouse = [(t, w) for t in terminals for w in warehouses]
vars_terminal_to_warehouse = LpVariable.dicts(
    "Route", (terminals, warehouses), lowBound=0, upBound=None, cat=LpInteger
)
vars.update(vars_terminal_to_warehouse)

# Flow betw plants & regional WHs (direct)
routes_plant_to_warehouse = [(p, w) for p in plants for w in warehouses]
vars_plant_to_warehouse = LpVariable.dicts(
    "Route", (plants, warehouses), lowBound=0, upBound=None, cat=LpInteger
)
# Cannot use update directly from vars_plant_to_warehouse
# as would overwrite keys from vars_plant_to_terminal
for key in vars_plant_to_warehouse:
    vars[key].update(vars_plant_to_warehouse[key])

routes = (
    routes_plant_to_terminal + routes_plant_to_warehouse + routes_terminal_to_warehouse
)

# (3) Add objective function to model
model += (
    lpSum([vars[origin][dest] * costs[origin][dest] for (origin, dest) in routes]),
    "sum_of_transport_costs",
)

# (4) Add constraints to model

# Capacity maximum constraints for plants
for p in plants:
    model += (
        lpSum([vars[p][dest] for dest in warehouses]) <= capacity[p],
        f"sum_of_flow_supplied_by_plant_[{p}]",
    )

# Supply demanded constraints for warehouses
for w in warehouses:
    model += (
        lpSum([vars[origin][w] for origin in plants]) >= demand[w],
        f"sum_of_flow_received_by_warehouse_[{w}]",
    )

# No holding constraints for terminals
for t in terminals:
    model += (
        lpSum([vars[origin][t] for origin in plants])
        - lpSum([vars[t][dest] for dest in warehouses])
        == 0,
        f"holding_at_terminal_[{t}]",
    )

# (5) Write out model to
model.writeLP("NetworkDistributionProblem.lp")
model.toJson("NetworkDistributionProblem.json")


# (6) Solve model
model.solve(solver=GLPK(msg=False))

print("Status:", LpStatus[model.status])

print(f"Optimal cost of transport: {model.objective}")

print("")
print("VARIABLES:")
for var in model.variables():
    print(f"Variable [{var.name}]: {var.value()}")

print("CONSTRAINTS:")
for name, constraint in model.constraints.items():
    print(f"{name}: {constraint.value()}")

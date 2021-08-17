\* network_distribution_problem *\
Minimize
sum_of_transport_costs: 122 Route_atlanta_charlotte
 + 82 Route_atlanta_columbus + 45 Route_atlanta_jacksonville
 + 31 Route_atlanta_knoxville + 114 Route_atlanta_philadelphia
 + 163 Route_atlanta_providence + 75 Route_atlanta_richmond
 + 35 Route_atlanta_scranton + 73 Route_charlotte_columbus
 + 143 Route_charlotte_jacksonville + 94 Route_charlotte_knoxville
 + 21 Route_charlotte_philadelphia + 44 Route_charlotte_providence
 + 61 Route_charlotte_richmond + 83 Route_cincinnati_charlotte
 + 15 Route_cincinnati_columbus + 113 Route_cincinnati_jacksonville
 + 34 Route_cincinnati_knoxville + 85 Route_cincinnati_philadelphia
 + 125 Route_cincinnati_providence + 76 Route_cincinnati_richmond
 + 72 Route_cincinnati_scranton + 75 Route_detroit_charlotte
 + 32 Route_detroit_columbus + 152 Route_detroit_jacksonville
 + 75 Route_detroit_knoxville + 85 Route_detroit_philadelphia
 + 106 Route_detroit_providence + 93 Route_detroit_richmond
 + 95 Route_detroit_scranton + 64 Route_scranton_columbus
 + 52 Route_scranton_jacksonville + 35 Route_scranton_knoxville
 + 84 Route_scranton_philadelphia + 124 Route_scranton_providence
 + 41 Route_scranton_richmond
Subject To
holding_at_terminal__charlotte_: Route_atlanta_charlotte
 - Route_charlotte_columbus - Route_charlotte_jacksonville
 - Route_charlotte_knoxville - Route_charlotte_philadelphia
 - Route_charlotte_providence - Route_charlotte_richmond
 + Route_cincinnati_charlotte + Route_detroit_charlotte = 0
holding_at_terminal__scranton_: Route_atlanta_scranton
 + Route_cincinnati_scranton + Route_detroit_scranton
 - Route_scranton_columbus - Route_scranton_jacksonville
 - Route_scranton_knoxville - Route_scranton_philadelphia
 - Route_scranton_providence - Route_scranton_richmond = 0
sum_of_flow_received_by_warehouse__columbus_: Route_atlanta_columbus
 + Route_cincinnati_columbus + Route_detroit_columbus >= 5
sum_of_flow_received_by_warehouse__jacksonville_: Route_atlanta_jacksonville
 + Route_cincinnati_jacksonville + Route_detroit_jacksonville >= 3
sum_of_flow_received_by_warehouse__knoxville_: Route_atlanta_knoxville
 + Route_cincinnati_knoxville + Route_detroit_knoxville >= 12
sum_of_flow_received_by_warehouse__philadelphia_: Route_atlanta_philadelphia
 + Route_cincinnati_philadelphia + Route_detroit_philadelphia >= 15
sum_of_flow_received_by_warehouse__providence_: Route_atlanta_providence
 + Route_cincinnati_providence + Route_detroit_providence >= 4
sum_of_flow_received_by_warehouse__richmond_: Route_atlanta_richmond
 + Route_cincinnati_richmond + Route_detroit_richmond >= 8
sum_of_flow_supplied_by_plant__atlanta_: Route_atlanta_columbus
 + Route_atlanta_jacksonville + Route_atlanta_knoxville
 + Route_atlanta_philadelphia + Route_atlanta_providence
 + Route_atlanta_richmond <= 20
sum_of_flow_supplied_by_plant__cincinnati_: Route_cincinnati_columbus
 + Route_cincinnati_jacksonville + Route_cincinnati_knoxville
 + Route_cincinnati_philadelphia + Route_cincinnati_providence
 + Route_cincinnati_richmond <= 20
sum_of_flow_supplied_by_plant__detroit_: Route_detroit_columbus
 + Route_detroit_jacksonville + Route_detroit_knoxville
 + Route_detroit_philadelphia + Route_detroit_providence
 + Route_detroit_richmond <= 20
Bounds
 0 <= Route_atlanta_charlotte
 0 <= Route_atlanta_columbus
 0 <= Route_atlanta_jacksonville
 0 <= Route_atlanta_knoxville
 0 <= Route_atlanta_philadelphia
 0 <= Route_atlanta_providence
 0 <= Route_atlanta_richmond
 0 <= Route_atlanta_scranton
 0 <= Route_charlotte_columbus
 0 <= Route_charlotte_jacksonville
 0 <= Route_charlotte_knoxville
 0 <= Route_charlotte_philadelphia
 0 <= Route_charlotte_providence
 0 <= Route_charlotte_richmond
 0 <= Route_cincinnati_charlotte
 0 <= Route_cincinnati_columbus
 0 <= Route_cincinnati_jacksonville
 0 <= Route_cincinnati_knoxville
 0 <= Route_cincinnati_philadelphia
 0 <= Route_cincinnati_providence
 0 <= Route_cincinnati_richmond
 0 <= Route_cincinnati_scranton
 0 <= Route_detroit_charlotte
 0 <= Route_detroit_columbus
 0 <= Route_detroit_jacksonville
 0 <= Route_detroit_knoxville
 0 <= Route_detroit_philadelphia
 0 <= Route_detroit_providence
 0 <= Route_detroit_richmond
 0 <= Route_detroit_scranton
 0 <= Route_scranton_columbus
 0 <= Route_scranton_jacksonville
 0 <= Route_scranton_knoxville
 0 <= Route_scranton_philadelphia
 0 <= Route_scranton_providence
 0 <= Route_scranton_richmond
Generals
Route_atlanta_charlotte
Route_atlanta_columbus
Route_atlanta_jacksonville
Route_atlanta_knoxville
Route_atlanta_philadelphia
Route_atlanta_providence
Route_atlanta_richmond
Route_atlanta_scranton
Route_charlotte_columbus
Route_charlotte_jacksonville
Route_charlotte_knoxville
Route_charlotte_philadelphia
Route_charlotte_providence
Route_charlotte_richmond
Route_cincinnati_charlotte
Route_cincinnati_columbus
Route_cincinnati_jacksonville
Route_cincinnati_knoxville
Route_cincinnati_philadelphia
Route_cincinnati_providence
Route_cincinnati_richmond
Route_cincinnati_scranton
Route_detroit_charlotte
Route_detroit_columbus
Route_detroit_jacksonville
Route_detroit_knoxville
Route_detroit_philadelphia
Route_detroit_providence
Route_detroit_richmond
Route_detroit_scranton
Route_scranton_columbus
Route_scranton_jacksonville
Route_scranton_knoxville
Route_scranton_philadelphia
Route_scranton_providence
Route_scranton_richmond
End

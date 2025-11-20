from graphviz import Digraph

dot = Digraph('GTA_Congestion_CLD_Detailed', format='png')
dot.attr(rankdir='LR', size='20,20')

variables = [
    "Highway Capacity",
    "Travel Time / Congestion",
    "Perceived Driving Convenience",
    "Car Usage / VKT",
    "Political Pressure for Road Expansion",
    "Housing Affordability (Job-Rich Areas)",
    "Suburban Residential Growth",
    "Average Commute Distance",
    "Transit Service Quality & Reliability",
    "Transit Ridership",
    "Relative Attractiveness of Transit",
    "Pressure on Urban Housing Prices"
]

for v in variables:
    dot.node(v, v, shape='box', style='rounded,filled', fillcolor='lightgray')

edges = [
    ("Highway Capacity", "Travel Time / Congestion", "-"),
    ("Travel Time / Congestion", "Perceived Driving Convenience", "-"),
    ("Perceived Driving Convenience", "Car Usage / VKT", "+"),
    ("Car Usage / VKT", "Travel Time / Congestion", "+"),
    ("Travel Time / Congestion", "Political Pressure for Road Expansion", "+"),
    ("Political Pressure for Road Expansion", "Highway Capacity", "+"),
    
    ("Housing Affordability (Job-Rich Areas)", "Suburban Residential Growth", "-"),
    ("Suburban Residential Growth", "Average Commute Distance", "+"),
    ("Average Commute Distance", "Car Usage / VKT", "+"),
    ("Travel Time / Congestion", "Pressure on Urban Housing Prices", "+"),
    ("Pressure on Urban Housing Prices", "Housing Affordability (Job-Rich Areas)", "-"),
    
    ("Travel Time / Congestion", "Relative Attractiveness of Transit", "+"),
    ("Relative Attractiveness of Transit", "Transit Ridership", "+"),
    ("Transit Ridership", "Car Usage / VKT", "-"),
    ("Transit Ridership", "Transit Service Quality & Reliability", "+"),
    ("Transit Service Quality & Reliability", "Relative Attractiveness of Transit", "+")
]

for src, dst, sign in edges:
    dot.edge(src, dst, label=sign)

dot.render('GTA_Congestion_CLD_Detailed', cleanup=True)


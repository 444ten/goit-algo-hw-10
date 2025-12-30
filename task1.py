import pulp

model = pulp.LpProblem("Maximize_Beverage_Production", pulp.LpMaximize)
L = pulp.LpVariable('Lemonade', lowBound=0, cat='Integer')
F = pulp.LpVariable('Fruit_Juice', lowBound=0, cat='Integer')

model += L + F, "Total_Products"

model += (2 * L + 1 * F <= 100), "Water_Constraint"
model += (1 * L <= 50), "Sugar_Constraint"
model += (1 * L <= 30), "Lemon_Juice_Constraint"
model += (2 * F <= 40), "Fruit_Puree_Constraint"

model.solve(pulp.PULP_CBC_CMD(msg=False))

print(f"Status: {pulp.LpStatus[model.status]}")
print(f"Lemonade produced: {L.varValue}")
print(f"Fruit Juice produced: {F.varValue}")
print(f"Total products: {pulp.value(model.objective)}")
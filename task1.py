from pulp import LpMaximize, LpProblem, LpVariable

model = LpProblem(name="maximize_production", sense=LpMaximize)

# Змінні рішення
lemonade = LpVariable(name="Lemonade", lowBound=0, cat='Integer')
fruit_juice = LpVariable(name="Fruit_Juice", lowBound=0, cat='Integer')

# Функція цілі: максимізація кількості вироблених напоїв
model += lemonade + fruit_juice, "Total Production"

# Обмеження ресурсів
model += (2 * lemonade + 1 * fruit_juice <= 100), "Water Constraint"
model += (1 * lemonade <= 50), "Sugar Constraint"
model += (1 * lemonade <= 30), "Lemon Juice Constraint"
model += (2 * fruit_juice <= 40), "Fruit Puree Constraint"

model.solve()
print(f"Optimal production:")
print(f"Lemonade: {lemonade.varValue}")
print(f"Fruit Juice: {fruit_juice.varValue}")

from pulp import LpMaximize, LpProblem, LpVariable

model = LpProblem(name="maximize_production", sense=LpMaximize)

# Змінні рішення
lemonade = LpVariable(name="Lemonade", lowBound=0, cat='Integer')
fruit_juice = LpVariable(name="Fruit_Juice", lowBound=0, cat='Integer')

# Функція цілі: максимізація кількості вироблених напоїв
model += lemonade + fruit_juice, "Total Production"

# Обмеження ресурсів
model += (2 * lemonade + 1 * fruit_juice <= 100), "Вода"
model += (1 * lemonade <= 50), "Цукор"
model += (1 * lemonade <= 30), "Лимонний сік"
model += (2 * fruit_juice <= 40), "Фруктове пюре"

model.solve()
print(f"Оптимальне виробництво:")
print(f"Лимонад: {lemonade.varValue}")
print(f"Фруктовий сік: {fruit_juice.varValue}")

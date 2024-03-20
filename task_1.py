import pulp

# Ініціалізація моделі
model = pulp.LpProblem("Максимізація виробництва напоїв", pulp.LpMaximize)

# Оголошення змінних
limonade = pulp.LpVariable('Лімонад', lowBound=0, cat='Integer')
juce = pulp.LpVariable('Фруктовий_сік', lowBound=0, cat='Integer')

# Додавання обмежень за інгредієнтами
model += 2 * limonade + 1 * juce <= 100, "Обмеження води"
model += 1 * limonade <= 50, "Обмеження цукру"
model += 1 * limonade <= 30, "Обмеження лимонного соку"
model += 2 * juce <= 40, "Обмеження фруктового пюре"

# Цільова функція: максимізація загальної кількості вироблених напоїв
model += limonade + juce, "Загальна кількість продукції"

# Розв'язок задачі
model.solve()

# Вивід результатів
print(f"Кількість виробленого лімонаду: {limonade.varValue}")
print(f"Кількість виробленого фруктового соку: {juce.varValue}")
print("Загальна кількість продукції:", limonade.varValue + juce.varValue)

'''Жадібні алгоритми та динамічне програмування'''

#Початкові дані
items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}

def greedy_algorithm(items, budget):
    '''Функція жадібного алгоритму.
    Сортуємо страви за співвідношенням калорій до вартості в спадному порядку'''
    sorted_items = sorted(items.items(),
                          key=lambda x: x[1]['calories'] / x[1]['cost'],
                          reverse=True)

    total_cost = 0
    total_calories = 0
    selected_items = []

    for item, data in sorted_items:
        if total_cost + data['cost'] <= budget:
            selected_items.append(item)
            total_cost += data['cost']
            total_calories += data['calories']

    return selected_items, total_calories

# Приклад використання
budget = 100
selected_items, total_calories = greedy_algorithm(items, budget)
print("Жадібний алгоритм:")
print("Вибрані страви:", selected_items)
print("Загальна калорійність:", total_calories)

def dynamic_programming(items, budget):
    '''Функція динамічного програмування.
    Ініціалізація таблиці DP, де dp[i][w] зберігає максимальну 
    калорійність для перших i предметів з бюджетом w'''

    dp = [[0 for _ in range(budget + 1)] for _ in range(len(items) + 1)]
    item_list = list(items.items())

    for i in range(1, len(items) + 1):
        item, data = item_list[i-1]
        for w in range(1, budget + 1):
            if data['cost'] <= w:
                dp[i][w] = max(dp[i-1][w], dp[i-1][w - data['cost']] + data['calories'])
            else:
                dp[i][w] = dp[i-1][w]

    # Відновлення вибраних предметів
    w = budget
    selected_items = []
    total_calories = dp[len(items)][budget]

    for i in range(len(items), 0, -1):
        if dp[i][w] != dp[i-1][w]:
            item, data = item_list[i-1]
            selected_items.append(item)
            w -= data['cost']
    
    return selected_items, total_calories

# Приклад використання
selected_items, total_calories = dynamic_programming(items, budget)
print("Динамічне програмування:")
print("Вибрані страви:", selected_items)
print("Загальна калорійність:", total_calories)

#Порівняння результатів
# Приклад використання обох алгоритмів для порівняння результатів

budget = 100

# Жадібний алгоритм
selected_items_greedy, total_calories_greedy = greedy_algorithm(items, budget)
print("Жадібний алгоритм:")
print("Вибрані страви:", selected_items_greedy)
print("Загальна калорійність:", total_calories_greedy)

# Динамічне програмування
selected_items_dp, total_calories_dp = dynamic_programming(items, budget)
print("Динамічне програмування:")
print("Вибрані страви:", selected_items_dp)
print("Загальна калорійність:", total_calories_dp)

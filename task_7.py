import random
import matplotlib.pyplot as plt

def simulate_dice_rolls(num_rolls):
    sums = [0] * 13  # Індекси від 0 до 12, але будемо використовувати від 2 до 12
    for _ in range(num_rolls):
        roll1 = random.randint(1, 6)
        roll2 = random.randint(1, 6)
        roll_sum = roll1 + roll2
        sums[roll_sum] += 1
    return sums

def calculate_probabilities(sums, num_rolls):
    probabilities = [0] * 13
    for i in range(2, 13):
        probabilities[i] = sums[i] / num_rolls
    return probabilities

def plot_probabilities(probabilities):
    x = range(2, 13)
    y = [probabilities[i] for i in x]

    plt.bar(x, y, color='blue', alpha=0.7)
    plt.xlabel('Сума')
    plt.ylabel('Імовірність')
    plt.title('Імовірності сум при киданні двох кубиків (Метод Монте-Карло)')
    plt.xticks(x)
    plt.grid(axis='y')
    plt.show()

# Виконання симуляції
num_rolls = 100000
sums = simulate_dice_rolls(num_rolls)
probabilities = calculate_probabilities(sums, num_rolls)

# Виведення результатів
print("Сума\tІмовірність")
for i in range(2, 13):
    print(f"{i}\t{probabilities[i] * 100:.2f}%")

# Побудова графіка
plot_probabilities(probabilities)

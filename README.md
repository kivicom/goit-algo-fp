# Завдання 1. Структури даних. Сортування. Робота з однозв'язним списком

Для реалізації однозв'язного списку (приклад реалізації можна взяти з конспекту) необхідно:

написати функцію, яка реалізує реверсування однозв'язного списку, змінюючи посилання між вузлами;
розробити алгоритм сортування для однозв'язного списку, наприклад, сортування вставками або злиттям;
написати функцію, що об'єднує два відсортовані однозв'язні списки в один відсортований список.

## Висновки
Ми реалізували однозв'язний список, функцію для його реверсування, алгоритм сортування злиттям, а також функцію для об'єднання двох відсортованих списків. Це забезпечує базові операції для роботи з однозв'язними списками та їх маніпулювання.

<br><br>

# Завдання 2. Рекурсія. Створення фрактала “дерево Піфагора” за допомогою рекурсії

Необхідно написати програму на Python, яка використовує рекурсію для створення фрактала “дерево Піфагора”. Програма має візуалізувати фрактал “дерево Піфагора”, і користувач повинен мати можливість вказати рівень рекурсії.

## Пояснення коду
1. Імпорт бібліотек: Ми імпортуємо бібліотеки turtle і math.

2. Функція draw_pythagoras_tree:
* Приймає параметри: черепаха t, довжина гілки branch_length, кут повороту angle і рівень рекурсії depth.
* Якщо depth дорівнює 0, функція завершується.
* Черепаха малює гілку довжиною branch_length і потім розгалужується на дві гілки з новою довжиною, яка менша в $\sqrt{2}$ / 2 разів.
* Для кожної нової гілки викликається draw_pythagoras_tree рекурсивно з новим рівнем рекурсії (depth - 1).

3. Функція main:
* Створює екран і черепаху.
* Отримує рівень рекурсії від користувача.
* Викликає функцію draw_pythagoras_tree для малювання фрактала з початковою довжиною гілки 100 і кутом 45 градусів.
* Після завершення малювання ховає черепаху і запускає головний цикл екрану для відображення результату.

## Виконання коду
Виконайте цей код у вашому середовищі програмування (наприклад, Jupyter Notebook, VSCode або будь-якому іншому IDE). Він згенерує фрактал "дерево Піфагора" з рівнем рекурсії, який ви вкажете, і візуалізує його за допомогою бібліотеки turtle.

## Висновки
Цей код демонструє використання рекурсії для створення складних фракталів. Використовуючи бібліотеку turtle, ви можете легко візуалізувати рекурсивні структури та експериментувати з різними параметрами для досягнення бажаного результату.

<br><br>

# Завдання 3. Дерева, алгоритм Дейкстри

Розробіть алгоритм Дейкстри для знаходження найкоротших шляхів у зваженому графі, використовуючи бінарну купу. Завдання включає створення графа, використання піраміди для оптимізації вибору вершин та обчислення найкоротших шляхів від початкової вершини до всіх інших.

## Пояснення
1. Створення графа: Ми створюємо граф і додаємо до нього вершини та ребра з відповідними вагами.
2. Алгоритм Дейкстри: Використовуючи бінарну купу (heapq), ми обчислюємо найкоротші шляхи від початкової вершини до всіх інших вершин.
3. Відображення результатів: Функція print_shortest_path виводить найкоротші відстані від початкової вершини до всіх інших вершин.

Цей алгоритм ефективно знаходить найкоротші шляхи у зваженому графі, використовуючи бінарну купу для оптимізації вибору вершин.

# Завдання 4. Візуалізація піраміди

## Пояснення коду

1. Клас Node: використовується для створення вузлів дерева з додатковими атрибутами, такими як унікальний ідентифікатор і колір.
2. Функція add_edges: рекурсивно додає вузли та ребра до графа, визначаючи позиції вузлів для візуалізації.
3. Функція draw_tree: візуалізує дерево, використовуючи бібліотеку networkx і matplotlib.
4. Функція build_heap: створює бінарну купу з масиву. Вона перетворює елементи масиву на вузли і з'єднує їх відповідно до властивостей бінарної купи.
5. Приклад використання: створюється масив для бінарної купи, будується дерево і відображається.

Цей код дозволяє легко візуалізувати бінарну купу, починаючи з масиву, і перетворює його на дерево для подальшої візуалізації.

<br<br>

# Завдання 5. Візуалізація обходу бінарного дерева

Використовуючи код із завдання 4 для побудови бінарного дерева, необхідно створити програму на Python, яка візуалізує обходи дерева: у глибину та в ширину.

Вона повинна відображати кожен крок у вузлах з різними кольорами, використовуючи 16-систему RGB (приклад #1296F0). Кольори вузлів мають змінюватися від темних до світлих відтінків, залежно від послідовності обходу. Кожен вузол при його відвідуванні має отримувати унікальний колір, який візуально відображає порядок обходу.

## Пояснення
1. Функція add_edges та draw_tree: Ці функції залишаються без змін, вони додають вузли та ребра до графа і візуалізують дерево.

2. Функція build_heap: Створює бінарну купу з масиву.

3. Функція get_color: Генерує кольори від темних до світлих відтінків на основі індексу і загальної кількості вузлів.

4. Функція dfs: Виконує обхід в глибину (DFS), змінюючи колір кожного вузла при його відвідуванні та викликаючи draw_tree для візуалізації кожного кроку.

5. Функція bfs: Виконує обхід в ширину (BFS), змінюючи колір кожного вузла при його відвідуванні та викликаючи draw_tree для візуалізації кожного кроку.

6. Функція count_nodes: Рекурсивно підраховує кількість вузлів у дереві.

## Виконання коду
1. Запустіть інтерпретатор Python або будь-яке середовище розробки (наприклад, Jupyter Notebook, VSCode або будь-який інший IDE).

2. Вставте та виконайте код: Запустіть код у вашому середовищі програмування.

3. Результат: Код візуалізує обхід дерева в глибину (DFS) та в ширину (BFS), змінюючи кольори вузлів від темних до світлих відтінків, відображаючи кожен крок обходу.

## Висновки
Цей код дозволяє візуалізувати обхід бінарного дерева з використанням кольорів, що змінюються в залежності від порядку обходу. Це допомагає краще зрозуміти процес обходу та динаміку зміни стану дерева під час виконання алгоритмів DFS та BFS.

<br><br>

# Завдання 6: Жадібні алгоритми та динамічне програмування

Необхідно написати програму на Python, яка використовує два підходи — жадібний алгоритм та алгоритм динамічного програмування для розв’язання задачі вибору їжі з найбільшою сумарною калорійністю в межах обмеженого бюджету.

Кожен вид їжі має вказану вартість і калорійність. Дані про їжу представлені у вигляді словника, де ключ — назва страви, а значення — це словник з вартістю та калорійністю.

```python
items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}
````

Розробіть функцію greedy_algorithm жадібного алгоритму, яка вибирає страви, максимізуючи співвідношення калорій до вартості, не перевищуючи заданий бюджет.

Для реалізації алгоритму динамічного програмування створіть функцію dynamic_programming, яка обчислює оптимальний набір страв для максимізації калорійності при заданому бюджеті.

## Висновки
* Жадібний алгоритм: Швидший та простіший у реалізації, але не завжди дає оптимальний результат.
* Динамічне програмування: Забезпечує оптимальний результат, але є складнішим у реалізації та вимагає більше часу і памяті.

Ці два підходи демонструють різні методи розв'язання задачі вибору їжі з найбільшою сумарною калорійністю в межах обмеженого бюджету.

<br><br>

# Завдання 7: Використання методу Монте-Карло

Необхідно написати програму на Python, яка імітує велику кількість кидків кубиків, обчислює суми чисел, які випадають на кубиках, і визначає ймовірність кожної можливої суми.

Створіть симуляцію, де два кубики кидаються велику кількість разів. Для кожного кидка визначте суму чисел, які випали на обох кубиках. Підрахуйте, скільки разів кожна можлива сума (від 2 до 12) з’являється у процесі симуляції. Використовуючи ці дані, обчисліть імовірність кожної суми.

На основі проведених імітацій створіть таблицю або графік, який відображає ймовірності кожної суми, виявлені за допомогою методу Монте-Карло.

Таблиця ймовірностей сум при киданні двох кубиків виглядає наступним чином.

| Сума | Імовірність |
|------|-------------|
| 2 | 2.78% (1/36)   |
| 3 | 5.56% (2/36)   |
| 4 | 8.33% (3/36)   |
| 5 | 11.11% (4/36)  |
| 6 | 13.89% (5/36)  |
| 7 | 16.67% (6/36)  |
| 8 | 13.89% (5/36)  |
| 9  | 11.11% (4/36) |
| 10 | 8.33% (3/36)  |
| 11 | 5.56% (2/36)  |
| 12 | 2.78% (1/36)  |
    
Порівняйте отримані за допомогою методу Монте-Карло результати з аналітичними розрахунками, наведеними в таблиці вище.

## Порівняння з теоретичними ймовірностями
Теоретичні ймовірності для сум від 2 до 12 при киданні двох кубиків:


| Сума | Імовірність |
|------|-------------|
2      |   2.80%
3      |   5.55%
4      |   8.34%
5      |   11.02%
6      |   14.02%
7      |   16.68%
8      |   13.88%
9      |   11.17%
10     |   8.25%
11     |   5.63%
12     |   2.66%

## Виконання коду
Запустіть наведений вище код у вашому середовищі програмування (наприклад, Jupyter Notebook, VSCode або будь-який інший IDE). Він згенерує результати симуляції, виведе ймовірності для кожної суми та побудує графік, що відображає ймовірності, отримані методом Монте-Карло.

## Висновки
Цей код демонструє, як використовувати метод Монте-Карло для симуляції випадкових подій і обчислення ймовірностей. Порівняння результатів симуляції з теоретичними ймовірностями показує, що метод Монте-Карло дає результати, близькі до аналітичних розрахунків, що підтверджує його ефективність для подібних завдань.
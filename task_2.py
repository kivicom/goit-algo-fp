import turtle
import math

def draw_pythagoras_tree(t, branch_length, angle, depth):
    if depth == 0:
        return

    t.forward(branch_length)
    new_length = branch_length * math.sqrt(2) / 2

    t.left(angle)
    draw_pythagoras_tree(t, new_length, angle, depth - 1)

    t.right(2 * angle)
    draw_pythagoras_tree(t, new_length, angle, depth - 1)

    t.left(angle)
    t.backward(branch_length)

def main():
    # Створення екрану
    screen = turtle.Screen()
    screen.title("Фрактал 'дерево Піфагора'")
    screen.bgcolor("white")

    # Створення черепахи
    t = turtle.Turtle()
    t.color("brown")
    t.speed(0)
    t.left(90)  # Поворот черепахи вгору

    # Вхідні дані від користувача
    depth = int(input("Введіть рівень рекурсії: "))
    branch_length = 100  # Довжина початкової гілки
    angle = 45  # Кут повороту

    # Малювання фрактала
    draw_pythagoras_tree(t, branch_length, angle, depth)

    # Завершення роботи
    t.hideturtle()
    screen.mainloop()

if __name__ == "__main__":
    main()

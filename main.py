import cmath


def find_roots(a, b, c):
    # Вычисление корней уравнения вида: a * x^2 + b * x + c = 0.
    # Проверка на корректность коэффициентов
    if a == 0:
        raise ValueError("Первый коэффициент не может быть равен нулю для квадратного уравнения")

    if not all(isinstance(coef, (int, float)) for coef in (a, b, c)):
        raise TypeError("Коэффициенты должны быть числами")

    discriminant = b ** 2 - 4 * a * c

    sqrt_disc = cmath.sqrt(discriminant)
    denominator = 2 * a

    if discriminant > 0:
        root1 = (-b + sqrt_disc) / denominator
        root2 = (-b - sqrt_disc) / denominator
        return (root1, root2)
    elif discriminant == 0:
        root = -b / denominator
        return (root)
    else:
        root1 = (-b + sqrt_disc) / denominator
        root2 = (-b - sqrt_disc) / denominator
        return (root1, root2)

# Пример использования
a = -1
b = -5
c = 6

result = find_roots(a, b, c)
print("Корни уравнения:", result)

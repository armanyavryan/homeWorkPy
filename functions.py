# number = int(input())
def is_borring(number):
    x = number % 10
    number //= 10
    while number > 0:
        y = number % 10
        if y != x:
            break
        number //= 10

    return number <= 0

def line_segment_intersection(a1, b1, a2, b2):
    if a1>b1:
        a1, b1 = b1, a1
    if a2>b2:
        a2, b2 = b2, a2

    if a1 < a2 < b1:
        if b2 < b1:
            return b2 - a2
        else:
            return b1 - a2
    elif a1 < b2 < b1:
        if a1>a2:
            return b2 - a1
        else:
            return b2 - a2
    else:
        return 0


import math


def divisors_count(x):
    counts = 0
    for i in range (1, (int)(math.sqrt(x)) + 1):
        fdiv = x / i
        idiv = x // i
        isIntDivided = fdiv == idiv
        if  isIntDivided:
            if  idiv != i:
                counts += 2
            else:
                counts += 1
    return counts

# print("count:", divisorsCount(3))

def quadratic_equation(a, b, c):
    if a == 0:
        print("Non-quadratic equation")
        if b == 0:
            if c == 0:
                print("Infinite solutions")
            else:
                print("No solutions")
        else:
            x = - c / b
            print(f"One solution: {x}")
    else:
        print("Quadratic equation")
        d = b*b - 4*a*c
        print(f"Discriminant: {d}")
        if d < 0:
            print("No Solutions")
        elif d == 0:
            x = -b / a
            print(f"One solution: {x}")
        else:
            x1 = (-b + math.sqrt(d)) / a / 2
            x2 = (-b - math.sqrt(d)) / a / 2
            print(f"Two solutions: {x1} {x2}")


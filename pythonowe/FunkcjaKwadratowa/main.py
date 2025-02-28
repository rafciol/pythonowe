import math

print("\n Witaj! Co mam Ci policzyć? :) \n")
print("1. Miejsca zerowe\n2. Z postaci ogólnej na iloczynową\n3. Z postaci ogólnej na kanoniczną\n")
choice = int(input("Twój wybór: "))

def liczMiejscaZerowe(fa, fb, fc):
    delta = pow(fb, 2) - (4*fa*fc)

    if delta > 0:
        x1 = (-fb + math.sqrt(delta)) / 2*fa
        x2 = (-fb - math.sqrt(delta)) / 2*fa
        return x1, x2
    elif delta == 0:
        x0 = ((fb * (-1)) / 2*fa)
        return x0
    else:
        return "Funkcja nie ma miejsc zerowych."

if choice == 1:
    print("Funkcja kwadratowa ma postać: ax^2 + bx + c\n")
    a = float(input("Podaj a: "))
    b = float(input("Podaj a: "))
    c = float(input("Podaj a: "))
    print("Miejsca zerowe funkcji: ", liczMiejscaZerowe(a, b, c))
elif choice == 2:
    print("Funkcja kwadratowa ma postać: ax^2 + bx + c\n")
elif choice == 3:
    print("Funkcja kwadratowa ma postać: ax^2 + bx + c\n")
else:
    print("Nie ma takiej opcji, wybierz inną!")



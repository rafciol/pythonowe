import math

print("\n Witaj! Co mam Ci policzyć? :) \n")
print("1. Miejsca zerowe\n2. Z postaci ogólnej na iloczynową\n3. Z postaci ogólnej na kanoniczną\n")
choice = int(input("Twój wybór: "))


def liczMiejscaZerowe(fa, fb, fc):
    delta = pow(fb, 2) - (4 * fa * fc)

    if delta > 0:
        x1 = (-fb + math.sqrt(delta)) / (2 * fa)
        x2 = (-fb - math.sqrt(delta)) / (2 * fa)
        return x1, x2
    elif delta == 0:
        x0 = (-fb) / (2 * fa)
        return x0,
    else:
        return None

def schowajWspolczynnik(wk):
    if wk == 1:
        wk = ''
    else:
        wk = round(wk)

    return wk


if choice == 1:
    print("Funkcja kwadratowa ma postać: ax^2 + bx + c\n")
    a = float(input("Podaj a: "))
    b = float(input("Podaj b: "))
    c = float(input("Podaj c: "))

    miejsca_zerowe = liczMiejscaZerowe(a, b, c)
    if miejsca_zerowe:
        print("Miejsca zerowe funkcji:", miejsca_zerowe)
    else:
        print("Funkcja nie ma miejsc zerowych.")

elif choice == 2:
    print("Funkcja kwadratowa ma postać: ax^2 + bx + c\n")
    a = float(input("Podaj a: "))
    b = float(input("Podaj b: "))
    c = float(input("Podaj c: "))

    miejsca_zerowe = liczMiejscaZerowe(a, b, c)

    if miejsca_zerowe is None:
        print("Nie można zapisać w postaci iloczynowej – brak miejsc zerowych.")
    elif len(miejsca_zerowe) == 1:
        x0 = miejsca_zerowe[0]

        a = schowajWspolczynnik(a)

        if x0 < 0:
            print(f"Postać iloczynowa to: {a}(x + {x0})²")
        else:
            print(f"Postać iloczynowa to: {a}(x - {x0})²")

    else:
        a = schowajWspolczynnik(a)

        x1, x2 = miejsca_zerowe

        x1 = round(x1)
        x2 = round(x2)

        if x1 < 0 and x2 > 0:
            print(f"Postać iloczynowa to: {a}(x + {-x1}) (x - {x2})")
        elif x1 > 0 and x2 < 0:
            print(f"Postać iloczynowa to: {a}(x - {x1}) (x + {-x2})")
        elif x1 < 0 and x2 < 0:
            print(f"Postać iloczynowa to: {a}(x + {-x1}) (x + {-x2})")
        else:
            print(f"Postać iloczynowa to: {a}(x - {x1}) (x - {x2})")

elif choice == 3:
    print("Funkcja kwadratowa ma postać: ax^2 + bx + c\n")
    a = float(input("Podaj a: "))
    b = float(input("Podaj b: "))
    c = float(input("Podaj c: "))

    p = round(-b * 2*a)
    q = round(((pow(b, 2) - 4*a*c) * (-1)) / 4*a)

    if a == 1:
        a = ''
    else:
        a = round(a)

    if p < 0 and q > 0:
        print(f"Postać kanoniczna to: {a}(x + {-p})² + {q}")
    elif p > 0 and q < 0:
        print(f"Postać kanoniczna to: {a}(x - {p})² + {-q}")
    elif p < 0 and q < 0:
        print(f"Postać kanoniczna to: {a}(x + {-p})² - {-q}")
    else:
        print(f"Postać kanoniczna to: {a}(x - {p})² - {q}")

else:
    print("Nie ma takiej opcji, wybierz inną!")

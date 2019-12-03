# Tutaj zaczynamy nasza przygode
# Instrukcja print() wypisze nam w konsoli
# Podany przez nas argument
print("Hello World")

# Ponizej znajduja sie przyklady deklaracji zmiennych
# Zmienne mozemy traktowac jako swego rodzaju pojemniki
# na informacje. W jezyku Python nie trzeba myslec wczesniej
# o typach danych, dlatego mowimy, ze jest on jezykiem typowanym
# dynamicznie
variable = 10
a, b, c = -2, 3, 4
name = "Adrian"

print(variable)
print(a, b, c)
print(name)

# Na zmiennych mozemy wykonywac podstawowe operacje
# takie jak dodawanie, odejmowanie, mnozenie, dzielenie
result = a + b + c
print(result)
print(a + b + c)

# mozemy w "podobny" sposob dzialac na stringach
print(name + name)
# print(name*name) da mam blad
print(name * b)

# Jak wyznaczyc miejsca zerowe funkcji kwadratowej?
import math  # Niezbedna biblioteka do wyliczenia pierwiastka

a = int(input("Podaj wspl. a: "))  # Musimy wykonac rzutowanie na typ int, poniewaz
b = int(input("Podaj wspl. b: "))  # instrukcja input domyslnie zwraca nam typ string
c = int(input("Podaj wspl. c: "))  # co znacznie utrudni nam dzialania arytmetyczne

delta = b ** 2 - 4 * a * c       # zapis x ** y oznacza podniesienie x do potegi y

if delta < 0:                                           # operatory: <, >, <=, >=, ==
    print("brak miejsc zerowych")                       # zlozone warunki powstaja dzieki: and oraz or
elif delta == 0:                                        # negacje uzyskujemy przy pomocy: !
    print("jedno miejsce zerowe w x = ", -b / (2 * a))
elif delta > 0:                                         # Wciecia definiuja nam zakres dzialania, blok kodu
    print("x1 = ", (-b - math.sqrt(delta)) / (2 * a))
    print("x2 = ", (-b + math.sqrt(delta)) / (2 * a))

# Lista to zmienna zawierajaca zbior elementow.
# Elementami listy moga byc wszystkie dostepne w Python typy danych

list_of_numbers = [0, 1, 2, 3, 4, 5, 6]
list_of_words = ["Bardzo", "lubie", "pythona"]
mixed_list = [0, 1, "banan", "lista", 2, "przyklad"]

print(list_of_numbers)
print(list_of_words)
print(mixed_list)

print(list_of_numbers[3])     # wyswietlanie okreslonego elementu listy
print(list_of_words[-1])      # wyswietlanie ostatniego elementu listy
                              # (wartosci ujemne mozemy rozumiec jako "liczone od konca"

print(mixed_list[1:4])   # wyswietlanie pewnego fragmentu listy
print(mixed_list[1:])

print(True if "lista" in mixed_list else False)     # inline if, tworzymy go w sposob nastepujacy
                                                    # co_jesli_prawda if warunek else co_jesli_falsz

list_of_words.append("a")   # Dodanie jednego elementu do listy
list_of_words.extend(["listy", "są", "spoko"])  # powiekszenie listy o dodatkowy zbior elementow
mixed_list.insert(3, 42)     # umieszczenie elementu w wyznaczonym miejscu listy

print(list_of_words)
print(list_of_numbers)

list_of_numbers.remove(5)
print(list_of_numbers)

list0 = [1, 2, 3, 4, 5, 5, 6, 5]

# do usuniecia wielu tych samych elementow potrzebowac bedziemy petli

for x in range(5):  # range okresla nam wartosc liczbowa, ile razy petla ma sie wykonac
    print(x)

for element in list0:   # mozemy tez przechodzic dzieki takiej petli przez wszystkie elementy listy
    print(element)

# while True:
#     print("python")

without_5 = [element for element in list0 if element != 5]
print(without_5)

while 5 in list0:
    list0.remove(5)

print(list0)

p_str = ""
for row in range(0, 7):
    for column in range(0, 7):
        if column == 1 or ((row == 0 or row == 3) and 0 < column < 5) or \
                ((column == 5 or column == 1) and (row == 1 or row == 2)):
            p_str = p_str + "*"
        else:
            p_str = p_str + " "
    p_str = p_str+"\n"
print(p_str)

y_str = ""
for row in range(0, 7):
    for column in range(0, 7):
        if column == 3 and 2 < row < 7 or (column == row or column == 6 - row) and row < 3:
            y_str = y_str + "*"
        else:
            y_str = y_str + " "
    y_str = y_str + "\n"
print(y_str)

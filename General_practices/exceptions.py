#  Errors and Exceptions
"""
Két fő csoport: syntax errors, exceptions

Syntax errors:
- elírás beli probléma, nem megfelelő szintaxis esetén jön elő
- fontos tudni, hogy a javítás nem mindig az aláhúzott résznél szükséges

Exception:
- olyan hiba, amit a program futás közben kezelhet try/except segítségével.
"""

def ZeroDivisionError():
    print(x = 5 / 0)


def FileNotFoundError():
    open("nincs_ilyen.txt")


def KeyError():
    d = {"nev": "Anna"}
    print(d["kor"])


def IndexError():
    l = [1, 2, 3]
    print(l[5])


def ValueError():
    int("abc")


def TypeError():
    print("szoveg" + 5)


"""
try/except blokkon belül is használhatóak:
try:
    ....
except ValueError:
    ....

Ilyenkor az except csak akkor fut le ha ValueErrorba fut a blokk. Ezzel szemben ha except Exception: akkor minden kivételt elkap.
Ez utóbbival a fő probléma hogy elrekti hogy pontosan milyen hiba történt, így nehezebb debugolni.
Éppen ezért érdemes sepcifikálni a kivételt, mert könnyebb megoldani és kezelni a hibát.
"""
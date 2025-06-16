#  *args - tetszőleges számú paraméter (  funkció("teszt", 42, paramtéter) )
#  **kwargs - tetszőleges számú név = érték páros paramtére(kulcsszavas) (  funkció(nev='Lajos', kor=32, pro=True)  )



def osszegzo(*args):
    return sum(args)

print(osszegzo(1, 6, 8, 21, 34))


def mutasd(**kwargs):

    for key, value in kwargs.items():
        print(f"{key}: {value}")

mutasd(nev='Pepsi Béla', kor=45, hobbi='Amíg van bor, menni.')

def tipusok(*args):
    for elem in args:
        print(type(elem))

tipusok("hello", 42, 3.14, True)


def van_email(**kwargs):
    return 'email' in kwargs

print(van_email(nev='Lajos', email='lajos@teszt.hu'))
print(van_email(nev='Béla', kor=55))


def nevjegy(**kwargs):
    return "\n".join([f"{k.capitalize()}: {v}" for k, v in kwargs.items()])

print(nevjegy(név='Béla', jármű="Bicaj", üzemanyag='JófajtaBor'))
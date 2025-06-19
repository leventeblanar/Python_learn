#  list comprehension: olyan min egy for ciklus egy sorban
#  alap szintaxis: [kifejezés for elem in iterálható]
#  szűréssel: [kifejezés for elem in iterálható if feltétel]


def squares():

    squares = [x**2 for x in range (15)]
    print(squares)


def even_numbers():

    evens = [x for x in range(21) if x%2 == 0]
    print(evens)


def word_lenghts():

    words = ['alma', 'körte', 'cseresznye']

    words_len = [len(word) for word in words]
    print(words_len)


def sort_by_lenght():

    words = ['alma', 'körte', 'cseresznye']


    long_words = [w for w in words if len(w) >= 5]
    print(long_words) 


def conv_to_str():

    weights = [10, 25, 50]

    labels = [str(weight) + 'kg' for weight in weights]
    print(labels)


def positive_num():

    matrix = [[-1, 2, -3], [4, -5, 6]]

    positive_num = [num for row in matrix for num in row if num > 0]
    print(positive_num)


#  lista azon 1-20ig terjedő számokból amik párosak

def list_from_1_20():

    evens = [x for x in range(21) if x%2 == 0]
    squares = [y**2 for y in evens]
    print(squares)


def kisbetusites():
    
    words = ["Alma", "Körte", "barack", "SZILVA", "kiwi"]

    kisbetus = [word.lower() for word in words]
    at_least_5 = [word for word in kisbetus if len(word) >= 5]

    print(at_least_5)


def multiply_if_greater_10():

    numbers = [5, 8, 12, 25, 3, 18]

    greater_10 = [num for num in numbers if num > 10]
    multiply_2 = [num*2 for num in greater_10]

    print(multiply_2)


def dict_kulcs():

    adatok = {'a': 50, 'b': 120, 'c': 200, 'd': 85}

    keys_select = [keys for keys, value in adatok.items() if value > 100]

    print(keys_select)

def select_lista():

    lista1 = [1, 2, 3]
    lista2 = [2, 3, 4]

    parok = [(x, y) for x in lista1 for y in lista2 if x != y]

    print(parok)

def lista_from_tetelek():

    arak = {
    'kenyér': 499,
    'tej': 299,
    'vaj': 1290,
    'sajt': 1890,
    'alma': 499,
    'kávé': 2790
    }

    ezer_felett = [termek for termek, ar in arak.items() if ar > 1000]
    print(ezer_felett)


def targy_paros():

    diakok = ["Peti", "Anna"]
    tantargyak = ["matek", "töri", "biosz"]

    parok = [(diak, targy) for diak in diakok for targy in tantargyak if ((diak, targy) != ('Peti', 'matek'))]

    print(parok)

targy_paros()
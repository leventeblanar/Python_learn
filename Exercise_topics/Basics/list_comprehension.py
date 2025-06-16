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

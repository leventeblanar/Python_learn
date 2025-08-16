import re
from collections import Counter
from itertools import zip_longest, groupby
from collections import defaultdict

def select_emails():

    adatok = [
    "peter@gmail.com",
    "nememail.com",
    "hello@valami",
    "teszt@abc.hu",
    "ez.sem.jo",
    "no@dot"
    ]

    valid_emails = [s for s in adatok if "@" in s and "." in s.split("@")[-1]]
    print(valid_emails)


def capitelize_institution_names():

    adatok = [
        "moricz zsigmond általános iskola",
        "szegedi tudomany egyetem"
    ]

    for adat in adatok:
        adat_split = (adat.split(" "))
        capitelized =( [s.capitalize() for s in adat_split])
        uj_nev = " ".join(capitelized)
        print(uj_nev)
        

def normalize_words():

    tantargyak = [
    "matek",
    "fizika",
    "foldrajz",
    "testneveles",
    "irodalom",
    "tortenelem",
    "kemia",
    "biologia",
    "informatika",
    "enektanctestneveles"
    ]

    kulcsszavak = [
        "enek", "tanc", "testneveles", "matek", "fizika", "foldrajz",
        "irodalom", "tortenelem", "kemia", "biologia", "informatika"
    ]


    eredmeny = []
    
    for szo in tantargyak:
        i = 0
        while i<len(szo):
            talalat = False
            for kulcs in sorted(kulcsszavak, key=len, reverse=True):
                if szo[i:].startswith(kulcs):
                    eredmeny.append(kulcs)
                    i+=len(kulcs)
                    talalat = True
                    break
            if not talalat:
                i+=1
    
    nagybetusek = []
    
    for item in eredmeny:
        nagybetusek.append(item.capitalize())

    print(nagybetusek)


def create_normal_form():

    rovidites_szo = {
    "elte": "eötvös loránd tudományegyetem",
    "bme": "budapesti műszaki és gazdaságtudományi egyetem",
    "szte": "szegedi tudományegyetem",
    "ttk": "természettudományi kar",
    "ikt": "informatikai kar",
    "info": "informatika",
    "irod": "irodalom",
    "bio": "biológia",
    "kem": "kémia",
    "matek": "matematika",
    "tesi": "testnevelés"
    }
    
    eredmeny = []

    for rovid, hosszu in rovidites_szo.items():
        eredmeny.append(hosszu.title())

    print(eredmeny)


def short_form():

    intezmenyek = [
    "eotvos lorand tudomanyegyetem",
    "budapesti muszaki es gazdasagtudomanyi egyetem",
    "szegedi tudomanyegyetem",
    "informatikai kar",
    "informatika",
    "matematika",
    "biologia",
    "ismeretlen egyetem"
    ]

    hosszu_to_rovid = {
        "eotvos lorand tudomanyegyetem": "elte",
        "budapesti muszaki es gazdasagtudomanyi egyetem": "bme",
        "szegedi tudomanyegyetem": "szte",
        "termeszettudomanyi kar": "ttk",
        "informatikai kar": "ikt",
        "informatika": "info",
        "irodalom": "irod",
        "biologia": "bio",
        "kemia": "kem",
        "matematika": "matek",
        "testneveles": "tesi"
    }

    for hosszu, rovid in hosszu_to_rovid.items():
        if hosszu in intezmenyek:
            print(rovid)
        else:
            print(f"No match for {hosszu}")

    for nev in intezmenyek:
        rovidites = hosszu_to_rovid.get(nev, "???")
        print(f"{nev.title()} -> {rovidites.upper()}")


def create_list_to_read_from():

    tantargyak = [
    "matek",
    "fizika",
    "foldrajz",
    "testneveles",
    "irodalom",
    "tortenelem",
    "kemia",
    "biologia",
    "informatika",
    "enektanctestneveles"
    ]

    kulcsszavak = [
        "enek", "tanc", "testneveles", "matek", "fizika", "foldrajz",
        "irodalom", "tortenelem", "kemia", "biologia", "informatika"
    ]

    eredmeny = []

    for kulcsszo in kulcsszavak:
        if kulcsszo in tantargyak:
            eredmeny.append(kulcsszo)
    
    print(eredmeny)


def filter_invalid_usernames():

    usernames = [
    "peter123",
    "anna",
    "béla",
    "Juli",
    "ka",
    "rozi!",
    "endre",
    "viola"
    ]

    valid_usernames = []

    for name in usernames:
        if (
            len(name) >= 3 and
            name.isalpha() and
            name.islower() and
            all(ord(c) < 128 for c in name)
        ):
            valid_usernames.append(name)

    print(valid_usernames)


def normalize_phone_numbers():

    szamok = [
    "+36 30 123 4567",
    "06301234567",
    "30-123-4567",
    "06 1 234 5678",
    "0670123456",
    "1234567890",
    "06-70-1234-567"
    ]

    valid_phone_numbers = []

    for szam in szamok:
        szam_onlydigits = szam.replace("-", "").replace(" ", "").replace("+", "").strip("")

        if szam_onlydigits.startswith("36") and len(szam_onlydigits) == 11:
            szam_onlydigits = "0" + szam_onlydigits[1:]

        if len(szam_onlydigits) == 11 and szam.startswith("06"): 
            format_szam = f"+36 {szam_onlydigits[2:4]} {szam_onlydigits[4:7]} {szam_onlydigits[7:11]}"
            valid_phone_numbers.append(format_szam)

        print(szam_onlydigits)

    print(valid_phone_numbers)


def normalize_email_addresses():

    emails = [
        "  John.Doe@Example.com ",
        "user@example",
        "JANE@DOMAIN.HU",
        "wrongemail.com",
        "a@b.c",
        " test@valid.email  ",
        "nincs@pontosszeomlas"
    ]

    valid_email_addresses = []

    for email in emails:

        email_normalform = email.lower().strip()
        if "@" in email_normalform and "." in email_normalform.split("@")[-1]:
            valid_email_addresses.append(email_normalform)

    
    print(valid_email_addresses)


def normalize_names():

    names = [
    " John 123 Doe ",
    "JANE-Doe!!",
    "AnNa    MaRiA",
    "roBERT   smith ",
    "@Chris_O'Neil",
    "L@ur@ 123"
    ]

    normalized_names = []

    for name in names:
        normalized_name = re.sub(r'[^a-zA-Z\s]', '', name)
        normalized_name = normalized_name.lower().strip()
        name_final_form = re.sub(r'\s+', ' ', normalized_name)
        normalized_names.append(name_final_form)

    print(normalized_names)


def normalize_job_titles():

    titles = [
    "Senior-Developer (Python/Backend)!!!",
    "Data-Scientist 2023",
    "Junior QA Engineer!!",
    "DevOps@Lead#AWS",
    "Intern / Support",
    "CEO - Chief! Exec. Officer"
    ]

    normalized_jobs = []

    for title in titles:
        form_1st = re.sub(r"[^a-zA-Z\s()]", "", title)
        form_2nd = re.sub(r'\s+', ' ', form_1st).strip()
        final_form = form_2nd.lower().title()

        normalized_jobs.append(final_form)

    print(normalized_jobs)


def word_frequency():

    text = """
    Python is great, and Python is easy to learn. Python is loved by developers.
    Many developers use Python for web development, data analysis, machine learning, and more.
    """

    formated_text = re.sub(r'[^\w\s]', '', text)
    words = formated_text.lower().split(" ")

    counter = Counter(words)

        
    print(f"All the words: {counter}")
    print(f"5 most common: {counter.most_common(5)}")


def char_and_word_analyzer():

    text = """
    When using Python, it’s common to want to know how often characters or words appear.
    With Counter, you can get that info super easily. It’s awesome!
    """

    formated_text = re.sub(r'[^a-zA-Z\s]', '', text).lower()

    letter_counter = Counter(formated_text.replace(" ", ""))
    karakter_szamok = Counter(len(word) for word in formated_text.split(" "))

    for key, val in karakter_szamok.items():
        if key in (1, 2):
            print (f"{key} karakterből álló: {val}db")
    
    print(f'Number of each letters: {letter_counter}')


def starst_with_counter():

    text = """
    Data science is a dynamic and diverse field. Developers and data analysts use Python, SQL, and statistics 
    to solve practical problems. Strong skills in programming, problem-solving, and statistical thinking are 
    essential for success in data-driven industries. Sometimes data determines direction, sometimes people do.
    """

    formated_text = re.sub(r'[^a-zA-Z\s]', '', text).lower().split()

    first_letter = [word[0] for word in formated_text if word]

    first_letter_counter = Counter(first_letter)

    print(first_letter_counter)
    print(f"Most common 5: {first_letter_counter.most_common(5)}")


def match_people_to_roles():

    names = ['Anna', 'Béla', 'Csaba', 'Dóra']
    roles = ['Backend Developer', 'Project Manager', 'QA Engineer', 'Data Scientist']

    print("*** List of employees ***")
    for name, role in zip(names, roles):
        print(f"Employee: {name} - Role: {role}")


def print_team_overview():

    names = ['Anna', 'Béla', 'Csaba']
    roles = ['Backend Developer', 'Project Manager', 'QA Engineer', 'Data Scientist']

    if len(names) != len(roles):
        print("Warning: A name lista és roles lista hossza nem egyezik.")

    print("Team overview:")

    for index, (name, role) in enumerate(zip_longest(names, roles, fillvalue="N/A"), start=1):
        print(f"{index}. {name} - {role}")


def list_attendees_with_topics():

    attendees = ['Alex', 'Morgan', 'Taylor']
    topics = ['Docker basics', 'Debugging Python', 'Data pipelines', 'Unit testing']

    if len(attendees) != len(topics):
        print(f"Az attendees és topics list hossza nem egyezik.")

    print("Topics overview: ")

    for index, (attendee, topic) in enumerate(zip_longest(attendees, topics), start=1):
        if not attendee:
            attendee = "Extra topic (no presenter)"

        if not topic:
            topic = "No topic provided"
        
        print(f"{index}. {attendee} - {topic}")


def longest_word_in_list():

    words = [
    "analytics", "data", "machinelearning", "visualization", "python",
    "cloud", "statistics", "bigdata", "infrastructure", "model"
    ]

    longest_item = max(len(word) for word in words)
    shortest_item = min(len(word) for word in words)

    for index, word in enumerate(words, start=1):
        if len(word) == longest_item:
            print(f"The lognest word is at position {index}: '{word}' (length: {longest_item}) ")
        else:
            print(f"{index}. The word '{word}' is {len(word)} characters.")


def group_words_by_first_letter():

    words = [
    "Python", "pandas", "data", "dictionary", "debug", "loop", "lambda", 
    "List", "log", "map", "merge", "Machine", "model"
    ]

    grouped = defaultdict(list)

    for word in words:
        key = word[0].lower()
        grouped[key].append(word)

    print("Words grouped by first letter:\n")
    for letter, word_list in grouped.items():
        print(f"{letter}: {word_list}")

def group_words_by_length():

    words = [
    "data", "deep", "learning", "AI", "model", "train", "test", "predict", 
    "accuracy", "loss", "val", "epoch", "batch", "GPU", "CPU"
    ]

    grouped = defaultdict(list)

    for word in words:
        key = len(word)
        grouped[key].append(word)

    print("Words grouped by their length: ")
    for length, word_list in sorted(grouped.items()):
        print(f"{length}: {word_list}")


def group_words_by_last_letter():

    words = [
    "data", "panda", "alpha", "gamma", "theta", "delta", "omega", "zebra",
    "tuna", "kappa", "agenda", "banana", "drama", "area", "camera"
    ]

    grouped = defaultdict(list)

    for word in words:
        key = word[-1].lower()
        grouped[key].append(word)

    print("Words grouped by their last letter:")
    for last_letter, word_list in sorted(grouped.items()):
        print(f"{last_letter}: {word_list}")


def group_words_by_last_letter_v2():

    words = [
    "drive", "dive", "alive", "brave", "cave", "give", "love",
    "stone", "phone", "clone", "bone", "zone", "cone"
    ]

    grouped = defaultdict(list)

    for word in words:
        key = word[-1].lower()
        grouped[key].append(word)

    print("Words grouped by their last letter:")
    for last_letter, word_list in sorted(grouped.items()):
        print(f"{last_letter}: {word_list}")


def find_shortest_word():

    words = [
    "network", "AI", "backend", "frontend", "UX", "UI", "data", "devops", "api"
    ]

    shortest_words_list = []

    shortest_word = min(len(word) for word in words)

    for index, word in sorted(enumerate(words, start=1)):
        if len(word) == shortest_word:
            shortest_words_list.append((word, index))
        else:
            print(f"At index {index}: {word} is {len(word)} characters long.")

    print("However there are multiple words with the least amount of characters that are the following: ")
    for word, index in shortest_words_list:
        print(f"{word} is {len(word)} characters long and is at {index}")


def count_starting_letters():

    words = [
    "python", "pandas", "programming", "data", "debugging", "development", 
    "machine", "model", "memory", "logic", "language", "lambda", "loop"
    ]

    grouped = defaultdict(int)

    for word in words:
        key = word[0].lower()
        grouped[key] += 1

    print("Starting letter counter:")

    for key, counter in sorted(grouped.items()):
        print(f"{key}: {counter}")
    

def count_starting_ending_letter_match():

    words = [
    "level", "data", "deed", "code", "python", "radar", "loop", 
    "non", "refer", "stats", "banana", "alpha", "civic"
    ]

    grouped = defaultdict(int)

    for word in words:
        starts = word[0].lower()
        ends = word[-1].lower()
        if starts == ends:
            grouped[starts] += 1

    for letter, word_list in sorted(grouped.items()):
        print(f"{letter}: {word_list}")


def group_words_by_length_and_starting_letter():

    words = [
    "python", "data", "debug", "pandas", "machine", "model", "learning", 
    "api", "loop", "lambda", "logic", "script"
    ]

    grouped = defaultdict(list)

    for word in words:
        key = len(word)
        grouped[key].append(word)

    for length in grouped:
        grouped[length].sort()


    for length, word_list in sorted(grouped.items()):
        print(f"{length}: {word_list}")


def group_animals_by_first_letter():

    animals = [
    "zebra", "antelope", "alligator", "cat", "cougar", "cheetah",
    "dog", "donkey", "deer", "elephant", "emu", "eel"
    ]

    animals.sort(key=lambda x: x[0])

    for letter, group in groupby(animals, key=lambda x: x[0]):
        print(f"{letter}: {list(group)}")


def group_numbers_by_parity_and_range():

    def group_by(n):
        prarity = 'even' if n % 2 == 0 else 'odd'
        decade = f"{(n // 10) * 10}s"
        return f"{prarity}-{decade}"

    numbers = [
    1, 2, 5, 7, 10, 12, 13, 15, 22, 24, 27, 30, 33, 36, 37, 40, 41
    ]

    numbers.sort(key=group_by)

    for key, group in groupby(numbers, key=group_by):
        print(f"Group: {key} - {list(group)}")


def group_names_by_first_letter_and_length():

    names = [
    "Alice", "Albert", "Alex", "Anna", "Bob", "Ben", "Brenda", 
    "Cathy", "Carl", "Cameron", "Clara", "David", "Derek", "Dana"
    ]

    def group_by(name):
        first_letter = name[0].lower()
        length = len(name)
        return f"{first_letter}-{length}"

    names.sort(key=group_by)

    for key, group in groupby(names, key=group_by):
        print(f"Group: {key} - {list(group)}")

group_names_by_first_letter_and_length()
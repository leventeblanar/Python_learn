import random

print("Üdv a szuper-extra kvízjátékban!")
print("*******************************************")
print("A szabályok:")
print("- Minden kérdésnek csak egy helyes válasza van.")
print("- Egyszerűen válaszolj A, B, C vagy D betű beírásával.")
print("- Minden helyes válaszért kapsz egy pontot.")
print("- A sikeres teljesítéshez 75%-ot kell elérned.")
print("*******************************************")





def load_questions():  #simply returning the dictionary of questions here
    return [
        {"question": "Mi Magyarország fővárosa?", 
        "options": ["A) Budapest", "B) Pécs", "C) Debrecen", "D) Szeged"], 
        "answer": "A"},

        {"question": "Melyik évben kezdődött az első világháború?", 
        "options": ["A) 1914", "B) 1939", "C) 1815", "D) 1905"], 
        "answer": "A"},

        {"question": "Melyik bolygó a Naprendszer legnagyobb bolygója?", 
        "options": ["A) Mars", "B) Jupiter", "C) Föld", "D) Szaturnusz"], 
        "answer": "B"},

        {"question": "Hány kontinens található a Földön?", 
        "options": ["A) 5", "B) 6", "C) 7", "D) 8"], 
        "answer": "C"},

        {"question": "Ki írta a 'Pál utcai fiúk' című regényt?", 
        "options": ["A) Jókai Mór", "B) Móricz Zsigmond", "C) Molnár Ferenc", "D) Gárdonyi Géza"], 
        "answer": "C"},

        {"question": "Melyik elem kémiai jele az O?", 
        "options": ["A) Oxigén", "B) Arany", "C) Ólom", "D) Hidrogén"], 
        "answer": "A"},

        {"question": "Milyen színű a nulla a rulettkeréken?", 
        "options": ["A) Piros", "B) Fekete", "C) Zöld", "D) Fehér"], 
        "answer": "C"},

        {"question": "Ki festette a Mona Lisát?", 
        "options": ["A) Michelangelo", "B) Leonardo da Vinci", "C) Rembrandt", "D) Van Gogh"], 
        "answer": "B"},

        {"question": "Melyik a legnagyobb óceán a Földön?", 
        "options": ["A) Atlanti-óceán", "B) Indiai-óceán", "C) Csendes-óceán", "D) Jeges-tenger"], 
        "answer": "C"},

        {"question": "Melyik sportágban használnak ütőt és labdát?", 
        "options": ["A) Kosárlabda", "B) Tenisz", "C) Futball", "D) Jégkorong"], 
        "answer": "B"},

        {"question": "Milyen állat szerepel a magyar címerben?", 
        "options": ["A) Oroszlán", "B) Turul", "C) Medve", "D) Szarvas"], 
        "answer": "B"},

        {"question": "Melyik a periódusos rendszer első eleme?", 
        "options": ["A) Hélium", "B) Hidrogén", "C) Lítium", "D) Oxigén"], 
        "answer": "B"},

        {"question": "Melyik város híres a Colosseumról?", 
        "options": ["A) Párizs", "B) Athén", "C) Róma", "D) Madrid"], 
        "answer": "C"},

        {"question": "Milyen színnel jelölik általában a hideg víz csapját?", 
        "options": ["A) Piros", "B) Kék", "C) Zöld", "D) Fekete"], 
        "answer": "B"},

        {"question": "Melyik évben ember lépett először a Holdra?", 
        "options": ["A) 1961", "B) 1969", "C) 1972", "D) 1980"], 
        "answer": "B"},

        {"question": "Melyik anyag olvadáspontja alacsonyabb?", 
        "options": ["A) Víz", "B) Higany", "C) Arany", "D) Vas"], 
        "answer": "B"},

        {"question": "Hány órából áll egy nap?", 
        "options": ["A) 12", "B) 24", "C) 48", "D) 72"], 
        "answer": "B"},

        {"question": "Melyik növény adja a csokoládé alapanyagát?", 
        "options": ["A) Kakaó", "B) Kávé", "C) Vanília", "D) Fahéj"], 
        "answer": "A"},

        {"question": "Hány lába van egy póknak?", 
        "options": ["A) 6", "B) 8", "C) 10", "D) 12"], 
        "answer": "B"},

        {"question": "Melyik ország található a Kangaroo Island?", 
        "options": ["A) Új-Zéland", "B) Dél-Afrika", "C) Ausztrália", "D) Kanada"], 
        "answer": "C"}
]
def get_random_question(questions): # generating a random choice from the questions dict.
    return random.choice(questions) 

def ask_question(random_question): # display random_question, iterating through the options in the random_question and dusplaying it, finally asking for input and returning it
    print("Kérdés: ", random_question["question"])

    for option in random_question['options']:
        print(option)
    user_answer = input("Írd be a válaszod (A, B, C, D): ").strip().upper()
    return user_answer

def check_answer(user_answer, correct_answer): # check answer -> return user_answer == correct_answer () <- the correct_answer is known by defining it in the main() by providing the random_question['answer'] argument in the check_answer()
    return user_answer == correct_answer # return statements only give a value back, since we do not need to create a new variable, this way we can assign the value to the function

def main():
    questions = load_questions()
    points = 0

    while questions:  # Python handles empty dictionaries as False - so the program runs until the dict. has any elements - we are removing them one by one after answering them
        random_question = get_random_question(questions)
        user_answer = ask_question(random_question)

        if check_answer(user_answer, random_question["answer"]):
            print("Helyes! Szereztél egy pontot!\n")
            points += 1
        else:
            print(f"Helytelen! A helyes válasz: {random_question['answer']}.\n")

        questions.remove(random_question)

    total_questions = len(load_questions())
    passing_score = total_questions * 0.75
    print(f"A játék véget ért! Az összpontszámod: {points}/{total_questions}.")

    if points >= passing_score:
        print("Gratulálok! Sikeresen teljesítetted a kvízt! 🎉")
    else:
        print("Sajnos nem érted el a szükséges pontszámot. Próbáld újra!")


if __name__ == "__main__":
    main()
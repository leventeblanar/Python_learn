correct = 0
incorrect = 0

print("Welcome to my computer quiz")

playing = input("Do you want to play? (yes/no) ").lower()

if playing != "yes":
    quit()

print("Okay! Let's play! :)")

answer = input("What does CPU stand for? ").lower()
if answer == "central processing unit":
    print("Correct!")
    correct += 1
else:
    print("Incorrect!")
    incorrect += 1

answer = input("What does GPU stand for? ").lower()
if answer == "graphics processing unit":
    print("Correct!")
    correct += 1
else:
    print("Incorrect!")
    incorrect += 1

answer = input("What does RAM stand for? ").lower()
if answer == "random access memory":
    print("Correct!")
    correct += 1
else:
    print("Incorrect!")
    incorrect += 1

answer = input("What does PSU stand for? ").lower()
if answer == "power supply":
    print("Correct!")
    correct += 1
else:
    print("Incorrect!")
    incorrect += 1

print(correct)
print(incorrect)

if correct <= 3:
    print(f"You won! You got {correct} question right.")
else:
    print("You lost!")
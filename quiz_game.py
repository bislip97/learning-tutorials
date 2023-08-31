def new_game():

    guesses = []
    correct_guesses = 0
    question_num = 1

    for key in questions:
        print("--------------------")
        print(key)
        for i in options[question_num-1]:
            print(i)
        guess = input("Enter (A, B, C, or D): ")
        guess = guess.upper()
        guesses.append(guess)

        correct_guesses += check_answer(questions.get(key),guess)
        question_num += 1

    display_score(correct_guesses, guesses)

def check_answer(answer, guess):

    if answer == guess:
        print("Correct!")
        return 1
    else:
        print("Wrong!")
        return 0
def display_score(correct_guesses, guesses):
    print("--------------------")
    print("RESULTS")
    print("--------------------")
    print("Answers: ", end=" ")
    for i in questions:
        print(questions.get(i),end="")
    print()

    print("Guesses: ", end="")
    for i in guesses:
        print(i, end=" ")
    print()

    score = int((correct_guesses/len(questions))*100)
    print("Your  score is: "+str(score)+"%")

def play_again():

    response = input("Do you want to play again? (yes or no): ")
    response = response.upper()

    if response == "YES":
        return True
    else:
        return False


questions = {
    "What company created league of legends? ": "A",
    "What year was league of legends released? ": "B",
    "How many champions were there on release? ": "D",
    "How many champions are there now? ": "C"
}

options = [["A. Riot Games", "B. Blizzard", "C. Bungie", "D. Activision"],
           ["A. 2014", "B. 2009", "C. 2001", "D. 2007"],
           ["A. 25", "B. 164", "C. 100", "D. 40"],
           ["A. 200", "B. 50", "C. 164", "D. 187"]]

new_game()

while play_again():
    new_game()

print("Thanks for playing!")
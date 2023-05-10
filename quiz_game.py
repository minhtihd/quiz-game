import csv

listOfQuestions = []

def load_questions(questionSet):
    listOfQuestions = []
    with open(questionSet,newline='') as csvfile:
        my_reader = csv.reader(csvfile)
    for row in my_reader:
        listOfQuestions.append(row)
    return listOfQuestions


def ask_question(question):
    score = 0
    for oneQuestion in listOfQuestions:
       answer = input(oneQuestion)
       if answer == oneQuestion["3"]:
           score += 1
           print("Right bro.")
       else:
           print("Wrong bro.")

    return score    


def run_quiz():
    global newScore
    newScore = [ask_question(load_questions("quiz_questions.csv")),input("What is your name")]
    print("This is your score: {newScore[1]}")


if __name__ == "__main__":
    run_quiz()


def python_score(python_question, python_options, python_answers):
    python_score = 0
    for i in range(len(python_question)):
        print(python_question[i])
        for option in python_options[i]:
            print(option)
        answer=input("Enter your answer (A/B/C/D): ")
        if answer.upper() == python_answers[i]:
            print("Correct!")
            python_score += 1
        else:
            print("Incorrect!")
    return python_score

def aids_score(aids_question, aids_options, aids_answers):
    aids_score = 0
    for i in range(len(aids_question)):
        print(aids_question[i])
        for option in aids_options[i]:
            print(option)
        answer=input("Enter your answer (A/B/C/D): ")
        if answer.upper() == aids_answers[i]:
            print("Correct!")
            aids_score += 1
        else:
            print("Incorrect!")
    return aids_score

def cyber_score(cyber_question, cyber_options, cyber_answers):
    cyber_score = 0
    for i in range(len(cyber_question)):
        print(cyber_question[i])
        for option in cyber_options[i]:
            print(option)
        answer=input("Enter your answer (A/B/C/D): ")
        if answer.upper() == cyber_answers[i]:
            print("Correct!")
            cyber_score += 1
        else:
            print("Incorrect!")
    return cyber_score

def display_instructions():
    print("Welcome to the Quiz Game!")
    print("Instructions:")
    print("1. Choose a category from the main menu.")
    print("2. Answer the questions by typing A, B, C, or D.")
    print("3. Your score will be displayed at the end of the quiz.")
    print("4. Have fun and good luck!")


# def display_high_scores(high_scores):
#     high_score=python_score+cyber_score+aids_score
#     print(f"High Scores: {high_score}")

def questions_attempted(python_score, aids_score, cyber_score):
    total_attempted = python_score + aids_score + cyber_score
    return total_attempted

def wrong_answers(python_score, aids_score, cyber_score):
    total_wrong = (5 - python_score) + (5 - aids_score) + (5 - cyber_score)
    return total_wrong

def correct_answers(python_score, aids_score, cyber_score):
    total_correct = python_score + aids_score + cyber_score
    return total_correct

def percentage_score(python_score, aids_score, cyber_score):
    total_questions = 15  # Assuming there are 5 questions in each category
    total_correct = correct_answers(python_score, aids_score, cyber_score)
    percentage = (total_correct / total_questions) * 100
    return percentage
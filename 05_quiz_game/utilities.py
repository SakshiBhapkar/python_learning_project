# ================= PYTHON QUIZ =================

def python_score(python_question, python_options, python_answers):

    score = 0

    for i in range(len(python_question)):

        print("\n--------------------------------")
        print(python_question[i])

        for option in python_options[i]:
            print(option)

        answer = input("Enter your answer (A/B/C/D): ")

        if answer.upper() == python_answers[i]:
            print("Correct!")
            score += 1
        else:
            print("Incorrect!")

    return score


# ================= AI & DS QUIZ =================

def aids_score(aids_question, aids_options, aids_answers):

    score = 0

    for i in range(len(aids_question)):

        print("\n--------------------------------")
        print(aids_question[i])

        for option in aids_options[i]:
            print(option)

        answer = input("Enter your answer (A/B/C/D): ")

        if answer.upper() == aids_answers[i]:
            print("Correct!")
            score += 1
        else:
            print("Incorrect!")

    return score


# ================= CYBER SECURITY QUIZ =================

def cyber_score(cyber_question, cyber_options, cyber_answers):

    score = 0

    for i in range(len(cyber_question)):

        print("\n--------------------------------")
        print(cyber_question[i])

        for option in cyber_options[i]:
            print(option)

        answer = input("Enter your answer (A/B/C/D): ")

        if answer.upper() == cyber_answers[i]:
            print("Correct!")
            score += 1
        else:
            print("Incorrect!")

    return score


# ================= INSTRUCTIONS =================

def display_instructions():

    print("\n========== INSTRUCTIONS ==========")

    print("1. Choose Start Quiz from the main menu.")
    print("2. Choose one of the three subjects.")
    print("3. Choose Easy, Medium or Difficult level.")
    print("4. Answer each question using A, B, C or D.")
    print("5. Your score will be displayed after the quiz.")
    print("6. You can play different subjects and levels.")
    print("7. Have fun and improve your knowledge!")


# ================= RESULT FUNCTIONS =================

def questions_attempted(
    python_score,
    aids_score,
    cyber_score
):

    total_attempted = (
        python_score +
        aids_score +
        cyber_score
    )

    return total_attempted


def wrong_answers(
    python_score,
    aids_score,
    cyber_score
):

    total_wrong = (
        (5 - python_score) +
        (5 - aids_score) +
        (5 - cyber_score)
    )

    return total_wrong


def correct_answers(
    python_score,
    aids_score,
    cyber_score
):

    total_correct = (
        python_score +
        aids_score +
        cyber_score
    )

    return total_correct


def percentage_score(
    python_score,
    aids_score,
    cyber_score
):

    total_questions = 15

    total_correct = correct_answers(
        python_score,
        aids_score,
        cyber_score
    )

    percentage = (
        total_correct / total_questions
    ) * 100

    return percentage
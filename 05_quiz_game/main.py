import utilities
import question


print("====================================")
print("        WELCOME TO QUIZ MASTER")
print("====================================")

# Scores
python_score = 0
aids_score = 0
cyber_score = 0

choice = 0

while choice != 4:

    print("\n========== MAIN MENU ==========")
    print("1. Start Quiz")
    print("2. Instructions")
    print("3. High Scores")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    # ---------------- START QUIZ ----------------
    if choice == 1:

        print("\n========== CHOOSE SUBJECT ==========")
        print("1. Python")
        print("2. AI & Data Science")
        print("3. Cyber Security")

        category = int(input("Enter your choice: "))

        # ---------------- PYTHON ----------------
        if category == 1:

            print("\nYou chose Python.")

            print("\n---------- SELECT LEVEL ----------")
            print("1. Easy")
            print("2. Medium")
            print("3. Difficult")

            level = int(input("Enter level: "))

            if level == 1:

                print("\nStarting Python - Easy Quiz...")

                python_question = question.python_easy_question
                python_options = question.python_easy_options
                python_answers = question.python_easy_answers

                python_score = utilities.python_score(
                    python_question,
                    python_options,
                    python_answers
                )

                print(
                    f"\nYour final score is: "
                    f"{python_score}/{len(python_question)}"
                )

            elif level == 2:

                print("\nStarting Python - Medium Quiz...")

                python_question = question.python_medium_question
                python_options = question.python_medium_options
                python_answers = question.python_medium_answers

                python_score = utilities.python_score(
                    python_question,
                    python_options,
                    python_answers
                )

                print(
                    f"\nYour final score is: "
                    f"{python_score}/{len(python_question)}"
                )

            elif level == 3:

                print("\nStarting Python - Difficult Quiz...")

                python_question = question.python_difficult_question
                python_options = question.python_difficult_options
                python_answers = question.python_difficult_answers

                python_score = utilities.python_score(
                    python_question,
                    python_options,
                    python_answers
                )

                print(
                    f"\nYour final score is: "
                    f"{python_score}/{len(python_question)}"
                )

            else:
                print("Invalid level choice.")

        # ---------------- AI & DS ----------------
        elif category == 2:

            print("\nYou chose AI & Data Science.")

            print("\n---------- SELECT LEVEL ----------")
            print("1. Easy")
            print("2. Medium")
            print("3. Difficult")

            level = int(input("Enter level: "))

            if level == 1:

                print("\nStarting AI&DS - Easy Quiz...")

                aids_question = question.aids_easy_question
                aids_options = question.aids_easy_options
                aids_answers = question.aids_easy_answers

                aids_score = utilities.aids_score(
                    aids_question,
                    aids_options,
                    aids_answers
                )

                print(
                    f"\nYour final score is: "
                    f"{aids_score}/{len(aids_question)}"
                )

            elif level == 2:

                print("\nStarting AI&DS - Medium Quiz...")

                aids_question = question.aids_medium_question
                aids_options = question.aids_medium_options
                aids_answers = question.aids_medium_answers

                aids_score = utilities.aids_score(
                    aids_question,
                    aids_options,
                    aids_answers
                )

                print(
                    f"\nYour final score is: "
                    f"{aids_score}/{len(aids_question)}"
                )

            elif level == 3:

                print("\nStarting AI&DS - Difficult Quiz...")

                aids_question = question.aids_difficult_question
                aids_options = question.aids_difficult_options
                aids_answers = question.aids_difficult_answers

                aids_score = utilities.aids_score(
                    aids_question,
                    aids_options,
                    aids_answers
                )

                print(
                    f"\nYour final score is: "
                    f"{aids_score}/{len(aids_question)}"
                )

            else:
                print("Invalid level choice.")

        # ---------------- CYBER SECURITY ----------------
        elif category == 3:

            print("\nYou chose Cyber Security.")

            print("\n---------- SELECT LEVEL ----------")
            print("1. Easy")
            print("2. Medium")
            print("3. Difficult")

            level = int(input("Enter level: "))

            if level == 1:

                print("\nStarting Cyber Security - Easy Quiz...")

                cyber_question = question.cyber_easy_question
                cyber_options = question.cyber_easy_options
                cyber_answers = question.cyber_easy_answers

                cyber_score = utilities.cyber_score(
                    cyber_question,
                    cyber_options,
                    cyber_answers
                )

                print(
                    f"\nYour final score is: "
                    f"{cyber_score}/{len(cyber_question)}"
                )

            elif level == 2:

                print("\nStarting Cyber Security - Medium Quiz...")

                cyber_question = question.cyber_medium_question
                cyber_options = question.cyber_medium_options
                cyber_answers = question.cyber_medium_answers

                cyber_score = utilities.cyber_score(
                    cyber_question,
                    cyber_options,
                    cyber_answers
                )

                print(
                    f"\nYour final score is: "
                    f"{cyber_score}/{len(cyber_question)}"
                )

            elif level == 3:

                print("\nStarting Cyber Security - Difficult Quiz...")

                cyber_question = question.cyber_difficult_question
                cyber_options = question.cyber_difficult_options
                cyber_answers = question.cyber_difficult_answers

                cyber_score = utilities.cyber_score(
                    cyber_question,
                    cyber_options,
                    cyber_answers
                )

                print(
                    f"\nYour final score is: "
                    f"{cyber_score}/{len(cyber_question)}"
                )

            else:
                print("Invalid level choice.")

        else:
            print("Invalid subject choice.")

    # ---------------- INSTRUCTIONS ----------------
    elif choice == 2:

        utilities.display_instructions()

    # ---------------- HIGH SCORES ----------------
    elif choice == 3:

        print("\n========== HIGH SCORES ==========")

        print(f"Python Score       : {python_score}")
        print(f"AI&DS Score        : {aids_score}")
        print(f"Cyber Security     : {cyber_score}")

    # ---------------- EXIT ----------------
    elif choice == 4:

        print("\nThank you for playing Quiz Master!")

    else:

        print("Invalid choice. Please try again.")


print("\n====================================")
print("             GAME OVER")
print("====================================")
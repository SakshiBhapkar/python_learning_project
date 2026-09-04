import utilities  
print("Welcome to the Quiz Game!")
print("Choose the correct answer from the options provided.")
choice=0
while choice != 4:
    print("1. Start")
    print("2. Instructions")
    print("3. High Scores")
    print("4. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        print("Starting the quiz...")
        #quiz all code here
        category=0
        print("Choose a category:")
        print("1. Python:")
        print("2. AIDS:")
        print("3. Cyber Security:")
        category = int(input("Enter your choice: "))
        if category == 1:
            print("You chose Python category.")
            # Add code for Python quiz
            python_question = ['Question 1: What will be the output?\nx = 10\ny = 3\nprint(x % y)','Question 2: Which keyword is used to stop a loop immediately?','Question 3: What will be the output?\nname = "Python"\nprint(name[1:4])','Question 4: Which of the following is the correct way to take input from the user?','Question 5: What will be the output?\nage = 18\nif age >= 18:\n    print("Adult")\nelse:\n    print("Minor")']
            python_options = [["A. 1", "B. 2", "C. 3", "D. 4"],["A. break", "B. continue", "C. pass", "D. exit"],["A. Pyt", "B. yth", "C. tho", "D. hon"],['A. input("Enter name: ")', 'B. get("Enter name: ")','C. scan("Enter name: ")','D. read("Enter name: ")'],["A. Adult", "B. Minor", "C. Error", "D. None"]]
            python_answers = ["A", "A", "B", "A", "A"]
            python_score=utilities.python_score(python_question, python_options, python_answers)

            utilities.display_python_quiz
            print(f"Your final score is: {python_score}/{len(python_question)}")
        elif category == 2:
            print("You chose AIDS category.")
            # Add code for AIDS quiz
            aids_question = ['Question 1: What does AI stand for?','Question 2: Which of the following is an example of Machine Learning?','Question 3: What does DS stand for in AI&DS?','Question 4: Which language is commonly used for Data Science?','Question 5: What is the main purpose of Data Visualization?']
            aids_options = [["A. Artificial Intelligence", "B. Automated Information", "C. Advanced Internet", "D. Artificial Integration"],["A. Creating a website using HTML", "B. Training a model to predict house prices", "C. Writing a simple calculator", "D. Designing a logo"],["A. Data Structure", "B. Digital System", "C. Data Science", "D. Database System"],["A. HTML", "B. CSS", "C. Python", "D. Bootstrap"],["A. To delete data", "B. To hide data", "C. To make data larger", "D. To understand and present data visually"]]
            aids_answers = ["A", "B", "C", "C", "D"]
            aids_score=utilities.aids_score(aids_question, aids_options, aids_answers)
            utilities.display_aids_quiz
            print(f"Your final score is: {aids_score}/{len(aids_question)}")
        elif category == 3:
            print("You chose Cyber Security category.")
            # Add code for Cyber Security quiz
            cyber_question = ['Question 1: What is the main purpose of a firewall?', 'Question 2: Which of the following is an example of a strong password?','Question 3: What does phishing mean in Cyber Security?','Question 4: Which type of malware can replicate itself and spread to other computers?','Question 5: What is the purpose of encryption?']
            cyber_options = [
              ["A. To increase internet speed", "B. To protect a network from unauthorized access", "C. To store files", "D. To create passwords"],
              ["A. password123", "B. 12345678", "C. Sakshi@2026#Py", "D. qwerty"],
              ["A. Stealing information by pretending to be a trusted source", "B. Installing antivirus software", "C. Backing up files", "D. Updating an operating system"],
              ["A. Trojan", "B. Spyware", "C. Adware", "D. Computer worm"],
              ["A. To make data public", "B. To convert data into a protected form", "C. To delete data permanently", "D. To increase storage space"]]
            cyber_answers = ["B", "C", "A", "D", "B"]
            cyber_score=utilities.cyber_score(cyber_question, cyber_options, cyber_answers)
            print(f"Your final score is: {cyber_score}/{len(cyber_question)}")
        else:
            print("Invalid category choice.")
    elif choice == 2:
        print("Here are the instructions...")
        # Add code for instructions
        utilities.display_instructions()
    elif choice == 3:
        print("Here are the high scores...")
        # Add code for high scores
        # high_scores = {
        #     "Python": python_score,
        #     "AIDS": AIDS_score,
        #     "Cyber Security": cyber_score
        # }
        
        # utilities.display_high_scores(high_scores)
    elif choice == 4:
        print("Thank you for playing!")
    else:
        print("Invalid choice. Please try again.")  

print("displaying results...")
print(f"Total questions attempted: {utilities.questions_attempted(python_score, aids_score, cyber_score)}")
print(f"Wrong answers: {utilities.wrong_answers(python_score, aids_score, cyber_score)}")
print(f"Correct answers: {utilities.correct_answers(python_score, aids_score, cyber_score)}")
print(f"Percentage score: {utilities.percentage_score(python_score, aids_score, cyber_score):.2f}%")
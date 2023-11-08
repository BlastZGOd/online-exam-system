import random
import time

# Sample question bank
question_bank = {
    1: {"question": "What is 2 + 2?", "answer": "4"},
    2: {"question": "What is the capital of France?", "answer": "Paris"},
    3: {"question": "What is the largest planet in our solar system?", "answer": "Jupiter"}
    # Add more questions here
}

# Sample user database (username: password)
user_db = {
    "user1": "password1",
    "user2": "password2",
    # Add more users here
}

# Dictionary to store user session information
user_sessions = {}

# Time limit (in seconds) for answering each question
QUESTION_TIME_LIMIT = 180  # 3 minutes

def generate_question_paper():
    question_numbers = list(question_bank.keys())  # Convert keys into a list
    question_paper = random.sample(question_numbers, 3)  # Generate exactly 3 questions
    return [(q, question_bank[q]) for q in question_paper]

def authenticate_user(username, password):
    return username in user_db and user_db[username] == password

def take_exam(username):
    if username not in user_db:
        return "Invalid username."

    if username in user_sessions:
        return "User is already taking an exam."

    password = input("Enter your password: ")
    if not authenticate_user(username, password):
        return "Authentication failed."

    questions = generate_question_paper()
    user_sessions[username] = {"questions": questions, "user_answers": {}}
    
    score = 0
    for i, (question_number, question) in enumerate(questions, start=1):
        print(f"Q{i}: {question['question']}")
        start_time = time.time()
        user_answer = input("Your answer: ")
        end_time = time.time()
        elapsed_time = end_time - start_time
        
        if elapsed_time > QUESTION_TIME_LIMIT:
            del user_sessions[username]
            return "You exceeded the time limit for answering a question. Exam terminated."

        if user_answer == question['answer']:
            score += 1

    del user_sessions[username]  # Clear user session data
    return f"Exam completed. Your score is: {score}/3"  # Display score out of 3 questions

if __name__ == "__main__":
    while True:
        print("Welcome to the Online Exam System")
        username = input("Enter your username (or 'exit' to quit): ")
        if username == 'exit':
            break
        result = take_exam(username)
        print(result)
{
    "questions": [
        {
            "question": "What is the capital of France?",
            "choices": ["London", "Paris", "Berlin", "Madrid"],
            "correct_answer": "Paris"
        },
        {
            "question": "What is the largest planet in our solar system?",
            "choices": ["Jupiter", "Mars", "Venus", "Saturn"],
            "correct_answer": "Jupiter"
        },
        ...
    ]
}



import json
import random

def load_questions_from_file(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data['questions']

def generate_quiz(questions, num_questions):
    return random.sample(questions, num_questions)

def administer_quiz(quiz):
    score = 0
    for i, question in enumerate(quiz, 1):
        print(f"Question {i}: {question['question']}")
        for j, choice in enumerate(question['choices'], 1):
            print(f"{j}. {choice}")
        
        user_answer = input("Your answer (enter the number of your choice): ")
        if user_answer.isdigit() and 1 <= int(user_answer) <= len(question['choices']):
            user_choice = question['choices'][int(user_answer) - 1]
            if user_choice == question['correct_answer']:
                score += 1

    return score

if __name__ == "__main__":
    quiz_file_path = "quiz_questions.json"
    num_questions_in_quiz = 5  # You can adjust this to set the number of questions in each quiz
    
    questions = load_questions_from_file(quiz_file_path)
    quiz = generate_quiz(questions, num_questions_in_quiz)

    print("\n--- Quiz ---")
    score = administer_quiz(quiz)

    print(f"\nQuiz completed. Your score: {score}/{num_questions_in_quiz}")

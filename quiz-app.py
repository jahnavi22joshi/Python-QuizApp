import random
import time

class QuizApp:
    def __init__(self):
        self.questions = {
            "Python": [
                {
                    "question": "What is the correct way to create a list in Python?",
                    "options": ["A) list = (1, 2, 3)", "B) list = [1, 2, 3]", "C) list = {1, 2, 3}", "D) list = 1, 2, 3"],
                    "answer": "B",
                    "explanation": "Square brackets [] are used to create lists in Python."
                },
                {
                    "question": "Which keyword is used to define a function in Python?",
                    "options": ["A) function", "B) define", "C) def", "D) func"],
                    "answer": "C",
                    "explanation": "The 'def' keyword is used to define functions in Python."
                },
                {
                    "question": "What does the len() function do?",
                    "options": ["A) Returns the length of an object", "B) Creates a new list", "C) Deletes an item", "D) Sorts a list"],
                    "answer": "A",
                    "explanation": "len() returns the number of items in an object like string, list, tuple, etc."
                },
                {
                    "question": "Which of these is NOT a valid Python data type?",
                    "options": ["A) int", "B) float", "C) char", "D) bool"],
                    "answer": "C",
                    "explanation": "Python doesn't have a 'char' data type. Single characters are just strings of length 1."
                },
                {
                    "question": "What is the output of: print(3 == 3.0)?",
                    "options": ["A) False", "B) True", "C) Error", "D) None"],
                    "answer": "B",
                    "explanation": "Python considers 3 and 3.0 equal when using the == operator."
                }
            ],
            "General Knowledge": [
                {
                    "question": "What is the capital of Australia?",
                    "options": ["A) Sydney", "B) Melbourne", "C) Canberra", "D) Perth"],
                    "answer": "C",
                    "explanation": "Canberra is the capital city of Australia, not Sydney or Melbourne."
                },
                {
                    "question": "Which planet is known as the Red Planet?",
                    "options": ["A) Venus", "B) Mars", "C) Jupiter", "D) Saturn"],
                    "answer": "B",
                    "explanation": "Mars appears red due to iron oxide (rust) on its surface."
                },
                {
                    "question": "Who wrote 'Romeo and Juliet'?",
                    "options": ["A) Charles Dickens", "B) William Shakespeare", "C) Jane Austen", "D) Mark Twain"],
                    "answer": "B",
                    "explanation": "William Shakespeare wrote the famous tragedy 'Romeo and Juliet'."
                },
                {
                    "question": "What is the largest ocean on Earth?",
                    "options": ["A) Atlantic", "B) Indian", "C) Arctic", "D) Pacific"],
                    "answer": "D",
                    "explanation": "The Pacific Ocean is the largest and deepest ocean on Earth."
                },
                {
                    "question": "In which year did World War II end?",
                    "options": ["A) 1944", "B) 1945", "C) 1946", "D) 1947"],
                    "answer": "B",
                    "explanation": "World War II ended in 1945 with Japan's surrender in September."
                }
            ],
            "Math": [
                {
                    "question": "What is 15% of 200?",
                    "options": ["A) 25", "B) 30", "C) 35", "D) 40"],
                    "answer": "B",
                    "explanation": "15% of 200 = (15/100) × 200 = 30"
                },
                {
                    "question": "What is the square root of 144?",
                    "options": ["A) 11", "B) 12", "C) 13", "D) 14"],
                    "answer": "B",
                    "explanation": "12 × 12 = 144, so √144 = 12"
                },
                {
                    "question": "If x + 5 = 12, what is x?",
                    "options": ["A) 6", "B) 7", "C) 8", "D) 9"],
                    "answer": "B",
                    "explanation": "x = 12 - 5 = 7"
                },
                {
                    "question": "What is 2³ (2 to the power of 3)?",
                    "options": ["A) 6", "B) 8", "C) 9", "D) 12"],
                    "answer": "B",
                    "explanation": "2³ = 2 × 2 × 2 = 8"
                },
                {
                    "question": "What is the area of a circle with radius 5? (π ≈ 3.14)",
                    "options": ["A) 78.5", "B) 31.4", "C) 15.7", "D) 25"],
                    "answer": "A",
                    "explanation": "Area = πr² = 3.14 × 5² = 3.14 × 25 = 78.5"
                }
            ]
        }
        
        self.user_name = ""
        self.current_score = 0
        self.total_questions = 0
        self.high_scores = []
        
    def display_welcome(self):
        """Display welcome message and get user name"""
        print("=" * 50)
        print("🎯 WELCOME TO THE ULTIMATE QUIZ APP! 🎯")
        print("=" * 50)
        print("Test your knowledge across different categories!")
        print("Let's see how much you know! 🧠")
        print()
        
        self.user_name = input("Please enter your name: ").strip()
        if not self.user_name:
            self.user_name = "Anonymous"
        print(f"\nHello, {self.user_name}! Let's get started! 🚀")
        
    def display_menu(self):
        """Display main menu options"""
        print("\n" + "=" * 40)
        print("QUIZ CATEGORIES")
        print("=" * 40)
        print("1. 🐍 Python Programming")
        print("2. 🌍 General Knowledge")
        print("3. 🔢 Mathematics")
        print("4. 🎲 Random Mix (All Categories)")
        print("5. 📊 View High Scores")
        print("6. 🚪 Exit")
        print("=" * 40)
        
    def get_user_choice(self):
        """Get and validate user menu choice"""
        while True:
            try:
                choice = int(input("Select an option (1-6): "))
                if 1 <= choice <= 6:
                    return choice
                else:
                    print("❌ Please enter a number between 1 and 6.")
            except ValueError:
                print("❌ Please enter a valid number.")
                
    def get_quiz_settings(self):
        """Get quiz settings from user"""
        print("\n📝 QUIZ SETTINGS")
        print("-" * 20)
        
        while True:
            try:
                num_questions = int(input("How many questions? (1-15): "))
                if 1 <= num_questions <= 15:
                    break
                else:
                    print("❌ Please enter a number between 1 and 15.")
            except ValueError:
                print("❌ Please enter a valid number.")
        
        print("\n⏰ TIME LIMIT OPTIONS:")
        print("1. No time limit")
        print("2. 15 seconds per question")
        print("3. 30 seconds per question")
        
        while True:
            try:
                time_choice = int(input("Choose time limit (1-3): "))
                if time_choice == 1:
                    time_limit = None
                elif time_choice == 2:
                    time_limit = 15
                elif time_choice == 3:
                    time_limit = 30
                else:
                    print("❌ Please choose 1, 2, or 3.")
                    continue
                break
            except ValueError:
                print("❌ Please enter a valid number.")
                
        return num_questions, time_limit
        
    def select_questions(self, category, num_questions):
        """Select questions based on category"""
        if category == "Random Mix":
            all_questions = []
            for cat_questions in self.questions.values():
                all_questions.extend(cat_questions)
            selected_questions = random.sample(all_questions, min(num_questions, len(all_questions)))
        else:
            available_questions = self.questions[category]
            selected_questions = random.sample(available_questions, min(num_questions, len(available_questions)))
            
        return selected_questions
        
    def ask_question(self, question_data, question_num, total_questions, time_limit):
        """Ask a single question and get user response"""
        print(f"\n{'='*50}")
        print(f"QUESTION {question_num}/{total_questions}")
        print('='*50)
        print(f"❓ {question_data['question']}")
        print()
        
        for option in question_data['options']:
            print(f"   {option}")
        print()
        
        if time_limit:
            print(f"⏰ You have {time_limit} seconds to answer!")
            start_time = time.time()
        
        while True:
            if time_limit:
                elapsed_time = time.time() - start_time
                if elapsed_time > time_limit:
                    print(f"\n⏰ Time's up! The correct answer was {question_data['answer']}")
                    print(f"💡 {question_data['explanation']}")
                    return False
                    
            user_answer = input("Your answer (A/B/C/D): ").strip().upper()
            
            if user_answer in ['A', 'B', 'C', 'D']:
                break
            else:
                print("❌ Please enter A, B, C, or D.")
                
        # Check answer
        if user_answer == question_data['answer']:
            print("✅ Correct! Well done! 🎉")
            print(f"💡 {question_data['explanation']}")
            return True
        else:
            print(f"❌ Wrong! The correct answer was {question_data['answer']}")
            print(f"💡 {question_data['explanation']}")
            return False
            
    def run_quiz(self, category, num_questions, time_limit):
        """Run the complete quiz"""
        print(f"\n🎯 Starting {category} Quiz!")
        print(f"📝 {num_questions} questions")
        if time_limit:
            print(f"⏰ {time_limit} seconds per question")
        else:
            print("⏰ No time limit")
        
        input("\nPress Enter to begin...")
        
        questions = self.select_questions(category, num_questions)
        self.current_score = 0
        self.total_questions = len(questions)
        
        for i, question in enumerate(questions, 1):
            correct = self.ask_question(question, i, self.total_questions, time_limit)
            if correct:
                self.current_score += 1
                
            # Show progress
            if i < len(questions):
                print(f"\n📊 Current Score: {self.current_score}/{i}")
                input("Press Enter for next question...")
        
        self.show_final_results(category)
        
    def show_final_results(self, category):
        """Display final quiz results"""
        percentage = (self.current_score / self.total_questions) * 100
        
        print("\n" + "="*50)
        print("🏆 QUIZ COMPLETED! 🏆")
        print("="*50)
        print(f"Player: {self.user_name}")
        print(f"Category: {category}")
        print(f"Score: {self.current_score}/{self.total_questions}")
        print(f"Percentage: {percentage:.1f}%")
        
        # Performance feedback
        if percentage >= 90:
            print("🌟 OUTSTANDING! You're a genius! 🌟")
            grade = "A+"
        elif percentage >= 80:
            print("🎉 EXCELLENT! Great job! 🎉")
            grade = "A"
        elif percentage >= 70:
            print("👍 GOOD! Well done! 👍")
            grade = "B"
        elif percentage >= 60:
            print("👌 NOT BAD! Keep practicing! 👌")
            grade = "C"
        else:
            print("📚 Keep studying! You'll do better next time! 📚")
            grade = "D"
            
        print(f"Grade: {grade}")
        print("="*50)
        
        # Save high score
        score_entry = {
            'name': self.user_name,
            'category': category,
            'score': self.current_score,
            'total': self.total_questions,
            'percentage': percentage,
            'grade': grade
        }
        self.high_scores.append(score_entry)
        
    def show_high_scores(self):
        """Display high scores"""
        if not self.high_scores:
            print("\n📊 No scores recorded yet!")
            print("Play some quizzes to see your scores here! 🎯")
            return
            
        print("\n" + "="*60)
        print("🏆 HIGH SCORES 🏆")
        print("="*60)
        
        # Sort by percentage (descending)
        sorted_scores = sorted(self.high_scores, key=lambda x: x['percentage'], reverse=True)
        
        print(f"{'#':<3} {'Name':<15} {'Category':<15} {'Score':<10} {'%':<8} {'Grade':<5}")
        print("-" * 60)
        
        for i, score in enumerate(sorted_scores[:10], 1):  # Show top 10
            print(f"{i:<3} {score['name']:<15} {score['category']:<15} "
                  f"{score['score']}/{score['total']:<7} {score['percentage']:<7.1f} {score['grade']:<5}")
        
        print("="*60)
        
    def run(self):
        """Main application loop"""
        self.display_welcome()
        
        while True:
            self.display_menu()
            choice = self.get_user_choice()
            
            if choice == 1:
                num_q, time_limit = self.get_quiz_settings()
                self.run_quiz("Python", num_q, time_limit)
                
            elif choice == 2:
                num_q, time_limit = self.get_quiz_settings()
                self.run_quiz("General Knowledge", num_q, time_limit)
                
            elif choice == 3:
                num_q, time_limit = self.get_quiz_settings()
                self.run_quiz("Math", num_q, time_limit)
                
            elif choice == 4:
                num_q, time_limit = self.get_quiz_settings()
                self.run_quiz("Random Mix", num_q, time_limit)
                
            elif choice == 5:
                self.show_high_scores()
                
            elif choice == 6:
                print(f"\n👋 Thanks for playing, {self.user_name}!")
                print("Keep learning and come back soon! 🚀")
                break
                
            input("\nPress Enter to continue...")

# Run the quiz application
if __name__ == "__main__":
    quiz_app = QuizApp()
    quiz_app.run()
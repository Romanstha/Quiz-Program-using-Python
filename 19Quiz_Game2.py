print("Welcome to the Simple Quiz Game")

playing = input("Do you want to play the Quiz Game? (yes/no): ")
correct_score = 0

if playing.lower() != "yes":
    quit()

print("OKAY! Let's play the Quiz Game :)")
# Quiz Questions
questions = [
    {
        "question": "What is the chemical symbol for water?",
        "answer": "H20"
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "answer": "Mars"
    },
    {
        "question": "What is the smallest unit of data in a computer?",
        "answer": "Bit"
    },
    {
        "question": "Which programming language is known as the language of the web?",
        "answer": "JavaScript"
    },
    {
        "question": "Who is known as the father of computer science?",
        "answer": "Alan Turing"
    },
    {
        "question": "What does CPU stand for?",
        "answer": "Central Processing Unit"
    },
    {
        "question": "Which gas is most abundant in Earth's atmosphere?",
        "answer": "Nitrogen"
    },
    {
        "question": "What does HTML stand for?",
        "answer": "HyperText Markup Language"
    },
    {
        "question": "What is the speed of light in vacuum?",
        "answer": "3 x 10^8 m/s"
    },
    {
        "question": "Which programming language is used for developing Android apps?",
        "answer": "Kotlin"
    },
    {
        "question": "What does AI stand for?",
        "answer": "Artificial Intelligence"
    },
    {
        "question": "What is the capital of USA?",
        "answer": "Washington DC"
    },
    {
        "question": "Who invented the World Wide Web?",
        "answer": "Tim Berners-Lee"
    },
    {
        "question": "What is the capital of Australia?",
        "answer": "Canberra"
    },
{
        "question": "Which programming language is primarily used for data analysis??",
        "answer": "Python"
    },
{
        "question": "What is the full form of SQL?",
        "answer": "Structured Query Language"
    },
{
        "question": "What is the function of a router in a network?",
        "answer": "Direct Network Traffic"
    },
{
        "question": "Which tech company created the iPhone?",
        "answer": "Apple"
    },
{
        "question": "What year was the first iPhone released?",
        "answer": "2007"
    },
{
        "question": "Which storage device is fastest?",
        "answer": "Solid State Drive"
    },
{
        "question": "What does GPU stand for?",
        "answer": "Graphics Processing Unit"
    },
{
        "question": "Who was the first President of the United States?",
        "answer": "George Washington"
    },
{
        "question": "In what year did World War II end?",
        "answer": "1945"
    },
{
        "question":"Who discovered America in 1492?",
        "answer": "Christopher Columbus"
    },
{
        "question":"Which civilization built the pyramids?",
        "answer": "Egyptians"
    },
{
        "question":"Which empire was known as the 'Land of the Rising Sun'?",
        "answer": "Japanese Empire"
    },
{
        "question":"Who was the first man to set foot on the Moon?",
        "answer": "Neil Armstrong"
    },

]

for i, q in enumerate(questions,1):
    print(f"Question {i}: {q['question']}")
    answer = input("Enter your answer: ")
    if answer.lower() == q["answer"].lower():
        print("Correct!\n")
        correct_score += 1
    else:
        print(f"Wrong! The correct answer is {q['answer']}.\n")

wrong_score = len(questions) - correct_score

print("Quiz Completed!")
print(f"You have answered {correct_score} questions correctly out of {len(questions)} questions")
print(f"You have answered {wrong_score} questions incorrectly out of {len(questions)} questions")
print(f"Your score is: {correct_score/len(questions) * 100}%")
print("Thank you for playing the Quiz Game!")
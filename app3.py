# Install openai if not already installed (uncomment if running fresh)
# !pip install openai

import openai

# Set your OpenAI API key here
# Initialize the OpenAI client
client = openai.OpenAI(api_key=openai.api_key)

# Take input from the user
topic = input("Enter the quiz topic: ")
num_questions = input("Enter number of questions (e.g., 5): ")
difficulty = input("Enter difficulty level (Easy/Medium/Hard): ")

# Validate and convert number of questions to int
try:
    num_questions = int(num_questions)
except ValueError:
    print("Invalid number of questions, defaulting to 5.")
    num_questions = 5

# Create prompt for OpenAI
prompt = (
    f"Generate {num_questions} multiple-choice questions on the topic '{topic}' "
    f"with {difficulty.lower()} difficulty. For each question, include 4 options, "
    f"mark the correct answer, and provide a short explanation."
)

try:
    # Call the OpenAI API using the new client
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant that generates quizzes."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.7,
        max_tokens=1000,
    )
    quiz = response.choices[0].message.content

    # Print the quiz
    print("\nGenerated Quiz:\n")
    print(quiz)

except Exception as e:
    print(f"Error generating quiz: {e}")

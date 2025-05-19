import openai
import streamlit as st

st.title("Personalized Quiz Generator using GPT")

openai.api_key = st.secrets["openai_key"]  # Use secrets for safety

topic = st.text_input("Enter a topic (e.g., Photosynthesis)")
num_questions = st.slider("Number of questions", 1, 10, 5)
difficulty = st.selectbox("Difficulty", ["Easy", "Medium", "Hard"])

if st.button("Generate Quiz"):
    prompt = (
        f"Generate {num_questions} multiple-choice questions on the topic '{topic}' "
        f"with {difficulty.lower()} difficulty. Include 4 options, the correct answer, and a short explanation."
    )
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}]
        )
        st.markdown("### Quiz Output:")
        st.markdown(response.choices[0].message.content)
    except Exception as e:
        st.error(f"Error: {e}")

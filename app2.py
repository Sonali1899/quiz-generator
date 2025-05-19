import streamlit as st

st.title("📘 Personalized Quiz Generator (Demo Mode)")

# Input fields
topic = st.text_input("Enter a topic (e.g., Photosynthesis)")
num_questions = st.slider("Number of questions", 1, 10, 3)
difficulty = st.selectbox("Select difficulty", ["Easy", "Medium", "Hard"])

# Simulated output
demo_quiz = f"""
### ✅ Sample Quiz on: {topic or 'Photosynthesis'} ({difficulty})

1. What is the primary function of photosynthesis?  
A. To digest food  
B. To absorb minerals  
C. To produce glucose  
D. To store water  
✅ Correct Answer: C  
📝 Explanation: Photosynthesis converts light energy into glucose.

2. Which organelle performs photosynthesis?  
A. Nucleus  
B. Mitochondria  
C. Chloroplast  
D. Ribosome  
✅ Correct Answer: C  
📝 Explanation: Chloroplasts contain chlorophyll for light capture.

3. What gas do plants absorb during photosynthesis?  
A. Oxygen  
B. Nitrogen  
C. Hydrogen  
D. Carbon dioxide  
✅ Correct Answer: D  
📝 Explanation: Plants use CO₂ to form glucose in photosynthesis.
"""

if st.button("Generate Quiz"):
    st.markdown(demo_quiz)

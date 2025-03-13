import streamlit as st
import google.generativeai as genai

# 🎯 Configure Gemini API
genai.configure(api_key='AIzaSyByLOZAmBso2PXKwA-rt9t0bs3YOBJyxY4')

# 🔍 Function to generate test cases using Gemini API
def generate_test_case(prompt, language, model="models/gemini-1.5-pro-latest"):
    """
    Generate test cases using the Gemini API.
    :param prompt: User input describing the test case.
    :param language: Programming language for the test case.
    :param model: Gemini AI model to use.
    :return: Generated test case as a string.
    """
    model = genai.GenerativeModel(model)
    response = model.generate_content(f"Generate test cases in {language} for the following prompt: {prompt}")
    return response.text if response else "⚠️ No response received."

# 🖥️ Streamlit UI
st.title("📝 Test Case Generator App")

# 📌 User Inputs
st.markdown("### 🔹 Enter your test case details below:")
prompt = st.text_area("📝 Enter your test case prompt in plain English:")
language = st.text_input("💻 Enter the programming language:")

# 🚀 Generate Test Case Button
if st.button("🎯 Generate Test Cases"):
    if prompt.strip() and language.strip():
        with st.spinner("⏳ Generating test cases..."):
            test_cases = generate_test_case(prompt, language)
            st.subheader("✅ Generated Test Cases:")
            st.code(test_cases, language=language.lower())
    else:
        st.warning("⚠️ Please enter both the prompt and the programming language.")

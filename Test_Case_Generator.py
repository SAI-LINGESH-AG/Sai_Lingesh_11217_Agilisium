# import streamlit as st
# import google.generativeai as genai
# import config

# # Configure the Gemini API
# genai.configure(api_key=config.API_KEY)

# # Available Gemini models
# GEMINI_MODELS = [
#     "models/gemini-1.5-pro-latest", "models/gemini-1.5-pro-002", "models/gemini-1.5-flash-latest",
#     "models/gemini-2.0-pro-exp", "models/gemini-2.0-flash-lite-001"
# ]

# # Streamlit UI
# st.set_page_config(page_title="Test Case Generator", layout="wide")
# st.title("📝 TCG")
# st.write("Enter a plain English prompt and generate test cases in any programming language.")

# # User Inputs
# prompt = st.text_area("Enter your test case prompt:")
# language = st.text_input("Enter programming language:")
# model_choice = st.selectbox("Select Gemini Model:", GEMINI_MODELS)

# def generate_test_case(prompt, language, model_choice):
#     """Generate test cases using Gemini API."""
#     try:
#         model = genai.GenerativeModel(model_choice)
#         response = model.generate_content(f"Generate {language} test cases for: {prompt}")
#         return response.text
#     except Exception as e:
#         return f"Error: {str(e)}"

# # Generate Button
# if st.button("Generate Test Cases"):
#     if prompt.strip() and language.strip():
#         with st.spinner("Generating test cases..."):
#             test_cases = generate_test_case(prompt, language, model_choice)
#             st.text_area("Generated Test Cases:", test_cases, height=300)
#     else:
#         st.warning("Please enter a valid prompt and programming language.")

# import streamlit as st
# import google.generativeai as genai
# import config

# # Configure the Gemini API
# genai.configure(api_key=config.API_KEY)

# # Available Gemini models
# GEMINI_MODELS = [
#     "models/gemini-1.5-pro-latest", "models/gemini-1.5-pro-002", "models/gemini-1.5-flash-latest",
#     "models/gemini-2.0-pro-exp", "models/gemini-2.0-flash-lite-001"
# ]

# # Streamlit UI
# st.set_page_config(page_title="Test Case Generator", layout="wide")
# st.title("📝 Test Case Generator App")
# st.write("Enter a plain English prompt and generate test cases in any programming language.")

# # User Inputs
# prompt = st.text_area("Enter your test case prompt:")
# language = st.text_input("Enter programming language:")
# model_choice = st.selectbox("Select Gemini Model:", GEMINI_MODELS)

# def generate_test_case(prompt, language, model_choice):
#     """Generate test cases using Gemini API."""
#     try:
#         model = genai.GenerativeModel(model_choice)
#         response = model.generate_content(f"Generate {language} test cases for: {prompt}")
#         return response.text
#     except Exception as e:
#         return f"Error: {str(e)}"

# # Generate Button
# if st.button("Generate Test Cases"):
#     if prompt.strip() and language.strip():
#         with st.spinner("Generating test cases..."):
#             test_cases = generate_test_case(prompt, language, model_choice)
#             st.text_area("Generated Test Cases:", test_cases, height=300)

#             # Add Copy Button
#             st.button("Copy to Clipboard", on_click=st.write, args=(test_cases,))
            
#             # Add Download Button
#             file_extension = {
#                 "Python": "py", "Java": "java", "C++": "cpp", "JavaScript": "js",
#                 "Go": "go", "Ruby": "rb", "PHP": "php", "C#": "cs", "Swift": "swift"
#             }.get(language, "txt")
#             file_name = f"test_cases.{file_extension}"
#             st.download_button(label="Download Test Cases", data=test_cases, file_name=file_name, mime="text/plain")
#     else:
#         st.warning("Please enter a valid prompt and programming language.")

# import streamlit as st
# import google.generativeai as genai
# import config

# # Configure Gemini API
# genai.configure(api_key=config.API_KEY)

# # Function to generate test cases using Gemini API
# def generate_test_case(prompt, language, model="models/gemini-1.5-pro-latest"):
#     model = genai.GenerativeModel(model)
#     response = model.generate_content(f"Generate test cases in {language} for the following prompt: {prompt}")
#     return response.text if response else "No response received."

# # Streamlit UI
# st.title("Test Case Generator App")

# # User Inputs
# prompt = st.text_area("Enter your test case prompt in plain English:")
# language = st.text_input("Enter the programming language:")

# # Generate Test Case Button
# if st.button("Generate Test Cases"):
#     if prompt.strip() and language.strip():
#         with st.spinner("Generating test cases..."):
#             test_cases = generate_test_case(prompt, language)
#             st.subheader("Generated Test Cases:")
#             st.code(test_cases, language=language.lower())
#     else:
#         st.warning("Please enter both the prompt and the programming language.")


import streamlit as st
import google.generativeai as genai
import config

# 🎯 Configure Gemini API
genai.configure(api_key=config.API_KEY)

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


# import streamlit as st
# import google.generativeai as genai
# import config

# # 🎯 Configure Gemini API
# genai.configure(api_key=config.API_KEY)

# # 🔍 Function to generate test cases using Gemini API
# def generate_test_case(prompt, language, model="models/gemini-1.5-pro-latest"):
#     """
#     Generate test cases using the Gemini API.
#     :param prompt: User input describing the test case.
#     :param language: Programming language for the test case.
#     :param model: Gemini AI model to use.
#     :return: Generated test case as a string.
#     """
#     model = genai.GenerativeModel(model)
#     response = model.generate_content(f"Generate test cases in {language} for the following prompt: {prompt}")
#     return response.text if response else "⚠️ No response received."

# # 🖥️ Streamlit UI
# st.title("📝 Test Case Generator App")

# # 📌 User Inputs
# st.markdown("### 🔹 Enter your test case details below:")
# def placeholder_text(field_name, example):
#     """Displays a watermark-like example in input fields."""
#     return "" if st.session_state.get(field_name, "") else example

# prompt = st.text_area("📝 Enter your test case prompt in plain English:", placeholder_text("prompt", "Login functionality for an e-commerce website"))
# language = st.text_input("💻 Enter the programming language:", placeholder_text("language", "Python"))

# # 🚀 Generate Test Case Button
# if st.button("🎯 Generate Test Cases"):
#     if prompt.strip() and language.strip():
#         with st.spinner("⏳ Generating test cases..."):
#             test_cases = generate_test_case(prompt, language)
#             st.subheader("✅ Generated Test Cases:")
#             st.code(test_cases, language=language.lower())
#     else:
#         st.warning("⚠️ Please enter both the prompt and the programming language.")

# # 📌 Footer
# st.markdown("Developed with ❤️ using Streamlit and Gemini API")
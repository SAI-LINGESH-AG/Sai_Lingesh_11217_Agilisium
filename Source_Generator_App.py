# import streamlit as st
# import google.generativeai as genai
# import config

# # Configure Gemini API
# genai.configure(api_key=config.API_KEY)

# # Function to generate code using Gemini API
# def generate_code(prompt, language, model_name="gemini-1.5-pro-latest"):
#     try:
#         model = genai.GenerativeModel(model_name)
#         response = model.generate_content(f"Write {language} code for: {prompt}")
#         return response.text if response else "No response received."
#     except Exception as e:
#         return f"Error: {str(e)}"

# # Streamlit UI
# st.title("🔧 Source Code Generator App")
# st.write("Enter your prompt in plain English and specify the programming language.")

# # Input fields
# user_prompt = st.text_area("Enter your requirement:")
# language = st.text_input("Programming Language:")

# # Model selection
# model_name = st.selectbox("Select Gemini Model:", [
#     "gemini-1.5-pro-latest", "gemini-1.5-flash-latest", "gemini-2.0-flash"
# ])

# if st.button("Generate Code"):
#     if user_prompt and language:
#         with st.spinner("Generating code..."):
#             code_output = generate_code(user_prompt, language, model_name)
#         st.code(code_output, language.lower())
#     else:
#         st.warning("Please enter both the prompt and the programming language.")

# import streamlit as st
# import google.generativeai as genai
# import config

# # Configure Gemini API
# genai.configure(api_key=config.API_KEY)

# # Function to generate code using Gemini API
# def generate_code(prompt, language):
#     try:
#         model = genai.GenerativeModel("gemini-1.5-pro-latest")
#         response = model.generate_content(f"Write {language} code for: {prompt}")
#         return response.text if response else "No response received."
#     except Exception as e:
#         return f"Error: {str(e)}"

# # Streamlit UI
# st.title("🔧 Source Code Generator")
# st.write("Enter your prompt in plain English and specify the programming language.")

# # Input fields
# user_prompt = st.text_area("Enter your requirement:")
# language = st.text_input("Programming Language:")

# if st.button("Generate Code"):
#     if user_prompt and language:
#         with st.spinner("Generating code..."):
#             code_output = generate_code(user_prompt, language)
#         st.code(code_output, language.lower())
#     else:
#         st.warning("Please enter both the prompt and the programming language.")

import streamlit as st
import google.generativeai as genai
import config

# 🚀 Configure Gemini API
genai.configure(api_key=config.API_KEY)

# 🎯 Function to generate code using Gemini API
def generate_code(prompt, language):
    try:
        model = genai.GenerativeModel("gemini-1.5-pro-latest")
        response = model.generate_content(f"✍️ Write {language} code for: {prompt}")
        return response.text if response else "⚠️ No response received."
    except Exception as e:
        return f"❌ Error: {str(e)}"

# 🌟 Streamlit UI
st.title("🔧 Source Code Generator App ✨")
st.write("📝 Enter your prompt in plain English and specify the programming language.")

# 🖊️ Input fields
user_prompt = st.text_area("💡 Enter your requirement:")
language = st.text_input("📌 Programming Language:")

if st.button("🚀 Generate Code"):
    if user_prompt and language:
        with st.spinner("⏳ Generating code..."):
            code_output = generate_code(user_prompt, language)
        st.code(code_output, language.lower())
    else:
        st.warning("⚠️ Please enter both the prompt and the programming language.")
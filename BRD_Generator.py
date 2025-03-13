import streamlit as st
import google.generativeai as genai

# Configure Gemini API
genai.configure(api_key="AIzaSyByLOZAmBso2PXKwA-rt9t0bs3YOBJyxY4")
MODEL = "models/gemini-1.5-pro-latest"

def generate_document(doc_type, details):
    prompt = f"""
    Generate a well-structured {doc_type} document with proper formatting, headings, numbered sections, and bullet points based on the following details:
    {details}
    Ensure that no metadata such as 'Version', 'Date', or 'Prepared by' is included.
    """
    model = genai.GenerativeModel(MODEL)
    response = model.generate_content(prompt)
    return response.text if response else "Error generating document."

def main():
    st.set_page_config(page_title="Document Generator", layout="wide")
    st.title("📄 Document Generator")
    st.markdown("### Generate BRD")
    
    doc_type = st.selectbox("📌 Select Document Type:", ["BRD", "HLDd", "LLDd", "Design Document"])
    details = st.text_area("✍️ Enter project details:", height=150)
    
    if st.button("🚀 Generate Document"):
        if details:
            with st.spinner("Generating document..."):
                doc_content = generate_document(doc_type, details)
                st.session_state.generated_doc = doc_content
                st.success("✅ Document generated successfully!")
        else:
            st.warning("⚠️ Please enter project details.")
    
    if "generated_doc" in st.session_state:
        st.subheader("📑 Generated Document Preview:")
        st.text_area("", st.session_state.generated_doc, height=300)

if __name__ == "__main__":
    main()

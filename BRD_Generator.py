import streamlit as st
import google.generativeai as genai
from docx import Document
import io

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

def save_as_docx(text, doc_type):
    doc = Document()
    doc.add_heading(f"{doc_type} Document", level=1)
    
    lines = text.split("\n")
    for line in lines:
        line = line.strip()
        if not line:
            continue
        
        if line[0].isdigit() and "." in line:  # Numbered sections
            doc.add_heading(line, level=2)
        elif line.startswith("**") and line.endswith("**"):  # Bold headings
            doc.add_heading(line.strip("*"), level=3)
        elif line.startswith("- ") or line.startswith("* "):  # Bullet points
            doc.add_paragraph(line.strip("- *"), style="List Bullet")
        else:
            doc.add_paragraph(line)
    
    buffer = io.BytesIO()
    doc.save(buffer)
    buffer.seek(0)
    return buffer

def main():
    st.set_page_config(page_title="Document Generator", layout="wide")
    st.title("📄 DocGen")
    st.markdown("### Generate BRD, HLDd, LLDd, and Design Documents with AI-powered assistance.")
    
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
        
        file_name = f"{doc_type}_Document.docx"
        docx_file = save_as_docx(st.session_state.generated_doc, doc_type)
        
        st.download_button(
            label="📥 Download Document",
            data=docx_file,
            file_name=file_name,
            mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document"
        )

if __name__ == "__main__":
    main()

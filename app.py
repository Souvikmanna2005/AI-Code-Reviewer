import streamlit as st
from reviewer import review_code

st.title("🤖 AI Code Reviewer")

st.write("Paste your code below and click analyze.")

# Code input box
code = st.text_area("Paste your code here", height=300)

if st.button("Analyze Code"):

    if code.strip() == "":
        st.warning("Please paste some code first!")
    else:
        result = review_code(code)

        st.subheader("AI Review Result")
        st.write(result)

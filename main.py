import streamlit as st

st.set_page_config(page_title="Purchase Notice")
hide_st_style = """
<style>
#MainMenu {visibility : hidden; }
footer {visibility : hidden; }
</style>
"""
st.markdown(hide_st_style,unsafe_allow_html=True)
st.title("Note :")

st.markdown("""
- We will send you an Email within 48 to 72 hours with the Serial Key.
- In case you do not receive any email, please Contact Technical Support.

 - Note : In case the bank operation is aborted, an email will be sent to you informing you Thank you.

- Email Technical Support : TechnicalSupport@gmail.com
""")

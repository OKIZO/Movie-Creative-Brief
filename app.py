import streamlit as st
import json
from pptx import Presentation
from io import BytesIO

def check_password():
    if st.session_state.get("password_correct"):
        return True
    pwd = st.text_input("Password", type="password", key="pwd_input")
    if pwd:
        if pwd == st.secrets["password"]:
            st.session_state["password_correct"] = True
            return True
        else:
            st.error("パスワードが違います")
    return False

if check_password():
    st.title("PPT Generator")
    st.caption("HTMLツールからJSONを貼り付けてください")
    # ... 以下同じ

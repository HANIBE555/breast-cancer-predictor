
import streamlit as st
from PIL import Image
import base64

def set_bg(image_path):
    with open(image_path, "rb") as f:
        data = f.read()
    encoded = base64.b64encode(data).decode()
    st.markdown(
        f'''
        <style>
        .stApp {{
            background-image: url("data:image/png;base64,{encoded}");
            background-size: cover;
        }}
        </style>
        ''',
        unsafe_allow_html=True
    )

set_bg("IMG.png")

st.markdown("""
<style>
html, body, [class*="css"] {
    direction: rtl;
    text-align: right;
}
</style>
""", unsafe_allow_html=True)

st.title("🏥 ברוך הבא למערכת תחזית חזרת סרטן")
st.markdown("אנא בחר את הפעולה שתרצה לבצע:")

col1, col2 = st.columns(2)
with col1:
    if st.button("🔬 חיזוי סיכוי לחזרת מחלה"):
        st.switch_page("pages/1_חיזוי_חזרת_מחלה.py")

with col2:
    if st.button("🖼️ בדיקת CT"):
        st.switch_page("pages/2_בדיקת_CT.py")

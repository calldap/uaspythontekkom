import streamlit as st
import pandas as pd
from datetime import date

# =====================
# WRITE
# =====================
st.write("Ini adalah contoh penggunaan st.write()")

# =====================
# TEXT ELEMENTS
# =====================
st.title("Aplikasi Streamlit Dasar")
st.header("Modul Streamlit Halaman 9–11")
st.subheader("Contoh Text Elements")
st.caption("Praktikum Streamlit")

st.markdown("""
Streamlit menyediakan berbagai **text elements** seperti:
- Markdown
- Title
- Header
- Subheader
- Caption
""")

st.text("Ini adalah contoh st.text()")

st.code("""
import streamlit as st
st.write("Hello World")
""", language="python")

# =====================
# DATA DISPLAY
# =====================
st.header("Data Display")

data = {
    "Nama": ["Andi", "Budi", "Citra"],
    "Nilai": [85, 90, 88]
}

df = pd.DataFrame(data)

st.subheader("Dataframe")
st.dataframe(df)

st.subheader("Table")
st.table(df)

# =====================
# BASIC WIDGETS
# =====================
st.header("Basic Widgets")

# Text Input
nama = st.text_input("Masukkan Nama")

# Number Input
umur = st.number_input("Masukkan Umur", min_value=0)

# Datetime Input
tanggal_lahir = st.date_input("Tanggal Lahir", value=date.today())

# Radio Button
jenis_kelamin = st.radio(
    "Jenis Kelamin",
    ("Laki-laki", "Perempuan")
)

# Checkbox
setuju = st.checkbox("Saya menyetujui data di atas")

# Button
if st.button("Tampilkan Data"):
    if setuju:
        st.write("Nama:", nama)
        st.write("Umur:", umur)
        st.write("Tanggal Lahir:", tanggal_lahir)
        st.write("Jenis Kelamin:", jenis_kelamin)
    else:
        st.write("Silakan centang persetujuan terlebih dahulu")

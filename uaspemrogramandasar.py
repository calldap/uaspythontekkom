import streamlit as st
import pandas as pd

# =====================
# TITLE & TEXT ELEMENT
# =====================
st.title("Aplikasi Streamlit Sederhana")
st.header("Contoh Basic Elements & Widgets")
st.subheader("Modul Streamlit Halaman 9–11")
st.caption("Praktikum Streamlit Dasar")

st.markdown("""
Aplikasi ini dibuat untuk menampilkan:
- Text Elements  
- Data Display  
- Widgets  
- Layout (Sidebar & Columns)
""")

st.text("Ini adalah contoh penggunaan st.text()")

# =====================
# SIDEBAR
# =====================
st.sidebar.header("Menu Sidebar")
nama = st.sidebar.text_input("Masukkan Nama")
umur = st.sidebar.number_input("Masukkan Umur", min_value=0)

# =====================
# WIDGETS
# =====================
st.header("Input Pengguna")

hobi = st.text_input("Apa hobi Anda?")
tinggi = st.number_input("Tinggi badan (cm)", min_value=0)

jenis_kelamin = st.radio(
    "Jenis Kelamin",
    ("Laki-laki", "Perempuan")
)

setuju = st.checkbox("Saya menyetujui data di atas")

# =====================
# BUTTON & OUTPUT
# =====================
if st.button("Tampilkan Data"):
    if setuju:
        st.success("Data berhasil ditampilkan!")
        st.write("Nama:", nama)
        st.write("Umur:", umur)
        st.write("Hobi:", hobi)
        st.write("Tinggi Badan:", tinggi, "cm")
        st.write("Jenis Kelamin:", jenis_kelamin)
    else:
        st.warning("Silakan centang persetujuan terlebih dahulu")

# =====================
# DATA DISPLAY
# =====================
st.header("Contoh Dataframe")

data = {
    "Nama": ["Andi", "Budi", "Citra"],
    "Umur": [20, 21, 19],
    "Prodi": ["Informatika", "Sistem Informasi", "Teknik Komputer"]
}

df = pd.DataFrame(data)
st.dataframe(df)

# =====================
# COLUMNS LAYOUT
# =====================
st.header("Contoh Columns")

col1, col2 = st.columns(2)

with col1:
    st.markdown("### Kolom 1")
    st.write("Ini isi kolom pertama")

with col2:
    st.markdown("### Kolom 2")
    st.write("Ini isi kolom kedua")

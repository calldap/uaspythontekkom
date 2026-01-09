import streamlit as st

# =====================
# JUDUL APLIKASI
# =====================
st.title("Aplikasi Hitung Bangun Datar")

# =====================
# PILIH OPERASI
# =====================
operasi = st.selectbox(
    "Pilih operasi perhitungan",
    ["Hitung Keliling"]
)

# =====================
# PILIH JENIS HITUNG
# =====================
st.subheader("Pilih Hitung")

pilihan = st.radio(
    "",
    ("Keliling Segitiga", "Keliling Persegi Panjang", "Keliling Jajar Genjang")
)

# =====================
# FUNGSI PERHITUNGAN
# =====================
def keliling_segitiga(a, b, c):
    return a + b + c

def keliling_persegi_panjang(p, l):
    return 2 * (p + l)

def keliling_jajar_genjang(a, b):
    return 2 * (a + b)

# =====================
# INPUT & PROSES
# =====================
hasil = None

if pilihan == "Keliling Segitiga":
    sisi_a = st.number_input("Sisi A", value=20.0)
    sisi_b = st.number_input("Sisi B", value=30.0)
    sisi_c = st.number_input("Sisi C", value=100.0)

    if st.button("Hitung"):
        hasil = keliling_segitiga(sisi_a, sisi_b, sisi_c)

elif pilihan == "Keliling Persegi Panjang":
    panjang = st.number_input("Panjang", value=10.0)
    lebar = st.number_input("Lebar", value=5.0)

    if st.button("Hitung"):
        hasil = keliling_persegi_panjang(panjang, lebar)

elif pilihan == "Keliling Jajar Genjang":
    sisi_a = st.number_input("Sisi A", value=10.0)
    sisi_b = st.number_input("Sisi B", value=5.0)

    if st.button("Hitung"):
        hasil = keliling_jajar_genjang(sisi_a, sisi_b)

# =====================
# OUTPUT HASIL
# =====================
if hasil is not None:
    st.markdown(f"## 🟢 Hasil: **{hasil}**")

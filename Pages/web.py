import streamlit as st
import pandas as pd

# Konfigurasi halaman
st.set_page_config(page_title="Aplikasi Gizi", layout="wide")

# Load data CSV (hanya jika dibutuhkan)
@st.cache_data
def load_data():
    return pd.read_csv("database_gizi.csv")

data = load_data()

# Navigasi utama
halaman = st.selectbox("Pilih Halaman", ["Beranda", "Database Bahan Pangan", "Perhitungan Nilai Gizi"])

# ==================== BERANDA ====================
if halaman == "Beranda":
    st.title("🍽️ Aplikasi Gizi Sederhana")
    st.markdown("""
    Selamat datang di aplikasi interaktif untuk mengenal bahan pangan dan menghitung nilai gizi harian Anda!  
    
    ### Fitur Utama:
    - **Database Bahan Pangan**: Lihat kandungan gizi dari bahan-bahan umum.
    - **Perhitungan Nilai Gizi**: Hitung total gizi dari kombinasi bahan makanan.

    ---
    👉 Gunakan menu di atas untuk memilih halaman yang diinginkan.
    """)

# ==================== DATABASE BAHAN PANGAN ====================
elif halaman == "Database Bahan Pangan":
    st.title("📘 Database Bahan Pangan")

    sub_menu = st.selectbox("Pilih Bahan Pangan:", ["Beranda", "Nasi Putih", "Telur Ayam", "Tempe", "Tahu", "Daging Ayam"])
    st.markdown("---")

    if sub_menu == "Beranda":
        st.header("📘 Tentang Database Bahan Pangan")
        st.markdown("""
        Halaman ini berisi informasi singkat mengenai bahan pangan umum yang digunakan dalam perhitungan gizi.  
        Silakan pilih bahan pangan dari menu di atas untuk melihat kandungan gizinya.

        **Daftar bahan pangan:**
        - Nasi Putih
        - Telur Ayam
        - Tempe
        - Tahu
        - Daging Ayam

        ---
        *Catatan: Nilai gizi dapat bervariasi tergantung pada cara pengolahan dan jenis bahan pangan.*
        """)
    elif sub_menu == "Nasi Putih":
        st.header("🍚 Nasi Putih")
        st.markdown("""
        Nasi putih adalah sumber karbohidrat utama di Indonesia.  
        Dalam 100 gram, nasi mengandung sekitar:
        - 175 kkal  
        - 39 gram karbohidrat  
        - Sedikit protein dan lemak  
        """)
    elif sub_menu == "Telur Ayam":
        st.header("🥚 Telur Ayam")
        st.markdown("""
        Telur merupakan sumber protein hewani yang sangat baik.  
        Dalam 100 gram telur mengandung sekitar:
        - 155 kkal  
        - 13 gram protein  
        """)
    elif sub_menu == "Tempe":
        st.header("🍱 Tempe")
        st.markdown("""
        Tempe adalah sumber protein nabati hasil fermentasi kedelai.  
        Dalam 100 gram tempe mengandung:
        - 193 kkal  
        - 19 gram protein  
        - Lemak sehat  
        """)
    elif sub_menu == "Tahu":
        st.header("🍥 Tahu")
        st.markdown("""
        Tahu memiliki kandungan protein sedang dan cocok untuk makanan rendah kalori.  
        Dalam 100 gram tahu mengandung:
        - 80 kkal  
        - 8 gram protein  
        """)
    elif sub_menu == "Daging Ayam":
        st.header("🍗 Daging Ayam")
        st.markdown("""
        Daging ayam tanpa kulit adalah sumber protein hewani tinggi.  
        Dalam 100 gram daging ayam mengandung:
        - 165 kkal  
        - 31 gram protein  
        - Lemak rendah  
        """)

# ==================== PERHITUNGAN NILAI GIZI ====================
elif halaman == "Perhitungan Nilai Gizi":
    st.title("📊 Perhitungan Nilai Gizi")

    if "bahan_count" not in st.session_state:
        st.session_state.bahan_count = 1
    if "bahan_inputs" not in st.session_state:
        st.session_state.bahan_inputs = [{} for _ in range(st.session_state.bahan_count)]

    col_add, col_remove = st.columns([1, 1])
    with col_add:
        if st.button("➕ Tambah Bahan"):
            st.session_state.bahan_count += 1
            st.session_state.bahan_inputs.append({})
    with col_remove:
        if st.button("➖ Hapus Bahan") and st.session_state.bahan_count > 1:
            st.session_state.bahan_count -= 1
            st.session_state.bahan_inputs.pop()

    st.markdown("---")

    input_bahan_gram = []
    for i in range(st.session_state.bahan_count):
        col1, col2 = st.columns([2, 1])
        with col1:
            bahan = st.selectbox(f"Pilih Bahan ke-{i+1}", [""] + data["Bahan"].tolist(), key=f"bahan_{i}")
        with col2:
            if bahan:
                gram = st.number_input("Jumlah (gram)", min_value=0.0, key=f"gram_{i}")
                input_bahan_gram.append((bahan, gram))

    if st.button("Hitung Total Gizi"):
        total = {"Kalori": 0, "Protein": 0, "Lemak": 0, "Karbohidrat": 0}
        hasil_detail = []

        for bahan, gram in input_bahan_gram:
            matching_rows = data[data["Bahan"] == bahan]
            if not matching_rows.empty and gram > 0:
                row = matching_rows.iloc[0]
                faktor = gram / 100
                total["Kalori"] += row["Kalori"] * faktor
                total["Protein"] += row["Protein"] * faktor
                total["Lemak"] += row["Lemak"] * faktor
                total["Karbohidrat"] += row["Karbohidrat"] * faktor

                hasil_detail.append({
                    "Bahan": bahan,
                    "Gram": gram,
                    "Kalori": row["Kalori"] * faktor,
                    "Protein": row["Protein"] * faktor,
                    "Lemak": row["Lemak"] * faktor,
                    "Karbohidrat": row["Karbohidrat"] * faktor,
                })

        st.subheader("Total Nilai Gizi:")
        for k, v in total.items():
            st.write(f"*{k}:* {v:.2f}")

        if hasil_detail:
            st.subheader("Detail Per Bahan:")
            st.dataframe(pd.DataFrame(hasil_detail))

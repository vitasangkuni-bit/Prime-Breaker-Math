import streamlit as st
import random

# Konfigurasi Halaman Web
st.set_page_config(page_title="Code Breaker", page_icon="🔐", layout="centered")

# Inisialisasi Session State (agar status permainan tersimpan saat tombol diklik)
if 'page' not in st.session_state:
    st.session_state.page = 1
if 'score' not in st.session_state:
    st.session_state.score = 0
if 'num_prime' not in st.session_state:
    st.session_state.num_prime = random.randint(10, 50)
if 'fpb_a' not in st.session_state:
    st.session_state.fpb_a = random.randint(12, 48)
    st.session_state.fpb_b = random.randint(12, 48)
if 'mod_a' not in st.session_state:
    st.session_state.mod_a = random.randint(50, 150)
    st.session_state.mod_b = random.randint(5, 15)

def is_prime(n):
    if n < 2: return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0: return False
    return True

def cari_fpb(a, b):
    while b:
        a, b = b, a % b
    return a

# --- TAMPILAN WEB ---
st.title("🔐 Code Breaker: The Prime Conspiracy")
st.write("Selamatkan sistem dari peretasan dengan memecahkan kode matematika!")
st.divider()

# Level 1: Bilangan Prima
if st.session_state.page == 1:
    st.subheader("[LEVEL 1] Firewall Bilangan Prima")
    st.write(f"Sistem mendeteksi angka: **{st.session_state.num_prime}**")
    st.write("Apakah angka di atas termasuk **Bilangan Prima**?")
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("Ya, Bilangan Prima"):
            correct = is_prime(st.session_state.num_prime)
            if correct:
                st.session_state.score += 30
                st.success("Tepat sekali! Akses diterima (+30 Poin)")
            else:
                st.error("Salah! Angka tersebut bukan bilangan prima.")
            st.session_state.page = 2
            st.button("Lanjut ke Level 2 ➡️")
    with col2:
        if st.button("Bukan Bilangan Prima"):
            correct = not is_prime(st.session_state.num_prime)
            if correct:
                st.session_state.score += 30
                st.success("Tepat sekali! Akses diterima (+30 Poin)")
            else:
                st.error("Salah! Angka tersebut adalah bilangan prima.")
            st.session_state.page = 2
            st.button("Lanjut ke Level 2 ➡️")

# Level 2: FPB
elif st.session_state.page == 2:
    st.subheader("[LEVEL 2] Enkripsi FPB")
    a, b = st.session_state.fpb_a, st.session_state.fpb_b
    st.write(f"Tentukan Faktor Persekutuan Terbesar (**FPB**) dari angka **{a}** dan **{b}**:")
    
    ans = st.number_input("Masukkan Nilai FPB:", min_value=1, step=1)
    if st.button("Kirim Jawaban FPB"):
        real_fpb = cari_fpb(a, b)
        if ans == real_fpb:
            st.session_state.score += 35
            st.success(f"Jawaban Benar! FPB dari {a} dan {b} adalah {real_fpb} (+35 Poin)")
        else:
            st.error(f"Kurang tepat. FPB yang benar adalah {real_fpb}.")
        st.session_state.page = 3
        st.button("Lanjut ke Level 3 ➡️")

# Level 3: Modulo
elif st.session_state.page == 3:
    st.subheader("[LEVEL 3] Brankas Aritmatika Modulo")
    a, b = st.session_state.mod_a, st.session_state.mod_b
    st.write(f"Berapakah sisa pembagian dari **{a} mod {b}** ({a} dibagi {b})?")
    
    ans_mod = st.number_input("Masukkan Hasil Modulo:", min_value=0, step=1)
    if st.button("Retas Brankas"):
        real_mod = a % b
        if ans_mod == real_mod:
            st.session_state.score += 35
            st.success(f"Sempurna! Sisa pembagian adalah {real_mod} (+35 Poin)")
        else:
            st.error(f"Gagal! Sisa pembagian adalah {real_mod}.")
        st.session_state.page = 4
        st.button("Lihat Hasil Akhir 🏆")

# Level Final: Hasil Akhir
elif st.session_state.page == 4:
    st.subheader("🎉 MISI SELESAI!")
    st.metric(label="Total Skor Anda", value=f"{st.session_state.score} / 100")
    
    if st.session_state.score >= 65:
        st.balloons()
        st.success("STATUS: BERHASIL! Anda berhasil mengamankan sistem.")
    else:
        st.error("STATUS: GAGAL! Sistem terkunci. Coba lagi!")
        
    if st.button("Main Lagi 🔄"):
        st.session_state.clear()
        st.rerun()
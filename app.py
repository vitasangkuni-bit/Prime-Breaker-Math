import random
import streamlit as st

# 1. Konfigurasi Halaman & Tema Game
st.set_page_config(
    page_title="Prime Breaker: The Sieve Protocol",
    page_icon="🔐",
    layout="centered",
    initial_sidebar_state="expanded",
)

# 2. Desain Visual Kustom, Animasi Latar Cyber, & Maskot Agen
st.markdown(
    """
    <style>
    /* Hilangkan Header & Footer Streamlit */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    /* Animasi Latar Belakang Cyber Grid Bergerak */
    @keyframes cyberGrid {
        0% { background-position: 0 0; }
        100% { background-position: 60px 60px; }
    }
    
    @keyframes bgGlow {
        0% { background-color: #030712; }
        50% { background-color: #0f172a; }
        100% { background-color: #030712; }
    }
    
    .stApp {
        background-color: #030712;
        background-image: 
            linear-gradient(rgba(0, 240, 255, 0.12) 1px, transparent 1px),
            linear-gradient(90deg, rgba(255, 0, 127, 0.1) 1px, transparent 1px);
        background-size: 50px 50px;
        animation: cyberGrid 4s linear infinite, bgGlow 8s infinite ease-in-out;
        color: #f8fafc;
    }

    /* Kotak Kartu Game dengan Efek Neon */
    .cyber-card {
        background: linear-gradient(135deg, rgba(15, 23, 42, 0.95), rgba(30, 41, 59, 0.95));
        border: 2px solid #00f0ff;
        border-radius: 16px;
        padding: 25px;
        margin-bottom: 20px;
        box-shadow: 0 0 30px rgba(0, 240, 255, 0.35);
    }

    /* Kotak Brankas Rahasia (Vault) */
    .vault-box {
        background: linear-gradient(135deg, rgba(20, 10, 30, 0.95), rgba(40, 15, 50, 0.95));
        border: 3px solid #ff007f;
        border-radius: 20px;
        padding: 30px;
        text-align: center;
        box-shadow: 0 0 40px rgba(255, 0, 127, 0.6);
        animation: pulseVault 2s infinite ease-in-out;
    }

    @keyframes pulseVault {
        0% { box-shadow: 0 0 20px rgba(255, 0, 127, 0.4); }
        50% { box-shadow: 0 0 45px rgba(255, 0, 127, 0.8); }
        100% { box-shadow: 0 0 20px rgba(255, 0, 127, 0.4); }
    }

    .cyber-title {
        color: #00f0ff;
        font-family: 'Courier New', monospace;
        font-weight: bold;
        text-shadow: 0 0 15px rgba(0, 240, 255, 0.8);
    }

    /* Kotak Dialog Karakter Maskot */
    .mascot-box {
        background-color: rgba(0, 240, 255, 0.1);
        border-left: 5px solid #00f0ff;
        padding: 12px 18px;
        border-radius: 0 10px 10px 0;
        margin-bottom: 15px;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }

    div.stButton > button {
        background: linear-gradient(90deg, #00f0ff, #0088cc);
        color: #030712;
        font-weight: bold;
        border-radius: 10px;
        border: none;
        padding: 12px 24px;
        width: 100%;
        box-shadow: 0 0 15px rgba(0, 240, 255, 0.5);
        transition: 0.3s;
    }
    div.stButton > button:hover {
        background: linear-gradient(90deg, #ff007f, #cc0066);
        color: #ffffff;
        box-shadow: 0 0 25px rgba(255, 0, 127, 0.8);
    }
    </style>
""",
    unsafe_allow_html=True,
)


# 3. Fungsi Logika Matematika
def cek_prima(n):
  if n < 2:
    return False
  for i in range(2, int(n**0.5) + 1):
    if n % i == 0:
      return False
  return True


def cari_fpb(a, b):
  while b:
    a, b = b, a % b
  return a


# 4. Inisialisasi Memori Game (Session State)
if "level" not in st.session_state:
  st.session_state.level = 0  # 0 = Login, 1-3 = Level, 4 = Menang (Vault), 5 = Kalah
  st.session_state.score = 0
  st.session_state.nama = ""
  st.session_state.sub_soal = 1
  st.session_state.num_prima = random.randint(2, 50)
  st.session_state.fpb_a = random.randint(12, 48)
  st.session_state.fpb_b = random.randint(12, 48)
  st.session_state.mod_a = random.randint(50, 200)
  st.session_state.mod_b = random.randint(5, 20)
  st.session_state.pesan = ""


def reset_game():
  st.session_state.level = 0
  st.session_state.score = 0
  st.session_state.sub_soal = 1
  st.session_state.pesan = ""
  st.session_state.num_prima = random.randint(2, 50)
  st.session_state.fpb_a = random.randint(12, 48)
  st.session_state.fpb_b = random.randint(12, 48)
  st.session_state.mod_a = random.randint(50, 200)
  st.session_state.mod_b = random.randint(5, 20)


# --- HEADER UTAMA & BACKSOUND DI SIDEBAR ---
st.markdown(
    "<h1 class='cyber-title' style='text-align: center;'>⚡ 🔓 PRIME BREAKER: THE SIEVE PROTOCOL 🚀</h1>",
    unsafe_allow_html=True,
)
st.markdown(
    "<p style='text-align: center; color: #38bdf8;'>Misi Edukasi Teori Bilangan"
    " & Peretasan Brankas Angka</p>",
    unsafe_allow_html=True,
)

# Panel Kontrol Audio & Info di Sidebar
st.sidebar.markdown("### 🎮 PUSAT KONTROL ARCADE")
st.sidebar.markdown(
    "🎵 **Musik Latar Sibel** *(Nyalakan untuk pengalaman seru!)*"
)
st.sidebar.audio(
    "https://cdn.pixabay.com/download/audio/2022/05/27/audio_1808fbf756.mp3?filename=cyberpunk-2099-10701.mp3",
    format="audio/mp3",
)
st.sidebar.markdown("---")
st.sidebar.info(
    "💡 **Tips Presentasi:** Tekan **F11** di keyboard untuk masuk ke mode layar"
    " penuh agar terlihat seperti game PC sungguhan!"
)

# --- PANEL STATUS GAME ---
if 1 <= st.session_state.level <= 3:
  col1, col2 = st.columns(2)
  col1.metric("🛡️ Level Aktif", f"Level {st.session_state.level} / 3")
  col2.metric("⭐ Akumulasi Skor", f"{st.session_state.score} / 100 Poin")
  st.progress(st.session_state.level / 3)
  st.markdown("---")

# ==========================================
# LAYAR 0: LOGIN AGEN (MENU UTAMA)
# ==========================================
if st.session_state.level == 0:
  st.markdown(
      """
    <div class='cyber-card'>
        <h3 style='color: #ff007f;'>🛡️ SELAMAT DATANG, AGEN RAHASIA!</h3>
        <p>Brankas utama sistem berisi harta karun matematika terkunci rapat. Bantu kami memecahkan kode keamanan melalui 3 level penuh tantangan!</p>
        <div class='mascot-box'>
            <b>🤖 Maskot Cyber-Bot:</b> <i>"Hai Agen! Ingat, sistem kita sangat ketat. Jika kamu salah menebak satu soal saja, alarm berbunyi dan kamu harus mengulang dari Level 1!"</i>
        </div>
    </div>
    """,
      unsafe_allow_html=True,
  )

  nama_input = st.text_input(
      "Masukkan Nama Agen Kamu:", placeholder="Contoh: Agen Vita"
  )
  if st.button("🚀 MULAI MISI SEKARANG"):
    if nama_input.strip() != "":
      st.session_state.nama = nama_input
      st.session_state.level = 1
      st.rerun()
    else:
      st.warning("Nama agen wajib diisi sebelum memulai misi!")

# ==========================================
# LEVEL 1: FIREWALL BILANGAN PRIMA (3 Soal x 10 Poin = 30 Poin)
# ==========================================
elif st.session_state.level == 1:
  st.markdown(
      f"""
    <div class='cyber-card'>
        <h3 class='cyber-title'>🔥 [LEVEL 1] Sieve Firewall — Soal {st.session_state.sub_soal} dari 3</h3>
        <div class='mascot-box'>
            <b>🤖 Cyber-Bot:</b> <i>"Saringan pertama aktif! Periksa angka sinyal di bawah ini dengan teliti."</i>
        </div>
        <p>Sinyal Angka Terdeteksi: <strong style='font-size: 30px; color: #ff007f;'>{st.session_state.num_prima}</strong></p>
        <p>Apakah angka ini termasuk <strong>Bilangan Prima</strong>?</p>
    </div>
    """,
      unsafe_allow_html=True,
  )

  c1, c2 = st.columns(2)
  jawab = None
  with c1:
    if st.button("✅ Ya, Bilangan Prima"):
      jawab = True
  with c2:
    if st.button("❌ Bukan Bilangan Prima"):
      jawab = False

  if jawab is not None:
    benar = cek_prima(st.session_state.num_prima)
    if jawab == benar:
      st.session_state.score += 10
      if st.session_state.sub_soal < 3:
        st.session_state.sub_soal += 1
        st.session_state.num_prima = random.randint(2, 50)
      else:
        st.session_state.level = 2
        st.session_state.sub_soal = 1
      st.rerun()
    else:
      st.session_state.level = 5
      st.session_state.pesan = (
          f"Angka {st.session_state.num_prima} sebenarnya adalah"
          f" {'Bilangan Prima' if benar else 'Bukan Bilangan Prima'}."
      )
      st.rerun()

# ==========================================
# LEVEL 2: ENKRIPSI FPB (2 Soal x 20 Poin = 40 Poin)
# ==========================================
elif st.session_state.level == 2:
  st.markdown(
      f"""
    <div class='cyber-card'>
        <h3 class='cyber-title'>🔑 [LEVEL 2] Enkripsi Euclidean (FPB) — Soal {st.session_state.sub_soal} dari 2</h3>
        <div class='mascot-box'>
            <b>🤖 Cyber-Bot:</b> <i>"Bagus! Sekarang gunakan Algoritma Euclidean untuk mencari FPB dua kunci ini."</i>
        </div>
        <p>Temukan <strong>Faktor Persekutuan Terbesar (FPB)</strong> dari:</p>
        <p style='font-size: 30px; color: #ff007f;'><strong>{st.session_state.fpb_a}</strong> dan <strong>{st.session_state.fpb_b}</strong></p>
    </div>
    """,
      unsafe_allow_html=True,
  )

  ans_fpb = st.number_input("Masukkan nilai FPB:", min_value=1, step=1)
  if st.button("🔓 DEKRIPSI GERBANG FPB"):
    real_fpb = cari_fpb(st.session_state.fpb_a, st.session_state.fpb_b)
    if ans_fpb == real_fpb:
      st.session_state.score += 20
      if st.session_state.sub_soal < 2:
        st.session_state.sub_soal += 1
        st.session_state.fpb_a = random.randint(12, 48)
        st.session_state.fpb_b = random.randint(12, 48)
      else:
        st.session_state.level = 3
        st.session_state.sub_soal = 1
      st.rerun()
    else:
      st.session_state.level = 5
      st.session_state.pesan = (
          f"FPB yang benar dari {st.session_state.fpb_a} dan"
          f" {st.session_state.fpb_b} adalah {real_fpb}."
      )
      st.rerun()

# ==========================================
# LEVEL 3: BRANKAS AKHIR MODULO (1 Soal = 30 Poin)
# ==========================================
elif st.session_state.level == 3:
  st.markdown(
      f"""
    <div class='cyber-card'>
        <h3 class='cyber-title'>💥 [LEVEL 3] Brankas Akhir — Aritmatika Modulo</h3>
        <div class='mascot-box'>
            <b>🤖 Cyber-Bot:</b> <i>"Ini ujian terakhir kita! Hitung sisa pembagian untuk membuka pintu brankas utama."</i>
        </div>
        <p>Selesaikan operasi modulo berikut:</p>
        <p style='font-size: 32px; color: #ff007f;'><strong>{st.session_state.mod_a} mod {st.session_state.mod_b}</strong></p>
        <small>(Sisa bagi dari {st.session_state.mod_a} dibagi {st.session_state.mod_b})</small>
    </div>
    """,
      unsafe_allow_html=True,
  )

  ans_mod = st.number_input("Masukkan hasil modulo:", min_value=0, step=1)
  if st.button("💥 RETAS & BUKA BRANKAS UTAMA"):
    real_mod = st.session_state.mod_a % st.session_state.mod_b
    if ans_mod == real_mod:
      st.session_state.score += 30
      st.session_state.level = 4  # Menang & Buka Brankas
      st.rerun()
    else:
      st.session_state.level = 5
      st.session_state.pesan = (
          f"Sisa pembagian {st.session_state.mod_a} dibagi"
          f" {st.session_state.mod_b} adalah {real_mod}."
      )
      st.rerun()

# ==========================================
# LAYAR 4: MENANG & BRANKAS TERBUKA (VICTORY VAULT)
# ==========================================
elif st.session_state.level == 4:
  st.balloons()
  st.markdown(
      f"""
    <div class='vault-box'>
        <h1 style='color: #00ff88; font-size: 36px;'>🔓 BRANKAS UTAMA TERBUKA!</h1>
        <h2 style='color: #ffffff;'>SELAMAT, AGEN {st.session_state.nama.upper()}!</h2>
        <p style='color: #cbd5e1; font-size: 18px;'>Kamu berhasil menembus seluruh enkripsi tanpa satu pun kesalahan!</p>
        
        <div style='background: rgba(0, 255, 136, 0.15); border: 2px dashed #00ff88; border-radius: 12px; padding: 20px; margin: 20px 0;'>
            <h3 style='color: #00ff88; margin-bottom: 10px;'>💎 ISI BRANKAS RAHASIA:</h3>
            <p style='font-size: 20px;'>🏆 <b>Trofi Master Sieve Protocol</b></p>
            <p style='font-size: 20px;'>🔑 <b>Kunci Emas Teori Bilangan Mutlak</b></p>
            <p style='font-size: 22px; color: #ff007f; margin-top: 10px;'><b>Total Skor Akhir: {st.session_state.score} / 100 Poin (SEMPURNA!)</b></p>
        </div>
    </div>
    """,
      unsafe_allow_html=True,
  )

  if st.button("🔄 Mainkan Misi Baru"):
    reset_game()
    st.rerun()

# ==========================================
# LAYAR 5: GAGAL / SALAH JAWAB (RESET KE AWAL)
# ==========================================
elif st.session_state.level == 5:
  st.markdown(
      f"""
    <div class='cyber-card' style='border-color: #ff4b4b;'>
        <h2 style='color: #ff4b4b;'>🚨 ALARM BERBUNYI: JARINGAN TERKUNCI!</h2>
        <div class='mascot-box' style='border-left-color: #ff4b4b;'>
            <b>🤖 Cyber-Bot:</b> <i>"Waduh Agen {st.session_state.nama}, jawabanmu meleset!"</i>
        </div>
        <p><i>{st.session_state.pesan}</i></p>
        <p style='color: #ff4b4b; margin-top: 15px;'><b>Konsekuensi: Alarm keamanan aktif. Kamu harus mengulang misi dari Level 1!</b></p>
    </div>
    """,
      unsafe_allow_html=True,
  )

  if st.button("🔄 Coba Lagi dari Level 1"):
    reset_game()
    st.rerun()
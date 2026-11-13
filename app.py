import random
import streamlit as st

# 1. Konfigurasi Halaman
st.set_page_config(
    page_title="Prime Breaker: The Sieve Protocol", page_icon="🔐", layout="centered"
)

# 2. Desain Visual Kustom & Animasi Latar Cyber
st.markdown(
    """
    <style>
    /* Animasi Latar Belakang Cyberpunk yang Lebih Dinamis */
    @keyframes cyberPulse {
        0% { background-color: #050814; }
        50% { background-color: #111e38; }
        100% { background-color: #050814; }
    }
    
    .stApp {
        animation: cyberPulse 6s infinite ease-in-out;
        color: #e2e8f0;
    }

    /* Kotak Cyber dengan Efek Glow Neon */
    .cyber-box {
        background-color: rgba(15, 23, 42, 0.9);
        border: 2px solid #00f0ff;
        border-radius: 12px;
        padding: 20px;
        margin-bottom: 20px;
        box-shadow: 0 0 25px rgba(0, 240, 255, 0.3);
    }

    .cyber-title {
        color: #00f0ff;
        font-family: 'Courier New', monospace;
        font-weight: bold;
        text-shadow: 0 0 12px rgba(0, 240, 255, 0.6);
    }

    div.stButton > button {
        background-color: #00f0ff;
        color: #050814;
        font-weight: bold;
        border-radius: 8px;
        border: none;
        padding: 10px 20px;
        width: 100%;
        box-shadow: 0 0 12px rgba(0, 240, 255, 0.4);
        transition: 0.3s;
    }
    div.stButton > button:hover {
        background-color: #00b8cc;
        color: #ffffff;
        box-shadow: 0 0 20px rgba(0, 240, 255, 0.8);
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
  st.session_state.level = 0  # 0 = Login, 1-3 = Level, 4 = Menang, 5 = Kalah
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


# --- HEADER GAME & BACKSOUND PLAYER ---
st.markdown(
    "<h1 class='cyber-title'>🔐 PRIME BREAKER: THE SIEVE PROTOCOL</h1>",
    unsafe_allow_html=True,
)
st.caption(
    "Protokol Keamanan Teori Bilangan | Pecahkan Kode & Selamatkan Sistem"
)

# Pemutar Audio Musik Latar (Dilengkapi kontrol play supaya tidak diblokir browser)
st.sidebar.markdown("🎵 **Cyberpunk Backsound**")
st.sidebar.audio(
    "https://cdn.pixabay.com/download/audio/2022/05/27/audio_1808fbf756.mp3?filename=cyberpunk-2099-10701.mp3",
    format="audio/mp3",
    autoplay=True,
)

# --- PANEL STATUS ---
if 1 <= st.session_state.level <= 3:
  col1, col2 = st.columns(2)
  col1.metric("🛡️ Level Aktif", f"Level {st.session_state.level} / 3")
  col2.metric("⭐ Skor Sementara", f"{st.session_state.score} / 100 Poin")
  st.progress(st.session_state.level / 3)
  st.markdown("---")

# ==========================================
# LAYAR 0: LOGIN AGEN
# ==========================================
if st.session_state.level == 0:
  st.markdown(
      """
    <div class='cyber-box'>
        <h3>⚠️ ATURAN PROTOKOL KEAMANAN</h3>
        <p>Jaringan utama terkunci. Jika kamu <b>salah menjawab satu soal pun</b>, sistem akan mengunci total dan kamu harus <b>mengulang dari Level 1</b>!</p>
        <p><i>Nyalakan musik latar di sidebar kiri untuk pengalaman hacking yang maksimal!</i></p>
    </div>
    """,
      unsafe_allow_html=True,
  )

  nama_input = st.text_input("Masukkan Nama Agen:", placeholder="Contoh: Vita")
  if st.button("🚀 MULAI MISI"):
    if nama_input.strip() != "":
      st.session_state.nama = nama_input
      st.session_state.level = 1
      st.rerun()
    else:
      st.warning("Masukkan nama agen terlebih dahulu!")

# ==========================================
# LEVEL 1: FIREWALL BILANGAN PRIMA (3 Soal x 10 Poin = 30 Poin)
# ==========================================
elif st.session_state.level == 1:
  st.markdown(
      f"""
    <div class='cyber-box'>
        <h3 class='cyber-title'>[LEVEL 1] Sieve Firewall — Soal {st.session_state.sub_soal} dari 3</h3>
        <p>Sistem mendeteksi sinyal angka: <strong style='font-size: 24px; color: #00f0ff;'>{st.session_state.num_prima}</strong></p>
        <p>Apakah angka tersebut termasuk <strong>Bilangan Prima</strong>?</p>
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
    <div class='cyber-box'>
        <h3 class='cyber-title'>[LEVEL 2] Enkripsi Euclidean (FPB) — Soal {st.session_state.sub_soal} dari 2</h3>
        <p>Temukan <strong>Faktor Persekutuan Terbesar (FPB)</strong> dari dua kunci berikut:</p>
        <p style='font-size: 24px; color: #00f0ff;'><strong>{st.session_state.fpb_a}</strong> dan <strong>{st.session_state.fpb_b}</strong></p>
    </div>
    """,
      unsafe_allow_html=True,
  )

  ans_fpb = st.number_input("Masukkan nilai FPB:", min_value=1, step=1)
  if st.button("🔑 Buka Gerbang FPB"):
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
    <div class='cyber-box'>
        <h3 class='cyber-title'>[LEVEL 3] Brankas Akhir — Aritmatika Modulo</h3>
        <p>Hitung sisa pembagian terakhir untuk meretas brankas utama:</p>
        <p style='font-size: 26px; color: #00f0ff;'><strong>{st.session_state.mod_a} mod {st.session_state.mod_b}</strong></p>
        <small>(Sisa pembagian {st.session_state.mod_a} dibagi {st.session_state.mod_b})</small>
    </div>
    """,
      unsafe_allow_html=True,
  )

  ans_mod = st.number_input("Masukkan hasil modulo:", min_value=0, step=1)
  if st.button("💥 RETAS BRANKAS UTAMA"):
    real_mod = st.session_state.mod_a % st.session_state.mod_b
    if ans_mod == real_mod:
      st.session_state.score += 30
      st.session_state.level = 4
      st.rerun()
    else:
      st.session_state.level = 5
      st.session_state.pesan = (
          f"Sisa pembagian {st.session_state.mod_a} dibagi"
          f" {st.session_state.mod_b} adalah {real_mod}."
      )
      st.rerun()

# ==========================================
# LAYAR 4: MENANG (VICTORY - SKOR 100)
# ==========================================
elif st.session_state.level == 4:
  st.balloons()
  st.markdown(
      f"""
    <div class='cyber-box' style='border-color: #00ff88;'>
        <h2 style='color: #00ff88;'>🏆 MISI BERHASIL, AGEN {st.session_state.nama.upper()}!</h2>
        <p>Tanpa satu pun kesalahan, kamu berhasil menembus seluruh protokol keamanan!</p>
        <h3>Total Skor Sempurna: {st.session_state.score} / 100 Poin</h3>
    </div>
    """,
      unsafe_allow_html=True,
  )

  if st.button("🔄 Mainkan Lagi"):
    reset_game()
    st.rerun()

# ==========================================
# LAYAR 5: GAGAL / SALAH JAWAB (RESET KE AWAL)
# ==========================================
elif st.session_state.level == 5:
  st.markdown(
      f"""
    <div class='cyber-box' style='border-color: #ff4b4b;'>
        <h2 style='color: #ff4b4b;'>🚨 SISTEM MENGUNCI: JAWABAN SALAH!</h2>
        <p>Maaf Agen <b>{st.session_state.nama}</b>, analismu keliru.</p>
        <p><i>{st.session_state.pesan}</i></p>
        <p style='color: #ff4b4b; margin-top: 15px;'><b>Konsekuensi: Protokol gagal. Kamu harus mengulang misi dari awal!</b></p>
    </div>
    """,
      unsafe_allow_html=True,
  )

  if st.button("🔄 Coba Lagi dari Level 1"):
    reset_game()
    st.rerun()
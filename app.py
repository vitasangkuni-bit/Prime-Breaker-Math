import random
import streamlit as st

# 1. Konfigurasi Halaman
st.set_page_config(
    page_title="Prime Breaker: The Sieve Protocol",
    page_icon="🎮",
    layout="centered",
)

# 2. Desain Visual Kustom Super Menarik, Colorful, & Ramah Anak
st.markdown(
    """
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    /* Background Animasi Grid Neon & Warna Warni Bergerak (Garis-garis di belakang tulisan) */
    @keyframes moveGrid {
        0% { background-position: 0 0, 0 0; }
        100% { background-position: 60px 60px, 60px 60px; }
    }
    
    @keyframes rainbowGlow {
        0% { background-color: #0f0c29; }
        33% { background-color: #302b63; }
        66% { background-color: #24243e; }
        100% { background-color: #0f0c29; }
    }
    
    .stApp {
        background-color: #0f0c29;
        background-image: 
            linear-gradient(rgba(0, 240, 255, 0.35) 2px, transparent 2px),
            linear-gradient(90deg, rgba(255, 0, 127, 0.35) 2px, transparent 2px);
        background-size: 45px 45px;
        animation: moveGrid 3s linear infinite, rainbowGlow 8s infinite ease-in-out;
        color: #ffffff;
    }

    /* Banner Judul Game Arcade Super Keren */
    .arcade-banner {
        background: linear-gradient(135deg, #ff007f, #7928ca, #00f0ff);
        border: 4px solid #ffe600;
        border-radius: 24px;
        padding: 25px;
        text-align: center;
        box-shadow: 0 0 35px rgba(255, 0, 127, 0.8), inset 0 0 15px rgba(255, 255, 255, 0.5);
        margin-bottom: 25px;
    }

    /* Kotak Kartu Game Arcade */
    .arcade-card {
        background: linear-gradient(135deg, rgba(20, 25, 50, 0.95), rgba(50, 20, 70, 0.95));
        border: 4px solid #00f0ff;
        border-radius: 24px;
        padding: 30px;
        margin-bottom: 25px;
        box-shadow: 0 0 40px rgba(0, 240, 255, 0.6), inset 0 0 20px rgba(255, 0, 127, 0.4);
    }

    /* Kotak Brankas Rahasia (Vault) */
    .vault-box {
        background: linear-gradient(135deg, rgba(40, 10, 60, 0.95), rgba(80, 20, 100, 0.95));
        border: 5px solid #ffe600;
        border-radius: 28px;
        padding: 35px;
        text-align: center;
        box-shadow: 0 0 60px rgba(255, 230, 0, 0.9);
    }

    /* Kotak Robot Lucu */
    .robot-box {
        background: linear-gradient(90deg, rgba(0, 240, 255, 0.25), rgba(255, 0, 127, 0.25));
        border: 3px dashed #ffe600;
        border-radius: 18px;
        padding: 18px 22px;
        margin-bottom: 20px;
        display: flex;
        align-items: center;
        gap: 15px;
    }

    /* Tombol Arcade Super Menarik */
    div.stButton > button {
        background: linear-gradient(90deg, #ff007f, #7928ca, #00f0ff);
        color: #ffffff;
        font-weight: bold;
        font-size: 18px;
        border-radius: 16px;
        border: 3px solid #ffe600;
        padding: 14px 28px;
        width: 100%;
        box-shadow: 0 0 25px rgba(255, 0, 127, 0.7);
        transition: 0.3s;
    }
    div.stButton > button:hover {
        background: linear-gradient(90deg, #ffe600, #00ff88, #00f0ff);
        color: #0f0c29;
        box-shadow: 0 0 35px rgba(255, 230, 0, 1);
        transform: scale(1.03);
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


# --- BANNER JUDUL UTAMA & PEMUTAR AUDIO BACKSOUND ---
st.markdown(
    """
    <div class="arcade-banner">
        <h1 style='color: #ffe600; font-family: "Courier New", monospace; text-shadow: 0 0 20px #ff007f; margin: 0; font-size: 28px;'>🎮 ⚡ PRIME BREAKER: THE SIEVE PROTOCOL 🚀</h1>
        <p style='color: #ffffff; font-size: 16px; font-weight: bold; margin-top: 8px;'>✨ Petualangan Seru Matematika & Peretasan Brankas Angka ✨</p>
    </div>
""",
    unsafe_allow_html=True,
)

# Pemutar Audio dengan tombol play jelas
st.markdown(
    """
    <div style='background: linear-gradient(90deg, rgba(255,0,127,0.3), rgba(0,240,255,0.3)); border: 3px solid #ffe600; padding: 12px; border-radius: 18px; margin-bottom: 20px; text-align: center; box-shadow: 0 0 25px rgba(255,230,0,0.5);'>
        <span style='font-size: 18px; font-weight: bold; color: #ffe600;'>🎵 MUSIK BACKSOUND ARCADE AKTIF</span><br>
        <span style='font-size: 13px; color: #ffffff;'>Tekan tombol <b>Play ▶️</b> di bawah ini untuk mendengarkan musik serunya!</span>
    </div>
""",
    unsafe_allow_html=True,
)
st.audio(
    "https://cdn.pixabay.com/download/audio/2022/05/27/audio_1808fbf756.mp3?filename=cyberpunk-2099-10701.mp3",
    format="audio/mp3",
    autoplay=True,
)

st.markdown("---")

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
        <div class='arcade-card'>
            <h2 style='color: #ffe600; text-align: center;'>🌟 SELAMAT DATANG DI DUNIA SIBER! 🌟</h2>
            <div class='robot-box'>
                <span style='font-size: 40px;'>🤖</span>
                <div>
                    <b style='color: #00f0ff; font-size: 16px;'>Robot Maskot Coby:</b><br>
                    <i style='color: #ffffff; font-size: 14px;'>“Halo Agen Cilik! Brankas harta karun berisi mahkota matematika terkunci rapat. Jawab semua teka-teki dengan benar dan jangan sampai salah, ya!”</i>
                </div>
            </div>
            <p style='text-align: center; color: #ff007f; font-weight: bold; font-size: 15px;'>⚠️ ATURAN MAIN: Jawab salah satu saja, alarm berbunyi dan harus ulang dari Level 1!</p>
        </div>
    """,
      unsafe_allow_html=True,
  )

  nama_input = st.text_input(
      "Ketik Nama Agen Hebat Kamu:", placeholder="Contoh: Agen Bintang"
  )
  if st.button("🚀 MULAI PETUALANGAN SEKARANG!"):
    if nama_input.strip() != "":
      st.session_state.nama = nama_input
      st.session_state.level = 1
      st.rerun()
    else:
      st.warning("Yuk tulis nama kamu dulu sebelum mulai misi!")

# ==========================================
# LEVEL 1: FIREWALL BILANGAN PRIMA (3 Soal x 10 Poin = 30 Poin)
# ==========================================
elif st.session_state.level == 1:
  st.markdown(
      f"""
        <div class='arcade-card'>
            <h3 style='color: #00f0ff; text-align: center;'>🔥 LEVEL 1: UJIAN SARINGAN PRIMA (Soal {st.session_state.sub_soal}/3)</h3>
            <div class='robot-box'>
                <span style='font-size: 40px;'>🤖</span>
                <div>
                    <b style='color: #00f0ff; font-size: 16px;'>Robot Maskot Coby:</b><br>
                    <i style='color: #ffffff; font-size: 14px;'>“Apakah angka ajaib di bawah ini adalah Bilangan Prima? Ayo tebak dengan cermat!”</i>
                </div>
            </div>
            <div style='text-align: center; margin: 20px 0;'>
                <span style='font-size: 45px; font-weight: bold; color: #ffe600; background: rgba(0,0,0,0.6); padding: 12px 30px; border-radius: 18px; border: 3px solid #00f0ff;'>{st.session_state.num_prima}</span>
            </div>
        </div>
    """,
      unsafe_allow_html=True,
  )

  c1, c2 = st.columns(2)
  jawab = None
  with c1:
    if st.button("✨ YA, BILANGAN PRIMA"):
      jawab = True
  with c2:
    if st.button("❌ BUKAN BILANGAN PRIMA"):
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
        <div class='arcade-card'>
            <h3 style='color: #00f0ff; text-align: center;'>🔑 LEVEL 2: GERBANG KUNCI FPB (Soal {st.session_state.sub_soal}/2)</h3>
            <div class='robot-box'>
                <span style='font-size: 40px;'>🤖</span>
                <div>
                    <b style='color: #00f0ff; font-size: 16px;'>Robot Maskot Coby:</b><br>
                    <i style='color: #ffffff; font-size: 14px;'>“Hebat! Sekarang temukan Faktor Persekutuan Terbesar (FPB) dari dua angka di bawah ini ya.”</i>
                </div>
            </div>
            <div style='text-align: center; margin: 20px 0;'>
                <span style='font-size: 35px; font-weight: bold; color: #ffe600;'>{st.session_state.fpb_a} &nbsp; & &nbsp; {st.session_state.fpb_b}</span>
            </div>
        </div>
    """,
      unsafe_allow_html=True,
  )

  ans_fpb = st.number_input(
      "Masukkan Angka Hasil FPB Kamu:", min_value=1, step=1
  )
  if st.button("🔓 BUKA GERBANG FPB"):
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
        <div class='arcade-card'>
            <h3 style='color: #ff007f; text-align: center;'>💥 LEVEL 3: BRANKAS UTAMA MODULO</h3>
            <div class='robot-box'>
                <span style='font-size: 40px;'>🤖</span>
                <div>
                    <b style='color: #00f0ff; font-size: 16px;'>Robot Maskot Coby:</b><br>
                    <i style='color: #ffffff; font-size: 14px;'>“Tinggal selangkah lagi! Hitung sisa bagi (modulo) untuk membuka brankas rahasia!”</i>
                </div>
            </div>
            <div style='text-align: center; margin: 20px 0;'>
                <span style='font-size: 40px; font-weight: bold; color: #ffe600;'>{st.session_state.mod_a} mod {st.session_state.mod_b}</span>
            </div>
        </div>
    """,
      unsafe_allow_html=True,
  )

  ans_mod = st.number_input(
      "Masukkan Sisa Pembagian (Modulo):", min_value=0, step=1
  )
  if st.button("💥 RETAS & BUKA BRANKAS SEKARANG!"):
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
# LAYAR 4: MENANG & BRANKAS TERBUKA (VICTORY VAULT)
# ==========================================
elif st.session_state.level == 4:
  st.balloons()
  st.markdown(
      f"""
        <div class='vault-box'>
            <h1 style='color: #00ff88; font-size: 34px;'>🎉 HORE! BRANKAS RAHASIA TERBUKA! 🎉</h1>
            <h2 style='color: #ffffff;'>LUAR BIASA, AGEN {st.session_state.nama.upper()}!</h2>
            <p style='color: #cbd5e1; font-size: 17px;'>Kamu berhasil menyelesaikan semua misi matematika dengan sempurna!</p>
            
            <div style='background: rgba(0, 255, 136, 0.2); border: 3px dashed #00ff88; border-radius: 18px; padding: 22px; margin: 20px 0;'>
                <h3 style='color: #ffe600; margin-bottom: 12px;'>🎁 HADIAH DI DALAM BRANKAS:</h3>
                <p style='font-size: 20px;'>👑 <b>Mahkota Master Matematika Cilik</b></p>
                <p style='font-size: 20px;'>🏆 <b>Trofi Emas Agen Sibel Terhebat</b></p>
                <p style='font-size: 24px; color: #00ff88; margin-top: 12px; font-weight: bold;'>TOTAL SKOR: {st.session_state.score} / 100 POIN (SEMPURNA!)</p>
            </div>
        </div>
    """,
      unsafe_allow_html=True,
  )

  if st.button("🔄 MAIN LAGI DARI AWAL"):
    reset_game()
    st.rerun()

# ==========================================
# LAYAR 5: GAGAL / SALAH JAWAB (RESET KE AWAL)
# ==========================================
elif st.session_state.level == 5:
  st.markdown(
      f"""
        <div class='arcade-card' style='border-color: #ff4b4b; background: linear-gradient(135deg, rgba(50,10,10,0.95), rgba(20,20,30,0.95));'>
            <h2 style='color: #ff4b4b; text-align: center;'>🚨 WADUH, ALARM BERBUNYI! 🚨</h2>
            <div class='robot-box' style='border-color: #ff4b4b;'>
                <span style='font-size: 40px;'>🤖</span>
                <div>
                    <b style='color: #ff4b4b; font-size: 16px;'>Robot Maskot Coby:</b><br>
                    <i style='color: #ffffff; font-size: 14px;'>“Sayang sekali Agen {st.session_state.nama}, jawabanmu kurang tepat!”</i>
                </div>
            </div>
            <p style='text-align: center; font-size: 15px; color: #ffffff;'>{st.session_state.pesan}</p>
            <p style='text-align: center; color: #ff4b4b; font-weight: bold; font-size: 17px; margin-top: 15px;'>🔄 Jangan menyerah! Ayo ulangi lagi dari Level 1 untuk membuka brankasnya!</p>
        </div>
    """,
      unsafe_allow_html=True,
  )

  if st.button("🔄 COBA LAGI DARI LEVEL 1"):
    reset_game()
    st.rerun()
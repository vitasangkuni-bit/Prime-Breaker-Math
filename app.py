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
    
    /* Background Animasi Grid Neon & Warna Warni Bergerak (Area yang Dilingkari Merah) */
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

    /* Banner Judul Game Arcade Super Keren (Area Atas yang Dilingkari Hijau) */
    .arcade-banner {
        background: linear-gradient(135deg, #ff007f, #7928ca, #00f0ff);
        border: 4px solid #ffe600;
        border-radius: 24px;
        padding: 25px;
        text-align: center;
        box-shadow: 0 0 35px rgba(255, 0, 127, 0.8), inset 0 0 15px rgba(255, 255, 255, 0.5);
        margin-bottom: 25px;
        animation: bannerPulse 2s infinite ease-in-out;
    }

    @keyframes bannerPulse {
        0% { transform: scale(1); box-shadow: 0 0 30px rgba(255, 0, 127, 0.7); }
        50% { transform: scale(1.01); box-shadow: 0 0 50px rgba(0, 240, 255, 0.9); }
        100% { transform: scale(1); box-shadow: 0 0 30px rgba(255, 0, 127, 0.7); }
    }

    /* Kotak Kartu Game Arcade (Area Bawah yang Dilingkari Hijau) */
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
        animation: pulseVault 1.5s infinite ease-in-out;
    }

    @keyframes pulseVault {
        0% { box-shadow: 0 0 30px rgba(255, 230, 0, 0.5); }
        50% { box-shadow: 0 0 70px rgba(255, 230, 0, 1); }
        100% { box-shadow: 0 0 30px rgba(255, 230, 0, 0.5); }
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
        padding: 14px 2
import streamlit as st
from datetime import datetime

# Konfigurasi Halaman Streamlit
st.set_page_config(
    page_title="Sekretariat DPRK Aceh Jaya",
    page_icon="🏛️",
    layout="wide"
)

# Custom CSS untuk gaya header dan navigasi
st.markdown("""
    <style>
    /* Styling Header Atas */
    .header-title {
        font-size: 24px;
        font-weight: bold;
        color: #1E3A8A;
        margin-bottom: 0px;
    }
    .header-subtitle {
        font-size: 14px;
        color: #4B5563;
    }
    .weather-box {
        text-align: right;
        font-size: 14px;
        color: #374151;
    }
    .slogan {
        font-size: 13px;
        color: #6B7280;
        border-top: 1px solid #E5E7EB;
        border-bottom: 1px solid #E5E7EB;
        padding: 6px 0;
        margin-top: 10px;
        margin-bottom: 15px;
    }
    /* Banner Styling */
    .banner-box {
        background-color: #2D6A4F;
        color: white;
        padding: 30px;
        border-radius: 8px;
        text-align: center;
        font-size: 28px;
        font-weight: bold;
    }
    </style>
""", unsafe_allow_html=True)

# Top Bar: Logo/Judul & Widget Cuaca
col_logo, col_weather = st.columns([3, 1])

with col_logo:
    st.markdown('<div class="header-title">Sekretariat DPRK</div>', unsafe_allow_html=True)
    st.markdown('<div class="header-subtitle">Dewan Perwakilan Rakyat Kabupaten Aceh Jaya</div>', unsafe_allow_html=True)

with col_weather:
    st.markdown("""
        <div class="weather-box">
            📍 <b>Aceh Jaya</b><br>
            ☁️ 26 °C &nbsp;|&nbsp; Sumber: BMKG
        </div>
    """, unsafe_allow_html=True)

# Navigation Menu
menu_items = [
    "BERANDA", "PROFIL", "INFORMASI", "GALERI", 
    "LAYANAN", "INFORMASI PUBLIK", "KONTAK", "PORA ACEH 2026"
]

selected_menu = st.radio(
    label="Navigasi Utama",
    options=menu_items,
    horizontal=True,
    label_visibility="collapsed"
)

# Slogan
st.markdown(
    '<div class="slogan">Dewan Perwakilan Rakyat Kabupaten Aceh Jaya | Menuju Kabupaten Aceh Jaya yang lebih baik</div>', 
    unsafe_allow_html=True
)

# Konten berdasarkan Menu yang Dipilih
if selected_menu == "BERANDA":
    col_welcome, col_banner = st.columns([1, 2])
    
    with col_welcome:
        st.subheader("SELAMAT DATANG")
        st.write("di Website Resmi")
        st.header("Sekretariat DPRK")
        st.write("Kabupaten Aceh Jaya")
        
    with col_banner:
        st.markdown(
            '<div class="banner-box">Pemerintah<br>Kabupaten Aceh Jaya</div>', 
            unsafe_allow_html=True
        )

elif selected_menu == "PROFIL":
    st.title("Profil DPRK Aceh Jaya")
    st.write("Halaman ini berisi struktur organisasi dan profil pimpinan DPRK.")

elif selected_menu == "INFORMASI":
    st.title("Informasi Publik")
    st.write("Pengumuman dan berita terbaru terkait agenda DPRK Aceh Jaya.")

else:
    st.title(f"Halaman {selected_menu}")
    st.write(f"Konten untuk menu {selected_menu} sedang dalam pengembangan.")
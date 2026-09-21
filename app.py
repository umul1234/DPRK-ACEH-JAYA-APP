import streamlit as st
from datetime import datetime, timedelta
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import time
import random

# =========================================================
# KONFIGURASI HALAMAN
# =========================================================
st.set_page_config(
    page_title="DPRK Aceh Jaya | Portal Informasi Publik",
    page_icon="🏛️",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# =========================================================
# LOGO URL
# =========================================================
LOGO_URL = "https://i.imgur.com/bTNXnLF.png"

# =========================================================
# SESSION STATE
# =========================================================
if "page" not in st.session_state:
    st.session_state.page = "Beranda"
if "dark_mode" not in st.session_state:
    st.session_state.dark_mode = False
if "lang" not in st.session_state:
    st.session_state.lang = "ID"
if "chat_open" not in st.session_state:
    st.session_state.chat_open = False
if "show_notif" not in st.session_state:
    st.session_state.show_notif = False
if "news_index" not in st.session_state:
    st.session_state.news_index = 0

# =========================================================
# DATA
# =========================================================
PAGES = {
    "Beranda": "Beranda",
    "Profil": "Profil & Pimpinan",
    "Berita": "Berita & Agenda",
    "Galeri": "Galeri Foto & Video",
    "Layanan": "Layanan & Pengaduan",
    "JDIH": "JDIH & Transparansi",
    "Kontak": "Hubungi Kami",
}

# WARTA DPRK - Berita Utama
WARTA_DPRK = [
    {
        "title": "DPRK Aceh Jaya Gelar Rapat Paripurna Pandangan Fraksi terhadap Pertanggungjawaban APBK 2025",
        "date": "Jumat, 14 Agustus 2026",
        "desc": "Dewan Perwakilan Rakyat Kabupaten (DPRK) Aceh Jaya menggelar Rapat Paripurna Ke-IX Masa Persidangan II Tahun Sidang membahas pandangan fraksi terhadap pertanggungjawaban APBK.",
        "image": "https://images.unsplash.com/photo-1556761175-b413da4baf72?auto=format&fit=crop&w=800&q=80",
        "kategori": "Paripurna",
        "views": 1245,
    },
    {
        "title": "DPRK Aceh Jaya Gelar Rapat Paripurna ke-VIII Masa Persidangan II, Bahas Pertanggungjawaban APBK 2025 dan Perubahan AKD",
        "date": "Kamis, 30 Juli 2026",
        "desc": "Rapat Paripurna ke-VIII Masa Persidangan II membahas pertanggungjawaban APBK 2025 dan Perubahan Anggaran Kas Daerah.",
        "image": "https://images.unsplash.com/photo-1529107386315-e1a2ed48a620?auto=format&fit=crop&w=800&q=80",
        "kategori": "Paripurna",
        "views": 987,
    },
    {
        "title": "Ketua DPRK Aceh Jaya Dukung Pelestarian Mangrove, Dorong Penguatan Ekosistem Pesisir",
        "date": "Minggu, 26 Juli 2026",
        "desc": "Ketua DPRK Aceh Jaya Musliadi Z, S.E menyampaikan dukungan terhadap kegiatan Penanaman Mangrove Serentak dalam rangka memperingati Hari Mangrove.",
        "image": "https://images.unsplash.com/photo-1589578527966-fdac0f44566c?auto=format&fit=crop&w=800&q=80",
        "kategori": "Lingkungan",
        "views": 756,
    },
    {
        "title": "Ketua DPRK Aceh Jaya Apresiasi Kejari Aceh Jaya Berhasil Pulihkan Keuangan Negara Rp2,05 Miliar",
        "date": "Rabu, 22 Juli 2026",
        "desc": "Ketua DPRK Aceh Jaya menghadiri kegiatan Press Release Capaian Pemulihan Keuangan Negara yang diselenggarakan oleh Kejaksaan Negeri Aceh Jaya.",
        "image": "https://images.unsplash.com/photo-1577962917302-cd874c4e31d2?auto=format&fit=crop&w=800&q=80",
        "kategori": "Hukum",
        "views": 1123,
    },
]

# KESEKRETARIATAN
KESEKRETARIATAN = [
    {
        "title": "Apel Pagi Rutin, ASN DPRK Aceh Jaya Diingatkan Disiplin dan Komitmen Kerja",
        "date": "Senin, 06 April 2026",
        "desc": "Dalam amanatnya, Yuswardi menekankan pentingnya kedisiplinan dan komitmen dalam menjalankan tugas sebagai ASN.",
    },
    {
        "title": "Sekretaris DPRK Aceh Jaya Ikuti Vidcon Entry Meeting Pemeriksaan Laporan Keuangan 2025",
        "date": "Kamis, 02 April 2026",
        "desc": "Sekretaris DPRK Aceh Jaya, Abu Bakar, S.Pd.I., MH mengikuti video conference Entry Meeting Pemeriksaan Laporan Keuangan 2025.",
    },
]

# AGENDA TERKINI
AGENDA_TERKINI = [
    {
        "tanggal": "09 September 2026",
        "judul": "Rapat Pleno DPRK Aceh Jaya - 09 September 2026",
        "desc": "Rapat Pleno DPRK Aceh Jaya terhadap Rancangan Perubahan KUA-PPAS APBK Aceh Jaya Tahun Anggaran",
        "waktu": "09:00 WIB",
        "lokasi": "Ruang Rapat Paripurna",
    },
    {
        "tanggal": "07 September 2026",
        "judul": "Rapat Komisi III DPRK Aceh Jaya - 07 September 2026",
        "desc": "Rapat Dengar Pendapat Komisi III terkait Realisasi Program dan Kegiatan Pembangunan Jalan dan Jembatan pada Dinas PUPR.",
        "waktu": "10:00 WIB",
        "lokasi": "Ruang Komisi III",
    },
    {
        "tanggal": "01 September 2026",
        "judul": "Rapat Badan Musyawarah DPRK Aceh Jaya - 01 September 2026",
        "desc": "Rapat Badan Musyawarah tentang Penetapan Jadwal Rapat Paripurna DPRK Aceh Jaya.",
        "waktu": "14:00 WIB",
        "lokasi": "Ruang Banmus",
    },
]

# PIMPINAN DAN ANGGOTA DPRK
PIMPINAN_DAN_ANGGOTA = [
    ("MUSLIADI Z, S.E", "KETUA DPRK"),
    ("IRWANTO. NP", "WAKIL KETUA I DPRK"),
    ("TEUKU ASRIZAL, S.H", "WAKIL KETUA II DPRK"),
    ("ISKANDAR IBRAHIM", "ANGGOTA DPRK / KETUA KOMISI I"),
    ("H. DASRIL ARAHMAN. IB, S.E", "ANGGOTA DPRK / WAKIL KETUA KOMISI I"),
    ("WANTI CAHYA", "ANGGOTA DPRK / SEKRETARIS KOMISI I"),
    ("MUSLIM", "ANGGOTA DPRK / ANGGOTA KOMISI I"),
    ("Ir. FAUZI YAHYA", "ANGGOTA DPRK / KETUA KOMISI II"),
    ("AZHAR", "ANGGOTA DPRK / WAKIL KETUA KOMISI II"),
    ("FITRA AKHYAR, ST", "ANGGOTA DPRK / SEKRETARIS KOMISI II"),
    ("SAFRIYANTONI", "ANGGOTA DPRK / ANGGOTA KOMISI II"),
    ("AYUDI ILHAM, S.E", "ANGGOTA DPRK / ANGGOTA KOMISI II"),
    ("SUDIRMAN, S.P", "ANGGOTA DPRK / KETUA KOMISI III"),
    ("ABDUL MUTHALLEB", "ANGGOTA DPRK / WAKIL KETUA KOMISI III"),
    ("Drs. H. T. IRFAN TB., M.Si", "ANGGOTA DPRK / SEKRETARIS KOMISI III"),
    ("MUHAMMAD DIAH, S.E", "ANGGOTA DPRK / ANGGOTA KOMISI III"),
    ("HAZAMI, S.Pd", "ANGGOTA DPRK / KETUA KOMISI IV"),
    ("MUHAMMAD JAMIN", "ANGGOTA DPRK / WAKIL KETUA KOMISI IV"),
    ("HJ. FITRI MAYA LISA, S.Sos", "ANGGOTA DPRK / SEKRETARIS KOMISI IV"),
    ("USMAN. ID", "ANGGOTA DPRK / ANGGOTA KOMISI IV"),
]

# PEJABAT SEKRETARIAT
PEJABAT_SEKRETARIAT = [
    ("ABU BAKAR, S.Pd.I., M.H", "Sekretaris DPRK Aceh Jaya"),
    ("IRMA HANUM, SH", "Staf Ahli Bidang Pemerintahan, Hukum dan Politik"),
    ("HIDAYAT, SE., M.Si", "Kepala Bagian Umum dan Keuangan"),
    ("YUSWARDI, S.Kom", "Kepala Bagian Persidangan dan Perundang-Undangan"),
    ("NELLI FAUZIANA, SH., MH", "Kepala Bagian Fasilitasi Penganggaran dan Pengawasan"),
    ("IHSAN SALIM, S.A.P", "Kepala Sub Bagian Tata Usaha dan Kepegawaian"),
]

# JDIH DATA
JDIH_DATA = [
    ["1", "Qanun No. 5/2025", "Ketertiban Umum dan Ketenteraman Masyarakat", "Berlaku", "2025"],
    ["2", "Perbup No. 12/2026", "Penjabaran APBK Aceh Jaya 2026", "Berlaku", "2026"],
    ["3", "Qanun No. 2/2024", "Perlindungan Korban Bencana Alam", "Berlaku", "2024"],
    ["4", "Qanun No. 3/2024", "Pengelolaan Sampah dan Kebersihan", "Berlaku", "2024"],
    ["5", "Perbup No. 08/2025", "Standar Operasional Prosedur Pelayanan", "Berlaku", "2025"],
    ["6", "Qanun No. 1/2023", "Rencana Tata Ruang Wilayah", "Dicabut", "2023"],
]

# STATISTIK DATA
STATISTIK_DATA = {
    "Tahun": ["2021", "2022", "2023", "2024", "2025", "2026"],
    "Rapat": [45, 52, 48, 60, 55, 58],
    "Produk Hukum": [12, 15, 18, 22, 20, 24],
    "Pengaduan": [89, 95, 87, 120, 110, 135],
}

# =========================================================
# CSS STYLE - SUPER PREMIUM v2.0
# =========================================================
st.markdown(
    """
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=Plus+Jakarta+Sans:wght@500;600;700;800&display=swap');

:root {
    --primary: #064e3b;
    --primary-dark: #022c22;
    --primary-2: #0f6b58;
    --primary-3: #e9f5f1;
    --gold: #d5a52b;
    --gold-light: #fcd34d;
    --gold-soft: #f7efd4;
    --dark: #17322d;
    --text: #273936;
    --muted: #71817d;
    --bg: #f6f8f7;
    --white: #ffffff;
    --border: #e1e8e5;
    --shadow: 0 8px 28px rgba(12, 74, 62, .08);
    --shadow-lg: 0 20px 50px rgba(12, 74, 62, .15);
}

* { box-sizing: border-box; font-family: 'Inter', sans-serif; }
html, body, [class*="css"] { font-family: 'Inter', sans-serif; }
#MainMenu, footer, header { visibility: hidden; height: 0; }
.stApp { background: var(--bg); color: var(--text); transition: background 0.3s ease; }
.block-container { max-width: 100%; padding: 0 !important; }
section[data-testid="stSidebar"] { display: none; }

/* Dark Mode */
body.dark-mode {
    --bg: #0a1f1a;
    --text: #e8f0ed;
    --muted: #8fa39d;
    --border: #1e3d34;
    --white: #0f2a24;
}
body.dark-mode .stApp { background: #0a1f1a !important; }
body.dark-mode .brand-wrap { background: #0f2a24 !important; }
body.dark-mode .news-card, body.dark-mode .warta-item,
body.dark-mode .service-box, body.dark-mode .agenda-wrap,
body.dark-mode .profile-card { background: #0f2a24 !important; border-color: #1e3d34 !important; }

/* =========================================
   TOP BAR & BRAND
   ========================================= */
.govbar { 
    background: linear-gradient(90deg, #022c22 0%, #064e3b 100%); 
    color: rgba(255,255,255,.88); 
    min-height: 42px; 
    padding: 0 6%; 
    display: flex; 
    align-items: center; 
    justify-content: space-between; 
    font-size: 12px;
    position: relative;
    overflow: hidden;
}
.govbar::before {
    content: '';
    position: absolute;
    top: 0; left: -100%; right: 0; bottom: 0;
    background: linear-gradient(90deg, transparent, rgba(213,165,43,0.1), transparent);
    animation: shine 8s infinite;
}
@keyframes shine {
    0% { left: -100%; }
    50% { left: 100%; }
    100% { left: 100%; }
}
.govbar-left, .govbar-right { display: flex; gap: 20px; align-items: center; }
.govbar strong { color: #fff; }
.govbar-right a { color: rgba(255,255,255,.88); text-decoration: none; transition: color .15s ease; }
.govbar-right a:hover { color: var(--gold-light); text-decoration: underline; }

/* Brand */
.brand-wrap { background: #fff; border-bottom: 1px solid #e7ecea; padding: 18px 6%; position: relative; }
.brand-inner { display: flex; align-items: center; justify-content: space-between; gap: 24px; }
.brand { display: flex; align-items: center; gap: 14px; }
.brand-logo { width: 70px; height: 70px; border-radius: 8px; background: #fff; display: flex; align-items: center; justify-content: center; box-shadow: 0 4px 12px rgba(12,74,62,.18); overflow: hidden; transition: transform 0.3s ease; }
.brand-logo:hover { transform: scale(1.05) rotate(2deg); }
.brand-logo img { width: 100%; height: 100%; object-fit: contain; }
.brand-title { color: #123b33; font-family: 'Plus Jakarta Sans', sans-serif; font-size: 18px; line-height: 1.2; font-weight: 800; text-transform: uppercase; }
.brand-subtitle { margin-top: 4px; color: #788783; font-size: 11px; letter-spacing: .6px; }

/* =========================================
   NAVIGATION - SUPER PREMIUM
   ========================================= */
.nav-wrap { 
    background: linear-gradient(180deg, #065f46 0%, #022c22 100%); 
    border-bottom: 2px solid var(--gold); 
    padding: 0 6%;
    box-shadow: 0 8px 32px rgba(0,0,0,0.2), 0 2px 8px rgba(0,0,0,0.1);
    position: sticky;
    top: 0;
    z-index: 999;
}
.nav-wrap::before {
    content: '';
    position: absolute;
    top: 0; left: 0; right: 0;
    height: 1px;
    background: linear-gradient(90deg, transparent, rgba(255,255,255,0.4), transparent);
}
.nav-inner { min-height: 64px; display: flex; align-items: center; gap: 0; justify-content: center; }

.nav-button .stButton > button, 
.nav-button-active .stButton > button {
    background: transparent !important; 
    border: 1px solid transparent !important; 
    color: rgba(255,255,255,0.85) !important;
    font-size: 12.5px !important;
    font-weight: 700 !important;
    font-family: 'Plus Jakarta Sans', sans-serif !important;
    border-radius: 6px !important;
    padding: 14px 16px !important;
    min-height: 48px !important;
    width: 100% !important;
    transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1) !important;
    letter-spacing: 0.8px !important;
    text-transform: uppercase !important;
    white-space: nowrap !important;
    text-shadow: 0 1px 2px rgba(0,0,0,0.3);
}
.nav-button .stButton > button:hover { 
    color: #ffffff !important; 
    background: rgba(255,255,255,0.08) !important;
    border-color: rgba(255,255,255,0.15) !important;
    transform: translateY(-2px);
    box-shadow: 0 4px 12px rgba(0,0,0,0.15);
}
.nav-button-active .stButton > button {
    color: #ffffff !important; 
    font-weight: 800 !important; 
    background: linear-gradient(135deg, rgba(213, 165, 43, 0.2) 0%, rgba(213, 165, 43, 0.05) 100%) !important;
    border-color: rgba(213, 165, 43, 0.5) !important;
    box-shadow: 0 0 20px rgba(213, 165, 43, 0.15), inset 0 1px 0 rgba(255,255,255,0.1);
}

/* Running Text Premium */
.running-text-wrap { 
    background: linear-gradient(90deg, var(--gold) 0%, #e8b93a 50%, var(--gold) 100%); 
    color: var(--dark); 
    padding: 12px 0; 
    overflow: hidden; 
    white-space: nowrap; 
    border-bottom: 2px solid var(--primary);
    position: relative;
}
.running-text-wrap::before, .running-text-wrap::after {
    content: '';
    position: absolute;
    top: 0; bottom: 0;
    width: 60px;
    z-index: 2;
}
.running-text-wrap::before { left: 0; background: linear-gradient(90deg, var(--gold), transparent); }
.running-text-wrap::after { right: 0; background: linear-gradient(-90deg, var(--gold), transparent); }
.running-text { display: inline-block; padding-left: 100%; animation: marquee 40s linear infinite; font-size: 13px; font-weight: 600; }
@keyframes marquee { 0% { transform: translate(0, 0); } 100% { transform: translate(-100%, 0); } }

/* Hero dengan animasi */
.hero { 
    position: relative; 
    min-height: 520px; 
    display: flex; 
    align-items: center; 
    overflow: hidden; 
    background: linear-gradient(90deg, rgba(4,43,36,.95) 0%, rgba(8,74,62,.78) 45%, rgba(8,74,62,.35) 100%), 
                url('https://images.unsplash.com/photo-1529107386315-e1a2ed48a620?auto=format&fit=crop&w=1800&q=85') center/cover no-repeat; 
}
.hero::before {
    content: '';
    position: absolute;
    top: 0; left: 0; right: 0; bottom: 0;
    background: radial-gradient(ellipse at 30% 50%, rgba(213,165,43,0.15) 0%, transparent 60%);
    animation: pulse 4s ease-in-out infinite;
}
@keyframes pulse {
    0%, 100% { opacity: 0.5; }
    50% { opacity: 1; }
}
.hero-content { width: 88%; max-width: 1250px; margin: 0 auto; padding: 70px 0; color: white; position: relative; z-index: 2; }
.hero-kicker { 
    display: inline-block; 
    color: #f8df87; 
    font-size: 12px; 
    font-weight: 800; 
    letter-spacing: 1.5px; 
    margin-bottom: 14px;
    padding: 6px 14px;
    background: rgba(213,165,43,0.15);
    border: 1px solid rgba(213,165,43,0.3);
    border-radius: 20px;
    animation: fadeInUp 0.8s ease;
}
.hero h1 { 
    max-width: 720px; 
    font-family: 'Plus Jakarta Sans', sans-serif; 
    font-size: clamp(34px, 5vw, 60px); 
    line-height: 1.08; 
    margin: 0 0 20px; 
    font-weight: 800;
    animation: fadeInUp 1s ease;
}
.hero p { 
    max-width: 650px; 
    color: rgba(255,255,255,.88); 
    font-size: 16px; 
    line-height: 1.75; 
    margin-bottom: 28px;
    animation: fadeInUp 1.2s ease;
}
.hero-buttons { display: flex; flex-wrap: wrap; gap: 12px; animation: fadeInUp 1.4s ease; }
.hero-btn { 
    display: inline-block; 
    padding: 14px 26px; 
    border-radius: 6px; 
    background: var(--gold); 
    color: #fff !important; 
    text-decoration: none; 
    font-weight: 700; 
    font-size: 13px; 
    transition: all .3s ease;
    box-shadow: 0 4px 15px rgba(213,165,43,0.3);
}
.hero-btn:hover { 
    background: #c1961f; 
    transform: translateY(-3px); 
    box-shadow: 0 10px 25px rgba(213,165,43,0.5);
}
.hero-btn.secondary { 
    background: rgba(255,255,255,.12); 
    border: 1px solid rgba(255,255,255,.55);
    box-shadow: none;
}
.hero-btn.secondary:hover { background: rgba(255,255,255,.2); box-shadow: 0 10px 25px rgba(0,0,0,0.2); }

@keyframes fadeInUp {
    from { opacity: 0; transform: translateY(30px); }
    to { opacity: 1; transform: translateY(0); }
}

/* Floating Stats */
.floating-stats {
    position: absolute;
    bottom: 40px;
    right: 6%;
    display: flex;
    gap: 20px;
    z-index: 3;
    animation: fadeInUp 1.6s ease;
}
.floating-stat {
    background: rgba(255,255,255,0.1);
    backdrop-filter: blur(10px);
    border: 1px solid rgba(255,255,255,0.2);
    padding: 15px 20px;
    border-radius: 10px;
    text-align: center;
    min-width: 100px;
}
.floating-stat-num { color: var(--gold-light); font-size: 24px; font-weight: 800; }
.floating-stat-label { color: rgba(255,255,255,0.7); font-size: 10px; margin-top: 4px; }

/* Content */
.content { width: 88%; max-width: 1250px; margin: 0 auto; }
.section { padding: 48px 0; }
.section-head { display: flex; justify-content: space-between; align-items: end; gap: 20px; margin-bottom: 24px; }
.section-kicker { color: var(--primary-2); font-size: 11px; font-weight: 800; letter-spacing: 1.4px; text-transform: uppercase; margin-bottom: 6px; }
.section-title { color: #183d35; font-family: 'Plus Jakarta Sans', sans-serif; font-size: 27px; font-weight: 800; margin: 0; }
.section-desc { color: var(--muted); font-size: 13px; line-height: 1.6; margin-top: 7px; }

/* Service Box dengan hover 3D */
.service-box { 
    background: #fff; 
    border: 1px solid var(--border); 
    min-height: 160px; 
    padding: 25px 20px; 
    text-align: center; 
    transition: all .3s cubic-bezier(0.4, 0, 0.2, 1);
    border-radius: 12px;
    position: relative;
    overflow: hidden;
}
.service-box::before {
    content: '';
    position: absolute;
    top: 0; left: 0; right: 0;
    height: 3px;
    background: linear-gradient(90deg, var(--primary), var(--gold));
    transform: scaleX(0);
    transition: transform 0.4s ease;
}
.service-box:hover::before { transform: scaleX(1); }
.service-box:hover { 
    transform: translateY(-8px); 
    border-color: #b9d6ce; 
    box-shadow: 0 20px 40px rgba(12,74,62,0.15);
}
.service-icon { 
    width: 60px; 
    height: 60px; 
    margin: 0 auto 14px; 
    border-radius: 50%; 
    background: var(--primary-3); 
    color: var(--primary); 
    display: flex; 
    align-items: center; 
    justify-content: center; 
    font-size: 26px; 
    transition: all .4s ease;
}
.service-box:hover .service-icon { transform: scale(1.15) rotate(8deg); }
.service-icon.accent-gold { background: var(--gold-soft); color: #a97e1c; }
.service-icon.accent-blue { background: #e7eef7; color: #2f5f8f; }
.service-title { color: #183d35; font-size: 14px; font-weight: 800; margin-bottom: 7px; }
.service-desc { color: #7a8884; font-size: 11px; line-height: 1.5; }

/* News Grid */
.news-grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(280px, 1fr)); gap: 24px; }
.news-card { 
    background: #fff; 
    border: 1px solid var(--border); 
    border-radius: 12px; 
    overflow: hidden; 
    transition: all .3s ease; 
    height: 100%; 
    display: flex; 
    flex-direction: column;
    position: relative;
}
.news-card::after {
    content: '';
    position: absolute;
    bottom: 0; left: 0; right: 0;
    height: 3px;
    background: linear-gradient(90deg, var(--gold), var(--primary));
    transform: scaleX(0);
    transition: transform 0.4s ease;
}
.news-card:hover::after { transform: scaleX(1); }
.news-card:hover { 
    box-shadow: 0 20px 40px rgba(12,74,62,0.15); 
    border-color: #b9d6ce;
    transform: translateY(-4px);
}
.news-card-img { width: 100%; height: 180px; object-fit: cover; transition: transform .5s ease; }
.news-card:hover .news-card-img { transform: scale(1.08); }
.news-card-img-wrap { overflow: hidden; position: relative; }
.news-card-category {
    position: absolute;
    top: 12px;
    left: 12px;
    background: var(--gold);
    color: #fff;
    padding: 4px 10px;
    border-radius: 4px;
    font-size: 10px;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 0.5px;
}
.news-card-views {
    position: absolute;
    top: 12px;
    right: 12px;
    background: rgba(0,0,0,0.6);
    color: #fff;
    padding: 4px 10px;
    border-radius: 4px;
    font-size: 10px;
    font-weight: 600;
}
.news-card-body { padding: 18px; flex: 1; display: flex; flex-direction: column; }
.news-card h3 { color: #173b33; font-family: 'Plus Jakarta Sans', sans-serif; font-size: 16px; line-height: 1.4; margin: 0 0 8px; font-weight: 700; flex: 1; }
.news-card p { color: #71817d; font-size: 12px; line-height: 1.6; margin: 0 0 12px; }
.news-date { color: var(--primary-2); font-size: 11px; font-weight: 600; display: flex; align-items: center; gap: 5px; }

/* Warta DPRK List */
.warta-list { display: flex; flex-direction: column; gap: 16px; }
.warta-item { 
    background: #fff; 
    border: 1px solid var(--border); 
    border-radius: 12px; 
    padding: 20px; 
    transition: all .3s ease;
    border-left: 4px solid var(--primary-3);
}
.warta-item:hover { 
    box-shadow: 0 15px 30px rgba(12,74,62,0.1);
    border-left-color: var(--gold);
    transform: translateX(5px);
}
.warta-item h3 { color: var(--primary); font-family: 'Plus Jakarta Sans', sans-serif; font-size: 16px; margin: 0 0 8px; font-weight: 700; line-height: 1.4; }
.warta-item .date { color: var(--gold); font-size: 12px; font-weight: 700; margin-bottom: 8px; display: block; }
.warta-item p { color: var(--muted); font-size: 13px; line-height: 1.6; margin: 0; }

/* Agenda */
.agenda-wrap { background: #fff; border: 1px solid var(--border); border-radius: 12px; padding: 22px; }
.agenda-item { margin-bottom: 20px; padding-bottom: 20px; border-bottom: 1px solid var(--border); transition: all 0.3s ease; }
.agenda-item:last-child { border-bottom: none; margin-bottom: 0; padding-bottom: 0; }
.agenda-item:hover { padding-left: 10px; }
.agenda-date-badge { 
    display: inline-block; 
    background: linear-gradient(135deg, var(--primary), var(--primary-2)); 
    color: white; 
    padding: 6px 12px; 
    border-radius: 6px; 
    font-size: 11px; 
    font-weight: 700; 
    margin-bottom: 10px;
    box-shadow: 0 3px 10px rgba(6,78,59,0.3);
}
.agenda-title { color: #1b4138; font-weight: 800; font-size: 15px; margin-bottom: 8px; }
.agenda-desc { color: #7a

import streamlit as st
from datetime import datetime
import pandas as pd
import plotly.express as px
import random

# =========================================================
# KONFIGURASI HALAMAN
# =========================================================
st.set_page_config(
    page_title="Sekretariat DPRK | DPRK Aceh Jaya",
    page_icon="🏛️",
    layout="wide",
    initial_sidebar_state="collapsed",
)

LOGO_URL = "https://i.imgur.com/bTNXnLF.png"

# =========================================================
# SESSION STATE
# =========================================================
if "page" not in st.session_state:
    st.session_state.page = "Beranda"
if "slide_index" not in st.session_state:
    st.session_state.slide_index = 0
if "visitor_count" not in st.session_state:
    st.session_state.visitor_count = random.randint(15000, 25000)

# =========================================================
# DATA
# =========================================================
PAGES = {
    "Beranda": "Beranda",
    "Profil": "Profil",
    "Berita": "Berita",
    "Galeri": "Galeri",
    "Layanan": "Layanan",
    "JDIH": "JDIH",
    "Kontak": "Kontak",
}

HERO_SLIDES = [
    {
        "image": "https://images.unsplash.com/photo-1529107386315-e1a2ed48a620?auto=format&fit=crop&w=1800&q=85",
        "title": "Selamat Datang di Portal Resmi DPRK Aceh Jaya",
        "subtitle": "Mewujudkan Transparansi dan Akuntabilitas Pemerintahan Daerah",
    },
    {
        "image": "https://images.unsplash.com/photo-1556761175-b413da4baf72?auto=format&fit=crop&w=1800&q=85",
        "title": "Suara Masyarakat, Prioritas Kami",
        "subtitle": "Sampaikan Aspirasi Anda Melalui Portal Informasi Publik DPRK Aceh Jaya",
    },
    {
        "image": "https://images.unsplash.com/photo-1589578527966-fdac0f44566c?auto=format&fit=crop&w=1800&q=85",
        "title": "Membangun Aceh Jaya yang Lebih Baik",
        "subtitle": "Bersama DPRK Aceh Jaya Mewujudkan Pembangunan Berkelanjutan",
    },
]

WARTA_DPRK = [
    {
        "title": "DPRK Aceh Jaya Gelar Rapat Paripurna Pandangan Fraksi terhadap Pertanggungjawaban APBK 2025",
        "date": "Jumat, 14 Agustus 2026",
        "desc": "Dewan Perwakilan Rakyat Kabupaten (DPRK) Aceh Jaya menggelar Rapat Paripurna Ke-IX Masa Persidangan II Tahun Sidang membahas pandangan fraksi terhadap pertanggungjawaban APBK.",
        "image": "https://images.unsplash.com/photo-1556761175-b413da4baf72?auto=format&fit=crop&w=800&q=80",
        "kategori": "Paripurna",
    },
    {
        "title": "DPRK Aceh Jaya Gelar Rapat Paripurna ke-VIII Masa Persidangan II",
        "date": "Kamis, 30 Juli 2026",
        "desc": "Rapat Paripurna ke-VIII Masa Persidangan II membahas pertanggungjawaban APBK 2025 dan Perubahan Anggaran Kas Daerah.",
        "image": "https://images.unsplash.com/photo-1529107386315-e1a2ed48a620?auto=format&fit=crop&w=800&q=80",
        "kategori": "Paripurna",
    },
    {
        "title": "Ketua DPRK Aceh Jaya Dukung Pelestarian Mangrove",
        "date": "Minggu, 26 Juli 2026",
        "desc": "Ketua DPRK Aceh Jaya Musliadi Z, S.E menyampaikan dukungan terhadap kegiatan Penanaman Mangrove Serentak dalam rangka memperingati Hari Mangrove.",
        "image": "https://images.unsplash.com/photo-1589578527966-fdac0f44566c?auto=format&fit=crop&w=800&q=80",
        "kategori": "Lingkungan",
    },
    {
        "title": "Ketua DPRK Apresiasi Kejari Pulihkan Keuangan Negara Rp2,05 Miliar",
        "date": "Rabu, 22 Juli 2026",
        "desc": "Ketua DPRK Aceh Jaya menghadiri kegiatan Press Release Capaian Pemulihan Keuangan Negara yang diselenggarakan oleh Kejaksaan Negeri Aceh Jaya.",
        "image": "https://images.unsplash.com/photo-1577962917302-cd874c4e31d2?auto=format&fit=crop&w=800&q=80",
        "kategori": "Hukum",
    },
]

KESEKRETARIATAN = [
    {"title": "Apel Pagi Rutin, ASN DPRK Aceh Jaya Diingatkan Disiplin dan Komitmen Kerja", "date": "Senin, 06 April 2026"},
    {"title": "Sekretaris DPRK Ikuti Vidcon Entry Meeting Pemeriksaan Laporan Keuangan 2025", "date": "Kamis, 02 April 2026"},
    {"title": "Rapat Koordinasi Persiapan Rapat Paripurna DPRK Aceh Jaya", "date": "Rabu, 01 April 2026"},
]

AGENDA_TERKINI = [
    {"hari": "09", "bulan_tahun": "09 2026", "tanggal_full": "Rabu, 09 September 2026", "judul": "Rapat Pleno DPRK Aceh Jaya - 09 September 2026", "desc": "Rapat Pleno DPRK Aceh Jaya terhadap Rancangan Perubahan KUA-PPAS APBK Aceh Jaya Tahun Anggaran."},
    {"hari": "07", "bulan_tahun": "09 2026", "tanggal_full": "Senin, 07 September 2026", "judul": "Rapat Komisi III DPRK Aceh Jaya - 07 September 2026", "desc": "Rapat Dengar Pendapat Komisi III terkait Realisasi Program dan Kegiatan Pembangunan Jalan dan Jembatan pada Dinas PUPR."},
    {"hari": "01", "bulan_tahun": "09 2026", "tanggal_full": "Selasa, 01 September 2026", "judul": "Rapat Badan Musyawarah DPRK Aceh Jaya - 01 September 2026", "desc": "Rapat Badan Musyawarah tentang Penetapan Jadwal Rapat Paripurna DPRK Aceh Jaya."},
]

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

PEJABAT_SEKRETARIAT = [
    ("ABU BAKAR, S.Pd.I., M.H", "Sekretaris DPRK Aceh Jaya"),
    ("IRMA HANUM, SH", "Staf Ahli Bidang Pemerintahan, Hukum dan Politik"),
    ("HIDAYAT, SE., M.Si", "Kepala Bagian Umum dan Keuangan"),
    ("YUSWARDI, S.Kom", "Kepala Bagian Persidangan dan Perundang-Undangan"),
    ("NELLI FAUZIANA, SH., MH", "Kepala Bagian Fasilitasi Penganggaran dan Pengawasan"),
    ("IHSAN SALIM, S.A.P", "Kepala Sub Bagian Tata Usaha dan Kepegawaian"),
]

JDIH_DATA = [
    ["1", "Qanun No. 5/2025", "Ketertiban Umum dan Ketenteraman Masyarakat", "Berlaku"],
    ["2", "Perbup No. 12/2026", "Penjabaran APBK Aceh Jaya 2026", "Berlaku"],
    ["3", "Qanun No. 2/2024", "Perlindungan Korban Bencana Alam", "Berlaku"],
    ["4", "Qanun No. 3/2024", "Pengelolaan Sampah dan Kebersihan", "Berlaku"],
    ["5", "Perbup No. 08/2025", "Standar Operasional Prosedur Pelayanan", "Berlaku"],
]

STATS_DATA = pd.DataFrame({
    "Bulan": ["Jan", "Feb", "Mar", "Apr", "Mei", "Jun", "Jul", "Agu", "Sep"],
    "Rapat": [8, 10, 7, 12, 9, 11, 8, 10, 9],
    "Pengaduan": [12, 15, 10, 18, 14, 20, 16, 22, 19],
})

ANGGARAN_DATA = pd.DataFrame({
    "Kategori": ["Infrastruktur", "Pendidikan", "Kesehatan", "Sosial", "Pertanian"],
    "Anggaran": [45, 25, 15, 8, 7],
})

# =========================================================
# CSS STYLE - FULLY FIXED
# =========================================================
st.markdown(
    """
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=Plus+Jakarta+Sans:wght@500;600;700;800&display=swap');

:root {
    --primary: #0d5e3a;
    --primary-dark: #083d26;
    --primary-2: #14734a;
    --gold: #c9a227;
    --gold-light: #e6c458;
    --bg: #f4f6f5;
    --white: #ffffff;
    --border: #e0e6e2;
    --text: #2c3835;
    --muted: #6b7a75;
}

* { box-sizing: border-box; font-family: 'Inter', sans-serif; }
html, body, [class*="css"] { font-family: 'Inter', sans-serif; }
#MainMenu, footer, header { visibility: hidden; height: 0; }
.stApp { background: var(--bg); color: var(--text); }
.block-container { max-width: 100%; padding: 0 !important; }
section[data-testid="stSidebar"] { display: none; }

/* ============================================
   TOP BAR
   ============================================ */
.topbar { 
    background: #083d26; 
    color: rgba(255,255,255,.85); 
    padding: 8px 5%; 
    display: flex; 
    align-items: center; 
    justify-content: space-between; 
    font-size: 12px; 
}
.topbar-left, .topbar-right { display: flex; gap: 18px; align-items: center; }
.topbar a { color: rgba(255,255,255,.85); text-decoration: none; }
.topbar a:hover { color: #e6c458; }
.topbar-clock { color: #e6c458; font-weight: 600; }

/* ============================================
   HEADER / BRAND
   ============================================ */
.header-wrap {
    background: #ffffff;
    padding: 18px 5%;
    border-bottom: 1px solid #e0e6e2;
}
.header-inner {
    display: flex;
    align-items: center;
    justify-content: space-between;
    gap: 24px;
    max-width: 1400px;
    margin: 0 auto;
}
.header-brand { display: flex; align-items: center; gap: 16px; }
.header-logo {
    width: 72px; height: 72px;
    border-radius: 8px;
    background: #fff;
    display: flex; align-items: center; justify-content: center;
    overflow: hidden;
}
.header-logo img { width: 100%; height: 100%; object-fit: contain; }
.header-text-title {
    color: #083d26;
    font-family: 'Plus Jakarta Sans', sans-serif;
    font-size: 20px;
    line-height: 1.15;
    font-weight: 800;
    text-transform: uppercase;
    letter-spacing: 0.3px;
}
.header-text-sub {
    color: #6b7a75;
    font-size: 11.5px;
    margin-top: 4px;
    letter-spacing: 0.5px;
}
.header-social { display: flex; gap: 8px; }
.header-social-item {
    width: 34px; height: 34px;
    border-radius: 50%;
    background: #0d5e3a;
    color: #ffffff;
    display: flex; align-items: center; justify-content: center;
    font-size: 13px;
    text-decoration: none;
    transition: all 0.25s ease;
}
.header-social-item:hover { background: #c9a227; transform: translateY(-2px); }

/* ============================================
   NAVBAR - FIXED (TEKS PUTIH JELAS)
   ============================================ */
.navbar {
    background: linear-gradient(180deg, #0d5e3a 0%, #0a4a2e 100%) !important;
    padding: 0 5%;
    border-bottom: 3px solid #c9a227;
    position: sticky;
    top: 0;
    z-index: 999;
    box-shadow: 0 4px 16px rgba(0,0,0,0.15);
}

/* FORCE semua button Streamlit di dalam navbar */
div[data-testid="stHorizontalBlock"] .stButton > button,
.navbar .stButton > button,
.navbar button {
    background: transparent !important;
    background-color: transparent !important;
    background-image: none !important;
    border: none !important;
    color: #ffffff !important;
    font-family: 'Plus Jakarta Sans', sans-serif !important;
    font-size: 13px !important;
    font-weight: 700 !important;
    padding: 18px 20px !important;
    border-radius: 0 !important;
    min-height: 56px !important;
    width: 100% !important;
    transition: all 0.25s ease !important;
    letter-spacing: 0.8px !important;
    text-transform: uppercase !important;
    position: relative !important;
    box-shadow: none !important;
    text-shadow: 0 1px 2px rgba(0,0,0,0.4) !important;
}

/* Force semua child text jadi putih */
.navbar .stButton > button p,
.navbar .stButton > button span,
.navbar .stButton > button div,
.navbar .stButton > button *,
.navbar button p,
.navbar button span,
.navbar button * {
    color: #ffffff !important;
    font-weight: 700 !important;
    opacity: 1 !important;
    fill: #ffffff !important;
}

/* Hover state */
.navbar .stButton > button:hover,
.navbar .stButton > button:focus,
.navbar .stButton > button:active {
    background: rgba(255,255,255,0.12) !important;
    background-color: rgba(255,255,255,0.12) !important;
    color: #ffffff !important;
    border: none !important;
}
.navbar .stButton > button:hover *,
.navbar .stButton > button:focus * {
    color: #ffffff !important;
}

/* Underline gold saat hover */
.navbar .stButton > button::after {
    content: '';
    position: absolute;
    bottom: 0; left: 50%;
    transform: translateX(-50%);
    width: 0;
    height: 3px;
    background: #e6c458;
    transition: width 0.3s ease;
}
.navbar .stButton > button:hover::after { width: 70%; }

/* Active nav */
.navbar .nav-active .stButton > button {
    background: rgba(201, 162, 39, 0.25) !important;
}
.navbar .nav-active .stButton > button,
.navbar .nav-active .stButton > button * {
    color: #e6c458 !important;
}
.navbar .nav-active .stButton > button::after { 
    width: 70%; 
    background: #e6c458; 
}

/* ============================================
   RUNNING TEXT
   ============================================ */
.running-text-bar {
    background: #ffffff;
    border-bottom: 1px solid #e0e6e2;
    padding: 10px 5%;
    display: flex;
    align-items: center;
    gap: 14px;
    overflow: hidden;
}
.running-label {
    background: #c9a227;
    color: #ffffff;
    padding: 5px 14px;
    border-radius: 3px;
    font-size: 11px;
    font-weight: 800;
    text-transform: uppercase;
    letter-spacing: 0.5px;
    flex-shrink: 0;
}
.running-scroll-wrap {
    flex: 1;
    overflow: hidden;
    white-space: nowrap;
    position: relative;
}
.running-scroll {
    display: inline-block;
    padding-left: 100%;
    animation: marquee 40s linear infinite;
    font-size: 13px;
    font-weight: 500;
    color: #2c3835;
}
@keyframes marquee {
    0% { transform: translate(0, 0); }
    100% { transform: translate(-100%, 0); }
}

/* ============================================
   HERO SLIDER
   ============================================ */
.hero-slider {
    position: relative;
    height: 480px;
    overflow: hidden;
    background: #000;
}
.hero-slide {
    position: absolute;
    top: 0; left: 0;
    width: 100%; height: 100%;
    display: flex;
    align-items: center;
    justify-content: center;
    text-align: center;
    color: #ffffff;
}
.hero-slide-content {
    position: relative;
    z-index: 3;
    max-width: 900px;
    padding: 0 5%;
}
.hero-slide-title {
    font-family: 'Plus Jakarta Sans', sans-serif;
    font-size: clamp(26px, 4vw, 48px);
    font-weight: 800;
    line-height: 1.15;
    margin-bottom: 16px;
    color: #ffffff !important;
    text-shadow: 0 4px 24px rgba(0,0,0,0.8);
}
.hero-slide-sub {
    font-size: clamp(13px, 1.4vw, 17px);
    color: rgba(255,255,255,0.95) !important;
    line-height: 1.7;
    max-width: 700px;
    margin: 0 auto 28px;
    text-shadow: 0 2px 12px rgba(0,0,0,0.7);
}
.hero-slide-btn {
    display: inline-block;
    padding: 13px 32px;
    background: #c9a227;
    color: #ffffff !important;
    text-decoration: none;
    font-weight: 700;
    font-size: 13px;
    border-radius: 4px;
    letter-spacing: 0.8px;
    text-transform: uppercase;
    transition: all 0.3s ease;
    box-shadow: 0 6px 20px rgba(201,162,39,0.4);
}
.hero-slide-btn:hover {
    background: #e6c458;
    transform: translateY(-3px);
    box-shadow: 0 10px 30px rgba(201,162,39,0.6);
}
.hero-dots {
    position: absolute;
    bottom: 24px;
    left: 50%;
    transform: translateX(-50%);
    display: flex;
    gap: 10px;
    z-index: 5;
}
.hero-dot {
    width: 12px; height: 12px;
    border-radius: 50%;
    background: rgba(255,255,255,0.5);
    border: 2px solid transparent;
}
.hero-dot.active {
    background: #c9a227;
    border-color: #ffffff;
    transform: scale(1.3);
}

/* ============================================
   INFO STATS - FIXED (BACKGROUND HIJAU MUNCUL)
   ============================================ */
.info-stats {
    background: linear-gradient(135deg, #0d5e3a 0%, #14734a 100%) !important;
    padding: 32px 5% !important;
    border-top: 3px solid #c9a227;
    border-bottom: 3px solid #c9a227;
}
.info-stats-inner {
    max-width: 1400px;
    margin: 0 auto;
}
.info-stat-item {
    text-align: center;
    padding: 12px 15px;
    position: relative;
}
.info-stat-item.has-divider::after {
    content: '';
    position: absolute;
    right: 0; top: 15px; bottom: 15px;
    width: 1px;
    background: rgba(255,255,255,0.2);
}
.info-stat-num {
    color: #e6c458 !important;
    font-size: 36px !important;
    font-weight: 800 !important;
    font-family: 'Plus Jakarta Sans', sans-serif !important;
    line-height: 1 !important;
    text-shadow: 0 2px 8px rgba(0,0,0,0.3) !important;
    display: block !important;
}
.info-stat-label {
    color: #ffffff !important;
    font-size: 12px !important;
    margin-top: 8px !important;
    text-transform: uppercase !important;
    letter-spacing: 1px !important;
    font-weight: 700 !important;
    text-shadow: 0 1px 3px rgba(0,0,0,0.3) !important;
    display: block !important;
}

/* ============================================
   SECTION HEADER
   ============================================ */
.section-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 22px;
    padding-bottom: 12px;
    border-bottom: 2px solid #e0e6e2;
    position: relative;
}
.section-header::after {
    content: '';
    position: absolute;
    bottom: -2px; left: 0;
    width: 80px;
    height: 2px;
    background: #0d5e3a;
}
.section-header-title {
    font-family: 'Plus Jakarta Sans', sans-serif;
    font-size: 20px;
    font-weight: 800;
    color: #083d26 !important;
    text-transform: uppercase;
    letter-spacing: 0.5px;
    margin: 0;
}
.section-header-title::before {
    content: '';
    display: inline-block;
    width: 4px;
    height: 18px;
    background: #c9a227;
    margin-right: 10px;
    vertical-align: middle;
    border-radius: 2px;
}
.section-header-link {
    color: #0d5e3a;
    font-size: 12px;
    font-weight: 700;
    text-decoration: none;
}
.section-header-link:hover { color: #c9a227; }

/* ============================================
   WARTA CARD
   ============================================ */
.warta-card {
    background: #ffffff;
    border: 1px solid #e0e6e2;
    border-radius: 6px;
    overflow: hidden;
    margin-bottom: 20px;
    transition: all 0.3s ease;
    display: flex;
    gap: 0;
}
.warta-card:hover {
    box-shadow: 0 10px 30px rgba(13,94,58,0.12);
    transform: translateY(-3px);
    border-color: rgba(201,162,39,0.4);
}
.warta-card-img {
    width: 260px;
    min-height: 180px;
    object-fit: cover;
    flex-shrink: 0;
    transition: transform 0.5s ease;
}
.warta-card:hover .warta-card-img { transform: scale(1.05); }
.warta-card-img-wrap {
    width: 260px;
    overflow: hidden;
    flex-shrink: 0;
    position: relative;
}
.warta-card-cat {
    position: absolute;
    top: 12px; left: 12px;
    background: #c9a227;
    color: #ffffff;
    padding: 4px 10px;
    border-radius: 3px;
    font-size: 10px;
    font-weight: 700;
    text-transform: uppercase;
}
.warta-card-body {
    padding: 20px 24px;
    flex: 1;
    display: flex;
    flex-direction: column;
}
.warta-card-date {
    color: #6b7a75;
    font-size: 11px;
    font-weight: 600;
    margin-bottom: 8px;
}
.warta-card-title {
    color: #083d26 !important;
    font-family: 'Plus Jakarta Sans', sans-serif;
    font-size: 17px;
    line-height: 1.4;
    font-weight: 700;
    margin: 0 0 10px;
}
.warta-card:hover .warta-card-title { color: #14734a !important; }
.warta-card-desc {
    color: #6b7a75;
    font-size: 13px;
    line-height: 1.65;
    margin: 0;
    flex: 1;
}
.warta-card-readmore {
    color: #0d5e3a;
    font-size: 12px;
    font-weight: 700;
    text-decoration: none;
    margin-top: 12px;
    display: inline-block;
}
.warta-card-readmore:hover { color: #c9a227; }

/* ============================================
   SIDEBAR WIDGET
   ============================================ */
.sidebar-widget {
    background: #ffffff;
    border: 1px solid #e0e6e2;
    border-radius: 6px;
    margin-bottom: 24px;
    overflow: hidden;
}
.sidebar-widget-head {
    background: #0d5e3a;
    color: #ffffff !important;
    padding: 14px 18px;
    font-family: 'Plus Jakarta Sans', sans-serif;
    font-size: 13px;
    font-weight: 800;
    text-transform: uppercase;
    letter-spacing: 0.8px;
    border-bottom: 3px solid #c9a227;
}
.sidebar-widget-body {
    padding: 0;
    background: #ffffff;
}

/* Kesekretariatan item */
.kesekret-item {
    padding: 14px 18px;
    border-bottom: 1px solid #e0e6e2;
    display: flex;
    gap: 12px;
    transition: background 0.2s ease;
}
.kesekret-item:last-child { border-bottom: none; }
.kesekret-item:hover { background: #f9faf9; }
.kesekret-icon {
    width: 42px;
    height: 42px;
    border-radius: 50%;
    background: linear-gradient(135deg, #0d5e3a, #14734a);
    color: #ffffff;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 16px;
    flex-shrink: 0;
}
.kesekret-content { flex: 1; }
.kesekret-title {
    color: #083d26 !important;
    font-size: 12.5px;
    font-weight: 700;
    line-height: 1.4;
    margin: 0 0 4px;
}
.kesekret-item:hover .kesekret-title { color: #14734a !important; }
.kesekret-date {
    color: #6b7a75;
    font-size: 11px;
}

/* Agenda item dengan kotak tanggal */
.agenda-card {
    display: flex;
    padding: 16px 18px;
    border-bottom: 1px solid #e0e6e2;
    gap: 14px;
    transition: background 0.2s ease;
}
.agenda-card:last-child { border-bottom: none; }
.agenda-card:hover { background: #f9faf9; }
.agenda-date-box {
    width: 62px;
    height: 68px;
    background: linear-gradient(135deg, #0d5e3a, #14734a);
    color: #ffffff !important;
    border-radius: 6px;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    flex-shrink: 0;
    box-shadow: 0 4px 12px rgba(13,94,58,0.25);
    position: relative;
}
.agenda-date-box::before {
    content: '';
    position: absolute;
    top: 0; left: 0; right: 0;
    height: 3px;
    background: #c9a227;
    border-radius: 6px 6px 0 0;
}
.agenda-day {
    font-size: 24px;
    font-weight: 800;
    line-height: 1;
    color: #ffffff !important;
    font-family: 'Plus Jakarta Sans', sans-serif;
}
.agenda-month-year {
    font-size: 9px;
    font-weight: 700;
    letter-spacing: 0.5px;
    color: #ffffff !important;
    opacity: 0.95;
    margin-top: 4px;
}
.agenda-content { flex: 1; }
.agenda-title-link {
    color: #083d26 !important;
    font-size: 12.5px;
    font-weight: 700;
    line-height: 1.4;
    margin: 0 0 6px;
}
.agenda-card:hover .agenda-title-link { color: #14734a !important; }
.agenda-desc-short {
    color: #6b7a75;
    font-size: 11px;
    line-height: 1.5;
    margin: 0 0 6px;
}
.agenda-full-date {
    color: #c9a227;
    font-size: 10.5px;
    font-weight: 700;
}

/* ============================================
   LAYANAN ICON GRID
   ============================================ */
.layanan-icon {
    background: #ffffff;
    border: 1px solid #e0e6e2;
    border-radius: 8px;
    padding: 22px 16px;
    text-align: center;
    transition: all 0.3s ease;
    height: 100%;
    text-decoration: none;
    display: block;
    color: inherit;
}
.layanan-icon:hover {
    transform: translateY(-5px);
    box-shadow: 0 12px 30px rgba(13,94,58,0.12);
    border-color: #c9a227;
}
.layanan-icon-circle {
    width: 60px;
    height: 60px;
    margin: 0 auto 12px;
    border-radius: 50%;
    background: linear-gradient(135deg, #e8f5ef, #d4ece1);
    color: #0d5e3a;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 26px;
    transition: all 0.4s ease;
}
.layanan-icon:hover .layanan-icon-circle {
    background: linear-gradient(135deg, #c9a227, #e6c458);
    color: #ffffff;
    transform: scale(1.1) rotate(-8deg);
}
.layanan-icon-title {
    color: #083d26 !important;
    font-size: 13px;
    font-weight: 800;
    margin-bottom: 6px;
    font-family: 'Plus Jakarta Sans', sans-serif;
}
.layanan-icon-desc {
    color: #6b7a75;
    font-size: 11px;
    line-height: 1.5;
}

/* ============================================
   FOOTER
   ============================================ */
.footer-main {
    background: #0a2a1b;
    color: rgba(255,255,255,0.72);
    padding: 50px 5% 0;
    margin-top: 60px;
    border-top: 4px solid #c9a227;
}
.footer-inner {
    max-width: 1400px;
    margin: 0 auto;
}
.footer-grid {
    display: grid;
    grid-template-columns: 1.6fr 1fr 1fr 1fr;
    gap: 40px;
    padding-bottom: 40px;
}
.footer-col h4 {
    color: #ffffff !important;
    font-size: 13px;
    font-weight: 800;
    margin: 0 0 18px;
    text-transform: uppercase;
    letter-spacing: 0.5px;
    position: relative;
    padding-bottom: 10px;
}
.footer-col h4::after {
    content: '';
    position: absolute;
    bottom: 0; left: 0;
    width: 30px;
    height: 2px;
    background: #c9a227;
}
.footer-col p {
    color: rgba(255,255,255,0.6);
    font-size: 12.5px;
    line-height: 1.85;
    margin: 0 0 8px;
}
.footer-col a {
    display: block;
    color: rgba(255,255,255,0.6);
    font-size: 12.5px;
    line-height: 2.1;
    text-decoration: none;
    transition: all 0.2s ease;
}
.footer-col a:hover { color: #e6c458; padding-left: 5px; }
.footer-brand-block {
    display: flex;
    align-items: center;
    gap: 14px;
    margin-bottom: 18px;
}
.footer-logo-box {
    width: 56px;
    height: 56px;
    background: #ffffff;
    border-radius: 6px;
    display: flex;
    align-items: center;
    justify-content: center;
    overflow: hidden;
}
.footer-logo-box img { width: 100%; height: 100%; object-fit: contain; }
.footer-brand-title {
    color: #ffffff !important;
    font-family: 'Plus Jakarta Sans', sans-serif;
    font-size: 15px;
    font-weight: 800;
    text-transform: uppercase;
}
.footer-brand-sub {
    color: rgba(255,255,255,0.5);
    font-size: 10px;
    letter-spacing: 0.5px;
    margin-top: 3px;
}
.footer-social {
    display: flex;
    gap: 8px;
    margin-top: 18px;
}
.footer-social-item {
    width: 36px;
    height: 36px;
    background: rgba(255,255,255,0.08);
    border: 1px solid rgba(255,255,255,0.1);
    border-radius: 6px;
    color: #ffffff;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 14px;
    text-decoration: none;
    transition: all 0.25s ease;
}
.footer-social-item:hover {
    background: #c9a227;
    border-color: #c9a227;
    transform: translateY(-3px);
}
.footer-bottom {
    border-top: 1px solid rgba(255,255,255,0.08);
    padding: 20px 0;
    display: flex;
    justify-content: space-between;
    align-items: center;
    flex-wrap: wrap;
    gap: 10px;
    font-size: 11.5px;
    color: rgba(255,255,255,0.45);
}

/* ============================================
   FORM & INPUT
   ============================================ */
.stButton > button[kind="primary"] {
    background: #0d5e3a !important;
    border: none !important;
    color: #ffffff !important;
    border-radius: 6px !important;
    font-weight: 700 !important;
}
.stButton > button[kind="primary"]:hover {
    background: #14734a !important;
}
div[data-testid="stForm"] {
    background: #ffffff;
    border: 1px solid #e0e6e2;
    border-radius: 8px;
    padding: 24px !important;
}
.stTextInput input, .stTextArea textarea, div[data-baseweb="select"] > div {
    border-radius: 6px !important;
    border-color: #e0e6e2 !important;
}

/* Page container */
.page-container {
    width: 92%;
    max-width: 1400px;
    margin: 0 auto;
    padding: 30px 0;
}

/* Tabs */
.stTabs [data-baseweb="tab-list"] {
    gap: 4px;
    background: transparent;
    border-bottom: 2px solid #e0e6e2;
}
.stTabs [data-baseweb="tab"] {
    background: transparent;
    border-radius: 6px 6px 0 0;
    padding: 12px 24px;
    color: #6b7a75;
    font-weight: 700;
    font-family: 'Plus Jakarta Sans', sans-serif;
    font-size: 13px;
}
.stTabs [aria-selected="true"] {
    background: #f0f6f2 !important;
    color: #0d5e3a !important;
    border-bottom: 3px solid #0d5e3a;
}

/* Button default (bukan primary/navbar) */
.stButton > button {
    background: #0d5e3a !important;
    color: #ffffff !important;
    border: none !important;
    border-radius: 6px !important;
    font-weight: 700 !important;
}
.stButton > button:hover {
    background: #14734a !important;
}

/* Responsive */
@media (max-width: 900px) {
    .footer-grid { grid-template-columns: 1fr 1fr; gap: 28px; }
    .footer-bottom { flex-direction: column; text-align: center; }
    .warta-card { flex-direction: column; }
    .warta-card-img-wrap, .warta-card-img { width: 100%; height: 200px; }
    .hero-slider { height: 380px; }
}
</style>
""",
    unsafe_allow_html=True,
)

# =========================================================
# URL ROUTING
# =========================================================
PAGE_URLS = {v: k.lower().replace(" & ", "-").replace(" ", "-") for k, v in PAGES.items()}
URL_TO_PAGE = {v: k for k, v in PAGE_URLS.items()}

query_params = st.query_params
if "page" in query_params:
    target = query_params["page"]
    if target in URL_TO_PAGE:
        st.session_state.page = URL_TO_PAGE[target]
        del st.query_params["page"]
        st.rerun()

# =========================================================
# TOP BAR
# =========================================================
now = datetime.now()
st.markdown(
    f"""
<div class="topbar">
    <div class="topbar-left">
        <span>📞 (0655) 12345</span>
        <span>✉️ sekretariat@dprk.acehjaya.go.id</span>
    </div>
    <div class="topbar-right">
        <span class="topbar-clock">🕐 {now.strftime('%A, %d %B %Y | %H:%M:%S WIB')}</span>
        <a href="?page=kontak">Hubungi Kami</a>
        <span>|</span>
        <a href="?page=jdih">PPID</a>
    </div>
</div>
""",
    unsafe_allow_html=True,
)

# =========================================================
# HEADER BRAND
# =========================================================
st.markdown(
    f"""
<div class="header-wrap">
    <div class="header-inner">
        <div class="header-brand">
            <div class="header-logo">
                <img src="{LOGO_URL}" alt="Logo DPRK Aceh Jaya"
                     onerror="this.onerror=null;this.src='data:image/svg+xml,<svg xmlns=%22http://www.w3.org/2000/svg%22 viewBox=%220 0 100 100%22><text y=%22.9em%22 font-size=%2290%22>🏛️</text></svg>'">
            </div>
            <div>
                <div class="header-text-title">Sekretariat DPRK<br>Kabupaten Aceh Jaya</div>
                <div class="header-text-sub">PORTAL RESMI INFORMASI & ASPIRASI MASYARAKAT</div>
            </div>
        </div>
        <div class="header-social">
            <a href="#" class="header-social-item">f</a>
            <a href="#" class="header-social-item">𝕏</a>
            <a href="#" class="header-social-item">▶</a>
            <a href="#" class="header-social-item">◎</a>
            <a href="#" class="header-social-item">in</a>
        </div>
    </div>
</div>
""",
    unsafe_allow_html=True,
)

# =========================================================
# NAVBAR
# =========================================================
st.markdown('<div class="navbar">', unsafe_allow_html=True)
nav_cols = st.columns(7)
nav_keys = list(PAGES.keys())

for i, key in enumerate(nav_keys):
    with nav_cols[i]:
        active = "nav-active" if st.session_state.page == PAGES[key] else ""
        st.markdown(f'<div class="{active}">', unsafe_allow_html=True)
        if st.button(PAGES[key], key=f"nav_{key}", use_container_width=True):
            st.session_state.page = PAGES[key]
            st.rerun()
        st.markdown("</div>", unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)

# =========================================================
# RUNNING TEXT
# =========================================================
st.markdown(
    """
<div class="running-text-bar">
    <span class="running-label">📢 INFO TERKINI</span>
    <div class="running-scroll-wrap">
        <div class="running-scroll">
            Selamat Datang di Portal Resmi Sekretariat DPRK Kabupaten Aceh Jaya &nbsp;&nbsp;•&nbsp;&nbsp;
            Rapat Paripurna Pembahasan KUA-PPAS 2027 akan dilaksanakan pada 18 September 2026 &nbsp;&nbsp;•&nbsp;&nbsp;
            Layanan Pengaduan Masyarakat dapat diakses melalui menu Layanan &nbsp;&nbsp;•&nbsp;&nbsp;
            DPRK Aceh Jaya Raih Penghargaan Keterbukaan Informasi Publik 2026 &nbsp;&nbsp;•&nbsp;&nbsp;
            Mari wujudkan transparansi dan akuntabilitas pemerintahan daerah bersama DPRK Aceh Jaya.
        </div>
    </div>
</div>
""",
    unsafe_allow_html=True,
)

# =========================================================
# HALAMAN: BERANDA
# =========================================================
if st.session_state.page == "Beranda":
    # HERO SLIDER
    slide = HERO_SLIDES[st.session_state.slide_index % len(HERO_SLIDES)]
    st.markdown(
        f"""
    <div class="hero-slider">
        <div class="hero-slide" style="background: linear-gradient(135deg, rgba(8,61,38,0.85) 0%, rgba(13,94,58,0.65) 50%, rgba(8,61,38,0.85) 100%), url('{slide['image']}') center/cover no-repeat;">
            <div class="hero-slide-content">
                <div class="hero-slide-title">{slide['title']}</div>
                <div class="hero-slide-sub">{slide['subtitle']}</div>
                <a href="?page=layanan" class="hero-slide-btn">Sampaikan Aspirasi →</a>
            </div>
        </div>
        <div class="hero-dots">
            <div class="hero-dot {'active' if st.session_state.slide_index % len(HERO_SLIDES) == 0 else ''}"></div>
            <div class="hero-dot {'active' if st.session_state.slide_index % len(HERO_SLIDES) == 1 else ''}"></div>
            <div class="hero-dot {'active' if st.session_state.slide_index % len(HERO_SLIDES) == 2 else ''}"></div>
        </div>
    </div>
    """,
        unsafe_allow_html=True,
    )

    # Navigasi slider
    slide_cols = st.columns([1, 1, 1, 1, 1])
    with slide_cols[1]:
        if st.button("◀ Sebelumnya", key="slide_prev", use_container_width=True):
            st.session_state.slide_index = (st.session_state.slide_index - 1) % len(HERO_SLIDES)
            st.rerun()
    with slide_cols[3]:
        if st.button("Berikutnya ▶", key="slide_next", use_container_width=True):
            st.session_state.slide_index = (st.session_state.slide_index + 1) % len(HERO_SLIDES)
            st.rerun()

    # INFO STATS
    st.markdown('<div class="info-stats"><div class="info-stats-inner">', unsafe_allow_html=True)
    stat_cols = st.columns(4)
    stats = [
        ("20", "Anggota DPRK"),
        ("4", "Komisi DPRK"),
        ("120+", "Produk Hukum"),
        (f"{st.session_state.visitor_count:,}", "Total Kunjungan"),
    ]
    for i, (num, label) in enumerate(stats):
        with stat_cols[i]:
            divider = "has-divider" if i < len(stats) - 1 else ""
            st.markdown(
                f"""
            <div class="info-stat-item {divider}">
                <div class="info-stat-num">{num}</div>
                <div class="info-stat-label">{label}</div>
            </div>
            """,
                unsafe_allow_html=True,
            )
    st.markdown("</div></div>", unsafe_allow_html=True)

    # LAYANAN ICON GRID
    st.markdown('<div class="page-container">', unsafe_allow_html=True)
    st.markdown(
        """
    <div class="section-header">
        <h2 class="section-header-title">Layanan Publik</h2>
        <a href="?page=layanan" class="section-header-link">Lihat Semua →</a>
    </div>
    """,
        unsafe_allow_html=True,
    )

    layanan_items = [
        ("📢", "Pengaduan Masyarakat", "Sampaikan aspirasi & laporan", "layanan"),
        ("📜", "JDIH", "Produk hukum daerah", "jdih"),
        ("📅", "Agenda DPRK", "Jadwal rapat & sidang", "berita"),
        ("📊", "Transparansi", "Informasi publik", "jdih"),
        ("📂", "Dokumen Publik", "Akses dokumen resmi", "jdih"),
        ("🔗", "E-LHKPN", "Pelaporan harta kekayaan", "https://elhpkpn.kpk.go.id/"),
    ]
    cols = st.columns(6)
    for i, (icon, title, desc, target) in enumerate(layanan_items):
        with cols[i]:
            is_ext = target.startswith("http")
            href = target if is_ext else f"?page={target}"
            tgt = 'target="_blank" rel="noopener"' if is_ext else ""
            st.markdown(
                f"""
            <a href="{href}" {tgt} class="layanan-icon">
                <div class="layanan-icon-circle">{icon}</div>
                <div class="layanan-icon-title">{title}</div>
                <div class="layanan-icon-desc">{desc}</div>
            </a>
            """,
                unsafe_allow_html=True,
            )

    st.markdown("</div>", unsafe_allow_html=True)

    # KONTEN 2 KOLOM: WARTA + SIDEBAR
    st.markdown('<div class="page-container">', unsafe_allow_html=True)
    main_col, side_col = st.columns([2, 1])

    with main_col:
        st.markdown(
            """
        <div class="section-header">
            <h2 class="section-header-title">Warta DPRK</h2>
            <a href="?page=berita" class="section-header-link">Lihat Semua →</a>
        </div>
        """,
            unsafe_allow_html=True,
        )
        for item in WARTA_DPRK[:4]:
            st.markdown(
                f"""
            <div class="warta-card">
                <div class="warta-card-img-wrap">
                    <span class="warta-card-cat">{item['kategori']}</span>
                    <img class="warta-card-img" src="{item['image']}">
                </div>
                <div class="warta-card-body">
                    <div class="warta-card-date">📅 {item['date']}</div>
                    <h3 class="warta-card-title">{item['title']}</h3>
                    <p class="warta-card-desc">{item['desc'][:150]}...</p>
                    <a href="?page=berita" class="warta-card-readmore">Baca Selengkapnya →</a>
                </div>
            </div>
            """,
                unsafe_allow_html=True,
            )

    with side_col:
        # Widget Kesekretariatan
        st.markdown(
            """
        <div class="sidebar-widget">
            <div class="sidebar-widget-head">Kesekretariatan</div>
            <div class="sidebar-widget-body">
        """,
            unsafe_allow_html=True,
        )
        for item in KESEKRETARIATAN:
            st.markdown(
                f"""
            <div class="kesekret-item">
                <div class="kesekret-icon">📋</div>
                <div class="kesekret-content">
                    <p class="kesekret-title">{item['title']}</p>
                    <div class="kesekret-date">📅 {item['date']}</div>
                </div>
            </div>
            """,
                unsafe_allow_html=True,
            )
        st.markdown("</div></div>", unsafe_allow_html=True)

        # Widget Agenda
        st.markdown(
            """
        <div class="sidebar-widget">
            <div class="sidebar-widget-head">Agenda Terkini</div>
            <div class="sidebar-widget-body">
        """,
            unsafe_allow_html=True,
        )
        for item in AGENDA_TERKINI:
            st.markdown(
                f"""
            <div class="agenda-card">
                <div class="agenda-date-box">
                    <div class="agenda-day">{item['hari']}</div>
                    <div class="agenda-month-year">{item['bulan_tahun']}</div>
                </div>
                <div class="agenda-content">
                    <div class="agenda-title-link">{item['judul']}</div>
                    <p class="agenda-desc-short">{item['desc']}</p>
                    <div class="agenda-full-date">📅 {item['tanggal_full']}</div>
                </div>
            </div>
            """,
                unsafe_allow_html=True,
            )
        st.markdown("</div></div>", unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True)

    # STATISTIK DASHBOARD
    st.markdown('<div class="page-container">', unsafe_allow_html=True)
    st.markdown(
        """
    <div class="section-header">
        <h2 class="section-header-title">Statistik & Kinerja</h2>
    </div>
    """,
        unsafe_allow_html=True,
    )

    stat_col1, stat_col2 = st.columns(2)
    with stat_col1:
        fig1 = px.line(
            STATS_DATA, x="Bulan", y="Rapat", markers=True,
            title="Jumlah Rapat per Bulan 2026",
            color_discrete_sequence=["#0d5e3a"],
        )
        fig1.update_layout(
            plot_bgcolor="rgba(0,0,0,0)",
            paper_bgcolor="rgba(0,0,0,0)",
            font=dict(family="Inter", size=12, color="#2c3835"),
            title_font=dict(size=14, family="Plus Jakarta Sans", color="#083d26"),
            margin=dict(l=20, r=20, t=50, b=20),
            height=300,
        )
        fig1.update_traces(line=dict(width=3), marker=dict(size=9, line=dict(width=2, color="#fff")))
        st.plotly_chart(fig1, use_container_width=True)

    with stat_col2:
        fig2 = px.pie(
            ANGGARAN_DATA, values="Anggaran", names="Kategori",
            title="Alokasi Anggaran 2026 (%)",
            color_discrete_sequence=["#0d5e3a", "#c9a227", "#14734a", "#e6c458", "#6b7a75"],
            hole=0.5,
        )
        fig2.update_layout(
            plot_bgcolor="rgba(0,0,0,0)",
            paper_bgcolor="rgba(0,0,0,0)",
            font=dict(family="Inter", size=12, color="#2c3835"),
            title_font=dict(size=14, family="Plus Jakarta Sans", color="#083d26"),
            margin=dict(l=20, r=20, t=50, b=20),
            height=300,
        )
        st.plotly_chart(fig2, use_container_width=True)

    st.markdown("</div>", unsafe_allow_html=True)

# =========================================================
# HALAMAN: PROFIL
# =========================================================
elif st.session_state.page == "Profil":
    st.markdown('<div class="page-container">', unsafe_allow_html=True)
    st.markdown(
        """
    <div class="section-header">
        <h2 class="section-header-title">Profil DPRK Aceh Jaya</h2>
    </div>
    <p style="color: #6b7a75; font-size: 13.5px; line-height: 1.8; max-width: 900px; margin-bottom: 24px;">
        Dewan Perwakilan Rakyat Kabupaten Aceh Jaya sebagai unsur penyelenggara pemerintahan daerah bersama pemerintah daerah menjalankan fungsi legislasi, anggaran, dan pengawasan sesuai ketentuan peraturan perundang-undangan.
    </p>
    """,
        unsafe_allow_html=True,
    )

    tab1, tab2 = st.tabs(["🏛️ Pimpinan & Anggota DPRK", "🏢 Pejabat Sekretariat"])

    with tab1:
        st.markdown('<div style="display: grid; grid-template-columns: repeat(auto-fill, minmax(280px, 1fr)); gap: 14px; margin-top: 20px;">', unsafe_allow_html=True)
        for nama, jabatan in PIMPINAN_DAN_ANGGOTA:
            st.markdown(
                f"""
            <div style="background: #fff; border: 1px solid #e0e6e2; border-radius: 8px; padding: 18px; text-align: center; border-top: 3px solid #0d5e3a;">
                <div style="font-weight: 800; color: #0d5e3a; font-size: 13px; margin-bottom: 5px; font-family: 'Plus Jakarta Sans';">{nama}</div>
                <div style="color: #6b7a75; font-size: 11px; font-weight: 600;">{jabatan}</div>
            </div>
            """,
                unsafe_allow_html=True,
            )
        st.markdown('</div>', unsafe_allow_html=True)

    with tab2:
        st.markdown('<div style="display: grid; grid-template-columns: repeat(auto-fill, minmax(320px, 1fr)); gap: 14px; margin-top: 20px;">', unsafe_allow_html=True)
        for nama, jabatan in PEJABAT_SEKRETARIAT:
            st.markdown(
                f"""
            <div style="background: #fff; border: 1px solid #e0e6e2; border-radius: 8px; padding: 18px; text-align: center; border-top: 3px solid #c9a227;">
                <div style="font-weight: 800; color: #0d5e3a; font-size: 13px; margin-bottom: 5px; font-family: 'Plus Jakarta Sans';">{nama}</div>
                <div style="color: #6b7a75; font-size: 11.5px; font-weight: 600;">{jabatan}</div>
            </div>
            """,
                unsafe_allow_html=True,
            )
        st.markdown('</div>', unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True)

# =========================================================
# HALAMAN: BERITA
# =========================================================
elif st.session_state.page == "Berita":
    st.markdown('<div class="page-container">', unsafe_allow_html=True)
    st.markdown(
        """
    <div class="section-header">
        <h2 class="section-header-title">Warta DPRK</h2>
    </div>
    """,
        unsafe_allow_html=True,
    )

    categories = ["Semua"] + list(set(item["kategori"] for item in WARTA_DPRK))
    fc1, fc2, _ = st.columns([1.5, 1.5, 4])
    with fc1:
        selected = st.selectbox("🔍 Kategori", categories)
    with fc2:
        search = st.text_input("🔎 Cari berita", placeholder="Kata kunci...")

    filtered = WARTA_DPRK
    if selected != "Semua":
        filtered = [i for i in filtered if i["kategori"] == selected]
    if search:
        filtered = [i for i in filtered if search.lower() in i["title"].lower() or search.lower() in i["desc"].lower()]

    for item in filtered:
        st.markdown(
            f"""
        <div class="warta-card" style="margin-top: 16px;">
            <div class="warta-card-img-wrap">
                <span class="warta-card-cat">{item['kategori']}</span>
                <img class="warta-card-img" src="{item['image']}">
            </div>
            <div class="warta-card-body">
                <div class="warta-card-date">📅 {item['date']}</div>
                <h3 class="warta-card-title">{item['title']}</h3>
                <p class="warta-card-desc">{item['desc']}</p>
                <a href="#" class="warta-card-readmore">Baca Selengkapnya →</a>
            </div>
        </div>
        """,
            unsafe_allow_html=True,
        )

    if not filtered:
        st.info("Tidak ada berita yang sesuai pencarian.")

    st.markdown(
        """
    <div class="section-header" style="margin-top: 40px;">
        <h2 class="section-header-title">Agenda Terkini</h2>
    </div>
    """,
        unsafe_allow_html=True,
    )
    for item in AGENDA_TERKINI:
        st.markdown(
            f"""
        <div class="agenda-card" style="border: 1px solid #e0e6e2; border-radius: 6px; margin-bottom: 10px; background: #fff;">
            <div class="agenda-date-box">
                <div class="agenda-day">{item['hari']}</div>
                <div class="agenda-month-year">{item['bulan_tahun']}</div>
            </div>
            <div class="agenda-content">
                <div class="agenda-title-link">{item['judul']}</div>
                <p class="agenda-desc-short">{item['desc']}</p>
                <div class="agenda-full-date">📅 {item['tanggal_full']}</div>
            </div>
        </div>
        """,
            unsafe_allow_html=True,
        )
    st.markdown("</div>", unsafe_allow_html=True)

# =========================================================
# HALAMAN: GALERI
# =========================================================
elif st.session_state.page == "Galeri":
    st.markdown('<div class="page-container">', unsafe_allow_html=True)
    st.markdown(
        """
    <div class="section-header">
        <h2 class="section-header-title">Galeri Foto & Video</h2>
    </div>
    """,
        unsafe_allow_html=True,
    )

    gallery = [
        ("Rapat Paripurna", "https://images.unsplash.com/photo-1529107386315-e1a2ed48a620?auto=format&fit=crop&w=600&q=80"),
        ("Kunjungan Kerja", "https://images.unsplash.com/photo-1577962917302-cd874c4e31d2?auto=format&fit=crop&w=600&q=80"),
        ("Sosialisasi Qanun", "https://images.unsplash.com/photo-1556761175-b413da4baf72?auto=format&fit=crop&w=600&q=80"),
        ("Penanaman Mangrove", "https://images.unsplash.com/photo-1589578527966-fdac0f44566c?auto=format&fit=crop&w=600&q=80"),
        ("Rapat Komisi", "https://images.unsplash.com/photo-1517486808906-6ca8b3f04846?auto=format&fit=crop&w=600&q=80"),
        ("Bimbingan Teknis", "https://images.unsplash.com/photo-1523240795612-9a054b0db644?auto=format&fit=crop&w=600&q=80"),
    ]
    gcols = st.columns(3)
    for i, (title, img) in enumerate(gallery):
        with gcols[i % 3]:
            st.markdown(
                f"""
            <div style="background: #fff; border: 1px solid #e0e6e2; border-radius: 8px; overflow: hidden; margin-bottom: 16px;">
                <div style="overflow: hidden;">
                    <img src="{img}" style="width: 100%; height: 200px; object-fit: cover;">
                </div>
                <div style="padding: 14px; text-align: center;">
                    <div style="font-family: 'Plus Jakarta Sans'; font-weight: 700; color: #0d5e3a; font-size: 13px;">{title}</div>
                </div>
            </div>
            """,
                unsafe_allow_html=True,
            )
    st.markdown("</div>", unsafe_allow_html=True)

# =========================================================
# HALAMAN: LAYANAN
# =========================================================
elif st.session_state.page == "Layanan":
    st.markdown('<div class="page-container">', unsafe_allow_html=True)
    st.markdown(
        """
    <div class="section-header">
        <h2 class="section-header-title">Layanan Aspirasi & Pengaduan</h2>
    </div>
    <p style="color: #6b7a75; font-size: 13.5px; line-height: 1.8; max-width: 900px; margin-bottom: 24px;">
        Sampaikan aspirasi, laporan, atau pengaduan Anda kepada DPRK Aceh Jaya melalui formulir di bawah ini.
    </p>
    """,
        unsafe_allow_html=True,
    )

    col1, col2 = st.columns([2, 1])

    with col1:
        with st.form("form_aduan"):
            c1, c2 = st.columns(2)
            with c1:
                nama = st.text_input("Nama Lengkap *", placeholder="Nama lengkap Anda")
                nik = st.text_input("NIK (Opsional)", placeholder="16 digit NIK")
            with c2:
                kategori = st.selectbox("Kategori *", ["Pengaduan Masyarakat", "Infrastruktur & Jalan", "Pelayanan Publik", "Legislasi & Qanun", "Lingkungan & Bencana", "Lainnya"])
                prioritas = st.selectbox("Prioritas", ["Normal", "Penting", "Mendesak"])
            lokasi = st.text_input("Lokasi Kejadian", placeholder="Desa / Kecamatan")
            isi = st.text_area("Isi Laporan *", height=140, placeholder="Jelaskan laporan Anda secara detail...")
            lampiran = st.file_uploader("📎 Lampiran", type=["jpg", "jpeg", "png", "pdf"])

            submitted = st.form_submit_button("🚀 Kirim Laporan", type="primary", use_container_width=True)

            if submitted:
                if nama.strip() and isi.strip():
                    nomor = datetime.now().strftime("%Y%m%d%H%M%S")
                    st.success(f"✅ Laporan diterima! Nomor tiket: **ADU-{nomor}**")
                    st.info(f"📋 Kategori: {kategori} | Prioritas: {prioritas}")
                else:
                    st.error("⚠️ Mohon lengkapi Nama dan Isi Laporan.")

    with col2:
        st.markdown(
            """
        <div class="sidebar-widget">
            <div class="sidebar-widget-head">Kontak Kami</div>
            <div class="sidebar-widget-body" style="padding: 18px;">
                <p style="font-size: 12.5px; color: #6b7a75; line-height: 1.9; margin: 0 0 12px;">
                    <strong style="color: #0d5e3a;">📞 Telepon</strong><br>(0655) 12345
                </p>
                <p style="font-size: 12.5px; color: #6b7a75; line-height: 1.9; margin: 0 0 12px;">
                    <strong style="color: #0d5e3a;">✉️ Email</strong><br>sekretariat@dprk.acehjaya.go.id
                </p>
                <p style="font-size: 12.5px; color: #6b7a75; line-height: 1.9; margin: 0 0 12px;">
                    <strong style="color: #0d5e3a;">📍 Alamat</strong><br>Jl. Merdeka No. 01, Calang, Aceh Jaya
                </p>
                <p style="font-size: 12.5px; color: #6b7a75; line-height: 1.9; margin: 0;">
                    <strong style="color: #0d5e3a;">🕐 Jam Layanan</strong><br>Senin–Jumat, 08.00–16.00 WIB
                </p>
            </div>
        </div>
        """,
            unsafe_allow_html=True,
        )
    st.markdown("</div>", unsafe_allow_html=True)

# =========================================================
# HALAMAN: JDIH
# =========================================================
elif st.session_state.page == "JDIH":
    st.markdown('<div class="page-container">', unsafe_allow_html=True)
    st.markdown(
        """
    <div class="section-header">
        <h2 class="section-header-title">JDIH & Transparansi</h2>
    </div>
    <p style="color: #6b7a75; font-size: 13.5px; line-height: 1.8; max-width: 900px; margin-bottom: 24px;">
        Akses daftar produk hukum dan informasi publik DPRK Aceh Jaya.
    </p>
    """,
        unsafe_allow_html=True,
    )

    df = pd.DataFrame(JDIH_DATA, columns=["No", "Nomor & Tahun", "Tentang", "Status"])
    st.dataframe(df, use_container_width=True, hide_index=True)
    st.markdown("</div>", unsafe_allow_html=True)

# =========================================================
# HALAMAN: KONTAK
# =========================================================
else:
    st.markdown('<div class="page-container">', unsafe_allow_html=True)
    st.markdown(
        """
    <div class="section-header">
        <h2 class="section-header-title">Hubungi Kami</h2>
    </div>
    """,
        unsafe_allow_html=True,
    )

    cols = st.columns(3)
    contacts = [
        ("📍", "Alamat", "Jl. Merdeka No. 01, Calang, Kabupaten Aceh Jaya"),
        ("📞", "Telepon", "(0655) 12345"),
        ("✉️", "Email", "sekretariat@dprk.acehjaya.go.id"),
    ]
    for i, (icon, title, value) in enumerate(contacts):
        with cols[i]:
            st.markdown(
                f"""
            <div class="layanan-icon">
                <div class="layanan-icon-circle">{icon}</div>
                <div class="layanan-icon-title">{title}</div>
                <div class="layanan-icon-desc">{value}</div>
            </div>
            """,
                unsafe_allow_html=True,
            )

    st.markdown(
        """
    <div style="margin-top: 30px; background: #fff; border: 1px solid #e0e6e2; border-radius: 8px; padding: 24px;">
        <div class="section-header" style="margin-bottom: 16px;">
            <h2 class="section-header-title" style="font-size: 17px;">Peta Lokasi Kantor</h2>
        </div>
        <div style="width: 100%; height: 340px; border-radius: 6px; overflow: hidden; border: 1px solid #e0e6e2;">
            <iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3988.5!2d95.39!3d4.71!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x30403e5f3a0b0b0b%3A0x0!2sCalang%2C%20Aceh%20Jaya%20Regency%2C%20Aceh!5e0!3m2!1sen!2sid!4v1600000000000" width="100%" height="100%" style="border:0;" allowfullscreen="" loading="lazy"></iframe>
        </div>
    </div>
    """,
        unsafe_allow_html=True,
    )
    st.markdown("</div>", unsafe_allow_html=True)

# =========================================================
# FOOTER
# =========================================================
st.markdown(
    f"""
<div class="footer-main">
<div class="footer-inner">
<div class="footer-grid">

<div class="footer-col">
<div class="footer-brand-block">
<div class="footer-logo-box">
    <img src="{LOGO_URL}" alt="Logo DPRK Aceh Jaya"
         onerror="this.onerror=null;this.src='data:image/svg+xml,<svg xmlns=%22http://www.w3.org/2000/svg%22 viewBox=%220 0 100 100%22><text y=%22.9em%22 font-size=%2290%22>🏛️</text></svg>'">
</div>
<div>
<div class="footer-brand-title">DPRK ACEH JAYA</div>
<div class="footer-brand-sub">SEKRETARIAT DPRK</div>
</div>
</div>
<p style="color: rgba(255,255,255,0.6); font-size: 12.5px; line-height: 1.85; max-width: 340px; margin: 0 0 8px;">
Portal resmi Sekretariat Dewan Perwakilan Rakyat Kabupaten Aceh Jaya. Menyediakan informasi kelembagaan, berita, agenda, produk hukum, dan layanan aspirasi masyarakat.
</p>
<div class="footer-social">
<a href="#" class="footer-social-item">f</a>
<a href="#" class="footer-social-item">𝕏</a>
<a href="#" class="footer-social-item">▶</a>
<a href="#" class="footer-social-item">◎</a>
<a href="#" class="footer-social-item">in</a>
</div>
</div>

<div class="footer-col">
<h4>Navigasi</h4>
<a href="?page=beranda">Beranda</a>
<a href="?page=profil">Profil DPRK</a>
<a href="?page=profil">Pimpinan DPRK</a>
<a href="?page=berita">Berita & Agenda</a>
<a href="?page=galeri">Galeri</a>
</div>

<div class="footer-col">
<h4>Layanan</h4>
<a href="?page=layanan">Pengaduan Masyarakat</a>
<a href="?page=kontak">Informasi Publik</a>
<a href="?page=jdih">JDIH</a>
<a href="?page=jdih">Transparansi</a>
<a href="https://elhpkpn.kpk.go.id/" target="_blank">E-LHKPN</a>
</div>

<div class="footer-col">
<h4>Hubungi Kami</h4>
<p>📍 Jl. Merdeka No. 01</p>
<p>Calang, Kabupaten Aceh Jaya</p>
<p>📞 (0655) 12345</p>
<p>✉️ sekretariat@dprk.acehjaya.go.id</p>
<p>🕐 Senin–Jumat, 08.00–16.00 WIB</p>
</div>

</div>

<div class="footer-bottom">
<div>© {datetime.now().year} Sekretariat DPRK Kabupaten Aceh Jaya. Seluruh hak cipta dilindungi.</div>
<div>Portal Informasi Publik • Kabupaten Aceh Jaya</div>
</div>

</div>
</div>
""",
    unsafe_allow_html=True,
)

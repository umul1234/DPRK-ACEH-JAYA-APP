import streamlit as st
from datetime import datetime
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
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

LOGO_URL = "https://i.imgur.com/bTNXnLF.png"

# =========================================================
# SESSION STATE
# =========================================================
if "page" not in st.session_state:
    st.session_state.page = "Beranda"
if "dark_mode" not in st.session_state:
    st.session_state.dark_mode = False
if "show_chat" not in st.session_state:
    st.session_state.show_chat = False
if "show_notif" not in st.session_state:
    st.session_state.show_notif = False
if "visitor_count" not in st.session_state:
    st.session_state.visitor_count = random.randint(15000, 25000)
if "berita_filter" not in st.session_state:
    st.session_state.berita_filter = "Semua"

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
    {
        "title": "Sosialisasi Qanun No. 5 Tahun 2025 tentang Ketertiban Umum",
        "date": "Senin, 20 Juli 2026",
        "desc": "DPRK Aceh Jaya menggelar sosialisasi Qanun Nomor 5 Tahun 2025 tentang Ketertiban Umum dan Ketenteraman Masyarakat kepada seluruh elemen masyarakat.",
        "image": "https://images.unsplash.com/photo-1517486808906-6ca8b3f04846?auto=format&fit=crop&w=800&q=80",
        "kategori": "Legislasi",
        "views": 645,
    },
    {
        "title": "Kunjungan Kerja Komisi II ke Dinas Pendidikan Aceh Jaya",
        "date": "Kamis, 16 Juli 2026",
        "desc": "Komisi II DPRK Aceh Jaya melakukan kunjungan kerja ke Dinas Pendidikan untuk membahas program prioritas pendidikan tahun 2027.",
        "image": "https://images.unsplash.com/photo-1523240795612-9a054b0db644?auto=format&fit=crop&w=800&q=80",
        "kategori": "Kunjungan",
        "views": 534,
    },
]

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

AGENDA_TERKINI = [
    {"tanggal": "09 September 2026", "judul": "Rapat Pleno DPRK Aceh Jaya", "desc": "Rapat Pleno DPRK Aceh Jaya terhadap Rancangan Perubahan KUA-PPAS APBK Aceh Jaya Tahun Anggaran."},
    {"tanggal": "07 September 2026", "judul": "Rapat Komisi III DPRK Aceh Jaya", "desc": "Rapat Dengar Pendapat Komisi III terkait Realisasi Program dan Kegiatan Pembangunan Jalan dan Jembatan pada Dinas PUPR."},
    {"tanggal": "01 September 2026", "judul": "Rapat Badan Musyawarah DPRK Aceh Jaya", "desc": "Rapat Badan Musyawarah tentang Penetapan Jadwal Rapat Paripurna DPRK Aceh Jaya."},
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
    ["6", "Qanun No. 1/2023", "Rencana Tata Ruang Wilayah", "Dicabut"],
]

# Data Statistik
STATS_DATA = pd.DataFrame({
    "Bulan": ["Jan", "Feb", "Mar", "Apr", "Mei", "Jun", "Jul", "Agu", "Sep"],
    "Rapat": [8, 10, 7, 12, 9, 11, 8, 10, 9],
    "Pengaduan": [12, 15, 10, 18, 14, 20, 16, 22, 19],
    "Produk Hukum": [2, 3, 1, 4, 2, 3, 2, 4, 3],
})

ANGGARAN_DATA = pd.DataFrame({
    "Kategori": ["Infrastruktur", "Pendidikan", "Kesehatan", "Sosial", "Pertanian"],
    "Anggaran": [45, 25, 15, 8, 7],
})

# =========================================================
# CSS STYLE ULTRA PREMIUM
# =========================================================
st.markdown(
    """
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&family=Plus+Jakarta+Sans:wght@500;600;700;800&display=swap');

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
}

* { box-sizing: border-box; font-family: 'Inter', sans-serif; }
html, body, [class*="css"] { font-family: 'Inter', sans-serif; }
#MainMenu, footer, header { visibility: hidden; height: 0; }
.stApp { 
    background: var(--bg); 
    color: var(--text);
    background-image: 
        radial-gradient(circle at 10% 20%, rgba(213,165,43,0.05) 0%, transparent 40%),
        radial-gradient(circle at 90% 80%, rgba(6,78,59,0.05) 0%, transparent 40%);
    background-attachment: fixed;
}
.block-container { max-width: 100%; padding: 0 !important; }
section[data-testid="stSidebar"] { display: none; }

/* Scrollbar premium */
::-webkit-scrollbar { width: 10px; height: 10px; }
::-webkit-scrollbar-track { background: #e9f5f1; }
::-webkit-scrollbar-thumb { background: linear-gradient(180deg, #064e3b, #0f6b58); border-radius: 5px; }
::-webkit-scrollbar-thumb:hover { background: linear-gradient(180deg, #0f6b58, #d5a52b); }

/* ============================================
   TOP BAR - ULTRA PREMIUM
   ============================================ */
.govbar { 
    background: linear-gradient(90deg, #022c22 0%, #064e3b 50%, #022c22 100%); 
    color: rgba(255,255,255,.88); 
    min-height: 42px; 
    padding: 0 6%; 
    display: flex; 
    align-items: center; 
    justify-content: space-between; 
    font-size: 12px;
    position: relative;
    overflow: hidden;
    border-bottom: 1px solid rgba(213,165,43,0.2);
}
.govbar::before {
    content: '';
    position: absolute;
    top: 0; left: -100%; right: 0; bottom: 0;
    background: linear-gradient(90deg, transparent, rgba(213,165,43,0.15), transparent);
    animation: shineBar 6s infinite;
}
@keyframes shineBar {
    0% { left: -100%; }
    50%, 100% { left: 100%; }
}
.govbar-left, .govbar-right { display: flex; gap: 20px; align-items: center; position: relative; z-index: 2; }
.govbar strong { color: #fff; }
.govbar-right a { color: rgba(255,255,255,.88); text-decoration: none; transition: color .15s ease; }
.govbar-right a:hover { color: var(--gold-light); text-decoration: underline; }
.govbar-clock { 
    background: rgba(213,165,43,0.15); 
    padding: 4px 12px; 
    border-radius: 12px; 
    border: 1px solid rgba(213,165,43,0.3);
    color: var(--gold-light);
    font-weight: 600;
    font-variant-numeric: tabular-nums;
}

/* ============================================
   BRAND - PREMIUM
   ============================================ */
.brand-wrap { 
    background: #fff; 
    border-bottom: 1px solid #e7ecea; 
    padding: 18px 6%;
    position: relative;
}
.brand-wrap::after {
    content: '';
    position: absolute;
    bottom: 0; left: 0; right: 0;
    height: 3px;
    background: linear-gradient(90deg, var(--primary) 0%, var(--gold) 50%, var(--primary) 100%);
    opacity: 0.3;
}
.brand-inner { display: flex; align-items: center; justify-content: space-between; gap: 24px; }
.brand { display: flex; align-items: center; gap: 14px; }
.brand-logo { 
    width: 75px; height: 75px; 
    border-radius: 12px; 
    background: linear-gradient(145deg, #fff, #f6f8f7); 
    display: flex; 
    align-items: center; 
    justify-content: center; 
    box-shadow: 0 8px 24px rgba(12,74,62,.15), inset 0 1px 0 rgba(255,255,255,0.8); 
    overflow: hidden;
    transition: transform 0.4s cubic-bezier(0.4, 0, 0.2, 1);
    position: relative;
}
.brand-logo::before {
    content: '';
    position: absolute;
    top: 0; left: 0; right: 0; bottom: 0;
    background: radial-gradient(circle at 30% 30%, rgba(213,165,43,0.15), transparent 60%);
    border-radius: 12px;
}
.brand-logo:hover { transform: scale(1.08) rotate(-3deg); }
.brand-logo img { width: 100%; height: 100%; object-fit: contain; position: relative; z-index: 2; }
.brand-title { 
    color: #123b33; 
    font-family: 'Plus Jakarta Sans', sans-serif; 
    font-size: 19px; 
    line-height: 1.2; 
    font-weight: 800; 
    text-transform: uppercase;
    letter-spacing: 0.3px;
}
.brand-subtitle { 
    margin-top: 5px; 
    color: #788783; 
    font-size: 11px; 
    letter-spacing: .8px;
    display: flex;
    align-items: center;
    gap: 8px;
}
.brand-subtitle::before {
    content: '';
    width: 20px;
    height: 2px;
    background: var(--gold);
    display: inline-block;
}

/* Live Indicators */
.live-indicators {
    display: flex;
    gap: 15px;
    align-items: center;
}
.live-badge {
    display: flex;
    align-items: center;
    gap: 8px;
    background: linear-gradient(135deg, #f0fdf4, #dcfce7);
    border: 1px solid #86efac;
    padding: 8px 14px;
    border-radius: 20px;
    font-size: 11px;
    font-weight: 700;
    color: #166534;
}
.live-dot {
    width: 8px;
    height: 8px;
    border-radius: 50%;
    background: #22c55e;
    animation: pulseDot 1.5s ease-in-out infinite;
    box-shadow: 0 0 0 0 rgba(34, 197, 94, 0.7);
}
@keyframes pulseDot {
    0% { box-shadow: 0 0 0 0 rgba(34, 197, 94, 0.7); }
    70% { box-shadow: 0 0 0 10px rgba(34, 197, 94, 0); }
    100% { box-shadow: 0 0 0 0 rgba(34, 197, 94, 0); }
}

/* ============================================
   NAVIGATION - ULTRA PREMIUM
   ============================================ */
.nav-wrap { 
    background: linear-gradient(180deg, #065f46 0%, #022c22 100%); 
    border-bottom: 2px solid var(--gold); 
    padding: 0 6%;
    box-shadow: 0 12px 40px rgba(0,0,0,0.25), 0 2px 8px rgba(0,0,0,0.1);
    position: sticky;
    top: 0;
    z-index: 999;
}
.nav-wrap::before {
    content: '';
    position: absolute;
    top: 0; left: 0; right: 0;
    height: 1px;
    background: linear-gradient(90deg, transparent, rgba(255,255,255,0.5), transparent);
}
.nav-inner { min-height: 66px; display: flex; align-items: center; gap: 0; justify-content: center; }

.nav-button .stButton > button, 
.nav-button-active .stButton > button {
    background: transparent !important; 
    border: 1px solid transparent !important; 
    color: rgba(255,255,255,0.85) !important;
    font-size: 12px !important;
    font-weight: 700 !important;
    font-family: 'Plus Jakarta Sans', sans-serif !important;
    border-radius: 8px !important;
    padding: 14px 12px !important;
    min-height: 50px !important;
    width: 100% !important;
    transition: all 0.35s cubic-bezier(0.4, 0, 0.2, 1) !important;
    letter-spacing: 0.8px !important;
    text-transform: uppercase !important;
    white-space: nowrap !important;
    position: relative;
    overflow: hidden;
}
.nav-button .stButton > button::before {
    content: '';
    position: absolute;
    top: 50%; left: 50%;
    width: 0; height: 0;
    background: radial-gradient(circle, rgba(213,165,43,0.3) 0%, transparent 70%);
    border-radius: 50%;
    transform: translate(-50%, -50%);
    transition: width 0.5s ease, height 0.5s ease;
}
.nav-button .stButton > button:hover::before {
    width: 200px; height: 200px;
}
.nav-button .stButton > button:hover { 
    color: #ffffff !important; 
    background: rgba(255,255,255,0.08) !important;
    border-color: rgba(213,165,43,0.3) !important;
    transform: translateY(-3px);
    box-shadow: 0 8px 20px rgba(0,0,0,0.2);
}
.nav-button-active .stButton > button {
    color: #ffffff !important; 
    font-weight: 800 !important; 
    background: linear-gradient(135deg, rgba(213, 165, 43, 0.25) 0%, rgba(213, 165, 43, 0.08) 100%) !important;
    border-color: rgba(213, 165, 43, 0.6) !important;
    box-shadow: 0 0 25px rgba(213, 165, 43, 0.2), inset 0 1px 0 rgba(255,255,255,0.15);
    position: relative;
}
.nav-button-active .stButton > button::after {
    content: '';
    position: absolute;
    bottom: 3px; left: 50%;
    transform: translateX(-50%);
    width: 40%;
    height: 3px;
    background: linear-gradient(90deg, transparent, var(--gold-light), var(--gold), var(--gold-light), transparent);
    border-radius: 2px;
    box-shadow: 0 0 12px rgba(213,165,43,0.9);
    animation: glowPulse 2s ease-in-out infinite;
}
@keyframes glowPulse {
    0%, 100% { opacity: 0.8; }
    50% { opacity: 1; }
}

/* ============================================
   RUNNING TEXT PREMIUM
   ============================================ */
.running-text-wrap { 
    background: linear-gradient(90deg, #d5a52b 0%, #fcd34d 50%, #d5a52b 100%); 
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
    width: 80px;
    z-index: 2;
    pointer-events: none;
}
.running-text-wrap::before { left: 0; background: linear-gradient(90deg, #d5a52b, transparent); }
.running-text-wrap::after { right: 0; background: linear-gradient(-90deg, #d5a52b, transparent); }
.running-text { display: inline-block; padding-left: 100%; animation: marquee 45s linear infinite; font-size: 13px; font-weight: 700; }
@keyframes marquee { 0% { transform: translate(0, 0); } 100% { transform: translate(-100%, 0); } }

/* ============================================
   HERO ULTRA PREMIUM
   ============================================ */
.hero { 
    position: relative; 
    min-height: 560px; 
    display: flex; 
    align-items: center; 
    overflow: hidden; 
    background: linear-gradient(90deg, rgba(4,43,36,.97) 0%, rgba(8,74,62,.85) 45%, rgba(8,74,62,.4) 100%), 
                url('https://images.unsplash.com/photo-1529107386315-e1a2ed48a620?auto=format&fit=crop&w=1800&q=85') center/cover no-repeat; 
    background-attachment: fixed;
}
.hero::before {
    content: '';
    position: absolute;
    top: 0; left: 0; right: 0; bottom: 0;
    background: radial-gradient(ellipse at 20% 50%, rgba(213,165,43,0.18) 0%, transparent 60%);
    animation: pulseBg 5s ease-in-out infinite;
}
@keyframes pulseBg {
    0%, 100% { opacity: 0.5; transform: scale(1); }
    50% { opacity: 1; transform: scale(1.05); }
}
.hero::after {
    content: '';
    position: absolute;
    bottom: 0; left: 0; right: 0;
    height: 150px;
    background: linear-gradient(180deg, transparent, rgba(2,44,34,0.5));
    pointer-events: none;
}
.hero-content { width: 88%; max-width: 1250px; margin: 0 auto; padding: 70px 0; color: white; position: relative; z-index: 2; }
.hero-kicker { 
    display: inline-block; 
    color: #f8df87; 
    font-size: 12px; 
    font-weight: 800; 
    letter-spacing: 2px; 
    margin-bottom: 20px;
    padding: 8px 18px;
    background: rgba(213,165,43,0.15);
    border: 1px solid rgba(213,165,43,0.4);
    border-radius: 25px;
    animation: fadeInUp 0.8s ease;
    backdrop-filter: blur(10px);
}
.hero h1 { 
    max-width: 780px; 
    font-family: 'Plus Jakarta Sans', sans-serif; 
    font-size: clamp(36px, 5.5vw, 66px); 
    line-height: 1.05; 
    margin: 0 0 24px; 
    font-weight: 900;
    letter-spacing: -1px;
    animation: fadeInUp 1s ease;
    text-shadow: 0 4px 30px rgba(0,0,0,0.4);
}
.hero h1 span { 
    background: linear-gradient(135deg, #fcd34d, #d5a52b, #fcd34d);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
}
.hero p { 
    max-width: 680px; 
    color: rgba(255,255,255,.92); 
    font-size: 16px; 
    line-height: 1.8; 
    margin-bottom: 32px;
    animation: fadeInUp 1.2s ease;
}
.hero-buttons { display: flex; flex-wrap: wrap; gap: 14px; animation: fadeInUp 1.4s ease; }
.hero-btn { 
    display: inline-flex;
    align-items: center;
    gap: 10px;
    padding: 15px 30px; 
    border-radius: 8px; 
    background: linear-gradient(135deg, #d5a52b, #c1961f); 
    color: #fff !important; 
    text-decoration: none; 
    font-weight: 700; 
    font-size: 14px; 
    transition: all .35s cubic-bezier(0.4, 0, 0.2, 1);
    box-shadow: 0 8px 24px rgba(213,165,43,0.4), inset 0 1px 0 rgba(255,255,255,0.3);
    position: relative;
    overflow: hidden;
}
.hero-btn::before {
    content: '';
    position: absolute;
    top: 0; left: -100%;
    width: 100%; height: 100%;
    background: linear-gradient(90deg, transparent, rgba(255,255,255,0.3), transparent);
    transition: left 0.6s ease;
}
.hero-btn:hover::before { left: 100%; }
.hero-btn:hover { 
    transform: translateY(-4px); 
    box-shadow: 0 15px 35px rgba(213,165,43,0.55);
}
.hero-btn.secondary { 
    background: rgba(255,255,255,.1); 
    border: 2px solid rgba(255,255,255,.5);
    box-shadow: none;
    backdrop-filter: blur(10px);
}
.hero-btn.secondary:hover { 
    background: rgba(255,255,255,.2); 
    border-color: var(--gold-light);
    box-shadow: 0 15px 35px rgba(0,0,0,0.3);
}

@keyframes fadeInUp {
    from { opacity: 0; transform: translateY(40px); }
    to { opacity: 1; transform: translateY(0); }
}

/* Floating Stats Hero */
.floating-stats {
    position: absolute;
    bottom: 50px;
    right: 6%;
    display: flex;
    gap: 15px;
    z-index: 3;
    animation: fadeInUp 1.6s ease;
}
.floating-stat {
    background: rgba(255,255,255,0.08);
    backdrop-filter: blur(15px);
    border: 1px solid rgba(255,255,255,0.15);
    padding: 18px 24px;
    border-radius: 14px;
    text-align: center;
    min-width: 120px;
    transition: all 0.3s ease;
    position: relative;
    overflow: hidden;
}
.floating-stat::before {
    content: '';
    position: absolute;
    top: 0; left: 0; right: 0;
    height: 2px;
    background: linear-gradient(90deg, transparent, var(--gold-light), transparent);
}
.floating-stat:hover {
    transform: translateY(-5px);
    background: rgba(255,255,255,0.15);
    border-color: rgba(213,165,43,0.5);
}
.floating-stat-num { color: var(--gold-light); font-size: 26px; font-weight: 900; font-variant-numeric: tabular-nums; }
.floating-stat-label { color: rgba(255,255,255,0.75); font-size: 10px; margin-top: 5px; letter-spacing: 0.5px; text-transform: uppercase; }

/* ============================================
   CONTENT & SECTIONS
   ============================================ */
.content { width: 88%; max-width: 1250px; margin: 0 auto; }
.section { padding: 55px 0; }
.section-head { display: flex; justify-content: space-between; align-items: end; gap: 20px; margin-bottom: 28px; }
.section-kicker { 
    color: var(--primary-2); 
    font-size: 11px; 
    font-weight: 800; 
    letter-spacing: 1.8px; 
    text-transform: uppercase; 
    margin-bottom: 8px;
    display: inline-flex;
    align-items: center;
    gap: 10px;
}
.section-kicker::before {
    content: '';
    width: 24px;
    height: 2px;
    background: var(--gold);
    display: inline-block;
}
.section-title { 
    color: #183d35; 
    font-family: 'Plus Jakarta Sans', sans-serif; 
    font-size: 30px; 
    font-weight: 800; 
    margin: 0;
    letter-spacing: -0.5px;
    position: relative;
}
.section-desc { color: var(--muted); font-size: 13.5px; line-height: 1.7; margin-top: 8px; }

/* ============================================
   SERVICE BOX ULTRA
   ============================================ */
.service-box { 
    background: #fff; 
    border: 1px solid var(--border); 
    min-height: 180px; 
    padding: 28px 22px; 
    text-align: center; 
    transition: all .4s cubic-bezier(0.4, 0, 0.2, 1);
    border-radius: 14px;
    position: relative;
    overflow: hidden;
}
.service-box::before {
    content: '';
    position: absolute;
    top: 0; left: 0; right: 0;
    height: 4px;
    background: linear-gradient(90deg, var(--primary), var(--gold), var(--primary));
    transform: scaleX(0);
    transform-origin: left;
    transition: transform 0.5s ease;
}
.service-box::after {
    content: '';
    position: absolute;
    top: -50%; right: -50%;
    width: 200px; height: 200px;
    background: radial-gradient(circle, rgba(213,165,43,0.08) 0%, transparent 70%);
    border-radius: 50%;
    opacity: 0;
    transition: opacity 0.4s ease;
}
.service-box:hover::before { transform: scaleX(1); }
.service-box:hover::after { opacity: 1; }
.service-box:hover { 
    transform: translateY(-10px); 
    border-color: rgba(213,165,43,0.4); 
    box-shadow: 0 25px 50px rgba(12,74,62,0.18);
}
.service-icon { 
    width: 68px; 
    height: 68px; 
    margin: 0 auto 16px; 
    border-radius: 18px; 
    background: linear-gradient(145deg, #e9f5f1, #d5e8e1); 
    color: var(--primary); 
    display: flex; 
    align-items: center; 
    justify-content: center; 
    font-size: 30px; 
    transition: all .5s cubic-bezier(0.4, 0, 0.2, 1);
    box-shadow: 0 4px 12px rgba(12,74,62,0.1);
}
.service-box:hover .service-icon { 
    transform: scale(1.15) rotate(-8deg); 
    background: linear-gradient(145deg, #fcd34d, #d5a52b);
    color: #fff;
    box-shadow: 0 8px 24px rgba(213,165,43,0.4);
}
.service-icon.accent-gold { background: linear-gradient(145deg, #fef3c7, #fde68a); color: #a97e1c; }
.service-icon.accent-blue { background: linear-gradient(145deg, #dbeafe, #bfdbfe); color: #2f5f8f; }
.service-title { color: #183d35; font-size: 15px; font-weight: 800; margin-bottom: 8px; }
.service-desc { color: #7a8884; font-size: 11.5px; line-height: 1.6; }

/* ============================================
   NEWS CARD ULTRA
   ============================================ */
.news-grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(290px, 1fr)); gap: 26px; }
.news-card { 
    background: #fff; 
    border: 1px solid var(--border); 
    border-radius: 14px; 
    overflow: hidden; 
    transition: all .4s cubic-bezier(0.4, 0, 0.2, 1);
    height: 100%; 
    display: flex; 
    flex-direction: column;
    position: relative;
}
.news-card::after {
    content: '';
    position: absolute;
    bottom: 0; left: 0; right: 0;
    height: 4px;
    background: linear-gradient(90deg, var(--gold), var(--primary), var(--gold));
    transform: scaleX(0);
    transform-origin: left;
    transition: transform 0.5s ease;
}
.news-card:hover::after { transform: scaleX(1); }
.news-card:hover { 
    box-shadow: 0 25px 60px rgba(12,74,62,0.2); 
    border-color: rgba(213,165,43,0.4);
    transform: translateY(-8px);
}
.news-card-img { width: 100%; height: 200px; object-fit: cover; transition: transform .7s cubic-bezier(0.4, 0, 0.2, 1); }
.news-card:hover .news-card-img { transform: scale(1.12) rotate(1deg); }
.news-card-img-wrap { overflow: hidden; position: relative; }
.news-card-img-wrap::after {
    content: '';
    position: absolute;
    bottom: 0; left: 0; right: 0;
    height: 60%;
    background: linear-gradient(180deg, transparent, rgba(0,0,0,0.4));
    opacity: 0;
    transition: opacity 0.4s ease;
}
.news-card:hover .news-card-img-wrap::after { opacity: 1; }
.news-card-category {
    position: absolute;
    top: 14px;
    left: 14px;
    background: linear-gradient(135deg, var(--gold), #c1961f);
    color: #fff;
    padding: 5px 12px;
    border-radius: 6px;
    font-size: 10px;
    font-weight: 800;
    text-transform: uppercase;
    letter-spacing: 0.5px;
    box-shadow: 0 4px 12px rgba(213,165,43,0.4);
    z-index: 2;
}
.news-card-views {
    position: absolute;
    top: 14px;
    right: 14px;
    background: rgba(0,0,0,0.65);
    backdrop-filter: blur(10px);
    color: #fff;
    padding: 5px 12px;
    border-radius: 6px;
    font-size: 10px;
    font-weight: 700;
    z-index: 2;
}
.news-card-body { padding: 20px; flex: 1; display: flex; flex-direction: column; }
.news-card h3 { 
    color: #173b33; 
    font-family: 'Plus Jakarta Sans', sans-serif; 
    font-size: 16px; 
    line-height: 1.45; 
    margin: 0 0 10px; 
    font-weight: 700; 
    flex: 1;
    transition: color 0.3s ease;
}
.news-card:hover h3 { color: var(--primary-2); }
.news-card p { color: #71817d; font-size: 12.5px; line-height: 1.65; margin: 0 0 14px; }
.news-date { 
    color: var(--primary-2); 
    font-size: 11px; 
    font-weight: 700; 
    display: flex; 
    align-items: center; 
    gap: 6px;
    padding-top: 12px;
    border-top: 1px solid var(--border);
}

/* ============================================
   WARTA LIST
   ============================================ */
.warta-list { display: flex; flex-direction: column; gap: 18px; }
.warta-item { 
    background: #fff; 
    border: 1px solid var(--border); 
    border-radius: 14px; 
    padding: 24px; 
    transition: all .4s cubic-bezier(0.4, 0, 0.2, 1);
    border-left: 5px solid var(--primary-3);
    position: relative;
    overflow: hidden;
}
.warta-item::before {
    content: '';
    position: absolute;
    top: 0; left: 0; bottom: 0;
    width: 5px;
    background: linear-gradient(180deg, var(--gold), var(--primary));
    transform: scaleY(0);
    transform-origin: top;
    transition: transform 0.4s ease;
}
.warta-item:hover::before { transform: scaleY(1); }
.warta-item:hover { 
    box-shadow: 0 20px 45px rgba(12,74,62,0.12);
    border-left-color: transparent;
    transform: translateX(8px);
}
.warta-item h3 { color: var(--primary); font-family: 'Plus Jakarta Sans', sans-serif; font-size: 17px; margin: 0 0 10px; font-weight: 700; line-height: 1.45; }
.warta-item .date { 
    color: var(--gold); 
    font-size: 12px; 
    font-weight: 800; 
    margin-bottom: 10px; 
    display: inline-flex;
    align-items: center;
    gap: 6px;
    padding: 4px 10px;
    background: var(--gold-soft);
    border-radius: 4px;
}
.warta-item p { color: var(--muted); font-size: 13.5px; line-height: 1.7; margin: 0; }

/* ============================================
   AGENDA
   ============================================ */
.agenda-wrap { 
    background: #fff; 
    border: 1px solid var(--border); 
    border-radius: 14px; 
    padding: 25px;
    box-shadow: 0 4px 12px rgba(12,74,62,0.04);
}
.agenda-item { 
    margin-bottom: 22px; 
    padding-bottom: 22px; 
    border-bottom: 1px solid var(--border); 
    transition: all 0.3s ease;
    border-radius: 8px;
    padding-left: 14px;
    position: relative;
}
.agenda-item::before {
    content: '';
    position: absolute;
    left: 0; top: 8px; bottom: 8px;
    width: 3px;
    background: transparent;
    border-radius: 2px;
    transition: background 0.3s ease;
}
.agenda-item:hover::before { background: var(--gold); }
.agenda-item:hover { padding-left: 20px; background: #fafcfb; }
.agenda-item:last-child { border-bottom: none; margin-bottom: 0; padding-bottom: 0; }
.agenda-date-badge { 
    display: inline-flex;
    align-items: center;
    gap: 6px;
    background: linear-gradient(135deg, var(--primary), var(--primary-2)); 
    color: white; 
    padding: 7px 14px; 
    border-radius: 8px; 
    font-size: 11px; 
    font-weight: 800; 
    margin-bottom: 12px;
    box-shadow: 0 4px 12px rgba(6,78,59,0.25);
    letter-spacing: 0.3px;
}
.agenda-title { color: #1b4138; font-weight: 800; font-size: 15px; margin-bottom: 8px; line-height: 1.4; }
.agenda-desc { color: #7a8884; font-size: 12.5px; line-height: 1.65; }

/* ============================================
   INFO STRIP ULTRA
   ============================================ */
.info-strip { 
    background: linear-gradient(135deg, var(--primary) 0%, var(--primary-2) 50%, var(--primary) 100%); 
    color: white; 
    padding: 50px 6%;
    position: relative;
    overflow: hidden;
}
.info-strip::before {
    content: '';
    position: absolute;
    top: -50%; right: -10%;
    width: 500px; height: 500px;
    background: radial-gradient(circle, rgba(213,165,43,0.2) 0%, transparent 70%);
    border-radius: 50%;
    animation: floatOrb 8s ease-in-out infinite;
}
.info-strip::after {
    content: '';
    position: absolute;
    bottom: -50%; left: -10%;
    width: 400px; height: 400px;
    background: radial-gradient(circle, rgba(213,165,43,0.15) 0%, transparent 70%);
    border-radius: 50%;
    animation: floatOrb 10s ease-in-out infinite reverse;
}
@keyframes floatOrb {
    0%, 100% { transform: translate(0, 0); }
    50% { transform: translate(30px, -30px); }
}
.info-inner { width: 88%; max-width: 1250px; margin: auto; position: relative; z-index: 2; }
.info-item { text-align: center; padding: 8px 15px; position: relative; }
.info-item.has-divider::after { 
    content: ''; 
    position: absolute; 
    right: 0; top: 15px; bottom: 15px; 
    width: 1px; 
    background: linear-gradient(180deg, transparent, rgba(213,165,43,0.4), transparent); 
}
.info-number { 
    color: #f4d873; 
    font-size: 38px; 
    font-weight: 900; 
    font-variant-numeric: tabular-nums;
    text-shadow: 0 4px 20px rgba(213,165,43,0.4);
    line-height: 1;
}
.info-label { color: rgba(255,255,255,.85); font-size: 11.5px; margin-top: 8px; letter-spacing: 0.5px; text-transform: uppercase; font-weight: 600; }

/* ============================================
   TAB PREMIUM
   ============================================ */
.stTabs [data-baseweb="tab-list"] { 
    gap: 8px; 
    background: transparent; 
    border-bottom: 2px solid var(--border);
    padding-bottom: 0;
}
.stTabs [data-baseweb="tab"] { 
    background: transparent; 
    border-radius: 10px 10px 0 0; 
    padding: 14px 28px; 
    color: var(--muted); 
    font-weight: 700; 
    font-family: 'Plus Jakarta Sans', sans-serif;
    transition: all 0.3s ease;
    font-size: 13px;
}
.stTabs [aria-selected="true"] { 
    background: linear-gradient(180deg, var(--primary-3), transparent) !important; 
    color: var(--primary) !important; 
    border-bottom: 3px solid var(--primary);
}
.stTabs [data-baseweb="tab"]:hover { 
    background: #f2f7f5 !important; 
    color: var(--primary) !important; 
}

/* ============================================
   FORM PREMIUM
   ============================================ */
div[data-testid="stForm"] { 
    background: linear-gradient(145deg, #ffffff, #fafcfb); 
    border: 1px solid var(--border); 
    border-radius: 14px; 
    padding: 28px !important;
    box-shadow: 0 8px 24px rgba(12,74,62,0.06);
}
.stTextInput input, .stTextArea textarea, div[data-baseweb="select"] > div { 
    border-radius: 8px !important; 
    border-color: #d8e1de !important;
    transition: all 0.25s ease;
}
.stTextInput input:focus, .stTextArea textarea:focus { 
    border-color: var(--gold) !important;
    box-shadow: 0 0 0 3px rgba(213,165,43,0.15) !important;
}
.stButton > button[kind="primary"], .stFormSubmitButton > button { 
    background: linear-gradient(135deg, var(--primary), var(--primary-2)) !important; 
    border: none !important; 
    color: white !important; 
    border-radius: 8px !important; 
    font-weight: 700 !important;
    padding: 12px 24px !important;
    transition: all 0.3s ease !important;
    box-shadow: 0 4px 12px rgba(6,78,59,0.3) !important;
}
.stButton > button[kind="primary"]:hover, .stFormSubmitButton > button:hover { 
    background: linear-gradient(135deg, var(--primary-2), var(--gold)) !important; 
    transform: translateY(-2px);
    box-shadow: 0 8px 24px rgba(6,78,59,0.4) !important;
}
div[data-testid="stDataFrame"] { 
    border: 1px solid var(--border) !important; 
    border-radius: 12px !important; 
    overflow: hidden;
    box-shadow: 0 4px 12px rgba(12,74,62,0.05);
}

/* ============================================
   FOOTER ULTRA
   ============================================ */
.footer { 
    background: radial-gradient(ellipse at top left, #0d4438 0%, #022c22 62%), #022c22; 
    color: rgba(255,255,255,.75); 
    margin-top: 70px; 
    padding: 70px 6% 0; 
    position: relative;
    overflow: hidden;
}
.footer::before {
    content: '';
    position: absolute;
    top: 0; left: 0; right: 0;
    height: 3px;
    background: linear-gradient(90deg, transparent, var(--gold), transparent);
}
.footer::after {
    content: '';
    position: absolute;
    top: 20%; right: -10%;
    width: 500px; height: 500px;
    background: radial-gradient(circle, rgba(213,165,43,0.08) 0%, transparent 70%);
    border-radius: 50%;
    pointer-events: none;
}
.footer-container { width: 88%; max-width: 1250px; margin: 0 auto; position: relative; z-index: 2; }
.footer-grid { display: grid; grid-template-columns: 1.6fr 1fr 1fr 1fr; gap: 45px; padding-bottom: 50px; }
.footer-column h4 { 
    color: #fff; 
    font-size: 14px; 
    font-weight: 800; 
    margin: 0 0 20px;
    position: relative;
    padding-bottom: 12px;
    letter-spacing: 0.3px;
}
.footer-column h4::after {
    content: '';
    position: absolute;
    bottom: 0; left: 0;
    width: 30px;
    height: 2px;
    background: var(--gold);
}
.footer-column a { 
    display: block; 
    color: rgba(255,255,255,.62); 
    font-size: 12.5px; 
    line-height: 2.2; 
    text-decoration: none; 
    transition: all .25s ease;
    padding-left: 0;
}
.footer-column a:hover { color: var(--gold-light); padding-left: 8px; }
.footer-column p { color: rgba(255,255,255,.62); font-size: 12.5px; line-height: 1.9; margin: 0 0 10px; }
.footer-brand { display: flex; align-items: center; gap: 14px; margin-bottom: 22px; }
.footer-logo { 
    width: 55px; height: 55px; 
    border-radius: 10px; 
    flex-shrink: 0; 
    background: #fff; 
    display: flex; 
    align-items: center; 
    justify-content: center; 
    overflow: hidden;
    box-shadow: 0 8px 20px rgba(0,0,0,0.3);
}
.footer-logo img { width: 100%; height: 100%; object-fit: contain; }
.footer-brand-name { color: #fff; font-family: 'Plus Jakarta Sans', sans-serif; font-size: 15px; font-weight: 800; letter-spacing: 0.3px; }
.footer-brand-subtitle { color: rgba(255,255,255,.5); font-size: 10px; letter-spacing: .8px; margin-top: 3px; }
.footer-description { color: rgba(255,255,255,.58); font-size: 12.5px; line-height: 1.9; max-width: 360px; margin: 0 0 24px; }
.footer-social { display: flex; gap: 10px; }
.footer-social-item { 
    width: 40px; height: 40px; 
    border-radius: 10px; 
    background: rgba(255,255,255,.08); 
    border: 1px solid rgba(255,255,255,.14); 
    color: rgba(255,255,255,.85); 
    display: flex; 
    align-items: center; 
    justify-content: center; 
    font-size: 15px; 
    transition: all .3s ease; 
    text-decoration: none;
}
.footer-social-item:hover { 
    background: linear-gradient(135deg, var(--gold), #c1961f); 
    border-color: var(--gold); 
    color: #fff;
    transform: translateY(-4px) scale(1.08);
    box-shadow: 0 8px 20px rgba(213,165,43,0.4);
}
.footer-divider { border-top: 1px solid rgba(255,255,255,.1); }
.footer-bottom { padding: 22px 0 28px; display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 10px; color: rgba(255,255,255,.42); font-size: 11.5px; }

/* ============================================
   FLOATING WIDGETS
   ============================================ */
.floating-widgets {
    position: fixed;
    bottom: 30px;
    right: 30px;
    display: flex;
    flex-direction: column;
    gap: 12px;
    z-index: 9999;
}
.float-btn {
    width: 56px;
    height: 56px;
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 22px;
    cursor: pointer;
    transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
    box-shadow: 0 8px 24px rgba(0,0,0,0.2);
    border: none;
    text-decoration: none;
    position: relative;
}
.float-btn:hover { transform: scale(1.15) translateY(-4px); }
.float-btn.whatsapp { 
    background: linear-gradient(135deg, #25D366, #128C7E); 
    color: #fff;
}
.float-btn.whatsapp:hover { box-shadow: 0 12px 30px rgba(37,211,102,0.5); }
.float-btn.chat { 
    background: linear-gradient(135deg, var(--primary), var(--primary-2)); 
    color: #fff;
}
.float-btn.chat:hover { box-shadow: 0 12px 30px rgba(6,78,59,0.5); }
.float-btn.top { 
    background: linear-gradient(135deg, var(--gold), #c1961f); 
    color: #fff;
    font-size: 20px;
}
.float-btn.top:hover { box-shadow: 0 12px 30px rgba(213,165,43,0.5); }
.float-btn::after {
    content: attr(data-tooltip);
    position: absolute;
    right: 70px;
    top: 50%;
    transform: translateY(-50%) scale(0.8);
    background: rgba(0,0,0,0.85);
    color: #fff;
    padding: 8px 14px;
    border-radius: 8px;
    font-size: 12px;
    font-weight: 600;
    white-space: nowrap;
    opacity: 0;
    pointer-events: none;
    transition: all 0.3s ease;
}
.float-btn:hover::after { opacity: 1; transform: translateY(-50%) scale(1); }

/* Chat Box */
.chat-box {
    position: fixed;
    bottom: 100px;
    right: 30px;
    width: 340px;
    background: #fff;
    border-radius: 16px;
    box-shadow: 0 20px 60px rgba(0,0,0,0.25);
    overflow: hidden;
    z-index: 9998;
    animation: slideUp 0.4s ease;
    border: 1px solid var(--border);
}
@keyframes slideUp {
    from { opacity: 0; transform: translateY(20px); }
    to { opacity: 1; transform: translateY(0); }
}
.chat-header {
    background: linear-gradient(135deg, var(--primary), var(--primary-2));
    color: #fff;
    padding: 16px 20px;
    font-weight: 700;
    display: flex;
    justify-content: space-between;
    align-items: center;
}
.chat-body { padding: 20px; max-height: 300px; overflow-y: auto; }
.chat-message {
    background: var(--primary-3);
    padding: 12px 16px;
    border-radius: 12px;
    margin-bottom: 12px;
    font-size: 13px;
    color: var(--text);
    line-height: 1.5;
}
.chat-message.user {
    background: linear-gradient(135deg, var(--gold), #c1961f);
    color: #fff;
    margin-left: 40px;
}

/* ============================================
   SEARCH BAR
   ============================================ */
.search-wrap {
    background: linear-gradient(135deg, #f0fdf4, #dcfce7);
    padding: 20px 6%;
    border-bottom: 1px solid var(--border);
}
.search-inner { width: 88%; max-width: 1250px; margin: 0 auto; display: flex; gap: 12px; align-items: center; }
.search-icon { font-size: 20px; }

/* ============================================
   DARK MODE (via CSS class toggle)
   ============================================ */
.dark-mode .stApp { background: #0a1f1a !important; }
.dark-mode .brand-wrap { background: #0f2a24 !important; }
.dark-mode .brand-title { color: #e8f0ed !important; }
.dark-mode .news-card, .dark-mode .warta-item, .dark-mode .service-box, 
.dark-mode .agenda-wrap { background: #0f2a24 !important; border-color: #1e3d34 !important; }
.dark-mode .section-title { color: #e8f0ed !important; }

/* ============================================
   RESPONSIVE
   ============================================ */
@media (max-width: 850px) {
    .footer-grid { grid-template-columns: 1fr 1fr; row-gap: 35px; }
    .footer-bottom { flex-direction: column; text-align: center; }
    .news-grid { grid-template-columns: 1fr; }
    .floating-stats { position: static; padding: 20px 0; justify-content: center; margin-top: 20px; }
    .floating-stat { min-width: 80px; padding: 12px; }
    .floating-stat-num { font-size: 20px; }
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
<div class="govbar">
    <div class="govbar-left">
        <span>🇮🇩 Portal Informasi Pemerintahan Daerah</span>
        <span>|</span>
        <strong>DPRK ACEH JAYA</strong>
    </div>
    <div class="govbar-right">
        <span class="govbar-clock">🕐 {now.strftime('%H:%M:%S')} WIB</span>
        <a href="?page=kontak">Hubungi Kami</a>
        <span>|</span>
        <a href="?page=jdih">PPID</a>
    </div>
</div>
""",
    unsafe_allow_html=True,
)

# =========================================================
# BRAND + LIVE INDICATORS
# =========================================================
st.markdown(
    f"""
<div class="brand-wrap">
    <div class="brand-inner">
        <div class="brand">
            <div class="brand-logo">
                <img src="{LOGO_URL}" alt="Logo DPRK Aceh Jaya"
                     onerror="this.onerror=null;this.src='data:image/svg+xml,<svg xmlns=%22http://www.w3.org/2000/svg%22 viewBox=%220 0 100 100%22><text y=%22.9em%22 font-size=%2290%22>🏛️</text></svg>'">
            </div>
            <div>
                <div class="brand-title">Dewan Perwakilan Rakyat<br>Kabupaten Aceh Jaya</div>
                <div class="brand-subtitle">PORTAL INFORMASI PUBLIK DAN ASPIRASI MASYARAKAT</div>
            </div>
        </div>
        <div class="live-indicators">
            <div class="live-badge">
                <span class="live-dot"></span>
                <span>LIVE • SEDANG SIDANG</span>
            </div>
            <div class="live-badge" style="background: linear-gradient(135deg, #fffbeb, #fef3c7); border-color: #fcd34d; color: #92400e;">
                <span>👁️</span>
                <span>{st.session_state.visitor_count:,} Kunjungan</span>
            </div>
        </div>
    </div>
</div>
""",
    unsafe_allow_html=True,
)

# =========================================================
# NAVIGATION
# =========================================================
st.markdown('<div class="nav-wrap"><div class="nav-inner">', unsafe_allow_html=True)
nav_cols = st.columns(7)
nav_keys = list(PAGES.keys())

for i, key in enumerate(nav_keys):
    with nav_cols[i]:
        active_class = "nav-button-active" if st.session_state.page == PAGES[key] else "nav-button"
        st.markdown(f'<div class="{active_class}">', unsafe_allow_html=True)
        if st.button(PAGES[key].replace(" & ", " • "), key=f"nav_{key}", use_container_width=True):
            st.session_state.page = PAGES[key]
            st.rerun()
        st.markdown("</div>", unsafe_allow_html=True)

st.markdown("</div></div>", unsafe_allow_html=True)

# =========================================================
# RUNNING TEXT
# =========================================================
st.markdown(
    """
<div class="running-text-wrap">
    <div class="running-text">
        📢 Selamat Datang di Portal Resmi DPRK Aceh Jaya &nbsp;&nbsp;|&nbsp;&nbsp;
        📅 Rapat Paripurna Pembahasan KUA-PPAS 2027 akan dilaksanakan pada 18 September 2026 &nbsp;&nbsp;|&nbsp;&nbsp;
        📢 Layanan Pengaduan Masyarakat kini dapat diakses melalui menu Layanan & Pengaduan &nbsp;&nbsp;|&nbsp;&nbsp;
        🏆 DPRK Aceh Jaya Raih Penghargaan Keterbukaan Informasi Publik 2026 &nbsp;&nbsp;|&nbsp;&nbsp;
        Mari wujudkan transparansi dan akuntabilitas pemerintahan daerah bersama DPRK Aceh Jaya.
    </div>
</div>
""",
    unsafe_allow_html=True,
)

# =========================================================
# HALAMAN: BERANDA
# =========================================================
if st.session_state.page == "Beranda":
    st.markdown(
        f"""
    <section class="hero">
        <div class="hero-content">
            <div class="hero-kicker">✨ PORTAL RESMI DPRK ACEH JAYA</div>
            <h1>Suara Masyarakat,<br><span>Bagian dari Pembangunan</span><br>Aceh Jaya</h1>
            <p>Akses informasi kegiatan DPRK, produk hukum, agenda persidangan, layanan publik, serta sampaikan aspirasi masyarakat melalui satu portal informasi yang mudah diakses, transparan, dan akuntabel.</p>
            <div class="hero-buttons">
                <a class="hero-btn" href="?page=layanan">📢 Sampaikan Aspirasi</a>
                <a class="hero-btn secondary" href="?page=berita">📰 Lihat Berita</a>
            </div>
        </div>
        <div class="floating-stats">
            <div class="floating-stat">
                <div class="floating-stat-num">20</div>
                <div class="floating-stat-label">Anggota</div>
            </div>
            <div class="floating-stat">
                <div class="floating-stat-num">4</div>
                <div class="floating-stat-label">Komisi</div>
            </div>
            <div class="floating-stat">
                <div class="floating-stat-num">120+</div>
                <div class="floating-stat-label">Qanun</div>
            </div>
        </div>
    </section>
    """,
        unsafe_allow_html=True,
    )

    # Layanan Publik
    st.markdown('<div class="content">', unsafe_allow_html=True)
    st.markdown(
        """
    <section class="section">
        <div class="section-head">
            <div>
                <div class="section-kicker">Akses Cepat</div>
                <h2 class="section-title">Layanan Publik</h2>
                <div class="section-desc">Akses layanan dan informasi DPRK Aceh Jaya secara lebih mudah.</div>
            </div>
        </div>
    """,
        unsafe_allow_html=True,
    )

    services = [
        ("📢", "Pengaduan Masyarakat", "Sampaikan aspirasi, keluhan, dan laporan masyarakat.", "layanan"),
        ("📜", "JDIH", "Akses produk hukum dan dokumen peraturan daerah.", "jdih"),
        ("📅", "Agenda DPRK", "Lihat agenda rapat, sidang, dan kegiatan DPRK.", "berita"),
        ("📊", "Transparansi", "Informasi publik dan dokumen penyelenggaraan pemerintahan.", "jdih"),
        ("📂", "Dokumen Publik", "Dokumen yang dapat diakses oleh masyarakat.", "jdih"),
        ("🔗", "E-LHKPN", "Pelaporan harta kekayaan penyelenggara negara.", "https://elhpkpn.kpk.go.id/"),
    ]

    service_cols = st.columns(6)
    icon_accents = ["", "accent-gold", "accent-blue"]
    for i, (icon, title, desc, target) in enumerate(services):
        with service_cols[i]:
            accent = icon_accents[i % 3]
            is_external = target.startswith("http")
            link_target = 'target="_blank" rel="noopener noreferrer"' if is_external else ""
            href_val = target if is_external else f"?page={target}"
            st.markdown(
                f"""
            <a href="{href_val}" {link_target} style="text-decoration: none; color: inherit; display: block;">
                <div class="service-box">
                    <div class="service-icon {accent}">{icon}</div>
                    <div class="service-title">{title}</div>
                    <div class="service-desc">{desc}</div>
                </div>
            </a>
            """,
                unsafe_allow_html=True,
            )
    st.markdown("</section>", unsafe_allow_html=True)

    # Statistik Dashboard
    st.markdown(
        """
    <section class="section">
        <div class="section-head">
            <div>
                <div class="section-kicker">Data & Statistik</div>
                <h2 class="section-title">Dashboard Kinerja DPRK</h2>
                <div class="section-desc">Visualisasi data kegiatan dan kinerja DPRK Aceh Jaya periode 2026.</div>
            </div>
        </div>
    </section>
    """,
        unsafe_allow_html=True,
    )

    stat_col1, stat_col2 = st.columns(2)
    with stat_col1:
        fig1 = px.line(
            STATS_DATA, x="Bulan", y="Rapat",
            title="📅 Jumlah Rapat per Bulan",
            markers=True,
            color_discrete_sequence=["#064e3b"],
        )
        fig1.update_layout(
            plot_bgcolor="rgba(0,0,0,0)",
            paper_bgcolor="rgba(0,0,0,0)",
            font=dict(family="Inter", size=12, color="#273936"),
            title_font=dict(size=15, family="Plus Jakarta Sans", color="#183d35"),
            margin=dict(l=20, r=20, t=50, b=20),
            height=320,
        )
        fig1.update_traces(line=dict(width=3), marker=dict(size=10, line=dict(width=2, color="#fff")))
        st.plotly_chart(fig1, use_container_width=True)

    with stat_col2:
        fig2 = px.pie(
            ANGGARAN_DATA, values="Anggaran", names="Kategori",
            title="💰 Alokasi Anggaran 2026 (%)",
            color_discrete_sequence=["#064e3b", "#d5a52b", "#0f6b58", "#fcd34d", "#7a8884"],
            hole=0.5,
        )
        fig2.update_layout(
            plot_bgcolor="rgba(0,0,0,0)",
            paper_bgcolor="rgba(0,0,0,0)",
            font=dict(family="Inter", size=12, color="#273936"),
            title_font=dict(size=15, family="Plus Jakarta Sans", color="#183d35"),
            margin=dict(l=20, r=20, t=50, b=20),
            height=320,
        )
        st.plotly_chart(fig2, use_container_width=True)

    # Info Strip
    st.markdown('</div><div class="info-strip"><div class="info-inner">', unsafe_allow_html=True)
    stat_cols = st.columns(4)
    stats = [("2024–2029", "Masa Jabatan"), ("3", "Pimpinan DPRK"), ("4", "Komisi DPRK"), ("120+", "Produk Hukum")]
    for i, (number, label) in enumerate(stats):
        with stat_cols[i]:
            divider_class = "has-divider" if i < len(stats) - 1 else ""
            st.markdown(
                f"""
            <div class="info-item {divider_class}">
                <div class="info-number">{number}</div>
                <div class="info-label">{label}</div>
            </div>
            """,
                unsafe_allow_html=True,
            )
    st.markdown("</div></div><div class='content'>", unsafe_allow_html=True)

    # Warta & Agenda
    st.markdown('<section class="section">', unsafe_allow_html=True)
    st.markdown(
        """
    <div class="section-head">
        <div>
            <div class="section-kicker">Informasi Terbaru</div>
            <h2 class="section-title">WARTA DPRK & Agenda</h2>
        </div>
    </div>
    """,
        unsafe_allow_html=True,
    )

    col_warta, col_agenda = st.columns([2, 1])

    with col_warta:
        st.markdown('<div class="section-kicker" style="margin-bottom: 15px;">WARTA DPRK</div>', unsafe_allow_html=True)
        st.markdown('<div class="warta-list">', unsafe_allow_html=True)
        for item in WARTA_DPRK[:3]:
            st.markdown(
                f"""
            <div class="warta-item">
                <span class="date">📅 {item['date']}</span>
                <h3>{item['title']}</h3>
                <p>{item['desc']}</p>
            </div>
            """,
                unsafe_allow_html=True,
            )
        st.markdown('</div>', unsafe_allow_html=True)

    with col_agenda:
        st.markdown(
            """
        <div class="agenda-wrap">
            <div class="section-kicker">Jadwal</div>
            <div style="font-family:'Plus Jakarta Sans';font-size:18px;font-weight:800;color:#183d35;margin-bottom:22px;">AGENDA TERKINI</div>
        """,
            unsafe_allow_html=True,
        )
        for item in AGENDA_TERKINI:
            st.markdown(
                f"""
            <div class="agenda-item">
                <div class="agenda-date-badge">📅 {item['tanggal']}</div>
                <div class="agenda-title">{item['judul']}</div>
                <div class="agenda-desc">{item['desc']}</div>
            </div>
            """,
                unsafe_allow_html=True,
            )
        st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("</section>", unsafe_allow_html=True)

    # Kesekretariatan
    st.markdown(
        """
    <section class="section" style="background: #fff; border-radius: 14px; padding: 35px; border: 1px solid var(--border);">
        <div class="section-kicker" style="margin-bottom: 20px;">KESEKRETARIATAN</div>
        <div class="warta-list">
    """,
        unsafe_allow_html=True,
    )
    for item in KESEKRETARIATAN:
        st.markdown(
            f"""
        <div class="warta-item">
            <span class="date">📅 {item['date']}</span>
            <h3>{item['title']}</h3>
            <p>{item['desc']}</p>
        </div>
        """,
            unsafe_allow_html=True,
        )
    st.markdown("</div></section></div>", unsafe_allow_html=True)

# =========================================================
# HALAMAN: PROFIL & PIMPINAN
# =========================================================
elif st.session_state.page == "Profil & Pimpinan":
    st.markdown('<div class="content">', unsafe_allow_html=True)
    st.markdown(
        """
    <section class="section">
        <div class="section-kicker">Tentang DPRK</div>
        <h2 class="section-title">Profil DPRK Aceh Jaya</h2>
        <p class="section-desc">Dewan Perwakilan Rakyat Kabupaten Aceh Jaya sebagai unsur penyelenggara pemerintahan daerah bersama pemerintah daerah menjalankan fungsi legislasi, anggaran, dan pengawasan sesuai ketentuan peraturan perundang-undangan.</p>
    </section>
    """,
        unsafe_allow_html=True,
    )

    tab1, tab2 = st.tabs(["🏛️ Pimpinan dan Anggota DPRK", "🏢 Pejabat Sekretariat DPRK"])

    with tab1:
        st.markdown('<div style="display: grid; grid-template-columns: repeat(auto-fill, minmax(300px, 1fr)); gap: 16px; margin-top: 24px;">', unsafe_allow_html=True)
        for nama, jabatan in PIMPINAN_DAN_ANGGOTA:
            st.markdown(
                f"""
            <div style="background: #fff; border: 1px solid var(--border); border-radius: 12px; padding: 20px; text-align: center; transition: all 0.3s ease; border-top: 3px solid var(--primary);">
                <div style="font-weight: 800; color: var(--primary); font-size: 14px; margin-bottom: 6px; font-family: 'Plus Jakarta Sans';">{nama}</div>
                <div style="color: var(--muted); font-size: 11px; font-weight: 600; letter-spacing: 0.3px;">{jabatan}</div>
            </div>
            """,
                unsafe_allow_html=True,
            )
        st.markdown('</div>', unsafe_allow_html=True)

    with tab2:
        st.markdown('<div style="display: grid; grid-template-columns: repeat(auto-fill, minmax(350px, 1fr)); gap: 16px; margin-top: 24px;">', unsafe_allow_html=True)
        for nama, jabatan in PEJABAT_SEKRETARIAT:
            st.markdown(
                f"""
            <div style="background: #fff; border: 1px solid var(--border); border-radius: 12px; padding: 20px; text-align: center; transition: all 0.3s ease; border-top: 3px solid var(--gold);">
                <div style="font-weight: 800; color: var(--primary); font-size: 14px; margin-bottom: 6px; font-family: 'Plus Jakarta Sans';">{nama}</div>
                <div style="color: var(--muted); font-size: 12px; font-weight: 600;">{jabatan}</div>
            </div>
            """,
                unsafe_allow_html=True,
            )
        st.markdown('</div>', unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True)

# =========================================================
# HALAMAN: BERITA & AGENDA
# =========================================================
elif st.session_state.page == "Berita & Agenda":
    st.markdown('<div class="content">', unsafe_allow_html=True)
    st.markdown(
        """
    <section class="section">
        <div class="section-kicker">Publikasi</div>
        <h2 class="section-title">WARTA DPRK</h2>
        <p class="section-desc">Informasi kegiatan, rapat, agenda, dan aktivitas DPRK Aceh Jaya.</p>
    </section>
    """,
        unsafe_allow_html=True,
    )

    # Filter kategori
    categories = ["Semua"] + list(set(item["kategori"] for item in WARTA_DPRK))
    filter_col1, filter_col2, _ = st.columns([1.5, 1.5, 4])
    with filter_col1:
        selected = st.selectbox("🔍 Filter Kategori", categories, key="filter_berita")
    with filter_col2:
        search = st.text_input("🔎 Cari Berita", placeholder="Kata kunci...")

    filtered = WARTA_DPRK
    if selected != "Semua":
        filtered = [item for item in filtered if item["kategori"] == selected]
    if search:
        filtered = [item for item in filtered if search.lower() in item["title"].lower() or search.lower() in item["desc"].lower()]

    st.markdown('<div class="news-grid" style="margin-top: 30px;">', unsafe_allow_html=True)
    for item in filtered:
        st.markdown(
            f"""
        <div class="news-card">
            <div class="news-card-img-wrap">
                <span class="news-card-category">{item['kategori']}</span>
                <span class="news-card-views">👁️ {item['views']}</span>
                <img class="news-card-img" src="{item['image']}">
            </div>
            <div class="news-card-body">
                <h3>{item['title']}</h3>
                <p>{item['desc'][:130]}...</p>
                <div class="news-date">📅 {item['date']}</div>
            </div>
        </div>
        """,
            unsafe_allow_html=True,
        )
    st.markdown('</div>', unsafe_allow_html=True)

    if not filtered:
        st.info("Tidak ada berita yang sesuai dengan pencarian Anda.")

    st.markdown(
        """
    <section class="section">
        <div class="section-kicker" style="margin-top: 40px;">Agenda</div>
        <h2 class="section-title" style="font-size:24px;margin-bottom:20px;">AGENDA TERKINI</h2>
        <div class="agenda-wrap">
    """,
        unsafe_allow_html=True,
    )
    for item in AGENDA_TERKINI:
        st.markdown(
            f"""
        <div class="agenda-item">
            <div class="agenda-date-badge">📅 {item['tanggal']}</div>
            <div class="agenda-title">{item['judul']}</div>
            <div class="agenda-desc">{item['desc']}</div>
        </div>
        """,
            unsafe_allow_html=True,
        )
    st.markdown("</div></section></div>", unsafe_allow_html=True)

# =========================================================
# HALAMAN: GALERI
# =========================================================
elif st.session_state.page == "Galeri Foto & Video":
    st.markdown('<div class="content">', unsafe_allow_html=True)
    st.markdown(
        """
    <section class="section">
        <div class="section-kicker">Dokumentasi</div>
        <h2 class="section-title">Galeri Foto & Video</h2>
        <p class="section-desc">Dokumentasi kegiatan, rapat, dan aktivitas DPRK Aceh Jaya.</p>
    </section>
    """,
        unsafe_allow_html=True,
    )

    st.markdown('<div class="news-grid">', unsafe_allow_html=True)
    gallery_items = [
        ("Rapat Paripurna", "https://images.unsplash.com/photo-1529107386315-e1a2ed48a620?auto=format&fit=crop&w=600&q=80"),
        ("Kunjungan Kerja", "https://images.unsplash.com/photo-1577962917302-cd874c4e31d2?auto=format&fit=crop&w=600&q=80"),
        ("Sosialisasi Qanun", "https://images.unsplash.com/photo-1556761175-b413da4baf72?auto=format&fit=crop&w=600&q=80"),
        ("Penanaman Mangrove", "https://images.unsplash.com/photo-1589578527966-fdac0f44566c?auto=format&fit=crop&w=600&q=80"),
        ("Rapat Komisi", "https://images.unsplash.com/photo-1517486808906-6ca8b3f04846?auto=format&fit=crop&w=600&q=80"),
        ("Bimbingan Teknis", "https://images.unsplash.com/photo-1523240795612-9a054b0db644?auto=format&fit=crop&w=600&q=80"),
    ]
    for title, img in gallery_items:
        st.markdown(
            f"""
        <div class="news-card">
            <div class="news-card-img-wrap">
                <img class="news-card-img" src="{img}" style="height: 240px;">
            </div>
            <div class="news-card-body" style="justify-content: center; align-items: center; text-align: center; padding: 18px;">
                <h3 style="margin: 0; font-size: 15px;">{title}</h3>
            </div>
        </div>
        """,
            unsafe_allow_html=True,
        )
    st.markdown('</div>', unsafe_allow_html=True)

    # Video Section
    st.markdown(
        """
    <section class="section">
        <div class="section-kicker">Video</div>
        <h2 class="section-title" style="font-size: 24px; margin-bottom: 20px;">Video Dokumentasi</h2>
        <div style="background: #000; border-radius: 14px; overflow: hidden; aspect-ratio: 16/9; display: flex; align-items: center; justify-content: center; color: #fff; font-family: 'Plus Jakarta Sans';">
            <div style="text-align: center;">
                <div style="font-size: 60px; margin-bottom: 12px;">🎬</div>
                <div style="font-size: 18px; font-weight: 700;">Video Profil DPRK Aceh Jaya</div>
                <div style="font-size: 12px; opacity: 0.7; margin-top: 8px;">Embed YouTube di sini</div>
            </div>
        </div>
    </section>
    </div>
    """,
        unsafe_allow_html=True,
    )

# =========================================================
# HALAMAN: LAYANAN & PENGADUAN
# =========================================================
elif st.session_state.page == "Layanan & Pengaduan":
    st.markdown('<div class="content">', unsafe_allow_html=True)
    st.markdown(
        """
    <section class="section">
        <div class="section-kicker">Pelayanan Masyarakat</div>
        <h2 class="section-title">Layanan Aspirasi & Pengaduan</h2>
        <p class="section-desc">Sampaikan aspirasi, laporan, atau pengaduan kepada DPRK Aceh Jaya.</p>
    </section>
    """,
        unsafe_allow_html=True,
    )

    col1, col2 = st.columns([1.75, 1])

    with col1:
        st.markdown(
            """
        <div class="section-kicker">Formulir</div>
        <h3 style="color:#183d35;font-family:'Plus Jakarta Sans';font-size:22px;margin-bottom:18px;">Sampaikan Aspirasi Anda</h3>
        """,
            unsafe_allow_html=True,
        )

        with st.form("form_aduan"):
            c1, c2 = st.columns(2)
            with c1:
                nama = st.text_input("Nama Lengkap *", placeholder="Masukkan nama lengkap")
                nik = st.text_input("NIK (Opsional)", placeholder="16 digit")
            with c2:
                kategori = st.selectbox(
                    "Kategori Pengaduan *",
                    ["Pengaduan Masyarakat", "Infrastruktur & Jalan", "Pelayanan Publik", "Legislasi & Qanun", "Lingkungan & Bencana", "Lainnya"],
                )
                prioritas = st.selectbox("Tingkat Prioritas", ["Normal", "Penting", "Mendesak"])
            lokasi = st.text_input("Lokasi Kejadian (Opsional)", placeholder="Desa / Kecamatan / lokasi")
            isi = st.text_area("Isi Laporan / Aspirasi *", height=150, placeholder="Jelaskan aspirasi atau laporan secara jelas...")
            lampiran = st.file_uploader("📎 Lampiran (Foto/Dokumen)", type=["jpg", "jpeg", "png", "pdf"])

            submitted = st.form_submit_button("🚀 Kirim Aspirasi", type="primary", use_container_width=True)

            if submitted:
                if nama.strip() and isi.strip():
                    nomor = datetime.now().strftime("%Y%m%d%H%M%S")
                    st.success(f"✅ Laporan berhasil dicatat. Nomor tiket: **ADU-{nomor}**")
                    st.info(f"📋 Kategori: {kategori} | Prioritas: {prioritas}")
                    st.info("💾 Simpan nomor tiket untuk keperluan pengecekan tindak lanjut.")
                else:
                    st.error("⚠️ Mohon lengkapi Nama Lengkap dan Isi Laporan.")

    with col2:
        st.markdown(
            """
        <div class="agenda-wrap">
            <div class="section-kicker">Kontak</div>
            <h3 style="color:#183d35;font-family:'Plus Jakarta Sans';font-size:20px;margin-top:0;">Hubungi Kami</h3>
            <p style="font-size:12.5px;color:#71817d;line-height:1.9;">
                <strong>📞 Telepon</strong><br>(0655) 12345
            </p>
            <p style="font-size:12.5px;color:#71817d;line-height:1.9;">
                <strong>✉️ Email</strong><br>sekretariat@dprk.acehjaya.go.id
            </p>
            <p style="font-size:12.5px;color:#71817d;line-height:1.9;">
                <strong>📍 Alamat</strong><br>Jl. Merdeka No. 01, Calang, Aceh Jaya
            </p>
            <hr style="border:none;border-top:1px solid #edf1ef;">
            <p style="font-size:11.5px;color:#71817d;line-height:1.8;">Jam layanan: Senin–Jumat, 08.00–16.00 WIB.</p>
            <div style="margin-top: 20px; padding: 16px; background: linear-gradient(135deg, #f0fdf4, #dcfce7); border-radius: 10px; border: 1px solid #86efac;">
                <div style="font-size: 12px; font-weight: 700; color: #166534; margin-bottom: 6px;">⚡ Respon Cepat</div>
                <div style="font-size: 11px; color: #166534; line-height: 1.6;">Pengaduan akan ditindaklanjuti maksimal 3 hari kerja.</div>
            </div>
        </div>
        """,
            unsafe_allow_html=True,
        )

    # Rating
    st.markdown(
        """
    <div style="margin-top: 40px; background: #fff; border: 1px solid var(--border); border-radius: 14px; padding: 28px; text-align: center;">
        <div class="section-kicker" style="justify-content: center;">Feedback</div>
        <h3 style="font-family: 'Plus Jakarta Sans'; color: #183d35; font-size: 20px; margin: 10px 0;">Bagaimana Pengalaman Anda Menggunakan Portal Ini?</h3>
        <p style="color: var(--muted); font-size: 13px; margin-bottom: 20px;">Beri rating untuk membantu kami meningkatkan kualitas layanan.</p>
    """,
        unsafe_allow_html=True,
    )
    st.markdown("</div></div>", unsafe_allow_html=True)

# =========================================================
# HALAMAN: JDIH & TRANSPARANSI
# =========================================================
elif st.session_state.page == "JDIH & Transparansi":
    st.markdown('<div class="content">', unsafe_allow_html=True)
    st.markdown(
        """
    <section class="section">
        <div class="section-kicker">Dokumentasi Hukum</div>
        <h2 class="section-title">JDIH & Transparansi</h2>
        <p class="section-desc">Akses daftar produk hukum dan informasi publik DPRK Aceh Jaya.</p>
    </section>
    """,
        unsafe_allow_html=True,
    )

    info_cols = st.columns(4)
    cards = [
        ("⚖️", "Produk Hukum", "Qanun dan dokumen hukum daerah."),
        ("📊", "Transparansi", "Informasi penyelenggaraan pemerintahan."),
        ("📂", "Dokumen Publik", "Dokumen yang dapat diakses masyarakat."),
        ("📑", "Informasi Berkala", "Informasi yang diterbitkan secara berkala."),
    ]

    icon_accents = ["", "accent-gold", "accent-blue", "accent-gold"]
    for i, (icon, title, desc) in enumerate(cards):
        with info_cols[i]:
            st.markdown(
                f"""
            <div class="service-box" style="text-align:left;">
                <div class="service-icon {icon_accents[i]}" style="margin:0 0 15px;">{icon}</div>
                <div class="service-title">{title}</div>
                <div class="service-desc">{desc}</div>
            </div>
            """,
                unsafe_allow_html=True,
            )

    st.markdown(
        """
    <div style="margin-top:50px;">
        <div class="section-kicker">Database</div>
        <h2 class="section-title" style="font-size:24px;margin-bottom:20px;">Produk Hukum Daerah</h2>
    </div>
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
    st.markdown('<div class="content">', unsafe_allow_html=True)
    st.markdown(
        """
    <section class="section">
        <div class="section-kicker">Informasi Kontak</div>
        <h2 class="section-title">Hubungi DPRK Aceh Jaya</h2>
        <p class="section-desc">Gunakan informasi berikut untuk mendapatkan layanan dan informasi dari Sekretariat DPRK Aceh Jaya.</p>
    </section>
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
            <div class="service-box" style="min-height:190px;">
                <div class="service-icon">{icon}</div>
                <div class="service-title">{title}</div>
                <div class="service-desc" style="font-size:12.5px;">{value}</div>
            </div>
            """,
                unsafe_allow_html=True,
            )

    st.markdown(
        """
    <div style="margin-top:40px;background:#fff;border:1px solid #e1e8e5;border-radius:14px;padding:32px;box-shadow: 0 8px 24px rgba(12,74,62,0.06);">
        <div class="section-kicker">Lokasi Kantor</div>
        <h3 style="font-family:'Plus Jakarta Sans';color:#183d35;font-size:22px;margin-bottom:18px;">Peta & Lokasi</h3>
        <div style="width:100%;height:340px;border-radius:12px;overflow:hidden;border:1px solid #e1e8e5;">
            <iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3988.5!2d95.39!3d4.71!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x30403e5f3a0b0b0b%3A0x0!2sCalang%2C%20Aceh%20Jaya%20Regency%2C%20Aceh!5e0!3m2!1sen!2sid!4v1600000000000" width="100%" height="100%" style="border:0;" allowfullscreen="" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe>
        </div>
        <p style="font-size:12.5px;color:#71817d;line-height:1.9;margin-top:18px;">
            <strong>📍 Alamat Lengkap:</strong> Jl. Merdeka No. 01, Calang, Kabupaten Aceh Jaya, Aceh.
        </p>
        <hr style="border:none;border-top:1px solid #edf1ef;margin:22px 0;">
        <div class="section-kicker">Sekretariat</div>
        <h3 style="font-family:'Plus Jakarta Sans';color:#183d35;font-size:21px;margin-bottom:12px;">Jam Pelayanan</h3>
        <p style="font-size:12.5px;color:#71817d;line-height:1.9;">
            Senin–Kamis: 08.00–16.30 WIB<br>
            Jumat: 08.00–16.30 WIB<br>
            Sabtu–Minggu: Libur
        </p>
    </div>
    """,
        unsafe_allow_html=True,
    )
    st.markdown("</div>", unsafe_allow_html=True)

# =========================================================
# FLOATING WIDGETS
# =========================================================
st.markdown(
    """
<div class="floating-widgets">
    <a href="https://wa.me/6281234567890" target="_blank" class="float-btn whatsapp" data-tooltip="WhatsApp">💬</a>
    <button class="float-btn chat" data-tooltip="Live Chat" onclick="alert('Fitur chat akan segera hadir!')">💌</button>
    <a href="#" class="float-btn top" data-tooltip="Ke Atas">⬆️</a>
</div>
""",
    unsafe_allow_html=True,
)

# =========================================================
# FOOTER
# =========================================================
st.markdown(
    f"""
<div class="footer">
<div class="footer-container">
<div class="footer-grid">

<div class="footer-column">
<div class="footer-brand">
<div class="footer-logo">
    <img src="{LOGO_URL}" alt="Logo DPRK Aceh Jaya"
         onerror="this.onerror=null;this.src='data:image/svg+xml,<svg xmlns=%22http://www.w3.org/2000/svg%22 viewBox=%220 0 100 100%22><text y=%22.9em%22 font-size=%2290%22>🏛️</text></svg>'">
</div>
<div>
<div class="footer-brand-name">DPRK ACEH JAYA</div>
<div class="footer-brand-subtitle">PORTAL INFORMASI PUBLIK</div>
</div>
</div>
<p class="footer-description">
Portal resmi Dewan Perwakilan Rakyat Kabupaten Aceh Jaya
yang menyediakan informasi kelembagaan, berita, agenda,
produk hukum, layanan publik, dan aspirasi masyarakat.
</p>
<div class="footer-social">
<a href="#" class="footer-social-item">f</a>
<a href="#" class="footer-social-item">𝕏</a>
<a href="#" class="footer-social-item">▶</a>
<a href="#" class="footer-social-item">◎</a>
<a href="#" class="footer-social-item">in</a>
</div>
</div>

<div class="footer-column">
<h4>Navigasi</h4>
<a href="?page=beranda">Beranda</a>
<a href="?page=profil">Profil DPRK</a>
<a href="?page=profil">Pimpinan DPRK</a>
<a href="?page=berita">Berita & Agenda</a>
<a href="?page=galeri">Galeri</a>
</div>

<div class="footer-column">
<h4>Layanan Publik</h4>
<a href="?page=layanan">Pengaduan Masyarakat</a>
<a href="?page=kontak">Informasi Publik</a>
<a href="?page=jdih">JDIH</a>
<a href="?page=jdih">Transparansi</a>
<a href="https://elhpkpn.kpk.go.id/" target="_blank" rel="noopener noreferrer">E-LHKPN</a>
</div>

<div class="footer-column">
<h4>Hubungi Kami</h4>
<p>📍 Jl. Merdeka No. 01</p>
<p>Calang, Kabupaten Aceh Jaya</p>
<p>📞 (0655) 12345</p>
<p>✉️ sekretariat@dprk.acehjaya.go.id</p>
<p>🕐 Senin–Jumat, 08.00–16.00 WIB</p>
</div>

</div>

<div class="footer-divider"></div>

<div class="footer-bottom">
<div>© {datetime.now().year} DPRK Aceh Jaya. Seluruh hak cipta dilindungi.</div>
<div>Portal Informasi Publik • Kabupaten Aceh Jaya</div>
</div>

</div>
</div>
""",
    unsafe_allow_html=True,
)

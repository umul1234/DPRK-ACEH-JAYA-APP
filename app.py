import streamlit as st
from datetime import datetime
import pandas as pd
import plotly.express as px
import random

# =========================================================
# KONFIGURASI HALAMAN
# =========================================================
st.set_page_config(
    page_title="DPRK Aceh Jaya | Portal Resmi",
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
if "show_chat" not in st.session_state:
    st.session_state.show_chat = False

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
        "kicker": "PORTAL RESMI DPRK ACEH JAYA",
        "title": "Membangun Aceh Jaya yang Lebih Baik",
        "subtitle": "Bersama mewujudkan transparansi, akuntabilitas, dan pelayanan publik yang prima untuk masyarakat Aceh Jaya.",
    },
    {
        "image": "https://images.unsplash.com/photo-1556761175-b413da4baf72?auto=format&fit=crop&w=1800&q=85",
        "kicker": "SUARA MASYARAKAT",
        "title": "Aspirasi Anda Prioritas Kami",
        "subtitle": "Sampaikan aspirasi, keluhan, dan laporan Anda melalui portal informasi publik DPRK Aceh Jaya.",
    },
    {
        "image": "https://images.unsplash.com/photo-1589578527966-fdac0f44566c?auto=format&fit=crop&w=1800&q=85",
        "kicker": "TRANSPARANSI & AKUNTABILITAS",
        "title": "Keterbukaan Informasi Publik",
        "subtitle": "Akses produk hukum, agenda rapat, dan dokumen publik DPRK Aceh Jaya secara mudah dan cepat.",
    },
]

QUICK_LINKS = [
    {"icon": "📋", "title": "Pengaduan", "desc": "Lapor Online", "page": "layanan", "color": "#0d5e3a"},
    {"icon": "📜", "title": "JDIH", "desc": "Produk Hukum", "page": "jdih", "color": "#c9a227"},
    {"icon": "📅", "title": "Agenda", "desc": "Jadwal Rapat", "page": "berita", "color": "#14734a"},
    {"icon": "📊", "title": "Transparansi", "desc": "Info Publik", "page": "jdih", "color": "#0a2a1b"},
]

# Sambutan Pimpinan
SAMBUTAN = {
    "nama": "MUSLIADI Z, S.E",
    "jabatan": "Ketua DPRK Aceh Jaya",
    "foto": "https://images.unsplash.com/photo-1560250097-0b93528c311a?auto=format&fit=crop&w=400&q=80",
    "assalamualaikum": "Assalamu'alaikum Warahmatullahi Wabarakatuh,",
    "pembuka": "Selamat datang di Portal Resmi Dewan Perwakilan Rakyat Kabupaten (DPRK) Aceh Jaya. Portal ini hadir sebagai gerbang informasi dan komunikasi antara DPRK dengan seluruh masyarakat Aceh Jaya.",
    "quote": "Visi kami adalah mewujudkan DPRK yang responsif, transparan, dan akuntabel dalam menjalankan fungsi legislasi, anggaran, dan pengawasan.",
    "paragraf2": "Melalui portal ini, kami berkomitmen untuk menyediakan akses informasi publik yang mudah, cepat, dan transparan. Kami mengundang seluruh masyarakat untuk berpartisipasi aktif menyampaikan aspirasi dan mengawasi kinerja DPRK.",
    "penutup": "Mari bersama-sama membangun Aceh Jaya yang lebih maju, sejahtera, dan bermartabat.",
    "salam": "Salam hangat,",
}

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
    {"hari": "09", "bulan_tahun": "SEP 2026", "tanggal_full": "Rabu, 09 September 2026", "judul": "Rapat Pleno DPRK Aceh Jaya", "desc": "Rapat Pleno DPRK Aceh Jaya terhadap Rancangan Perubahan KUA-PPAS APBK Aceh Jaya Tahun Anggaran."},
    {"hari": "07", "bulan_tahun": "SEP 2026", "tanggal_full": "Senin, 07 September 2026", "judul": "Rapat Komisi III DPRK Aceh Jaya", "desc": "Rapat Dengar Pendapat Komisi III terkait Realisasi Program dan Kegiatan Pembangunan Jalan dan Jembatan pada Dinas PUPR."},
    {"hari": "01", "bulan_tahun": "SEP 2026", "tanggal_full": "Selasa, 01 September 2026", "judul": "Rapat Badan Musyawarah DPRK Aceh Jaya", "desc": "Rapat Badan Musyawarah tentang Penetapan Jadwal Rapat Paripurna DPRK Aceh Jaya."},
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
# CSS STYLE - SUPER PREMIUM v4.0
# =========================================================
st.markdown(
    """
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&family=Plus+Jakarta+Sans:wght@500;600;700;800;900&display=swap');

:root {
    --primary: #0d5e3a;
    --primary-dark: #083d26;
    --primary-2: #14734a;
    --primary-light: #e8f5ef;
    --gold: #c9a227;
    --gold-light: #e6c458;
    --gold-soft: #faf6e8;
    --bg: #f8faf9;
    --white: #ffffff;
    --border: #e5ebe7;
    --text: #0a1f18;
    --muted: #4a5a55;
}

* { box-sizing: border-box; font-family: 'Inter', sans-serif; }
html, body, [class*="css"] { font-family: 'Inter', sans-serif; }
#MainMenu, footer, header { visibility: hidden; height: 0; }
.stApp { background: var(--bg); color: #000000; }
.block-container { max-width: 100%; padding: 0 !important; }
section[data-testid="stSidebar"] { display: none; }

.stApp > div > div { gap: 0 !important; }
div[data-testid="stVerticalBlock"] { gap: 0 !important; }
.element-container { margin: 0 !important; }
div[data-testid="stMarkdownContainer"] { margin: 0 !important; padding: 0 !important; }
div[data-testid="stMarkdownContainer"] > p { margin: 0 !important; }
.stMarkdown { margin: 0 !important; }

/* ============================================
   TOP BAR MODERN
   ============================================ */
.topbar { 
    background: linear-gradient(90deg, #083d26 0%, #0d5e3a 100%);
    color: #ffffff !important; 
    padding: 8px 16px; 
    display: flex; 
    align-items: center; 
    justify-content: space-between; 
    font-size: 12px;
    flex-wrap: wrap;
    gap: 8px;
}
.topbar * { color: #ffffff !important; }
.topbar-left, .topbar-right { display: flex; gap: 16px; align-items: center; flex-wrap: wrap; }
.topbar-item { display: flex; align-items: center; gap: 6px; }
.topbar a { color: #ffffff !important; text-decoration: none; transition: color 0.2s; }
.topbar a:hover { color: #e6c458 !important; }
.topbar-badge {
    background: rgba(230, 196, 88, 0.2);
    color: #e6c458 !important;
    padding: 3px 10px;
    border-radius: 12px;
    font-size: 11px;
    font-weight: 700;
    border: 1px solid rgba(230, 196, 88, 0.3);
}
.topbar-lang {
    background: rgba(255,255,255,0.1);
    border: 1px solid rgba(255,255,255,0.2);
    color: #ffffff !important;
    padding: 3px 10px;
    border-radius: 4px;
    font-size: 11px;
    font-weight: 600;
    cursor: pointer;
    text-decoration: none;
}

/* ============================================
   HEADER MODERN
   ============================================ */
.header-wrap {
    background: #ffffff;
    padding: 18px 16px;
    border-bottom: 1px solid #e5ebe7;
    box-shadow: 0 2px 8px rgba(0,0,0,0.02);
}
.header-inner {
    display: flex;
    align-items: center;
    justify-content: space-between;
    gap: 16px;
    max-width: 1400px;
    margin: 0 auto;
    flex-wrap: wrap;
}
.header-brand { display: flex; align-items: center; gap: 14px; flex: 1; min-width: 250px; }
.header-logo {
    width: 68px; height: 68px;
    border-radius: 12px;
    background: linear-gradient(135deg, #f8faf9, #e8f5ef);
    display: flex; align-items: center; justify-content: center;
    overflow: hidden;
    flex-shrink: 0;
    border: 2px solid #e5ebe7;
    padding: 6px;
}
.header-logo img { width: 100%; height: 100%; object-fit: contain; }
.header-text-title {
    color: #083d26 !important;
    font-family: 'Plus Jakarta Sans', sans-serif;
    font-size: 17px;
    line-height: 1.2;
    font-weight: 800;
    text-transform: uppercase;
    letter-spacing: 0.3px;
}
.header-text-sub {
    color: #4a5a55 !important;
    font-size: 11px;
    margin-top: 4px;
    letter-spacing: 0.4px;
    font-weight: 500;
}
.header-actions { display: flex; gap: 8px; align-items: center; flex-wrap: wrap; }
.header-action-btn {
    display: inline-flex;
    align-items: center;
    gap: 6px;
    background: #f8faf9;
    border: 1px solid #e5ebe7;
    color: #083d26 !important;
    padding: 8px 14px;
    border-radius: 8px;
    font-size: 12px;
    font-weight: 700;
    text-decoration: none;
    transition: all 0.25s;
}
.header-action-btn:hover {
    background: #0d5e3a;
    color: #ffffff !important;
    border-color: #0d5e3a;
}
.header-action-primary {
    background: linear-gradient(135deg, #0d5e3a, #14734a);
    color: #ffffff !important;
    border: none;
    box-shadow: 0 4px 12px rgba(13,94,58,0.25);
}
.header-action-primary:hover {
    background: linear-gradient(135deg, #14734a, #c9a227);
    transform: translateY(-2px);
    box-shadow: 0 6px 20px rgba(13,94,58,0.35);
}

/* ============================================
   NAVBAR MODERN - STICKY
   ============================================ */
.navbar {
    background: #ffffff !important;
    padding: 0 16px;
    border-top: 3px solid #0d5e3a;
    border-bottom: 1px solid #e5ebe7;
    position: sticky;
    top: 0;
    z-index: 999;
    box-shadow: 0 4px 20px rgba(0,0,0,0.06);
}
.navbar-inner {
    max-width: 1400px;
    margin: 0 auto;
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 4px;
    flex-wrap: wrap;
    padding: 4px 0;
}
.nav-link {
    display: inline-block;
    background: transparent;
    color: #0a1f18 !important;
    font-family: 'Plus Jakarta Sans', sans-serif;
    font-size: 12.5px;
    font-weight: 700;
    padding: 14px 18px;
    border-radius: 0;
    text-decoration: none !important;
    letter-spacing: 0.4px;
    text-transform: uppercase;
    transition: all 0.25s ease;
    position: relative;
    white-space: nowrap;
}
.nav-link::after {
    content: '';
    position: absolute;
    bottom: 0;
    left: 50%;
    transform: translateX(-50%);
    width: 0;
    height: 3px;
    background: linear-gradient(90deg, #0d5e3a, #c9a227);
    transition: width 0.3s ease;
    border-radius: 2px;
}
.nav-link:hover {
    color: #0d5e3a !important;
}
.nav-link:hover::after {
    width: 60%;
}
.nav-link-active {
    color: #0d5e3a !important;
    font-weight: 800;
}
.nav-link-active::after {
    width: 80%;
}

/* ============================================
   RUNNING TEXT MODERN
   ============================================ */
.running-text-bar {
    background: linear-gradient(90deg, #f8faf9, #ffffff);
    border-bottom: 1px solid #e5ebe7;
    padding: 12px 16px;
    display: flex;
    align-items: center;
    gap: 14px;
    overflow: hidden;
}
.running-label {
    background: linear-gradient(135deg, #c9a227, #e6c458);
    color: #083d26 !important;
    padding: 6px 14px;
    border-radius: 20px;
    font-size: 10.5px;
    font-weight: 800;
    text-transform: uppercase;
    letter-spacing: 0.8px;
    flex-shrink: 0;
    box-shadow: 0 2px 8px rgba(201,162,39,0.3);
}
.running-scroll-wrap {
    flex: 1;
    overflow: hidden;
    white-space: nowrap;
    min-width: 0;
}
.running-scroll {
    display: inline-block;
    padding-left: 100%;
    animation: marquee 45s linear infinite;
    font-size: 12.5px;
    font-weight: 600;
    color: #0a1f18 !important;
}
@keyframes marquee {
    0% { transform: translate(0, 0); }
    100% { transform: translate(-100%, 0); }
}

/* ============================================
   HERO MODERN
   ============================================ */
.hero-modern {
    position: relative;
    min-height: 560px;
    overflow: hidden;
    display: flex;
    align-items: center;
    background: #000;
}
.hero-modern-bg {
    position: absolute;
    top: 0; left: 0;
    width: 100%; height: 100%;
    background-size: cover;
    background-position: center;
    animation: heroZoom 20s ease-in-out infinite;
}
@keyframes heroZoom {
    0%, 100% { transform: scale(1); }
    50% { transform: scale(1.08); }
}
.hero-modern-overlay {
    position: absolute;
    top: 0; left: 0;
    width: 100%; height: 100%;
    background: linear-gradient(120deg, rgba(8,61,38,0.92) 0%, rgba(13,94,58,0.75) 45%, rgba(8,61,38,0.55) 100%);
}
.hero-modern-pattern {
    position: absolute;
    top: 0; left: 0;
    width: 100%; height: 100%;
    background-image: radial-gradient(circle at 20% 30%, rgba(230,196,88,0.12) 0%, transparent 50%),
                      radial-gradient(circle at 80% 70%, rgba(230,196,88,0.08) 0%, transparent 50%);
    pointer-events: none;
}
.hero-modern-content {
    position: relative;
    z-index: 3;
    max-width: 1400px;
    margin: 0 auto;
    width: 92%;
    padding: 60px 0;
    color: #ffffff;
}
.hero-modern-kicker {
    display: inline-flex;
    align-items: center;
    gap: 10px;
    background: rgba(230,196,88,0.15);
    border: 1px solid rgba(230,196,88,0.4);
    color: #e6c458 !important;
    padding: 8px 18px;
    border-radius: 30px;
    font-size: 11.5px;
    font-weight: 800;
    letter-spacing: 1.8px;
    text-transform: uppercase;
    margin-bottom: 24px;
    backdrop-filter: blur(10px);
}
.hero-modern-kicker::before {
    content: '';
    width: 8px;
    height: 8px;
    border-radius: 50%;
    background: #e6c458;
    animation: pulseDot 2s infinite;
}
@keyframes pulseDot {
    0%, 100% { opacity: 1; transform: scale(1); }
    50% { opacity: 0.6; transform: scale(1.3); }
}
.hero-modern-title {
    font-family: 'Plus Jakarta Sans', sans-serif;
    font-size: clamp(30px, 5vw, 62px);
    font-weight: 900;
    line-height: 1.05;
    letter-spacing: -1.5px;
    margin-bottom: 22px;
    color: #ffffff !important;
    text-shadow: 0 4px 40px rgba(0,0,0,0.5);
    max-width: 900px;
}
.hero-modern-title span {
    background: linear-gradient(135deg, #e6c458 0%, #f5e090 50%, #c9a227 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
}
.hero-modern-sub {
    font-size: clamp(14px, 1.5vw, 18px);
    line-height: 1.7;
    color: rgba(255,255,255,0.92) !important;
    max-width: 720px;
    margin-bottom: 36px;
    text-shadow: 0 2px 12px rgba(0,0,0,0.4);
}
.hero-modern-buttons { display: flex; flex-wrap: wrap; gap: 12px; margin-bottom: 48px; }
.hero-modern-btn {
    display: inline-flex;
    align-items: center;
    gap: 10px;
    padding: 14px 28px;
    background: linear-gradient(135deg, #c9a227, #e6c458);
    color: #083d26 !important;
    text-decoration: none !important;
    font-weight: 800;
    font-size: 13px;
    border-radius: 8px;
    letter-spacing: 0.6px;
    text-transform: uppercase;
    box-shadow: 0 8px 24px rgba(201,162,39,0.4);
    transition: all 0.3s ease;
    border: 2px solid transparent;
}
.hero-modern-btn:hover {
    background: linear-gradient(135deg, #e6c458, #f5e090);
    transform: translateY(-3px);
    box-shadow: 0 12px 32px rgba(201,162,39,0.6);
}
.hero-modern-btn-outline {
    background: rgba(255,255,255,0.08);
    color: #ffffff !important;
    border: 2px solid rgba(255,255,255,0.5);
    backdrop-filter: blur(10px);
    box-shadow: none;
}
.hero-modern-btn-outline:hover {
    background: rgba(255,255,255,0.2);
    border-color: #e6c458;
    transform: translateY(-3px);
}

/* Hero Stats */
.hero-modern-stats {
    display: flex;
    flex-wrap: wrap;
    gap: 12px;
}
.hero-stat {
    background: rgba(255,255,255,0.08);
    backdrop-filter: blur(15px);
    border: 1px solid rgba(255,255,255,0.15);
    padding: 16px 22px;
    border-radius: 12px;
    min-width: 130px;
    transition: all 0.3s ease;
}
.hero-stat:hover {
    background: rgba(230,196,88,0.15);
    border-color: rgba(230,196,88,0.4);
    transform: translateY(-3px);
}
.hero-stat-num {
    font-family: 'Plus Jakarta Sans', sans-serif;
    color: #e6c458 !important;
    font-size: 26px;
    font-weight: 900;
    line-height: 1;
    display: block;
}
.hero-stat-label {
    color: rgba(255,255,255,0.85) !important;
    font-size: 10.5px;
    margin-top: 6px;
    text-transform: uppercase;
    letter-spacing: 0.8px;
    font-weight: 700;
}

/* ============================================
   QUICK ACCESS CARDS
   ============================================ */
.quick-access {
    background: #ffffff;
    padding: 32px 16px;
    border-bottom: 1px solid #e5ebe7;
}
.quick-access-inner {
    max-width: 1400px;
    margin: 0 auto;
}
.quick-grid {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 16px;
}
.quick-card {
    display: flex;
    align-items: center;
    gap: 14px;
    background: #f8faf9;
    border: 1px solid #e5ebe7;
    border-radius: 12px;
    padding: 18px;
    text-decoration: none !important;
    color: #0a1f18 !important;
    transition: all 0.3s ease;
    position: relative;
    overflow: hidden;
}
.quick-card::before {
    content: '';
    position: absolute;
    top: 0; left: -100%;
    width: 100%; height: 100%;
    background: linear-gradient(90deg, transparent, rgba(255,255,255,0.6), transparent);
    transition: left 0.6s ease;
}
.quick-card:hover::before { left: 100%; }
.quick-card:hover {
    transform: translateY(-4px);
    box-shadow: 0 12px 30px rgba(13,94,58,0.12);
    border-color: #0d5e3a;
}
.quick-icon {
    width: 52px;
    height: 52px;
    border-radius: 12px;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 24px;
    flex-shrink: 0;
    box-shadow: 0 4px 12px rgba(0,0,0,0.08);
}
.quick-content { min-width: 0; }
.quick-title {
    font-family: 'Plus Jakarta Sans', sans-serif;
    font-size: 13.5px;
    font-weight: 800;
    color: #083d26 !important;
    margin: 0 0 3px;
    white-space: nowrap;
    overflow: hidden;
    text-overflow: ellipsis;
}
.quick-desc {
    font-size: 11px;
    color: #4a5a55 !important;
    font-weight: 500;
}

/* ============================================
   SECTION STYLES
   ============================================ */
.page-container {
    width: 92%;
    max-width: 1400px;
    margin: 0 auto;
    padding: 50px 0;
}
.section-header-modern {
    text-align: center;
    margin-bottom: 40px;
}
.section-kicker-modern {
    display: inline-block;
    color: #c9a227 !important;
    font-size: 11.5px;
    font-weight: 800;
    letter-spacing: 2.5px;
    text-transform: uppercase;
    margin-bottom: 12px;
    position: relative;
    padding: 0 30px;
}
.section-kicker-modern::before,
.section-kicker-modern::after {
    content: '';
    position: absolute;
    top: 50%;
    width: 20px;
    height: 2px;
    background: #c9a227;
}
.section-kicker-modern::before { left: 0; }
.section-kicker-modern::after { right: 0; }
.section-title-modern {
    font-family: 'Plus Jakarta Sans', sans-serif;
    font-size: clamp(22px, 3vw, 34px);
    font-weight: 900;
    color: #083d26 !important;
    letter-spacing: -0.5px;
    line-height: 1.15;
    margin: 0 0 12px;
}
.section-desc-modern {
    color: #4a5a55 !important;
    font-size: 14px;
    line-height: 1.7;
    max-width: 720px;
    margin: 0 auto;
}

/* ============================================
   SAMBUTAN PIMPINAN (Mayor's Remarks Style)
   ============================================ */
.sambutan-section {
    background: linear-gradient(135deg, #ffffff 0%, #f8faf9 100%);
    padding: 60px 16px;
    position: relative;
    overflow: hidden;
}
.sambutan-section::before {
    content: '';
    position: absolute;
    top: -50%; right: -20%;
    width: 600px; height: 600px;
    background: radial-gradient(circle, rgba(13,94,58,0.05) 0%, transparent 70%);
    border-radius: 50%;
}
.sambutan-inner {
    max-width: 1400px;
    margin: 0 auto;
    display: grid;
    grid-template-columns: 320px 1fr;
    gap: 48px;
    align-items: start;
    position: relative;
    z-index: 2;
}
.sambutan-photo-wrap {
    position: relative;
    text-align: center;
}
.sambutan-photo {
    width: 100%;
    max-width: 320px;
    aspect-ratio: 3/4;
    object-fit: cover;
    border-radius: 16px;
    box-shadow: 0 20px 60px rgba(13,94,58,0.25);
    border: 4px solid #ffffff;
    position: relative;
    z-index: 2;
}
.sambutan-photo-frame {
    position: absolute;
    top: 16px; left: 16px;
    width: 100%;
    max-width: 320px;
    aspect-ratio: 3/4;
    border: 3px solid #c9a227;
    border-radius: 16px;
    z-index: 1;
}
.sambutan-photo-info {
    margin-top: 24px;
    background: #ffffff;
    border: 1px solid #e5ebe7;
    border-radius: 12px;
    padding: 16px;
    box-shadow: 0 8px 24px rgba(0,0,0,0.04);
}
.sambutan-nama {
    font-family: 'Plus Jakarta Sans', sans-serif;
    font-size: 16px;
    font-weight: 900;
    color: #083d26 !important;
    text-transform: uppercase;
    letter-spacing: 0.3px;
    margin: 0 0 4px;
}
.sambutan-jabatan {
    color: #c9a227 !important;
    font-size: 11.5px;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 1px;
}
.sambutan-content {
    padding-top: 20px;
}
.sambutan-assalam {
    font-family: 'Plus Jakarta Sans', sans-serif;
    font-size: 16px;
    font-weight: 700;
    color: #0d5e3a !important;
    margin-bottom: 20px;
}
.sambutan-text {
    color: #0a1f18 !important;
    font-size: 14.5px;
    line-height: 1.9;
    margin-bottom: 18px;
}
.sambutan-quote {
    border-left: 4px solid #c9a227;
    background: linear-gradient(90deg, #faf6e8, #ffffff);
    padding: 18px 22px;
    border-radius: 0 12px 12px 0;
    margin: 24px 0;
    font-family: 'Plus Jakarta Sans', sans-serif;
    font-size: 15px;
    font-weight: 600;
    font-style: italic;
    color: #083d26 !important;
    line-height: 1.7;
    position: relative;
}
.sambutan-quote::before {
    content: '"';
    position: absolute;
    top: 0; left: 12px;
    font-size: 60px;
    color: rgba(201,162,39,0.15);
    font-family: Georgia, serif;
    line-height: 1;
}
.sambutan-salam {
    margin-top: 28px;
    padding-top: 20px;
    border-top: 1px solid #e5ebe7;
}
.sambutan-salam-line {
    color: #4a5a55 !important;
    font-size: 13.5px;
    margin: 0 0 4px;
}
.sambutan-salam-nama {
    font-family: 'Plus Jakarta Sans', sans-serif;
    font-size: 15px;
    font-weight: 900;
    color: #083d26 !important;
    text-transform: uppercase;
    margin: 8px 0 4px;
}
.sambutan-salam-jabatan {
    color: #c9a227 !important;
    font-size: 12px;
    font-weight: 700;
}

/* ============================================
   WARTA GRID MODERN
   ============================================ */
.warta-grid-modern {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 24px;
}
.warta-card-modern {
    background: #ffffff;
    border: 1px solid #e5ebe7;
    border-radius: 16px;
    overflow: hidden;
    text-decoration: none !important;
    color: inherit;
    transition: all 0.35s cubic-bezier(0.4, 0, 0.2, 1);
    display: flex;
    flex-direction: column;
    position: relative;
}
.warta-card-modern:hover {
    transform: translateY(-8px);
    box-shadow: 0 25px 60px rgba(13,94,58,0.18);
    border-color: rgba(201,162,39,0.4);
}
.warta-card-modern-img {
    position: relative;
    width: 100%;
    height: 220px;
    overflow: hidden;
}
.warta-card-modern-img img {
    width: 100%;
    height: 100%;
    object-fit: cover;
    transition: transform 0.7s ease;
}
.warta-card-modern:hover .warta-card-modern-img img {
    transform: scale(1.1);
}
.warta-card-modern-img::after {
    content: '';
    position: absolute;
    bottom: 0; left: 0; right: 0;
    height: 50%;
    background: linear-gradient(180deg, transparent, rgba(0,0,0,0.5));
}
.warta-card-modern-cat {
    position: absolute;
    top: 14px; left: 14px;
    background: linear-gradient(135deg, #c9a227, #e6c458);
    color: #083d26 !important;
    padding: 6px 14px;
    border-radius: 20px;
    font-size: 10.5px;
    font-weight: 800;
    text-transform: uppercase;
    letter-spacing: 0.6px;
    z-index: 2;
    box-shadow: 0 4px 12px rgba(201,162,39,0.4);
}
.warta-card-modern-body {
    padding: 24px;
    flex: 1;
    display: flex;
    flex-direction: column;
}
.warta-card-modern-date {
    display: inline-flex;
    align-items: center;
    gap: 6px;
    color: #c9a227 !important;
    font-size: 11px;
    font-weight: 800;
    text-transform: uppercase;
    letter-spacing: 0.5px;
    margin-bottom: 12px;
}
.warta-card-modern-title {
    font-family: 'Plus Jakarta Sans', sans-serif;
    font-size: 17px;
    font-weight: 800;
    color: #083d26 !important;
    line-height: 1.4;
    margin: 0 0 12px;
    letter-spacing: -0.2px;
    transition: color 0.25s;
}
.warta-card-modern:hover .warta-card-modern-title {
    color: #0d5e3a !important;
}
.warta-card-modern-desc {
    color: #4a5a55 !important;
    font-size: 13px;
    line-height: 1.65;
    margin: 0 0 16px;
    flex: 1;
}
.warta-card-modern-more {
    display: inline-flex;
    align-items: center;
    gap: 6px;
    color: #0d5e3a !important;
    font-size: 12px;
    font-weight: 800;
    text-transform: uppercase;
    letter-spacing: 0.6px;
    transition: gap 0.25s;
}
.warta-card-modern:hover .warta-card-modern-more {
    gap: 12px;
    color: #c9a227 !important;
}

/* ============================================
   AGENDA + SIDEBAR
   ============================================ */
.content-grid-2col {
    display: grid;
    grid-template-columns: 2fr 1fr;
    gap: 32px;
}
.widget-modern {
    background: #ffffff;
    border: 1px solid #e5ebe7;
    border-radius: 16px;
    overflow: hidden;
    margin-bottom: 24px;
    box-shadow: 0 4px 12px rgba(0,0,0,0.03);
}
.widget-modern-head {
    background: linear-gradient(135deg, #0d5e3a, #14734a);
    color: #ffffff !important;
    padding: 16px 20px;
    font-family: 'Plus Jakarta Sans', sans-serif;
    font-size: 13px;
    font-weight: 800;
    text-transform: uppercase;
    letter-spacing: 0.8px;
    display: flex;
    align-items: center;
    justify-content: space-between;
    border-bottom: 3px solid #c9a227;
}
.widget-modern-head::before {
    content: '';
    position: absolute;
}
.widget-modern-body { padding: 0; }

.agenda-item-modern {
    display: flex;
    gap: 14px;
    padding: 16px 20px;
    border-bottom: 1px solid #e5ebe7;
    transition: background 0.2s;
}
.agenda-item-modern:last-child { border-bottom: none; }
.agenda-item-modern:hover { background: #f8faf9; }
.agenda-date-modern {
    width: 60px;
    height: 68px;
    background: linear-gradient(135deg, #0d5e3a, #14734a);
    color: #ffffff !important;
    border-radius: 10px;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    flex-shrink: 0;
    position: relative;
    box-shadow: 0 4px 12px rgba(13,94,58,0.25);
}
.agenda-date-modern::before {
    content: '';
    position: absolute;
    top: 0; left: 0; right: 0;
    height: 4px;
    background: #c9a227;
    border-radius: 10px 10px 0 0;
}
.agenda-day-modern {
    font-family: 'Plus Jakarta Sans', sans-serif;
    font-size: 24px;
    font-weight: 900;
    line-height: 1;
    color: #ffffff !important;
}
.agenda-month-modern {
    font-size: 9px;
    font-weight: 800;
    color: #ffffff !important;
    margin-top: 4px;
    letter-spacing: 0.5px;
}
.agenda-content-modern { flex: 1; min-width: 0; }
.agenda-title-modern {
    color: #083d26 !important;
    font-family: 'Plus Jakarta Sans', sans-serif;
    font-size: 13.5px;
    font-weight: 800;
    line-height: 1.4;
    margin: 0 0 6px;
}
.agenda-desc-modern {
    color: #4a5a55 !important;
    font-size: 11.5px;
    line-height: 1.55;
    margin: 0 0 6px;
    display: -webkit-box;
    -webkit-line-clamp: 2;
    -webkit-box-orient: vertical;
    overflow: hidden;
}
.agenda-footer-modern {
    display: flex;
    align-items: center;
    gap: 6px;
    color: #c9a227 !important;
    font-size: 10.5px;
    font-weight: 800;
    text-transform: uppercase;
    letter-spacing: 0.4px;
}

/* Kesekretariatan item */
.kesekret-item-modern {
    display: flex;
    gap: 12px;
    padding: 14px 20px;
    border-bottom: 1px solid #e5ebe7;
    transition: background 0.2s;
}
.kesekret-item-modern:last-child { border-bottom: none; }
.kesekret-item-modern:hover { background: #f8faf9; }
.kesekret-icon-modern {
    width: 40px;
    height: 40px;
    border-radius: 10px;
    background: linear-gradient(135deg, #e8f5ef, #d1e8dd);
    color: #0d5e3a !important;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 18px;
    flex-shrink: 0;
}
.kesekret-title-modern {
    color: #083d26 !important;
    font-size: 12.5px;
    font-weight: 700;
    line-height: 1.45;
    margin: 0 0 4px;
}
.kesekret-date-modern {
    color: #c9a227 !important;
    font-size: 10.5px;
    font-weight: 700;
}

/* ============================================
   STATS SECTION
   ============================================ */
.stats-section-modern {
    background: linear-gradient(135deg, #083d26 0%, #0d5e3a 50%, #083d26 100%);
    padding: 60px 16px;
    position: relative;
    overflow: hidden;
}
.stats-section-modern::before {
    content: '';
    position: absolute;
    top: -50%; right: -20%;
    width: 600px; height: 600px;
    background: radial-gradient(circle, rgba(230,196,88,0.15) 0%, transparent 60%);
    border-radius: 50%;
    animation: floatOrb 12s ease-in-out infinite;
}
@keyframes floatOrb {
    0%, 100% { transform: translate(0, 0); }
    50% { transform: translate(30px, -30px); }
}
.stats-inner {
    max-width: 1400px;
    margin: 0 auto;
    position: relative;
    z-index: 2;
}
.stats-grid-modern {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 24px;
}
.stat-item-modern {
    text-align: center;
    padding: 28px 20px;
    background: rgba(255,255,255,0.06);
    backdrop-filter: blur(10px);
    border: 1px solid rgba(255,255,255,0.12);
    border-radius: 16px;
    transition: all 0.3s ease;
}
.stat-item-modern:hover {
    background: rgba(230,196,88,0.12);
    border-color: rgba(230,196,88,0.35);
    transform: translateY(-6px);
}
.stat-num-modern {
    font-family: 'Plus Jakarta Sans', sans-serif;
    color: #e6c458 !important;
    font-size: 42px;
    font-weight: 900;
    line-height: 1;
    margin-bottom: 8px;
    letter-spacing: -1px;
    text-shadow: 0 4px 20px rgba(230,196,88,0.4);
}
.stat-label-modern {
    color: #ffffff !important;
    font-size: 12.5px;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 1px;
}

/* ============================================
   LAYANAN GRID
   ============================================ */
.layanan-grid-modern {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 20px;
}
.layanan-card-modern {
    background: #ffffff;
    border: 1px solid #e5ebe7;
    border-radius: 16px;
    padding: 28px 22px;
    text-align: center;
    text-decoration: none !important;
    color: inherit;
    transition: all 0.35s ease;
    position: relative;
    overflow: hidden;
}
.layanan-card-modern::before {
    content: '';
    position: absolute;
    top: 0; left: 0; right: 0;
    height: 4px;
    background: linear-gradient(90deg, #0d5e3a, #c9a227);
    transform: scaleX(0);
    transform-origin: left;
    transition: transform 0.4s ease;
}
.layanan-card-modern:hover::before { transform: scaleX(1); }
.layanan-card-modern:hover {
    transform: translateY(-8px);
    box-shadow: 0 25px 50px rgba(13,94,58,0.15);
    border-color: rgba(201,162,39,0.3);
}
.layanan-icon-modern {
    width: 68px;
    height: 68px;
    margin: 0 auto 16px;
    border-radius: 18px;
    background: linear-gradient(135deg, #e8f5ef, #d1e8dd);
    color: #0d5e3a !important;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 30px;
    transition: all 0.4s ease;
    box-shadow: 0 4px 12px rgba(13,94,58,0.08);
}
.layanan-card-modern:hover .layanan-icon-modern {
    background: linear-gradient(135deg, #c9a227, #e6c458);
    color: #ffffff !important;
    transform: scale(1.1) rotate(-8deg);
    box-shadow: 0 8px 24px rgba(201,162,39,0.4);
}
.layanan-title-modern {
    font-family: 'Plus Jakarta Sans', sans-serif;
    font-size: 14px;
    font-weight: 800;
    color: #083d26 !important;
    margin: 0 0 6px;
    letter-spacing: -0.2px;
}
.layanan-desc-modern {
    color: #4a5a55 !important;
    font-size: 11.5px;
    line-height: 1.5;
}

/* ============================================
   FOOTER MODERN
   ============================================ */
.footer-modern {
    background: #062b1b;
    color: #ffffff !important;
    padding: 60px 16px 0;
    margin-top: 0;
    position: relative;
    overflow: hidden;
}
.footer-modern::before {
    content: '';
    position: absolute;
    top: 0; left: 0; right: 0;
    height: 4px;
    background: linear-gradient(90deg, #0d5e3a, #c9a227, #e6c458, #c9a227, #0d5e3a);
}
.footer-modern * { color: #ffffff !important; }
.footer-inner-modern {
    max-width: 1400px;
    margin: 0 auto;
    position: relative;
    z-index: 2;
}
.footer-grid-modern {
    display: grid;
    grid-template-columns: 1.8fr 1fr 1fr 1.2fr;
    gap: 40px;
    padding-bottom: 40px;
}
.footer-col-modern h4 {
    color: #ffffff !important;
    font-size: 13px;
    font-weight: 800;
    margin: 0 0 20px;
    text-transform: uppercase;
    letter-spacing: 1px;
    position: relative;
    padding-bottom: 12px;
}
.footer-col-modern h4::after {
    content: '';
    position: absolute;
    bottom: 0; left: 0;
    width: 32px;
    height: 2px;
    background: #c9a227;
}
.footer-col-modern p {
    color: rgba(255,255,255,0.7) !important;
    font-size: 12.5px;
    line-height: 1.9;
    margin: 0 0 8px;
}
.footer-col-modern a {
    display: block;
    color: rgba(255,255,255,0.7) !important;
    font-size: 12.5px;
    line-height: 2.1;
    text-decoration: none;
    transition: all 0.2s ease;
}
.footer-col-modern a:hover { color: #e6c458 !important; padding-left: 6px; }
.footer-brand-modern {
    display: flex;
    align-items: center;
    gap: 14px;
    margin-bottom: 20px;
}
.footer-logo-modern {
    width: 56px;
    height: 56px;
    background: #ffffff;
    border-radius: 10px;
    display: flex;
    align-items: center;
    justify-content: center;
    overflow: hidden;
    padding: 6px;
    box-shadow: 0 8px 20px rgba(0,0,0,0.3);
}
.footer-logo-modern img { width: 100%; height: 100%; object-fit: contain; }
.footer-brand-title-modern {
    color: #ffffff !important;
    font-family: 'Plus Jakarta Sans', sans-serif;
    font-size: 14.5px;
    font-weight: 800;
    text-transform: uppercase;
    letter-spacing: 0.3px;
}
.footer-brand-sub-modern {
    color: #e6c458 !important;
    font-size: 10px;
    letter-spacing: 1px;
    margin-top: 4px;
    font-weight: 700;
}
.footer-social-modern {
    display: flex;
    gap: 8px;
    margin-top: 20px;
}
.footer-social-item-modern {
    width: 38px;
    height: 38px;
    background: rgba(255,255,255,0.08);
    border: 1px solid rgba(255,255,255,0.12);
    border-radius: 10px;
    color: #ffffff !important;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 14px;
    text-decoration: none;
    transition: all 0.3s;
}
.footer-social-item-modern:hover {
    background: linear-gradient(135deg, #c9a227, #e6c458);
    border-color: #c9a227;
    color: #083d26 !important;
    transform: translateY(-4px);
}
.footer-bottom-modern {
    border-top: 1px solid rgba(255,255,255,0.08);
    padding: 24px 0;
    display: flex;
    justify-content: space-between;
    align-items: center;
    flex-wrap: wrap;
    gap: 12px;
    font-size: 11.5px;
    color: rgba(255,255,255,0.5) !important;
}
.footer-bottom-modern * { color: rgba(255,255,255,0.5) !important; }

/* ============================================
   CHAT WIDGET "SAVIRA"
   ============================================ */
.chat-widget {
    position: fixed;
    bottom: 24px;
    right: 24px;
    z-index: 9999;
}
.chat-btn {
    width: 64px;
    height: 64px;
    border-radius: 50%;
    background: linear-gradient(135deg, #0d5e3a, #14734a);
    color: #ffffff !important;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 26px;
    text-decoration: none;
    box-shadow: 0 12px 30px rgba(13,94,58,0.4);
    border: 3px solid #ffffff;
    transition: all 0.3s ease;
    position: relative;
    animation: chatPulse 2.5s infinite;
}
@keyframes chatPulse {
    0%, 100% { box-shadow: 0 12px 30px rgba(13,94,58,0.4), 0 0 0 0 rgba(13,94,58,0.5); }
    50% { box-shadow: 0 12px 30px rgba(13,94,58,0.4), 0 0 0 15px rgba(13,94,58,0); }
}
.chat-btn:hover {
    transform: scale(1.1);
    background: linear-gradient(135deg, #c9a227, #e6c458);
    color: #083d26 !important;
}
.chat-label {
    position: absolute;
    bottom: 76px;
    right: 0;
    background: #ffffff;
    color: #083d26 !important;
    padding: 8px 14px;
    border-radius: 20px;
    font-size: 12px;
    font-weight: 800;
    white-space: nowrap;
    box-shadow: 0 8px 24px rgba(0,0,0,0.15);
    opacity: 0;
    pointer-events: none;
    transition: all 0.3s;
    border: 2px solid #c9a227;
}
.chat-btn:hover + .chat-label,
.chat-widget:hover .chat-label {
    opacity: 1;
    transform: translateY(-8px);
}

/* ============================================
   FORM & INPUTS
   ============================================ */
.stButton > button {
    background: linear-gradient(135deg, #0d5e3a, #14734a) !important;
    color: #ffffff !important;
    border: none !important;
    border-radius: 8px !important;
    font-weight: 700 !important;
    box-shadow: 0 4px 12px rgba(13,94,58,0.25) !important;
}
.stButton > button:hover {
    background: linear-gradient(135deg, #14734a, #c9a227) !important;
    transform: translateY(-2px);
}
div[data-testid="stForm"] {
    background: #ffffff;
    border: 1px solid #e5ebe7;
    border-radius: 16px;
    padding: 24px !important;
    box-shadow: 0 4px 20px rgba(0,0,0,0.04);
}
.stTextInput input, .stTextArea textarea, div[data-baseweb="select"] > div {
    border-radius: 8px !important;
    border-color: #e5ebe7 !important;
    color: #000000 !important;
}
.stTextInput input:focus, .stTextArea textarea:focus {
    border-color: #c9a227 !important;
    box-shadow: 0 0 0 3px rgba(201,162,39,0.15) !important;
}

/* Tabs */
.stTabs [data-baseweb="tab-list"] {
    gap: 4px;
    background: transparent;
    border-bottom: 2px solid #e5ebe7;
}
.stTabs [data-baseweb="tab"] {
    background: transparent;
    border-radius: 8px 8px 0 0;
    padding: 12px 20px;
    color: #4a5a55 !important;
    font-weight: 700;
    font-family: 'Plus Jakarta Sans', sans-serif;
    font-size: 13px;
}
.stTabs [aria-selected="true"] {
    background: #f0f6f2 !important;
    color: #0d5e3a !important;
    border-bottom: 3px solid #0d5e3a;
}

/* ============================================
   RESPONSIVE TABLET
   ============================================ */
@media (max-width: 1100px) {
    .quick-grid { grid-template-columns: repeat(2, 1fr); }
    .warta-grid-modern { grid-template-columns: repeat(2, 1fr); }
    .stats-grid-modern { grid-template-columns: repeat(2, 1fr); }
    .layanan-grid-modern { grid-template-columns: repeat(2, 1fr); }
    .content-grid-2col { grid-template-columns: 1fr; }
    .footer-grid-modern { grid-template-columns: 1fr 1fr; gap: 32px; }
    .sambutan-inner { grid-template-columns: 280px 1fr; gap: 32px; }
}

/* ============================================
   RESPONSIVE MOBILE
   ============================================ */
@media (max-width: 768px) {
    /* Topbar */
    .topbar { 
        flex-direction: column; 
        gap: 8px; 
        text-align: center; 
        padding: 10px 12px;
    }
    .topbar-left, .topbar-right { 
        justify-content: center; 
        gap: 10px; 
        font-size: 11px;
    }
    .topbar-item { font-size: 11px; }
    
    /* Header */
    .header-wrap { padding: 14px 12px; }
    .header-inner { gap: 12px; }
    .header-logo { width: 52px; height: 52px; border-radius: 10px; }
    .header-text-title { font-size: 13.5px; }
    .header-text-sub { font-size: 9.5px; }
    .header-actions { 
        width: 100%; 
        justify-content: center; 
        margin-top: 12px; 
        padding-top: 12px;
        border-top: 1px solid #e5ebe7;
    }
    .header-action-btn { font-size: 11px; padding: 7px 12px; }
    
    /* NAVBAR MOBILE */
    .navbar { padding: 0 8px; }
    .navbar-inner { gap: 0; padding: 2px 0; }
    .nav-link {
        font-size: 10px !important;
        padding: 12px 8px !important;
        flex: 1 1 calc(25% - 2px);
        max-width: calc(25% - 2px);
        text-align: center;
        letter-spacing: 0 !important;
        min-width: 0;
    }
    
    /* Running text */
    .running-text-bar { padding: 10px 12px; gap: 10px; }
    .running-label { font-size: 9.5px; padding: 5px 10px; }
    .running-scroll { font-size: 11.5px; }
    
    /* Hero */
    .hero-modern { min-height: 480px; }
    .hero-modern-content { padding: 40px 0; }
    .hero-modern-kicker { font-size: 10px; padding: 6px 14px; letter-spacing: 1.2px; margin-bottom: 16px; }
    .hero-modern-title { font-size: 26px; margin-bottom: 14px; letter-spacing: -0.5px; }
    .hero-modern-sub { font-size: 13px; margin-bottom: 24px; line-height: 1.6; }
    .hero-modern-buttons { gap: 8px; margin-bottom: 28px; }
    .hero-modern-btn { padding: 11px 20px; font-size: 11px; }
    .hero-modern-stats { gap: 8px; }
    .hero-stat { padding: 12px 16px; min-width: 100px; }
    .hero-stat-num { font-size: 20px; }
    .hero-stat-label { font-size: 9px; }
    
    /* Quick access */
    .quick-access { padding: 24px 12px; }
    .quick-grid { grid-template-columns: 1fr 1fr; gap: 10px; }
    .quick-card { padding: 14px; gap: 10px; }
    .quick-icon { width: 44px; height: 44px; font-size: 20px; border-radius: 10px; }
    .quick-title { font-size: 12px; }
    .quick-desc { font-size: 10px; }
    
    /* Page container */
    .page-container { width: 95%; padding: 32px 0; }
    
    /* Section header */
    .section-header-modern { margin-bottom: 28px; }
    .section-kicker-modern { font-size: 10.5px; letter-spacing: 2px; }
    .section-title-modern { font-size: 22px; }
    .section-desc-modern { font-size: 12.5px; }
    
    /* Sambutan */
    .sambutan-section { padding: 40px 12px; }
    .sambutan-inner { 
        grid-template-columns: 1fr; 
        gap: 28px; 
    }
    .sambutan-photo-wrap { max-width: 260px; margin: 0 auto; }
    .sambutan-photo-frame { display: none; }
    .sambutan-assalam { font-size: 15px; }
    .sambutan-text { font-size: 13.5px; line-height: 1.8; }
    .sambutan-quote { font-size: 14px; padding: 14px 18px; }
    .sambutan-salam-nama { font-size: 14px; }
    
    /* Warta grid */
    .warta-grid-modern { grid-template-columns: 1fr; gap: 16px; }
    .warta-card-modern-img { height: 200px; }
    .warta-card-modern-body { padding: 20px; }
    .warta-card-modern-title { font-size: 15px; }
    .warta-card-modern-desc { font-size: 12.5px; }
    
    /* Content 2 col */
    .content-grid-2col { grid-template-columns: 1fr; gap: 24px; }
    .widget-modern { margin-bottom: 16px; }
    .widget-modern-head { padding: 12px 16px; font-size: 12px; }
    .agenda-item-modern { padding: 12px 16px; gap: 12px; }
    .agenda-date-modern { width: 52px; height: 60px; }
    .agenda-day-modern { font-size: 20px; }
    .agenda-title-modern { font-size: 12.5px; }
    .agenda-desc-modern { font-size: 11px; }
    .kesekret-item-modern { padding: 12px 16px; }
    .kesekret-icon-modern { width: 36px; height: 36px; font-size: 16px; }
    .kesekret-title-modern { font-size: 11.5px; }
    
    /* Stats */
    .stats-section-modern { padding: 40px 12px; }
    .stats-grid-modern { grid-template-columns: repeat(2, 1fr); gap: 12px; }
    .stat-item-modern { padding: 20px 12px; }
    .stat-num-modern { font-size: 32px; }
    .stat-label-modern { font-size: 11px; }
    
    /* Layanan */
    .layanan-grid-modern { grid-template-columns: repeat(2, 1fr); gap: 12px; }
    .layanan-card-modern { padding: 20px 14px; }
    .layanan-icon-modern { width: 56px; height: 56px; font-size: 24px; border-radius: 14px; }
    .layanan-title-modern { font-size: 12.5px; }
    .layanan-desc-modern { font-size: 10.5px; }
    
    /* Footer */
    .footer-modern { padding: 40px 14px 0; }
    .footer-grid-modern { grid-template-columns: 1fr; gap: 28px; padding-bottom: 28px; }
    .footer-col-modern h4 { font-size: 12.5px; margin-bottom: 14px; padding-bottom: 8px; }
    .footer-col-modern p, .footer-col-modern a { font-size: 12px; }
    .footer-logo-modern { width: 48px; height: 48px; }
    .footer-brand-title-modern { font-size: 13px; }
    .footer-social-item-modern { width: 34px; height: 34px; font-size: 13px; }
    .footer-bottom-modern { flex-direction: column; text-align: center; padding: 18px 0; font-size: 11px; }
    
    /* Chat */
    .chat-widget { bottom: 16px; right: 16px; }
    .chat-btn { width: 56px; height: 56px; font-size: 22px; }
    
    /* Tabs */
    .stTabs [data-baseweb="tab"] { padding: 10px 14px; font-size: 12px; }
}

/* Extra small */
@media (max-width: 400px) {
    .nav-link { font-size: 9.5px !important; padding: 10px 4px !important; }
    .hero-modern-title { font-size: 22px; }
    .hero-modern-sub { font-size: 12px; }
    .quick-icon { width: 38px; height: 38px; font-size: 18px; }
    .quick-title { font-size: 11px; }
    .quick-desc { font-size: 9px; }
    .stat-num-modern { font-size: 26px; }
    .stat-label-modern { font-size: 10px; }
    .layanan-icon-modern { width: 48px; height: 48px; font-size: 20px; }
    .layanan-title-modern { font-size: 11.5px; }
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
        <div class="topbar-item">
            <span>📞</span>
            <span>(0655) 12345</span>
        </div>
        <div class="topbar-item">
            <span>✉️</span>
            <span>sekretariat@dprk.acehjaya.go.id</span>
        </div>
    </div>
    <div class="topbar-right">
        <span class="topbar-badge">🟢 ONLINE</span>
        <div class="topbar-item">
            <span>🕐</span>
            <span>{now.strftime('%H:%M WIB')}</span>
        </div>
        <a href="#" class="topbar-lang">🇮🇩 ID</a>
    </div>
</div>
""",
    unsafe_allow_html=True,
)

# =========================================================
# HEADER MODERN
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
                <div class="header-text-title">DPRK Kabupaten Aceh Jaya</div>
                <div class="header-text-sub">PORTAL RESMI INFORMASI & ASPIRASI MASYARAKAT</div>
            </div>
        </div>
        <div class="header-actions">
            <a href="?page=layanan" class="header-action-btn">📢 Lapor</a>
            <a href="?page=jdih" class="header-action-btn">📜 JDIH</a>
            <a href="?page=layanan" class="header-action-btn header-action-primary">💬 Hubungi</a>
        </div>
    </div>
</div>
""",
    unsafe_allow_html=True,
)

# =========================================================
# NAVBAR
# =========================================================
nav_items_html = ""
for key in PAGES.keys():
    page_value = PAGES[key]
    url_key = page_value.lower().replace(" & ", "-").replace(" ", "-")
    active_class = "nav-link-active" if st.session_state.page == page_value else ""
    nav_items_html += f'<a href="?page={url_key}" class="nav-link {active_class}">{page_value}</a>'

st.markdown(
    f"""
<div class="navbar">
    <div class="navbar-inner">
        {nav_items_html}
    </div>
</div>
""",
    unsafe_allow_html=True,
)

# =========================================================
# RUNNING TEXT
# =========================================================
st.markdown(
    """
<div class="running-text-bar">
    <span class="running-label">📢 INFO TERKINI</span>
    <div class="running-scroll-wrap">
        <div class="running-scroll">
            Selamat Datang di Portal Resmi DPRK Kabupaten Aceh Jaya &nbsp;&nbsp;★&nbsp;&nbsp;
            Rapat Paripurna Pembahasan KUA-PPAS 2027 akan dilaksanakan pada 18 September 2026 &nbsp;&nbsp;★&nbsp;&nbsp;
            Layanan Pengaduan Masyarakat kini dapat diakses melalui menu Layanan &nbsp;&nbsp;★&nbsp;&nbsp;
            DPRK Aceh Jaya Raih Penghargaan Keterbukaan Informasi Publik 2026 &nbsp;&nbsp;★&nbsp;&nbsp;
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
    slide = HERO_SLIDES[st.session_state.slide_index % len(HERO_SLIDES)]
    st.markdown(
        f"""
    <section class="hero-modern">
        <div class="hero-modern-bg" style="background-image: url('{slide['image']}');"></div>
        <div class="hero-modern-overlay"></div>
        <div class="hero-modern-pattern"></div>
        <div class="hero-modern-content">
            <div class="hero-modern-kicker">{slide['kicker']}</div>
            <h1 class="hero-modern-title">
                {slide['title'].split(' ')[0]} <span>{' '.join(slide['title'].split(' ')[1:3])}</span> {' '.join(slide['title'].split(' ')[3:])}
            </h1>
            <p class="hero-modern-sub">{slide['subtitle']}</p>
            <div class="hero-modern-buttons">
                <a href="?page=layanan" class="hero-modern-btn">📢 Sampaikan Aspirasi</a>
                <a href="?page=berita" class="hero-modern-btn hero-modern-btn-outline">📰 Lihat Berita</a>
            </div>
            <div class="hero-modern-stats">
                <div class="hero-stat">
                    <span class="hero-stat-num">20</span>
                    <div class="hero-stat-label">Anggota DPRK</div>
                </div>
                <div class="hero-stat">
                    <span class="hero-stat-num">4</span>
                    <div class="hero-stat-label">Komisi</div>
                </div>
                <div class="hero-stat">
                    <span class="hero-stat-num">120+</span>
                    <div class="hero-stat-label">Produk Hukum</div>
                </div>
                <div class="hero-stat">
                    <span class="hero-stat-num">{st.session_state.visitor_count:,}</span>
                    <div class="hero-stat-label">Kunjungan</div>
                </div>
            </div>
        </div>
    </section>
    """,
        unsafe_allow_html=True,
    )

    # Navigasi slide
    nav_slide_cols = st.columns([1, 4, 1])
    with nav_slide_cols[0]:
        if st.button("◀ Prev", key="slide_prev", use_container_width=True):
            st.session_state.slide_index = (st.session_state.slide_index - 1) % len(HERO_SLIDES)
            st.rerun()
    with nav_slide_cols[2]:
        if st.button("Next ▶", key="slide_next", use_container_width=True):
            st.session_state.slide_index = (st.session_state.slide_index + 1) % len(HERO_SLIDES)
            st.rerun()

    # QUICK ACCESS CARDS
    st.markdown('<div class="quick-access"><div class="quick-access-inner">', unsafe_allow_html=True)
    quick_cols = st.columns(4)
    for i, item in enumerate(QUICK_LINKS):
        with quick_cols[i]:
            st.markdown(
                f"""
            <a href="?page={item['page']}" class="quick-card">
                <div class="quick-icon" style="background: linear-gradient(135deg, {item['color']}22, {item['color']}44); color: {item['color']};">{item['icon']}</div>
                <div class="quick-content">
                    <div class="quick-title">{item['title']}</div>
                    <div class="quick-desc">{item['desc']}</div>
                </div>
            </a>
            """,
                unsafe_allow_html=True,
            )
    st.markdown("</div></div>", unsafe_allow_html=True)

    # SAMBUTAN PIMPINAN (Mayor's Remarks Style)
    st.markdown(
        f"""
    <section class="sambutan-section">
        <div class="sambutan-inner">
            <div class="sambutan-photo-wrap">
                <div class="sambutan-photo-frame"></div>
                <img class="sambutan-photo" src="{SAMBUTAN['foto']}" alt="{SAMBUTAN['nama']}">
                <div class="sambutan-photo-info">
                    <div class="sambutan-nama">{SAMBUTAN['nama']}</div>
                    <div class="sambutan-jabatan">{SAMBUTAN['jabatan']}</div>
                </div>
            </div>
            <div class="sambutan-content">
                <div class="section-kicker-modern" style="text-align:left; padding:0;">SAMBUTAN PIMPINAN</div>
                <h2 class="section-title-modern" style="text-align:left; margin-top:8px;">Membangun Aceh Jaya yang Lebih Baik</h2>
                <div class="sambutan-assalam">{SAMBUTAN['assalamualaikum']}</div>
                <p class="sambutan-text">{SAMBUTAN['pembuka']}</p>
                <div class="sambutan-quote">{SAMBUTAN['quote']}</div>
                <p class="sambutan-text">{SAMBUTAN['paragraf2']}</p>
                <p class="sambutan-text">{SAMBUTAN['penutup']}</p>
                <div class="sambutan-salam">
                    <p class="sambutan-salam-line">{SAMBUTAN['salam']}</p>
                    <div class="sambutan-salam-nama">{SAMBUTAN['nama']}</div>
                    <div class="sambutan-salam-jabatan">{SAMBUTAN['jabatan']}</div>
                </div>
            </div>
        </div>
    </section>
    """,
        unsafe_allow_html=True,
    )

    # LAYANAN PUBLIK
    st.markdown('<div class="page-container">', unsafe_allow_html=True)
    st.markdown(
        """
    <div class="section-header-modern">
        <div class="section-kicker-modern">AKSES CEPAT</div>
        <h2 class="section-title-modern">Layanan Publik</h2>
        <p class="section-desc-modern">Akses layanan dan informasi DPRK Aceh Jaya secara mudah dan cepat.</p>
    </div>
    """,
        unsafe_allow_html=True,
    )

    layanan_items = [
        ("📢", "Pengaduan Masyarakat", "Sampaikan aspirasi & laporan", "layanan"),
        ("📜", "JDIH", "Produk hukum daerah", "jdih"),
        ("📅", "Agenda DPRK", "Jadwal rapat & sidang", "berita"),
        ("📊", "Transparansi", "Informasi publik", "jdih"),
    ]

    lay_cols = st.columns(4)
    for i, (icon, title, desc, target) in enumerate(layanan_items):
        with lay_cols[i]:
            is_ext = target.startswith("http")
            href = target if is_ext else f"?page={target}"
            tgt = 'target="_blank" rel="noopener"' if is_ext else ""
            st.markdown(
                f"""
            <a href="{href}" {tgt} class="layanan-card-modern">
                <div class="layanan-icon-modern">{icon}</div>
                <div class="layanan-title-modern">{title}</div>
                <div class="layanan-desc-modern">{desc}</div>
            </a>
            """,
                unsafe_allow_html=True,
            )

    st.markdown("</div>", unsafe_allow_html=True)

    # STATS SECTION
    st.markdown(
        f"""
    <section class="stats-section-modern">
        <div class="stats-inner">
            <div class="section-header-modern" style="margin-bottom: 32px;">
                <div class="section-kicker-modern" style="color: #e6c458;">DALAM ANGKA</div>
                <h2 class="section-title-modern" style="color: #ffffff;">DPRK Aceh Jaya</h2>
            </div>
            <div class="stats-grid-modern">
                <div class="stat-item-modern">
                    <div class="stat-num-modern">20</div>
                    <div class="stat-label-modern">Anggota DPRK</div>
                </div>
                <div class="stat-item-modern">
                    <div class="stat-num-modern">4</div>
                    <div class="stat-label-modern">Komisi DPRK</div>
                </div>
                <div class="stat-item-modern">
                    <div class="stat-num-modern">120+</div>
                    <div class="stat-label-modern">Produk Hukum</div>
                </div>
                <div class="stat-item-modern">
                    <div class="stat-num-modern">{st.session_state.visitor_count:,}</div>
                    <div class="stat-label-modern">Total Kunjungan</div>
                </div>
            </div>
        </div>
    </section>
    """,
        unsafe_allow_html=True,
    )

    # WARTA + AGENDA (2 COLUMN)
    st.markdown('<div class="page-container">', unsafe_allow_html=True)
    st.markdown(
        """
    <div class="section-header-modern">
        <div class="section-kicker-modern">INFORMASI TERBARU</div>
        <h2 class="section-title-modern">Warta DPRK</h2>
        <p class="section-desc-modern">Informasi kegiatan, rapat, agenda, dan aktivitas DPRK Aceh Jaya.</p>
    </div>
    """,
        unsafe_allow_html=True,
    )

    main_col, side_col = st.columns([2, 1])

    with main_col:
        for item in WARTA_DPRK[:3]:
            st.markdown(
                f"""
            <div class="warta-card-modern" style="margin-bottom: 16px;">
                <div class="warta-card-modern-img">
                    <span class="warta-card-modern-cat">{item['kategori']}</span>
                    <img src="{item['image']}">
                </div>
                <div class="warta-card-modern-body">
                    <div class="warta-card-modern-date">📅 {item['date']}</div>
                    <h3 class="warta-card-modern-title">{item['title']}</h3>
                    <p class="warta-card-modern-desc">{item['desc'][:180]}...</p>
                    <a href="?page=berita" class="warta-card-modern-more">Baca Selengkapnya →</a>
                </div>
            </div>
            """,
                unsafe_allow_html=True,
            )

    with side_col:
        # Widget Agenda
        st.markdown(
            """
        <div class="widget-modern">
            <div class="widget-modern-head">📅 Agenda Terkini</div>
            <div class="widget-modern-body">
        """,
            unsafe_allow_html=True,
        )
        for item in AGENDA_TERKINI:
            st.markdown(
                f"""
            <div class="agenda-item-modern">
                <div class="agenda-date-modern">
                    <div class="agenda-day-modern">{item['hari']}</div>
                    <div class="agenda-month-modern">{item['bulan_tahun']}</div>
                </div>
                <div class="agenda-content-modern">
                    <div class="agenda-title-modern">{item['judul']}</div>
                    <p class="agenda-desc-modern">{item['desc']}</p>
                    <div class="agenda-footer-modern">📅 {item['tanggal_full']}</div>
                </div>
            </div>
            """,
                unsafe_allow_html=True,
            )
        st.markdown("</div></div>", unsafe_allow_html=True)

        # Widget Kesekretariatan
        st.markdown(
            """
        <div class="widget-modern">
            <div class="widget-modern-head">📰 Kesekretariatan</div>
            <div class="widget-modern-body">
        """,
            unsafe_allow_html=True,
        )
        for item in KESEKRETARIATAN:
            st.markdown(
                f"""
            <div class="kesekret-item-modern">
                <div class="kesekret-icon-modern">📋</div>
                <div>
                    <div class="kesekret-title-modern">{item['title']}</div>
                    <div class="kesekret-date-modern">📅 {item['date']}</div>
                </div>
            </div>
            """,
                unsafe_allow_html=True,
            )
        st.markdown("</div></div>", unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True)

    # STATISTIK CHART
    st.markdown('<div class="page-container">', unsafe_allow_html=True)
    st.markdown(
        """
    <div class="section-header-modern">
        <div class="section-kicker-modern">DATA & STATISTIK</div>
        <h2 class="section-title-modern">Dashboard Kinerja</h2>
        <p class="section-desc-modern">Visualisasi data kegiatan dan kinerja DPRK Aceh Jaya periode 2026.</p>
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
            font=dict(family="Inter", size=11, color="#000000"),
            title_font=dict(size=14, family="Plus Jakarta Sans", color="#000000"),
            margin=dict(l=10, r=10, t=50, b=10),
            height=320,
        )
        fig1.update_traces(line=dict(width=3), marker=dict(size=10, line=dict(width=2, color="#fff")))
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
            font=dict(family="Inter", size=11, color="#000000"),
            title_font=dict(size=14, family="Plus Jakarta Sans", color="#000000"),
            margin=dict(l=10, r=10, t=50, b=10),
            height=320,
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
    <div class="section-header-modern">
        <div class="section-kicker-modern">TENTANG DPRK</div>
        <h2 class="section-title-modern">Profil DPRK Aceh Jaya</h2>
        <p class="section-desc-modern">Dewan Perwakilan Rakyat Kabupaten Aceh Jaya sebagai unsur penyelenggara pemerintahan daerah bersama pemerintah daerah menjalankan fungsi legislasi, anggaran, dan pengawasan.</p>
    </div>
    """,
        unsafe_allow_html=True,
    )

    tab1, tab2 = st.tabs(["🏛️ Pimpinan & Anggota", "🏢 Pejabat Sekretariat"])

    with tab1:
        cols = st.columns(2)
        for i, (nama, jabatan) in enumerate(PIMPINAN_DAN_ANGGOTA):
            with cols[i % 2]:
                st.markdown(
                    f"""
                <div style="background: #fff; border: 1px solid #e5ebe7; border-radius: 12px; padding: 16px; text-align: center; border-top: 3px solid #0d5e3a; margin-bottom: 12px; transition: all 0.3s;">
                    <div style="font-weight: 800; color: #083d26; font-size: 12.5px; margin-bottom: 4px; font-family: 'Plus Jakarta Sans';">{nama}</div>
                    <div style="color: #c9a227; font-size: 10.5px; font-weight: 700; text-transform: uppercase;">{jabatan}</div>
                </div>
                """,
                    unsafe_allow_html=True,
                )

    with tab2:
        cols = st.columns(2)
        for i, (nama, jabatan) in enumerate(PEJABAT_SEKRETARIAT):
            with cols[i % 2]:
                st.markdown(
                    f"""
                <div style="background: #fff; border: 1px solid #e5ebe7; border-radius: 12px; padding: 16px; text-align: center; border-top: 3px solid #c9a227; margin-bottom: 12px;">
                    <div style="font-weight: 800; color: #083d26; font-size: 12.5px; margin-bottom: 4px; font-family: 'Plus Jakarta Sans';">{nama}</div>
                    <div style="color: #4a5a55; font-size: 10.5px; font-weight: 600;">{jabatan}</div>
                </div>
                """,
                    unsafe_allow_html=True,
                )

    st.markdown("</div>", unsafe_allow_html=True)

# =========================================================
# HALAMAN: BERITA
# =========================================================
elif st.session_state.page == "Berita":
    st.markdown('<div class="page-container">', unsafe_allow_html=True)
    st.markdown(
        """
    <div class="section-header-modern">
        <div class="section-kicker-modern">PUBLIKASI</div>
        <h2 class="section-title-modern">Warta DPRK</h2>
        <p class="section-desc-modern">Informasi kegiatan, rapat, agenda, dan aktivitas DPRK Aceh Jaya.</p>
    </div>
    """,
        unsafe_allow_html=True,
    )

    categories = ["Semua"] + list(set(item["kategori"] for item in WARTA_DPRK))
    fc1, fc2 = st.columns(2)
    with fc1:
        selected = st.selectbox("🔍 Kategori", categories)
    with fc2:
        search = st.text_input("🔎 Cari", placeholder="Kata kunci...")

    filtered = WARTA_DPRK
    if selected != "Semua":
        filtered = [i for i in filtered if i["kategori"] == selected]
    if search:
        filtered = [i for i in filtered if search.lower() in i["title"].lower() or search.lower() in i["desc"].lower()]

    # Grid 3 kolom
    for i in range(0, len(filtered), 3):
        cols = st.columns(3)
        for j in range(3):
            if i + j < len(filtered):
                item = filtered[i + j]
                with cols[j]:
                    st.markdown(
                        f"""
                    <div class="warta-card-modern" style="margin-bottom: 16px;">
                        <div class="warta-card-modern-img">
                            <span class="warta-card-modern-cat">{item['kategori']}</span>
                            <img src="{item['image']}">
                        </div>
                        <div class="warta-card-modern-body">
                            <div class="warta-card-modern-date">📅 {item['date']}</div>
                            <h3 class="warta-card-modern-title">{item['title']}</h3>
                            <p class="warta-card-modern-desc">{item['desc'][:130]}...</p>
                            <a href="#" class="warta-card-modern-more">Baca →</a>
                        </div>
                    </div>
                    """,
                        unsafe_allow_html=True,
                    )

    if not filtered:
        st.info("Tidak ada berita yang sesuai pencarian.")

    st.markdown("</div>", unsafe_allow_html=True)

# =========================================================
# HALAMAN: GALERI
# =========================================================
elif st.session_state.page == "Galeri":
    st.markdown('<div class="page-container">', unsafe_allow_html=True)
    st.markdown(
        """
    <div class="section-header-modern">
        <div class="section-kicker-modern">DOKUMENTASI</div>
        <h2 class="section-title-modern">Galeri Foto & Video</h2>
        <p class="section-desc-modern">Dokumentasi kegiatan, rapat, dan aktivitas DPRK Aceh Jaya.</p>
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

    for i in range(0, len(gallery), 3):
        cols = st.columns(3)
        for j in range(3):
            if i + j < len(gallery):
                title, img = gallery[i + j]
                with cols[j]:
                    st.markdown(
                        f"""
                    <div style="background: #fff; border: 1px solid #e5ebe7; border-radius: 12px; overflow: hidden; margin-bottom: 12px; transition: all 0.3s;">
                        <div style="overflow: hidden;">
                            <img src="{img}" style="width: 100%; height: 180px; object-fit: cover;">
                        </div>
                        <div style="padding: 14px; text-align: center;">
                            <div style="font-family: 'Plus Jakarta Sans'; font-weight: 700; color: #083d26; font-size: 12.5px;">{title}</div>
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
    <div class="section-header-modern">
        <div class="section-kicker-modern">PELAYANAN MASYARAKAT</div>
        <h2 class="section-title-modern">Layanan Aspirasi & Pengaduan</h2>
        <p class="section-desc-modern">Sampaikan aspirasi, laporan, atau pengaduan Anda kepada DPRK Aceh Jaya.</p>
    </div>
    """,
        unsafe_allow_html=True,
    )

    with st.form("form_aduan"):
        c1, c2 = st.columns(2)
        with c1:
            nama = st.text_input("Nama Lengkap *", placeholder="Nama lengkap")
            nik = st.text_input("NIK (Opsional)", placeholder="16 digit NIK")
        with c2:
            kategori = st.selectbox("Kategori *", ["Pengaduan Masyarakat", "Infrastruktur & Jalan", "Pelayanan Publik", "Legislasi & Qanun", "Lingkungan & Bencana", "Lainnya"])
            prioritas = st.selectbox("Prioritas", ["Normal", "Penting", "Mendesak"])
        lokasi = st.text_input("Lokasi Kejadian", placeholder="Desa / Kecamatan")
        isi = st.text_area("Isi Laporan *", height=140, placeholder="Jelaskan laporan Anda...")
        lampiran = st.file_uploader("📎 Lampiran", type=["jpg", "jpeg", "png", "pdf"])

        submitted = st.form_submit_button("🚀 Kirim Laporan", type="primary", use_container_width=True)

        if submitted:
            if nama.strip() and isi.strip():
                nomor = datetime.now().strftime("%Y%m%d%H%M%S")
                st.success(f"✅ Laporan diterima! Nomor tiket: **ADU-{nomor}**")
                st.info(f"📋 Kategori: {kategori} | Prioritas: {prioritas}")
            else:
                st.error("⚠️ Mohon lengkapi Nama dan Isi Laporan.")

    st.markdown(
        """
    <div class="widget-modern" style="margin-top: 24px;">
        <div class="widget-modern-head">📞 Kontak Kami</div>
        <div class="widget-modern-body" style="padding: 20px;">
            <p style="font-size: 13px; color: #083d26; line-height: 1.9; margin: 0 0 12px;">
                <strong style="color: #0d5e3a;">📞 Telepon</strong><br>(0655) 12345
            </p>
            <p style="font-size: 13px; color: #083d26; line-height: 1.9; margin: 0 0 12px;">
                <strong style="color: #0d5e3a;">✉️ Email</strong><br>sekretariat@dprk.acehjaya.go.id
            </p>
            <p style="font-size: 13px; color: #083d26; line-height: 1.9; margin: 0 0 12px;">
                <strong style="color: #0d5e3a;">📍 Alamat</strong><br>Jl. Merdeka No. 01, Calang, Aceh Jaya
            </p>
            <p style="font-size: 13px; color: #083d26; line-height: 1.9; margin: 0;">
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
    <div class="section-header-modern">
        <div class="section-kicker-modern">DOKUMENTASI HUKUM</div>
        <h2 class="section-title-modern">JDIH & Transparansi</h2>
        <p class="section-desc-modern">Akses daftar produk hukum dan informasi publik DPRK Aceh Jaya.</p>
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
    st.markdown('<div class="page-container">', unsafe_allow_html=True)
    st.markdown(
        """
    <div class="section-header-modern">
        <div class="section-kicker-modern">INFORMASI KONTAK</div>
        <h2 class="section-title-modern">Hubungi Kami</h2>
        <p class="section-desc-modern">Gunakan informasi berikut untuk mendapatkan layanan dari Sekretariat DPRK Aceh Jaya.</p>
    </div>
    """,
        unsafe_allow_html=True,
    )

    cols = st.columns(3)
    contacts = [
        ("📍", "Alamat", "Jl. Merdeka No. 01, Calang, Aceh Jaya"),
        ("📞", "Telepon", "(0655) 12345"),
        ("✉️", "Email", "sekretariat@dprk.acehjaya.go.id"),
    ]
    for i, (icon, title, value) in enumerate(contacts):
        with cols[i]:
            st.markdown(
                f"""
            <div class="layanan-card-modern">
                <div class="layanan-icon-modern">{icon}</div>
                <div class="layanan-title-modern">{title}</div>
                <div class="layanan-desc-modern">{value}</div>
            </div>
            """,
                unsafe_allow_html=True,
            )

    st.markdown(
        """
    <div style="margin-top: 30px; background: #fff; border: 1px solid #e5ebe7; border-radius: 16px; padding: 24px;">
        <div class="section-header-modern" style="margin-bottom: 20px;">
            <h2 class="section-title-modern" style="font-size: 20px;">Peta Lokasi Kantor</h2>
        </div>
        <div style="width: 100%; height: 340px; border-radius: 12px; overflow: hidden; border: 1px solid #e5ebe7;">
            <iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3988.5!2d95.39!3d4.71!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x30403e5f3a0b0b0b%3A0x0!2sCalang%2C%20Aceh%20Jaya%20Regency%2C%20Aceh!5e0!3m2!1sen!2sid!4v1600000000000" width="100%" height="100%" style="border:0;" allowfullscreen="" loading="lazy"></iframe>
        </div>
    </div>
    """,
        unsafe_allow_html=True,
    )
    st.markdown("</div>", unsafe_allow_html=True)

# =========================================================
# CHAT WIDGET "SAVIRA"
# =========================================================
st.markdown(
    """
<div class="chat-widget">
    <a href="?page=layanan" class="chat-btn" title="Chat dengan SAVIRA">💬</a>
    <div class="chat-label">💬 Chat SAVIRA!</div>
</div>
""",
    unsafe_allow_html=True,
)

# =========================================================
# FOOTER
# =========================================================
st.markdown(
    f"""
<footer class="footer-modern">
<div class="footer-inner-modern">
<div class="footer-grid-modern">

<div class="footer-col-modern">
<div class="footer-brand-modern">
<div class="footer-logo-modern">
    <img src="{LOGO_URL}" alt="Logo DPRK Aceh Jaya"
         onerror="this.onerror=null;this.src='data:image/svg+xml,<svg xmlns=%22http://www.w3.org/2000/svg%22 viewBox=%220 0 100 100%22><text y=%22.9em%22 font-size=%2290%22>🏛️</text></svg>'">
</div>
<div>
<div class="footer-brand-title-modern">DPRK ACEH JAYA</div>
<div class="footer-brand-sub-modern">SEKRETARIAT DPRK</div>
</div>
</div>
<p style="color: rgba(255,255,255,0.7); font-size: 12.5px; line-height: 1.85; margin: 0 0 8px;">
Portal resmi Sekretariat Dewan Perwakilan Rakyat Kabupaten Aceh Jaya. Menyediakan informasi kelembagaan, berita, agenda, produk hukum, dan layanan aspirasi masyarakat.
</p>
<div class="footer-social-modern">
<a href="#" class="footer-social-item-modern">f</a>
<a href="#" class="footer-social-item-modern">𝕏</a>
<a href="#" class="footer-social-item-modern">▶</a>
<a href="#" class="footer-social-item-modern">◎</a>
<a href="#" class="footer-social-item-modern">in</a>
</div>
</div>

<div class="footer-col-modern">
<h4>Navigasi</h4>
<a href="?page=beranda">Beranda</a>
<a href="?page=profil">Profil DPRK</a>
<a href="?page=berita">Berita & Agenda</a>
<a href="?page=galeri">Galeri</a>
<a href="?page=kontak">Kontak</a>
</div>

<div class="footer-col-modern">
<h4>Layanan Publik</h4>
<a href="?page=layanan">Pengaduan Masyarakat</a>
<a href="?page=kontak">Informasi Publik</a>
<a href="?page=jdih">JDIH</a>
<a href="?page=jdih">Transparansi</a>
<a href="https://elhpkpn.kpk.go.id/" target="_blank">E-LHKPN</a>
</div>

<div class="footer-col-modern">
<h4>Hubungi Kami</h4>
<p>📍 Jl. Merdeka No. 01</p>
<p>Calang, Kabupaten Aceh Jaya</p>
<p>📞 (0655) 12345</p>
<p>✉️ sekretariat@dprk.acehjaya.go.id</p>
<p>🕐 Senin–Jumat, 08.00–16.00 WIB</p>
</div>

</div>

<div class="footer-bottom-modern">
<div>© {datetime.now().year} Sekretariat DPRK Kabupaten Aceh Jaya. Seluruh hak cipta dilindungi.</div>
<div>Portal Informasi Publik • Kabupaten Aceh Jaya</div>
</div>

</div>
</footer>
""",
    unsafe_allow_html=True,
)

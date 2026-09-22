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
    st.session_state.visitor_count = random.randint(25000, 45000)

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

SAMBUTAN = {
    "nama": "MUSLIADI Z, S.E",
    "jabatan": "Ketua DPRK Aceh Jaya",
    "foto": "https://i.imgur.com/mEWIdvc.jpg",
    "assalamualaikum": "Assalamu'alaikum Warahmatullahi Wabarakatuh,",
    "pembuka": "Selamat datang di Portal Resmi Dewan Perwakilan Rakyat Kabupaten (DPRK) Aceh Jaya. Portal ini hadir sebagai gerbang informasi dan komunikasi antara DPRK dengan seluruh masyarakat Aceh Jaya.",
    "quote": "Visi kami adalah mewujudkan DPRK yang responsif, transparan, dan akuntabel dalam menjalankan fungsi legislasi, anggaran, dan pengawasan.",
    "paragraf2": "Melalui portal ini, kami berkomitmen untuk menyediakan akses informasi publik yang mudah, cepat, dan transparan. Kami mengundang seluruh masyarakat untuk berpartisipasi aktif menyampaikan aspirasi dan mengawasi kinerja DPRK.",
    "penutup": "Mari bersama-sama membangun Aceh Jaya yang lebih maju, sejahtera, dan bermartabat.",
}

WARTA_DPRK = [
    {
        "title": "DPRK Aceh Jaya Gelar Rapat Paripurna Pandangan Fraksi terhadap Pertanggungjawaban APBK 2025",
        "date": "Jumat, 14 Agustus 2026",
        "desc": "Dewan Perwakilan Rakyat Kabupaten (DPRK) Aceh Jaya menggelar Rapat Paripurna Ke-IX Masa Persidangan II Tahun Sidang membahas pandangan fraksi terhadap pertanggungjawaban APBK.",
        "image": "https://images.unsplash.com/photo-1556761175-b413da4baf72?auto=format&fit=crop&w=800&q=80",
        "kategori": "Paripurna",
        "views": 2450,
    },
    {
        "title": "DPRK Aceh Jaya Gelar Rapat Paripurna ke-VIII Masa Persidangan II",
        "date": "Kamis, 30 Juli 2026",
        "desc": "Rapat Paripurna ke-VIII Masa Persidangan II membahas pertanggungjawaban APBK 2025 dan Perubahan Anggaran Kas Daerah.",
        "image": "https://images.unsplash.com/photo-1529107386315-e1a2ed48a620?auto=format&fit=crop&w=800&q=80",
        "kategori": "Paripurna",
        "views": 1876,
    },
    {
        "title": "Ketua DPRK Aceh Jaya Dukung Pelestarian Mangrove",
        "date": "Minggu, 26 Juli 2026",
        "desc": "Ketua DPRK Aceh Jaya Musliadi Z, S.E menyampaikan dukungan terhadap kegiatan Penanaman Mangrove Serentak dalam rangka memperingati Hari Mangrove.",
        "image": "https://images.unsplash.com/photo-1589578527966-fdac0f44566c?auto=format&fit=crop&w=800&q=80",
        "kategori": "Lingkungan",
        "views": 1523,
    },
    {
        "title": "Ketua DPRK Apresiasi Kejari Pulihkan Keuangan Negara Rp2,05 Miliar",
        "date": "Rabu, 22 Juli 2026",
        "desc": "Ketua DPRK Aceh Jaya menghadiri kegiatan Press Release Capaian Pemulihan Keuangan Negara yang diselenggarakan oleh Kejaksaan Negeri Aceh Jaya.",
        "image": "https://images.unsplash.com/photo-1577962917302-cd874c4e31d2?auto=format&fit=crop&w=800&q=80",
        "kategori": "Hukum",
        "views": 2103,
    },
    {
        "title": "Sosialisasi Qanun No. 5 Tahun 2025 tentang Ketertiban Umum",
        "date": "Senin, 20 Juli 2026",
        "desc": "DPRK Aceh Jaya menggelar sosialisasi Qanun Nomor 5 Tahun 2025 tentang Ketertiban Umum dan Ketenteraman Masyarakat.",
        "image": "https://images.unsplash.com/photo-1517486808906-6ca8b3f04846?auto=format&fit=crop&w=800&q=80",
        "kategori": "Legislasi",
        "views": 987,
    },
    {
        "title": "Kunjungan Kerja Komisi II ke Dinas Pendidikan Aceh Jaya",
        "date": "Kamis, 16 Juli 2026",
        "desc": "Komisi II DPRK Aceh Jaya melakukan kunjungan kerja ke Dinas Pendidikan untuk membahas program prioritas pendidikan tahun 2027.",
        "image": "https://images.unsplash.com/photo-1523240795612-9a054b0db644?auto=format&fit=crop&w=800&q=80",
        "kategori": "Kunjungan",
        "views": 756,
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
    ["6", "Qanun No. 1/2023", "Rencana Tata Ruang Wilayah", "Dicabut"],
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

MITRA = [
    "🏛️ KPK", "⚖️ Kejaksaan", "🚔 Polri", "🏦 BPK", "📊 BPS",
    "🎓 Universitas", "🏥 RSUD", "📚 Dinas Pendidikan", "🌾 Dinas Pertanian", "🛣️ PUPR"
]

# =========================================================
# CSS STYLE - ULTRA PREMIUM COMPACT MOBILE v6.0
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
html { scroll-behavior: smooth; }
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

::-webkit-scrollbar { width: 10px; height: 10px; }
::-webkit-scrollbar-track { background: #e8f5ef; }
::-webkit-scrollbar-thumb { background: linear-gradient(180deg, #0d5e3a, #c9a227); border-radius: 10px; }

/* ============================================
   TOP BAR
   ============================================ */
.topbar { 
    background: linear-gradient(90deg, #062b1b 0%, #083d26 50%, #062b1b 100%);
    color: #ffffff !important; 
    padding: 8px 16px; 
    display: flex; 
    align-items: center; 
    justify-content: space-between; 
    font-size: 11.5px;
    flex-wrap: wrap;
    gap: 8px;
    position: relative;
    overflow: hidden;
}
.topbar::before {
    content: '';
    position: absolute;
    top: 0; left: -100%;
    width: 100%; height: 100%;
    background: linear-gradient(90deg, transparent, rgba(230,196,88,0.15), transparent);
    animation: topbarShine 8s infinite;
}
@keyframes topbarShine {
    0% { left: -100%; }
    100% { left: 100%; }
}
.topbar * { color: #ffffff !important; }
.topbar-left, .topbar-right { display: flex; gap: 16px; align-items: center; flex-wrap: wrap; position: relative; z-index: 2; }
.topbar-item { display: flex; align-items: center; gap: 6px; }
.topbar a { color: #ffffff !important; text-decoration: none; }
.topbar a:hover { color: #e6c458 !important; }
.topbar-badge {
    display: inline-flex;
    align-items: center;
    gap: 6px;
    background: rgba(34, 197, 94, 0.2);
    color: #22c55e !important;
    padding: 3px 10px;
    border-radius: 12px;
    font-size: 10.5px;
    font-weight: 800;
    border: 1px solid rgba(34, 197, 94, 0.4);
}
.topbar-badge::before {
    content: '';
    width: 6px;
    height: 6px;
    border-radius: 50%;
    background: #22c55e;
    animation: pulseGreen 1.5s infinite;
}
@keyframes pulseGreen {
    0%, 100% { box-shadow: 0 0 0 0 rgba(34,197,94,0.7); opacity: 1; }
    50% { box-shadow: 0 0 0 8px rgba(34,197,94,0); opacity: 0.7; }
}
.topbar-lang {
    background: rgba(230,196,88,0.15);
    border: 1px solid rgba(230,196,88,0.3);
    color: #e6c458 !important;
    padding: 3px 10px;
    border-radius: 4px;
    font-size: 10.5px;
    font-weight: 700;
    text-decoration: none;
}

/* ============================================
   HEADER
   ============================================ */
.header-wrap {
    background: #ffffff;
    padding: 18px 16px;
    border-bottom: 1px solid #e5ebe7;
    box-shadow: 0 2px 12px rgba(0,0,0,0.03);
    position: relative;
    z-index: 100;
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
    border-radius: 14px;
    background: linear-gradient(135deg, #ffffff, #f8faf9);
    display: flex; align-items: center; justify-content: center;
    overflow: hidden;
    flex-shrink: 0;
    border: 2px solid #e5ebe7;
    padding: 6px;
    box-shadow: 0 4px 12px rgba(13,94,58,0.08);
    transition: all 0.3s ease;
}
.header-logo:hover { transform: scale(1.05) rotate(-3deg); box-shadow: 0 8px 24px rgba(13,94,58,0.2); }
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
    padding: 9px 16px;
    border-radius: 10px;
    font-size: 12px;
    font-weight: 700;
    text-decoration: none;
    transition: all 0.25s;
}
.header-action-btn:hover {
    background: #0d5e3a;
    color: #ffffff !important;
    border-color: #0d5e3a;
    transform: translateY(-2px);
    box-shadow: 0 6px 16px rgba(13,94,58,0.25);
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
    box-shadow: 0 8px 24px rgba(13,94,58,0.35);
}

/* ============================================
   NAVBAR
   ============================================ */
.navbar {
    background: linear-gradient(180deg, #ffffff 0%, #fbfcfb 100%) !important;
    padding: 0 16px;
    border-top: 3px solid transparent;
    border-image: linear-gradient(90deg, #0d5e3a, #c9a227, #0d5e3a) 1;
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
.nav-link:hover { color: #0d5e3a !important; }
.nav-link:hover::after { width: 60%; }
.nav-link-active { color: #0d5e3a !important; font-weight: 800; }
.nav-link-active::after { width: 80%; }

/* ============================================
   RUNNING TEXT
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
    display: flex;
    align-items: center;
    gap: 6px;
}
.running-label::before {
    content: '';
    width: 6px;
    height: 6px;
    border-radius: 50%;
    background: #ef4444;
    animation: pulseRed 1.5s infinite;
}
@keyframes pulseRed {
    0%, 100% { opacity: 1; }
    50% { opacity: 0.4; }
}
.running-scroll-wrap { flex: 1; overflow: hidden; white-space: nowrap; min-width: 0; }
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
   HERO
   ============================================ */
.hero-ultra {
    position: relative;
    min-height: 620px;
    overflow: hidden;
    display: flex;
    align-items: center;
    background: #000;
}
.hero-ultra-bg {
    position: absolute;
    top: 0; left: 0;
    width: 100%; height: 100%;
    background-size: cover;
    background-position: center;
    animation: heroZoomUltra 25s ease-in-out infinite;
}
@keyframes heroZoomUltra {
    0%, 100% { transform: scale(1); }
    50% { transform: scale(1.1) translate(-1%, -1%); }
}
.hero-ultra-overlay {
    position: absolute;
    top: 0; left: 0;
    width: 100%; height: 100%;
    background: 
        linear-gradient(120deg, rgba(8,61,38,0.95) 0%, rgba(13,94,58,0.75) 45%, rgba(8,61,38,0.5) 100%),
        radial-gradient(ellipse at 20% 30%, rgba(230,196,88,0.15) 0%, transparent 60%),
        radial-gradient(ellipse at 80% 70%, rgba(230,196,88,0.1) 0%, transparent 50%);
}
.hero-ultra-grid {
    position: absolute;
    top: 0; left: 0;
    width: 100%; height: 100%;
    background-image: 
        linear-gradient(rgba(230,196,88,0.03) 1px, transparent 1px),
        linear-gradient(90deg, rgba(230,196,88,0.03) 1px, transparent 1px);
    background-size: 50px 50px;
    opacity: 0.5;
    pointer-events: none;
}
.hero-ultra-content {
    position: relative;
    z-index: 3;
    max-width: 1400px;
    margin: 0 auto;
    width: 92%;
    padding: 80px 0;
    color: #ffffff;
}
.hero-ultra-kicker {
    display: inline-flex;
    align-items: center;
    gap: 10px;
    background: rgba(230,196,88,0.15);
    border: 1px solid rgba(230,196,88,0.4);
    color: #e6c458 !important;
    padding: 10px 22px;
    border-radius: 30px;
    font-size: 11.5px;
    font-weight: 800;
    letter-spacing: 2px;
    text-transform: uppercase;
    margin-bottom: 28px;
    backdrop-filter: blur(20px);
}
.hero-ultra-kicker::before {
    content: '';
    width: 8px;
    height: 8px;
    border-radius: 50%;
    background: #e6c458;
    animation: pulseDotUltra 2s infinite;
    box-shadow: 0 0 12px #e6c458;
}
@keyframes pulseDotUltra {
    0%, 100% { opacity: 1; transform: scale(1); }
    50% { opacity: 0.7; transform: scale(1.4); }
}
.hero-ultra-title {
    font-family: 'Plus Jakarta Sans', sans-serif;
    font-size: clamp(32px, 5.5vw, 72px);
    font-weight: 900;
    line-height: 1.02;
    letter-spacing: -2px;
    margin-bottom: 26px;
    color: #ffffff !important;
    text-shadow: 0 6px 60px rgba(0,0,0,0.5);
    max-width: 950px;
}
.hero-ultra-title span {
    background: linear-gradient(135deg, #e6c458 0%, #f5e090 30%, #c9a227 70%, #e6c458 100%);
    background-size: 200% auto;
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    animation: gradientShift 5s ease infinite;
}
@keyframes gradientShift {
    0%, 100% { background-position: 0% center; }
    50% { background-position: 100% center; }
}
.hero-ultra-sub {
    font-size: clamp(14px, 1.6vw, 19px);
    line-height: 1.75;
    color: rgba(255,255,255,0.92) !important;
    max-width: 720px;
    margin-bottom: 40px;
}
.hero-ultra-buttons { display: flex; flex-wrap: wrap; gap: 14px; margin-bottom: 56px; }
.hero-ultra-btn {
    display: inline-flex;
    align-items: center;
    gap: 10px;
    padding: 16px 32px;
    background: linear-gradient(135deg, #c9a227, #e6c458);
    color: #083d26 !important;
    text-decoration: none !important;
    font-weight: 800;
    font-size: 13.5px;
    border-radius: 10px;
    letter-spacing: 0.6px;
    text-transform: uppercase;
    box-shadow: 0 10px 30px rgba(201,162,39,0.45);
    transition: all 0.35s cubic-bezier(0.4, 0, 0.2, 1);
    border: 2px solid transparent;
    position: relative;
    overflow: hidden;
}
.hero-ultra-btn::before {
    content: '';
    position: absolute;
    top: 0; left: -100%;
    width: 100%; height: 100%;
    background: linear-gradient(90deg, transparent, rgba(255,255,255,0.5), transparent);
    transition: left 0.6s ease;
}
.hero-ultra-btn:hover::before { left: 100%; }
.hero-ultra-btn:hover { transform: translateY(-4px); box-shadow: 0 16px 40px rgba(201,162,39,0.6); }
.hero-ultra-btn-outline {
    background: rgba(255,255,255,0.08);
    color: #ffffff !important;
    border: 2px solid rgba(255,255,255,0.5);
    backdrop-filter: blur(15px);
    box-shadow: none;
}
.hero-ultra-btn-outline:hover { background: rgba(255,255,255,0.2); border-color: #e6c458; transform: translateY(-4px); }

.hero-ultra-stats { display: grid; grid-template-columns: repeat(4, 1fr); gap: 16px; max-width: 900px; }
.hero-stat-ultra {
    background: rgba(255,255,255,0.06);
    backdrop-filter: blur(20px);
    border: 1px solid rgba(255,255,255,0.15);
    padding: 20px 22px;
    border-radius: 16px;
    transition: all 0.35s ease;
    position: relative;
    overflow: hidden;
}
.hero-stat-ultra::before {
    content: '';
    position: absolute;
    top: 0; left: 0; right: 0;
    height: 3px;
    background: linear-gradient(90deg, transparent, #e6c458, transparent);
    transform: translateX(-100%);
    transition: transform 0.6s ease;
}
.hero-stat-ultra:hover::before { transform: translateX(100%); }
.hero-stat-ultra:hover { background: rgba(230,196,88,0.12); border-color: rgba(230,196,88,0.4); transform: translateY(-4px); }
.hero-stat-num-ultra {
    font-family: 'Plus Jakarta Sans', sans-serif;
    color: #e6c458 !important;
    font-size: 30px;
    font-weight: 900;
    line-height: 1;
    display: block;
}
.hero-stat-label-ultra {
    color: rgba(255,255,255,0.85) !important;
    font-size: 10.5px;
    margin-top: 8px;
    text-transform: uppercase;
    letter-spacing: 0.8px;
    font-weight: 700;
}

/* ============================================
   MITRA MARQUEE
   ============================================ */
.mitra-section {
    background: #ffffff;
    padding: 24px 0;
    border-bottom: 1px solid #e5ebe7;
    overflow: hidden;
}
.mitra-label {
    text-align: center;
    font-size: 10.5px;
    color: #4a5a55 !important;
    font-weight: 800;
    letter-spacing: 2px;
    text-transform: uppercase;
    margin-bottom: 16px;
}
.mitra-track {
    display: flex;
    gap: 40px;
    animation: mitraScroll 30s linear infinite;
    width: max-content;
}
@keyframes mitraScroll {
    0% { transform: translateX(0); }
    100% { transform: translateX(-50%); }
}
.mitra-item {
    display: inline-flex;
    align-items: center;
    gap: 10px;
    font-family: 'Plus Jakarta Sans', sans-serif;
    font-size: 14px;
    font-weight: 800;
    color: #083d26 !important;
    white-space: nowrap;
    padding: 8px 16px;
    background: #f8faf9;
    border-radius: 10px;
    border: 1px solid #e5ebe7;
}

/* ============================================
   SECTIONS
   ============================================ */
.page-container { width: 92%; max-width: 1400px; margin: 0 auto; padding: 60px 0; }
.section-header-modern { text-align: center; margin-bottom: 50px; }
.section-kicker-modern {
    display: inline-block;
    color: #c9a227 !important;
    font-size: 11.5px;
    font-weight: 800;
    letter-spacing: 3px;
    text-transform: uppercase;
    margin-bottom: 14px;
    position: relative;
    padding: 0 40px;
}
.section-kicker-modern::before,
.section-kicker-modern::after {
    content: '';
    position: absolute;
    top: 50%;
    width: 28px;
    height: 2px;
    background: linear-gradient(90deg, transparent, #c9a227);
}
.section-kicker-modern::before { left: 0; }
.section-kicker-modern::after { right: 0; transform: scaleX(-1); }
.section-title-modern {
    font-family: 'Plus Jakarta Sans', sans-serif;
    font-size: clamp(24px, 3.2vw, 38px);
    font-weight: 900;
    color: #083d26 !important;
    letter-spacing: -1px;
    line-height: 1.15;
    margin: 0 0 14px;
}
.section-desc-modern { color: #4a5a55 !important; font-size: 14.5px; line-height: 1.75; max-width: 720px; margin: 0 auto; }

/* ============================================
   QUICK ACCESS
   ============================================ */
.quick-access-glass {
    background: linear-gradient(135deg, #f8faf9 0%, #ffffff 100%);
    padding: 40px 16px;
    border-bottom: 1px solid #e5ebe7;
}
.quick-access-inner { max-width: 1400px; margin: 0 auto; }
.quick-card-glass {
    display: flex;
    flex-direction: column;
    align-items: center;
    text-align: center;
    background: linear-gradient(135deg, #ffffff, #f8faf9);
    border: 1px solid #e5ebe7;
    border-radius: 20px;
    padding: 32px 20px;
    text-decoration: none !important;
    color: #0a1f18 !important;
    transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
    position: relative;
    overflow: hidden;
    box-shadow: 0 4px 16px rgba(0,0,0,0.03);
}
.quick-card-glass:hover { transform: translateY(-10px); box-shadow: 0 30px 60px rgba(13,94,58,0.18); border-color: #c9a227; }
.quick-icon-glass {
    width: 72px; height: 72px; border-radius: 20px;
    display: flex; align-items: center; justify-content: center;
    font-size: 32px; margin-bottom: 18px;
    background: linear-gradient(135deg, #e8f5ef, #d1e8dd);
    color: #0d5e3a !important;
    transition: all 0.5s cubic-bezier(0.4, 0, 0.2, 1);
    box-shadow: 0 8px 24px rgba(13,94,58,0.1);
}
.quick-card-glass:hover .quick-icon-glass {
    background: linear-gradient(135deg, #c9a227, #e6c458);
    color: #ffffff !important;
    transform: scale(1.1) rotate(-10deg);
    box-shadow: 0 12px 32px rgba(201,162,39,0.4);
}
.quick-title-glass { font-family: 'Plus Jakarta Sans', sans-serif; font-size: 15px; font-weight: 800; color: #083d26 !important; margin: 0 0 6px; }
.quick-desc-glass { font-size: 12px; color: #4a5a55 !important; font-weight: 500; }

/* ============================================
   SAMBUTAN
   ============================================ */
.sambutan-section-ultra {
    background: linear-gradient(135deg, #ffffff 0%, #f8faf9 50%, #faf6e8 100%);
    padding: 80px 16px;
    position: relative;
    overflow: hidden;
}
.sambutan-section-ultra::before {
    content: '';
    position: absolute;
    top: -50%; right: -20%;
    width: 800px; height: 800px;
    background: radial-gradient(circle, rgba(13,94,58,0.06) 0%, transparent 60%);
    border-radius: 50%;
}
.sambutan-inner-ultra {
    max-width: 1400px;
    margin: 0 auto;
    display: grid;
    grid-template-columns: 340px 1fr;
    gap: 60px;
    align-items: start;
    position: relative;
    z-index: 2;
}
.sambutan-photo-wrap-ultra { position: relative; text-align: center; }
.sambutan-photo-ultra {
    width: 100%;
    max-width: 340px;
    aspect-ratio: 3/4;
    object-fit: cover;
    border-radius: 20px;
    box-shadow: 0 30px 80px rgba(13,94,58,0.3);
    border: 5px solid #ffffff;
    position: relative;
    z-index: 3;
}
.sambutan-photo-info-ultra {
    margin-top: 28px;
    background: #ffffff;
    border: 1px solid #e5ebe7;
    border-radius: 16px;
    padding: 20px;
    box-shadow: 0 12px 32px rgba(0,0,0,0.06);
}
.sambutan-nama-ultra {
    font-family: 'Plus Jakarta Sans', sans-serif;
    font-size: 17px;
    font-weight: 900;
    color: #083d26 !important;
    text-transform: uppercase;
    margin: 0 0 5px;
}
.sambutan-jabatan-ultra { color: #c9a227 !important; font-size: 12px; font-weight: 800; text-transform: uppercase; letter-spacing: 1.2px; }
.sambutan-content-ultra { padding-top: 24px; }
.sambutan-assalam-ultra {
    font-family: 'Plus Jakarta Sans', sans-serif;
    font-size: 17px;
    font-weight: 700;
    color: #0d5e3a !important;
    margin-bottom: 24px;
    padding: 14px 20px;
    background: linear-gradient(90deg, #e8f5ef, #ffffff);
    border-radius: 12px;
    border-left: 4px solid #0d5e3a;
}
.sambutan-text-ultra { color: #0a1f18 !important; font-size: 14.5px; line-height: 1.95; margin-bottom: 20px; }
.sambutan-quote-ultra {
    border-left: 5px solid #c9a227;
    background: linear-gradient(90deg, #faf6e8, #ffffff 60%);
    padding: 24px 28px;
    border-radius: 0 16px 16px 0;
    margin: 28px 0;
    font-family: 'Plus Jakarta Sans', sans-serif;
    font-size: 16px;
    font-weight: 600;
    font-style: italic;
    color: #083d26 !important;
    line-height: 1.7;
}
.sambutan-salam-ultra { margin-top: 32px; padding-top: 24px; border-top: 2px dashed #e5ebe7; }
.sambutan-salam-line-ultra { color: #4a5a55 !important; font-size: 13.5px; margin: 0 0 6px; }
.sambutan-salam-nama-ultra { font-family: 'Plus Jakarta Sans', sans-serif; font-size: 16px; font-weight: 900; color: #083d26 !important; text-transform: uppercase; margin: 10px 0 4px; }
.sambutan-salam-jabatan-ultra { color: #c9a227 !important; font-size: 12.5px; font-weight: 700; }

/* ============================================
   TRENDING
   ============================================ */
.trending-main {
    background: #ffffff;
    border: 1px solid #e5ebe7;
    border-radius: 20px;
    overflow: hidden;
    transition: all 0.4s ease;
}
.trending-main:hover { transform: translateY(-6px); box-shadow: 0 30px 60px rgba(13,94,58,0.18); border-color: #c9a227; }
.trending-main-img { position: relative; width: 100%; height: 380px; overflow: hidden; }
.trending-main-img img { width: 100%; height: 100%; object-fit: cover; }
.trending-main-img::after {
    content: '';
    position: absolute;
    bottom: 0; left: 0; right: 0;
    height: 60%;
    background: linear-gradient(180deg, transparent, rgba(0,0,0,0.7));
}
.trending-badge {
    position: absolute;
    top: 20px; left: 20px;
    background: linear-gradient(135deg, #ef4444, #dc2626);
    color: #ffffff !important;
    padding: 8px 16px;
    border-radius: 20px;
    font-size: 11px;
    font-weight: 800;
    text-transform: uppercase;
    z-index: 2;
    box-shadow: 0 4px 16px rgba(239,68,68,0.4);
}
.trending-main-content { padding: 28px; }
.trending-main-cat {
    display: inline-block;
    background: linear-gradient(135deg, #c9a227, #e6c458);
    color: #083d26 !important;
    padding: 5px 14px;
    border-radius: 20px;
    font-size: 10.5px;
    font-weight: 800;
    text-transform: uppercase;
    margin-bottom: 14px;
}
.trending-main-title {
    font-family: 'Plus Jakarta Sans', sans-serif;
    font-size: 24px;
    font-weight: 900;
    color: #083d26 !important;
    line-height: 1.35;
    margin: 0 0 12px;
}
.trending-main-desc { color: #4a5a55 !important; font-size: 14px; line-height: 1.75; margin: 0 0 18px; }
.trending-main-meta { display: flex; gap: 20px; color: #c9a227 !important; font-size: 11.5px; font-weight: 800; text-transform: uppercase; }
.trending-list { display: flex; flex-direction: column; gap: 16px; }
.trending-item {
    display: flex;
    gap: 14px;
    background: #ffffff;
    border: 1px solid #e5ebe7;
    border-radius: 16px;
    padding: 16px;
    text-decoration: none !important;
    color: inherit;
    transition: all 0.3s ease;
    position: relative;
}
.trending-item:hover { border-color: #c9a227; transform: translateX(6px); box-shadow: 0 12px 32px rgba(13,94,58,0.12); }
.trending-rank {
    position: absolute;
    top: -8px; left: -8px;
    width: 32px; height: 32px;
    background: linear-gradient(135deg, #0d5e3a, #14734a);
    color: #ffffff !important;
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    font-family: 'Plus Jakarta Sans', sans-serif;
    font-size: 14px;
    font-weight: 900;
    border: 3px solid #ffffff;
    box-shadow: 0 4px 12px rgba(13,94,58,0.3);
}
.trending-item:nth-child(1) .trending-rank { background: linear-gradient(135deg, #ef4444, #dc2626); }
.trending-item:nth-child(2) .trending-rank { background: linear-gradient(135deg, #f59e0b, #d97706); }
.trending-item:nth-child(3) .trending-rank { background: linear-gradient(135deg, #c9a227, #e6c458); }
.trending-thumb { width: 80px; height: 80px; border-radius: 12px; object-fit: cover; flex-shrink: 0; }
.trending-info { flex: 1; min-width: 0; }
.trending-info-cat { color: #c9a227 !important; font-size: 10px; font-weight: 800; text-transform: uppercase; margin-bottom: 6px; }
.trending-info-title {
    font-family: 'Plus Jakarta Sans', sans-serif;
    font-size: 13px;
    font-weight: 800;
    color: #083d26 !important;
    line-height: 1.4;
    margin: 0 0 6px;
    display: -webkit-box;
    -webkit-line-clamp: 2;
    -webkit-box-orient: vertical;
    overflow: hidden;
}
.trending-info-meta { color: #4a5a55 !important; font-size: 10.5px; font-weight: 600; }

/* ============================================
   WARTA CARD
   ============================================ */
.warta-card-ultra {
    background: #ffffff;
    border: 1px solid #e5ebe7;
    border-radius: 20px;
    overflow: hidden;
    text-decoration: none !important;
    color: inherit;
    transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
    display: flex;
    flex-direction: column;
    position: relative;
}
.warta-card-ultra:hover { transform: translateY(-10px); box-shadow: 0 30px 70px rgba(13,94,58,0.2); border-color: rgba(201,162,39,0.4); }
.warta-card-ultra-img { position: relative; width: 100%; height: 220px; overflow: hidden; }
.warta-card-ultra-img img { width: 100%; height: 100%; object-fit: cover; transition: transform 0.8s ease; }
.warta-card-ultra:hover .warta-card-ultra-img img { transform: scale(1.12); }
.warta-card-ultra-cat {
    position: absolute;
    top: 14px; left: 14px;
    background: linear-gradient(135deg, #c9a227, #e6c458);
    color: #083d26 !important;
    padding: 6px 14px;
    border-radius: 20px;
    font-size: 10.5px;
    font-weight: 800;
    text-transform: uppercase;
    z-index: 2;
    box-shadow: 0 4px 12px rgba(201,162,39,0.4);
}
.warta-card-ultra-views {
    position: absolute;
    top: 14px; right: 14px;
    background: rgba(0,0,0,0.6);
    color: #ffffff !important;
    padding: 6px 12px;
    border-radius: 20px;
    font-size: 10.5px;
    font-weight: 800;
    z-index: 2;
    backdrop-filter: blur(10px);
}
.warta-card-ultra-body { padding: 24px; flex: 1; display: flex; flex-direction: column; }
.warta-card-ultra-date { display: inline-flex; align-items: center; gap: 6px; color: #c9a227 !important; font-size: 11px; font-weight: 800; text-transform: uppercase; margin-bottom: 12px; }
.warta-card-ultra-title {
    font-family: 'Plus Jakarta Sans', sans-serif;
    font-size: 16.5px;
    font-weight: 800;
    color: #083d26 !important;
    line-height: 1.4;
    margin: 0 0 12px;
}
.warta-card-ultra-desc { color: #4a5a55 !important; font-size: 13px; line-height: 1.65; margin: 0 0 16px; flex: 1; }
.warta-card-ultra-more { display: inline-flex; align-items: center; gap: 6px; color: #0d5e3a !important; font-size: 12px; font-weight: 800; text-transform: uppercase; }

/* ============================================
   WIDGET
   ============================================ */
.widget-ultra {
    background: #ffffff;
    border: 1px solid #e5ebe7;
    border-radius: 20px;
    overflow: hidden;
    margin-bottom: 24px;
    box-shadow: 0 4px 20px rgba(0,0,0,0.04);
}
.widget-ultra-head {
    background: linear-gradient(135deg, #0d5e3a, #14734a);
    color: #ffffff !important;
    padding: 18px 22px;
    font-family: 'Plus Jakarta Sans', sans-serif;
    font-size: 13.5px;
    font-weight: 800;
    text-transform: uppercase;
    border-bottom: 3px solid #c9a227;
}
.agenda-item-ultra { display: flex; gap: 16px; padding: 18px 22px; border-bottom: 1px solid #e5ebe7; transition: all 0.25s ease; }
.agenda-item-ultra:last-child { border-bottom: none; }
.agenda-item-ultra:hover { background: #f8faf9; padding-left: 26px; }
.agenda-date-ultra {
    width: 64px; height: 72px;
    background: linear-gradient(135deg, #0d5e3a, #14734a);
    color: #ffffff !important;
    border-radius: 12px;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    flex-shrink: 0;
    position: relative;
    box-shadow: 0 6px 16px rgba(13,94,58,0.25);
}
.agenda-date-ultra::before {
    content: '';
    position: absolute;
    top: 0; left: 0; right: 0;
    height: 4px;
    background: #c9a227;
    border-radius: 12px 12px 0 0;
}
.agenda-day-ultra { font-family: 'Plus Jakarta Sans', sans-serif; font-size: 26px; font-weight: 900; line-height: 1; color: #ffffff !important; }
.agenda-month-ultra { font-size: 9.5px; font-weight: 800; color: #ffffff !important; margin-top: 4px; }
.agenda-content-ultra { flex: 1; min-width: 0; }
.agenda-title-ultra { color: #083d26 !important; font-family: 'Plus Jakarta Sans', sans-serif; font-size: 13.5px; font-weight: 800; line-height: 1.4; margin: 0 0 6px; }
.agenda-desc-ultra { color: #4a5a55 !important; font-size: 11.5px; line-height: 1.55; margin: 0 0 8px; display: -webkit-box; -webkit-line-clamp: 2; -webkit-box-orient: vertical; overflow: hidden; }
.agenda-footer-ultra { display: inline-flex; align-items: center; gap: 6px; color: #c9a227 !important; font-size: 10.5px; font-weight: 800; text-transform: uppercase; padding: 4px 10px; background: #faf6e8; border-radius: 8px; }

.kesekret-item-ultra { display: flex; gap: 14px; padding: 16px 22px; border-bottom: 1px solid #e5ebe7; transition: all 0.25s ease; }
.kesekret-item-ultra:last-child { border-bottom: none; }
.kesekret-item-ultra:hover { background: #f8faf9; padding-left: 26px; }
.kesekret-icon-ultra {
    width: 44px; height: 44px;
    border-radius: 12px;
    background: linear-gradient(135deg, #e8f5ef, #d1e8dd);
    color: #0d5e3a !important;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 20px;
    flex-shrink: 0;
}
.kesekret-title-ultra { color: #083d26 !important; font-size: 13px; font-weight: 700; line-height: 1.45; margin: 0 0 5px; }
.kesekret-date-ultra { color: #c9a227 !important; font-size: 10.5px; font-weight: 800; }

/* ============================================
   STATS SECTION
   ============================================ */
.stats-section-ultra {
    background: linear-gradient(135deg, #062b1b 0%, #0d5e3a 50%, #062b1b 100%);
    padding: 80px 16px;
    position: relative;
    overflow: hidden;
}
.stats-inner-ultra { max-width: 1400px; margin: 0 auto; position: relative; z-index: 2; }
.stats-grid-ultra { display: grid; grid-template-columns: repeat(4, 1fr); gap: 24px; }
.stat-item-ultra {
    text-align: center;
    padding: 36px 24px;
    background: rgba(255,255,255,0.06);
    backdrop-filter: blur(15px);
    border: 1px solid rgba(255,255,255,0.12);
    border-radius: 20px;
    transition: all 0.4s ease;
}
.stat-item-ultra:hover { background: rgba(230,196,88,0.12); border-color: rgba(230,196,88,0.4); transform: translateY(-8px); }
.stat-icon-ultra { font-size: 32px; margin-bottom: 12px; display: block; }
.stat-num-ultra { font-family: 'Plus Jakarta Sans', sans-serif; color: #e6c458 !important; font-size: 44px; font-weight: 900; line-height: 1; margin-bottom: 10px; }
.stat-label-ultra { color: #ffffff !important; font-size: 12.5px; font-weight: 700; text-transform: uppercase; letter-spacing: 1.2px; }

/* ============================================
   LAYANAN CARD
   ============================================ */
.layanan-card-ultra {
    background: #ffffff;
    border: 1px solid #e5ebe7;
    border-radius: 20px;
    padding: 32px 24px;
    text-align: center;
    text-decoration: none !important;
    color: inherit;
    transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
    position: relative;
    overflow: hidden;
}
.layanan-card-ultra:hover { transform: translateY(-10px); box-shadow: 0 30px 60px rgba(13,94,58,0.18); border-color: rgba(201,162,39,0.3); }
.layanan-icon-ultra {
    width: 80px; height: 80px;
    margin: 0 auto 20px;
    border-radius: 24px;
    background: linear-gradient(135deg, #e8f5ef, #d1e8dd);
    color: #0d5e3a !important;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 36px;
    transition: all 0.5s cubic-bezier(0.4, 0, 0.2, 1);
}
.layanan-card-ultra:hover .layanan-icon-ultra {
    background: linear-gradient(135deg, #c9a227, #e6c458);
    color: #ffffff !important;
    transform: scale(1.1) rotate(-8deg);
}
.layanan-title-ultra { font-family: 'Plus Jakarta Sans', sans-serif; font-size: 15px; font-weight: 800; color: #083d26 !important; margin: 0 0 8px; }
.layanan-desc-ultra { color: #4a5a55 !important; font-size: 12px; line-height: 1.55; }

/* ============================================
   FOOTER
   ============================================ */
.footer-ultra {
    background: linear-gradient(180deg, #062b1b 0%, #041f13 100%);
    color: #ffffff !important;
    padding: 70px 16px 0;
    position: relative;
    overflow: hidden;
}
.footer-ultra::before {
    content: '';
    position: absolute;
    top: 0; left: 0; right: 0;
    height: 5px;
    background: linear-gradient(90deg, #0d5e3a, #c9a227, #e6c458, #c9a227, #0d5e3a);
    background-size: 200% auto;
    animation: gradientShift 5s linear infinite;
}
.footer-ultra * { color: #ffffff !important; }
.footer-inner-ultra { max-width: 1400px; margin: 0 auto; position: relative; z-index: 2; }
.footer-grid-ultra { display: grid; grid-template-columns: 1.8fr 1fr 1fr 1.2fr; gap: 44px; padding-bottom: 44px; }
.footer-col-ultra h4 {
    color: #ffffff !important;
    font-size: 13.5px;
    font-weight: 800;
    margin: 0 0 22px;
    text-transform: uppercase;
    letter-spacing: 1.2px;
    position: relative;
    padding-bottom: 14px;
}
.footer-col-ultra h4::after {
    content: '';
    position: absolute;
    bottom: 0; left: 0;
    width: 36px;
    height: 3px;
    background: linear-gradient(90deg, #c9a227, #e6c458);
}
.footer-col-ultra p { color: rgba(255,255,255,0.7) !important; font-size: 12.5px; line-height: 1.9; margin: 0 0 8px; }
.footer-col-ultra a { display: block; color: rgba(255,255,255,0.7) !important; font-size: 12.5px; line-height: 2.15; text-decoration: none; transition: all 0.25s ease; }
.footer-col-ultra a:hover { color: #e6c458 !important; padding-left: 8px; }
.footer-brand-ultra { display: flex; align-items: center; gap: 16px; margin-bottom: 22px; }
.footer-logo-ultra {
    width: 60px; height: 60px;
    background: #ffffff;
    border-radius: 14px;
    display: flex;
    align-items: center;
    justify-content: center;
    overflow: hidden;
    padding: 8px;
    box-shadow: 0 10px 30px rgba(0,0,0,0.4);
}
.footer-logo-ultra img { width: 100%; height: 100%; object-fit: contain; }
.footer-brand-title-ultra { color: #ffffff !important; font-family: 'Plus Jakarta Sans', sans-serif; font-size: 15px; font-weight: 800; text-transform: uppercase; }
.footer-brand-sub-ultra { color: #e6c458 !important; font-size: 10px; letter-spacing: 1.2px; margin-top: 4px; font-weight: 800; }
.footer-social-ultra { display: flex; gap: 10px; margin-top: 22px; }
.footer-social-item-ultra {
    width: 42px; height: 42px;
    background: rgba(255,255,255,0.08);
    border: 1px solid rgba(255,255,255,0.15);
    border-radius: 12px;
    color: #ffffff !important;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 15px;
    text-decoration: none;
    transition: all 0.3s;
}
.footer-social-item-ultra:hover { background: linear-gradient(135deg, #c9a227, #e6c458); color: #083d26 !important; transform: translateY(-5px); }
.footer-bottom-ultra { border-top: 1px solid rgba(255,255,255,0.08); padding: 26px 0; display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 14px; font-size: 11.5px; color: rgba(255,255,255,0.5) !important; }
.footer-bottom-ultra * { color: rgba(255,255,255,0.5) !important; }

/* ============================================
   CHAT WIDGET
   ============================================ */
.chat-widget {
    position: fixed;
    bottom: 24px; right: 24px;
    z-index: 9999;
    display: flex;
    flex-direction: column;
    align-items: flex-end;
    gap: 12px;
}
.chat-btn {
    width: 68px; height: 68px;
    border-radius: 50%;
    background: linear-gradient(135deg, #0d5e3a, #14734a);
    color: #ffffff !important;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 28px;
    text-decoration: none;
    box-shadow: 0 14px 40px rgba(13,94,58,0.45);
    border: 4px solid #ffffff;
    transition: all 0.3s ease;
    animation: chatPulse 2.5s infinite;
}
@keyframes chatPulse {
    0%, 100% { box-shadow: 0 14px 40px rgba(13,94,58,0.45), 0 0 0 0 rgba(13,94,58,0.5); }
    50% { box-shadow: 0 14px 40px rgba(13,94,58,0.45), 0 0 0 18px rgba(13,94,58,0); }
}
.chat-btn:hover { transform: scale(1.1) rotate(-10deg); background: linear-gradient(135deg, #c9a227, #e6c458); color: #083d26 !important; }
.chat-label {
    background: #ffffff;
    color: #083d26 !important;
    padding: 10px 18px;
    border-radius: 20px;
    font-size: 12.5px;
    font-weight: 800;
    box-shadow: 0 8px 24px rgba(0,0,0,0.15);
    border: 2px solid #c9a227;
}

/* ============================================
   FORM
   ============================================ */
.stButton > button {
    background: linear-gradient(135deg, #0d5e3a, #14734a) !important;
    color: #ffffff !important;
    border: none !important;
    border-radius: 10px !important;
    font-weight: 700 !important;
    box-shadow: 0 6px 16px rgba(13,94,58,0.25) !important;
}
.stButton > button:hover { background: linear-gradient(135deg, #14734a, #c9a227) !important; transform: translateY(-2px); }
div[data-testid="stForm"] { background: #ffffff; border: 1px solid #e5ebe7; border-radius: 20px; padding: 28px !important; }
.stTextInput input, .stTextArea textarea, div[data-baseweb="select"] > div { border-radius: 10px !important; border-color: #e5ebe7 !important; color: #000000 !important; }

.stTabs [data-baseweb="tab-list"] { gap: 4px; background: transparent; border-bottom: 2px solid #e5ebe7; }
.stTabs [data-baseweb="tab"] { background: transparent; border-radius: 10px 10px 0 0; padding: 14px 22px; color: #4a5a55 !important; font-weight: 700; font-size: 13px; }
.stTabs [aria-selected="true"] { background: linear-gradient(180deg, #f0f6f2, transparent) !important; color: #0d5e3a !important; border-bottom: 3px solid #0d5e3a; }

/* ============================================
   TABLET
   ============================================ */
@media (max-width: 1100px) {
    .quick-grid-glass { grid-template-columns: repeat(2, 1fr); }
    .warta-grid-ultra { grid-template-columns: repeat(2, 1fr); }
    .stats-grid-ultra { grid-template-columns: repeat(2, 1fr); }
    .layanan-grid-ultra { grid-template-columns: repeat(2, 1fr); }
    .trending-grid { grid-template-columns: 1fr; }
    .footer-grid-ultra { grid-template-columns: 1fr 1fr; gap: 32px; }
    .sambutan-inner-ultra { grid-template-columns: 280px 1fr; gap: 40px; }
    .hero-ultra-stats { grid-template-columns: repeat(2, 1fr); max-width: 600px; }
}

/* ============================================
   MOBILE (≤ 768px)
   ============================================ */
@media (max-width: 768px) {
    .topbar { flex-direction: column; gap: 6px; text-align: center; padding: 8px 12px; }
    .topbar-left, .topbar-right { justify-content: center; gap: 8px; font-size: 10.5px; }
    
    .header-wrap { padding: 12px 12px; }
    .header-logo { width: 50px; height: 50px; border-radius: 10px; }
    .header-text-title { font-size: 13px; }
    .header-text-sub { font-size: 9px; }
    .header-actions { width: 100%; justify-content: center; margin-top: 10px; padding-top: 10px; border-top: 1px solid #e5ebe7; gap: 6px; }
    .header-action-btn { font-size: 10.5px; padding: 7px 12px; }
    
    .navbar { padding: 0 8px; }
    .navbar-inner { gap: 0; padding: 2px 0; }
    .nav-link { font-size: 10px !important; padding: 12px 8px !important; flex: 1 1 calc(25% - 2px); max-width: calc(25% - 2px); text-align: center; letter-spacing: 0 !important; min-width: 0; }
    
    .running-text-bar { padding: 10px 12px; gap: 10px; }
    .running-label { font-size: 9.5px; padding: 5px 10px; }
    .running-scroll { font-size: 11.5px; }
    
    .hero-ultra { min-height: 480px; }
    .hero-ultra-content { padding: 40px 0; }
    .hero-ultra-kicker { font-size: 9.5px; padding: 6px 12px; letter-spacing: 1.2px; margin-bottom: 16px; }
    .hero-ultra-title { font-size: 24px; margin-bottom: 14px; letter-spacing: -0.6px; }
    .hero-ultra-sub { font-size: 12.5px; margin-bottom: 22px; line-height: 1.6; }
    .hero-ultra-buttons { gap: 6px; margin-bottom: 28px; }
    .hero-ultra-btn { padding: 11px 20px; font-size: 11px; }
    .hero-ultra-stats { grid-template-columns: repeat(2, 1fr); gap: 8px; }
    .hero-stat-ultra { padding: 12px 14px; }
    .hero-stat-num-ultra { font-size: 20px; }
    .hero-stat-label-ultra { font-size: 8.5px; }
    
    .quick-access-glass { padding: 24px 12px; }
    .quick-grid-glass { grid-template-columns: 1fr 1fr; gap: 10px; }
    .quick-card-glass { padding: 18px 12px; }
    .quick-icon-glass { width: 52px; height: 52px; font-size: 22px; margin-bottom: 12px; }
    .quick-title-glass { font-size: 12px; }
    .quick-desc-glass { font-size: 10px; }
    
    .page-container { width: 95%; padding: 36px 0; }
    .section-header-modern { margin-bottom: 28px; }
    .section-kicker-modern { font-size: 10px; letter-spacing: 2px; padding: 0 30px; }
    .section-title-modern { font-size: 20px; }
    .section-desc-modern { font-size: 12.5px; }
    
    .sambutan-section-ultra { padding: 40px 12px; }
    .sambutan-inner-ultra { grid-template-columns: 1fr; gap: 28px; }
    .sambutan-photo-wrap-ultra { max-width: 240px; margin: 0 auto; }
    .sambutan-assalam-ultra { font-size: 14px; padding: 12px 16px; }
    .sambutan-text-ultra { font-size: 13px; line-height: 1.75; }
    .sambutan-quote-ultra { font-size: 13.5px; padding: 16px 20px; }
    
    .trending-main-img { height: 220px; }
    .trending-main-content { padding: 18px; }
    .trending-main-title { font-size: 17px; }
    .trending-main-desc { font-size: 12px; }
    .trending-thumb { width: 64px; height: 64px; }
    .trending-info-title { font-size: 11.5px; }
    
    .warta-card-ultra-img { height: 180px; }
    .warta-card-ultra-body { padding: 18px; }
    .warta-card-ultra-title { font-size: 14.5px; }
    .warta-card-ultra-desc { font-size: 12px; }
    
    .widget-ultra { margin-bottom: 16px; }
    .widget-ultra-head { padding: 14px 16px; font-size: 12px; }
    .agenda-item-ultra { padding: 14px 16px; gap: 12px; }
    .agenda-date-ultra { width: 52px; height: 60px; }
    .agenda-day-ultra { font-size: 20px; }
    .agenda-title-ultra { font-size: 12px; }
    .agenda-desc-ultra { font-size: 10.5px; }
    
    .stats-section-ultra { padding: 44px 12px; }
    .stats-grid-ultra { grid-template-columns: 1fr 1fr; gap: 10px; }
    .stat-item-ultra { padding: 20px 12px; }
    .stat-num-ultra { font-size: 26px; }
    .stat-label-ultra { font-size: 10px; }
    
    .layanan-card-ultra { padding: 20px 12px; }
    .layanan-icon-ultra { width: 56px; height: 56px; font-size: 24px; margin-bottom: 14px; }
    .layanan-title-ultra { font-size: 12px; }
    .layanan-desc-ultra { font-size: 10px; }
    
    .footer-ultra { padding: 40px 14px 0; }
    .footer-grid-ultra { grid-template-columns: 1fr; gap: 26px; padding-bottom: 26px; }
    .footer-col-ultra h4 { font-size: 12px; margin-bottom: 12px; padding-bottom: 8px; }
    .footer-col-ultra p, .footer-col-ultra a { font-size: 11.5px; }
    .footer-logo-ultra { width: 48px; height: 48px; }
    .footer-brand-title-ultra { font-size: 13px; }
    .footer-social-item-ultra { width: 36px; height: 36px; font-size: 13px; }
    .footer-bottom-ultra { flex-direction: column; text-align: center; padding: 18px 0; font-size: 10.5px; }
    
    .chat-widget { bottom: 14px; right: 14px; gap: 8px; }
    .chat-btn { width: 56px; height: 56px; font-size: 22px; }
    .chat-label { font-size: 11px; padding: 8px 14px; }
    
    .stTabs [data-baseweb="tab"] { padding: 10px 14px; font-size: 11px; }
}

/* ============================================
   EXTRA SMALL PHONES (≤ 480px) - COMPACT
   ============================================ */
@media (max-width: 480px) {
    html { font-size: 13px; }
    
    /* Topbar */
    .topbar { padding: 6px 10px !important; gap: 4px !important; }
    .topbar-left, .topbar-right { gap: 6px !important; }
    .topbar-item { font-size: 9.5px !important; gap: 4px !important; }
    .topbar-badge { padding: 2px 8px !important; font-size: 8.5px !important; }
    .topbar-lang { padding: 2px 7px !important; font-size: 8.5px !important; }
    
    /* Header compact */
    .header-wrap { padding: 10px 10px !important; }
    .header-inner { gap: 8px !important; }
    .header-logo { width: 42px !important; height: 42px !important; border-radius: 10px !important; padding: 4px !important; }
    .header-text-title { font-size: 11.5px !important; line-height: 1.2 !important; }
    .header-text-sub { font-size: 8px !important; margin-top: 2px !important; }
    .header-actions { 
        justify-content: space-between !important;
        margin-top: 8px !important;
        padding-top: 8px !important;
        gap: 4px !important;
    }
    .header-action-btn { 
        font-size: 10px !important; 
        padding: 6px 10px !important; 
        border-radius: 6px !important;
        flex: 1;
        justify-content: center;
    }
    
    /* Navbar grid 4 kolom */
    .navbar { padding: 0 6px !important; }
    .navbar-inner { 
        display: grid !important;
        grid-template-columns: repeat(4, 1fr) !important;
        gap: 2px !important;
        padding: 4px 0 !important;
    }
    .nav-link {
        font-size: 9px !important;
        padding: 8px 2px !important;
        letter-spacing: 0 !important;
        text-align: center;
        width: 100% !important;
        max-width: 100% !important;
        flex: none !important;
        border-radius: 4px;
    }
    .nav-link::after { height: 2px !important; }
    
    /* Running */
    .running-text-bar { padding: 8px 10px !important; gap: 6px !important; }
    .running-label { font-size: 8.5px !important; padding: 4px 8px !important; }
    .running-scroll { font-size: 10.5px !important; }
    
    /* Hero */
    .hero-ultra { min-height: 420px !important; }
    .hero-ultra-content { padding: 30px 0 !important; width: 94% !important; }
    .hero-ultra-kicker { font-size: 8.5px !important; padding: 5px 10px !important; margin-bottom: 12px !important; }
    .hero-ultra-title { font-size: 22px !important; margin-bottom: 12px !important; letter-spacing: -0.6px !important; }
    .hero-ultra-sub { font-size: 11.5px !important; margin-bottom: 20px !important; }
    .hero-ultra-buttons { gap: 6px !important; margin-bottom: 24px !important; }
    .hero-ultra-btn { padding: 10px 16px !important; font-size: 10.5px !important; }
    .hero-ultra-stats { gap: 8px !important; }
    .hero-stat-ultra { padding: 10px 12px !important; }
    .hero-stat-num-ultra { font-size: 18px !important; }
    .hero-stat-label-ultra { font-size: 8px !important; }
    
    /* Mitra */
    .mitra-section { padding: 14px 0 !important; }
    .mitra-label { font-size: 8.5px !important; margin-bottom: 10px !important; }
    .mitra-track { gap: 20px !important; }
    .mitra-item { font-size: 10px !important; padding: 5px 10px !important; }
    
    /* Quick access */
    .quick-access-glass { padding: 20px 10px !important; }
    .quick-card-glass { padding: 14px 8px !important; border-radius: 12px !important; }
    .quick-icon-glass { width: 42px !important; height: 42px !important; font-size: 18px !important; margin-bottom: 8px !important; }
    .quick-title-glass { font-size: 11px !important; }
    .quick-desc-glass { font-size: 9px !important; }
    
    /* Section */
    .page-container { padding: 24px 0 !important; }
    .section-header-modern { margin-bottom: 22px !important; }
    .section-kicker-modern { font-size: 9px !important; padding: 0 24px !important; }
    .section-title-modern { font-size: 18px !important; }
    .section-desc-modern { font-size: 11.5px !important; }
    
    /* Sambutan */
    .sambutan-section-ultra { padding: 30px 10px !important; }
    .sambutan-photo-wrap-ultra { max-width: 200px !important; }
    .sambutan-photo-info-ultra { padding: 12px !important; margin-top: 16px !important; }
    .sambutan-nama-ultra { font-size: 12.5px !important; }
    .sambutan-jabatan-ultra { font-size: 9.5px !important; }
    .sambutan-assalam-ultra { font-size: 13px !important; padding: 10px 14px !important; margin-bottom: 16px !important; }
    .sambutan-text-ultra { font-size: 12px !important; line-height: 1.7 !important; margin-bottom: 14px !important; }
    .sambutan-quote-ultra { font-size: 12.5px !important; padding: 14px 16px !important; }
    
    /* Trending */
    .trending-main-img { height: 180px !important; }
    .trending-main-content { padding: 16px !important; }
    .trending-main-title { font-size: 15px !important; }
    .trending-main-desc { font-size: 11.5px !important; }
    .trending-thumb { width: 56px !important; height: 56px !important; }
    .trending-info-title { font-size: 11px !important; }
    
    /* Warta */
    .warta-card-ultra-img { height: 150px !important; }
    .warta-card-ultra-body { padding: 14px !important; }
    .warta-card-ultra-title { font-size: 13px !important; }
    .warta-card-ultra-desc { font-size: 11px !important; }
    
    /* Widget */
    .widget-ultra-head { padding: 12px 14px !important; font-size: 11px !important; }
    .agenda-item-ultra { padding: 12px 14px !important; gap: 10px !important; }
    .agenda-date-ultra { width: 46px !important; height: 52px !important; border-radius: 8px !important; }
    .agenda-day-ultra { font-size: 18px !important; }
    .agenda-title-ultra { font-size: 11px !important; }
    .agenda-desc-ultra { font-size: 9.5px !important; }
    
    /* Stats */
    .stats-section-ultra { padding: 30px 10px !important; }
    .stats-grid-ultra { gap: 8px !important; }
    .stat-item-ultra { padding: 16px 10px !important; }
    .stat-icon-ultra { font-size: 20px !important; margin-bottom: 6px !important; }
    .stat-num-ultra { font-size: 22px !important; margin-bottom: 6px !important; }
    .stat-label-ultra { font-size: 9px !important; }
    
    /* Layanan */
    .layanan-card-ultra { padding: 16px 10px !important; }
    .layanan-icon-ultra { width: 44px !important; height: 44px !important; font-size: 18px !important; margin-bottom: 10px !important; }
    .layanan-title-ultra { font-size: 10.5px !important; }
    .layanan-desc-ultra { font-size: 9px !important; }
    
    /* Footer */
    .footer-ultra { padding: 30px 12px 0 !important; }
    .footer-grid-ultra { gap: 20px !important; padding-bottom: 20px !important; }
    .footer-col-ultra h4 { font-size: 11px !important; margin-bottom: 10px !important; padding-bottom: 8px !important; }
    .footer-col-ultra p, .footer-col-ultra a { font-size: 11px !important; }
    .footer-logo-ultra { width: 42px !important; height: 42px !important; padding: 5px !important; }
    .footer-brand-title-ultra { font-size: 12px !important; }
    .footer-social-item-ultra { width: 32px !important; height: 32px !important; font-size: 12px !important; }
    .footer-bottom-ultra { font-size: 10px !important; }
    
    /* Chat */
    .chat-widget { bottom: 12px !important; right: 12px !important; }
    .chat-btn { width: 48px !important; height: 48px !important; font-size: 20px !important; border-width: 3px !important; }
    .chat-label { font-size: 10px !important; padding: 6px 12px !important; }
    
    /* Columns stack */
    div[data-testid="column"] {
        min-width: 100% !important;
        flex: 1 1 100% !important;
    }
    
    /* Streamlit buttons */
    .stButton > button { font-size: 12px !important; padding: 8px 14px !important; }
    
    /* Tabs */
    .stTabs [data-baseweb="tab"] { padding: 8px 12px !important; font-size: 10.5px !important; }
    
    /* Plotly charts */
    .js-plotly-plot { font-size: 9px !important; }
}

/* ============================================
   NARROW PHONES (≤ 380px)
   ============================================ */
@media (max-width: 380px) {
    html { font-size: 12px; }
    .nav-link { font-size: 8.5px !important; padding: 7px 2px !important; }
    .hero-ultra-title { font-size: 20px !important; }
    .hero-ultra-sub { font-size: 11px !important; }
    .hero-stat-num-ultra { font-size: 16px !important; }
    .hero-stat-label-ultra { font-size: 7.5px !important; }
    .quick-icon-glass { width: 38px !important; height: 38px !important; font-size: 16px !important; }
    .stat-num-ultra { font-size: 20px !important; }
    .layanan-icon-ultra { width: 40px !important; height: 40px !important; font-size: 16px !important; }
    .section-title-modern { font-size: 16px !important; }
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
        <div class="topbar-item"><span>📞</span><span>(0655) 12345</span></div>
        <div class="topbar-item"><span>✉️</span><span>sekretariat@dprk.acehjaya.go.id</span></div>
    </div>
    <div class="topbar-right">
        <span class="topbar-badge">ONLINE</span>
        <div class="topbar-item"><span>🕐</span><span>{now.strftime('%H:%M WIB')}</span></div>
        <a href="#" class="topbar-lang">🇮🇩 ID</a>
    </div>
</div>
""",
    unsafe_allow_html=True,
)

# =========================================================
# HEADER
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
    <span class="running-label">INFO</span>
    <div class="running-scroll-wrap">
        <div class="running-scroll">
            Selamat Datang di Portal Resmi DPRK Kabupaten Aceh Jaya &nbsp;&nbsp;★&nbsp;&nbsp;
            Rapat Paripurna Pembahasan KUA-PPAS 2027 akan dilaksanakan pada 18 September 2026 &nbsp;&nbsp;★&nbsp;&nbsp;
            Layanan Pengaduan Masyarakat kini dapat diakses melalui menu Layanan &nbsp;&nbsp;★&nbsp;&nbsp;
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
    <section class="hero-ultra">
        <div class="hero-ultra-bg" style="background-image: url('{slide['image']}');"></div>
        <div class="hero-ultra-overlay"></div>
        <div class="hero-ultra-grid"></div>
        <div class="hero-ultra-content">
            <div class="hero-ultra-kicker">{slide['kicker']}</div>
            <h1 class="hero-ultra-title">
                {slide['title'].split(' ')[0]} <span>{' '.join(slide['title'].split(' ')[1:3])}</span> {' '.join(slide['title'].split(' ')[3:])}
            </h1>
            <p class="hero-ultra-sub">{slide['subtitle']}</p>
            <div class="hero-ultra-buttons">
                <a href="?page=layanan" class="hero-ultra-btn">📢 Sampaikan Aspirasi</a>
                <a href="?page=berita" class="hero-ultra-btn hero-ultra-btn-outline">📰 Lihat Berita</a>
            </div>
            <div class="hero-ultra-stats">
                <div class="hero-stat-ultra">
                    <span class="hero-stat-num-ultra">20</span>
                    <div class="hero-stat-label-ultra">Anggota DPRK</div>
                </div>
                <div class="hero-stat-ultra">
                    <span class="hero-stat-num-ultra">4</span>
                    <div class="hero-stat-label-ultra">Komisi</div>
                </div>
                <div class="hero-stat-ultra">
                    <span class="hero-stat-num-ultra">120+</span>
                    <div class="hero-stat-label-ultra">Produk Hukum</div>
                </div>
                <div class="hero-stat-ultra">
                    <span class="hero-stat-num-ultra">{st.session_state.visitor_count:,}</span>
                    <div class="hero-stat-label-ultra">Kunjungan</div>
                </div>
            </div>
        </div>
    </section>
    """,
        unsafe_allow_html=True,
    )

    nav_slide_cols = st.columns([1, 4, 1])
    with nav_slide_cols[0]:
        if st.button("◀ Prev", key="slide_prev", use_container_width=True):
            st.session_state.slide_index = (st.session_state.slide_index - 1) % len(HERO_SLIDES)
            st.rerun()
    with nav_slide_cols[2]:
        if st.button("Next ▶", key="slide_next", use_container_width=True):
            st.session_state.slide_index = (st.session_state.slide_index + 1) % len(HERO_SLIDES)
            st.rerun()

    mitra_html = "".join([f'<div class="mitra-item">{m}</div>' for m in MITRA * 2])
    st.markdown(
        f"""
    <div class="mitra-section">
        <div class="mitra-label">DIDUKUNG OLEH INSTANSI & MITRA STRATEGIS</div>
        <div class="mitra-track">
            {mitra_html}
        </div>
    </div>
    """,
        unsafe_allow_html=True,
    )

    # QUICK ACCESS
    st.markdown('<div class="quick-access-glass"><div class="quick-access-inner">', unsafe_allow_html=True)
    quick_cols = st.columns(4)
    quick_data = [
        ("📢", "Pengaduan", "Lapor Online", "layanan"),
        ("📜", "JDIH", "Produk Hukum", "jdih"),
        ("📅", "Agenda", "Jadwal Rapat", "berita"),
        ("📊", "Transparansi", "Info Publik", "jdih"),
    ]
    for i, (icon, title, desc, target) in enumerate(quick_data):
        with quick_cols[i]:
            st.markdown(
                f"""
            <a href="?page={target}" class="quick-card-glass">
                <div class="quick-icon-glass">{icon}</div>
                <div class="quick-title-glass">{title}</div>
                <div class="quick-desc-glass">{desc}</div>
            </a>
            """,
                unsafe_allow_html=True,
            )
    st.markdown("</div></div>", unsafe_allow_html=True)

    # SAMBUTAN
    st.markdown(
        f"""
    <section class="sambutan-section-ultra">
        <div class="sambutan-inner-ultra">
            <div class="sambutan-photo-wrap-ultra">
                <img class="sambutan-photo-ultra" src="{SAMBUTAN['foto']}" alt="{SAMBUTAN['nama']}"
                     onerror="this.onerror=null;this.src='https://images.unsplash.com/photo-1560250097-0b93528c311a?auto=format&fit=crop&w=400&q=80'">
                <div class="sambutan-photo-info-ultra">
                    <div class="sambutan-nama-ultra">{SAMBUTAN['nama']}</div>
                    <div class="sambutan-jabatan-ultra">{SAMBUTAN['jabatan']}</div>
                </div>
            </div>
            <div class="sambutan-content-ultra">
                <div class="section-kicker-modern" style="text-align:left; padding:0;">SAMBUTAN PIMPINAN</div>
                <h2 class="section-title-modern" style="text-align:left; margin-top:10px;">Membangun Aceh Jaya yang Lebih Baik</h2>
                <div class="sambutan-assalam-ultra">{SAMBUTAN['assalamualaikum']}</div>
                <p class="sambutan-text-ultra">{SAMBUTAN['pembuka']}</p>
                <div class="sambutan-quote-ultra">{SAMBUTAN['quote']}</div>
                <p class="sambutan-text-ultra">{SAMBUTAN['paragraf2']}</p>
                <p class="sambutan-text-ultra">{SAMBUTAN['penutup']}</p>
                <div class="sambutan-salam-ultra">
                    <p class="sambutan-salam-line-ultra">Salam hangat,</p>
                    <div class="sambutan-salam-nama-ultra">{SAMBUTAN['nama']}</div>
                    <div class="sambutan-salam-jabatan-ultra">{SAMBUTAN['jabatan']}</div>
                </div>
            </div>
        </div>
    </section>
    """,
        unsafe_allow_html=True,
    )

    # LAYANAN
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
            st.markdown(
                f"""
            <a href="?page={target}" class="layanan-card-ultra">
                <div class="layanan-icon-ultra">{icon}</div>
                <div class="layanan-title-ultra">{title}</div>
                <div class="layanan-desc-ultra">{desc}</div>
            </a>
            """,
                unsafe_allow_html=True,
            )

    st.markdown("</div>", unsafe_allow_html=True)

    # TRENDING + SIDEBAR
    st.markdown('<div class="page-container">', unsafe_allow_html=True)
    st.markdown(
        """
    <div class="section-header-modern">
        <div class="section-kicker-modern">TRENDING HARI INI</div>
        <h2 class="section-title-modern">Warta Terpopuler</h2>
        <p class="section-desc-modern">Berita dan agenda terhangat dari DPRK Aceh Jaya.</p>
    </div>
    """,
        unsafe_allow_html=True,
    )

    trending_main = WARTA_DPRK[0]
    trending_side = WARTA_DPRK[1:4]

    tr_col1, tr_col2 = st.columns([2, 1])
    with tr_col1:
        st.markdown(
            f"""
        <div class="trending-main">
            <div class="trending-main-img">
                <div class="trending-badge">🔥 TRENDING #1</div>
                <img src="{trending_main['image']}">
            </div>
            <div class="trending-main-content">
                <span class="trending-main-cat">{trending_main['kategori']}</span>
                <h3 class="trending-main-title">{trending_main['title']}</h3>
                <p class="trending-main-desc">{trending_main['desc'][:200]}...</p>
                <div class="trending-main-meta">
                    <span>📅 {trending_main['date']}</span>
                    <span>👁️ {trending_main['views']:,} views</span>
                </div>
            </div>
        </div>
        """,
            unsafe_allow_html=True,
        )

    with tr_col2:
        st.markdown('<div class="trending-list">', unsafe_allow_html=True)
        for i, item in enumerate(trending_side, start=2):
            st.markdown(
                f"""
            <a href="?page=berita" class="trending-item">
                <div class="trending-rank">{i}</div>
                <img class="trending-thumb" src="{item['image']}">
                <div class="trending-info">
                    <div class="trending-info-cat">{item['kategori']}</div>
                    <div class="trending-info-title">{item['title']}</div>
                    <div class="trending-info-meta">👁️ {item['views']:,}</div>
                </div>
            </a>
            """,
                unsafe_allow_html=True,
            )
        st.markdown('</div>', unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True)

    # WARTA + WIDGET
    st.markdown('<div class="page-container">', unsafe_allow_html=True)
    main_col, side_col = st.columns([2, 1])

    with main_col:
        st.markdown(
            """
        <div class="section-header-modern" style="text-align:left; margin-bottom:28px;">
            <div class="section-kicker-modern" style="text-align:left; padding:0;">WARTA DPRK</div>
            <h2 class="section-title-modern" style="text-align:left;">Berita Terbaru</h2>
        </div>
        """,
            unsafe_allow_html=True,
        )
        for i in range(0, min(4, len(WARTA_DPRK)), 2):
            wcols = st.columns(2)
            for j in range(2):
                if i + j < len(WARTA_DPRK):
                    item = WARTA_DPRK[i + j]
                    with wcols[j]:
                        st.markdown(
                            f"""
                        <div class="warta-card-ultra" style="margin-bottom: 18px;">
                            <div class="warta-card-ultra-img">
                                <span class="warta-card-ultra-cat">{item['kategori']}</span>
                                <span class="warta-card-ultra-views">👁️ {item['views']:,}</span>
                                <img src="{item['image']}">
                            </div>
                            <div class="warta-card-ultra-body">
                                <div class="warta-card-ultra-date">📅 {item['date']}</div>
                                <h3 class="warta-card-ultra-title">{item['title']}</h3>
                                <p class="warta-card-ultra-desc">{item['desc'][:110]}...</p>
                                <a href="?page=berita" class="warta-card-ultra-more">Baca Selengkapnya →</a>
                            </div>
                        </div>
                        """,
                            unsafe_allow_html=True,
                        )

    with side_col:
        st.markdown(
            """
        <div class="widget-ultra">
            <div class="widget-ultra-head">📅 Agenda Terkini</div>
            <div class="widget-ultra-body">
        """,
            unsafe_allow_html=True,
        )
        for item in AGENDA_TERKINI:
            st.markdown(
                f"""
            <div class="agenda-item-ultra">
                <div class="agenda-date-ultra">
                    <div class="agenda-day-ultra">{item['hari']}</div>
                    <div class="agenda-month-ultra">{item['bulan_tahun']}</div>
                </div>
                <div class="agenda-content-ultra">
                    <div class="agenda-title-ultra">{item['judul']}</div>
                    <p class="agenda-desc-ultra">{item['desc']}</p>
                    <div class="agenda-footer-ultra">📅 {item['tanggal_full']}</div>
                </div>
            </div>
            """,
                unsafe_allow_html=True,
            )
        st.markdown("</div></div>", unsafe_allow_html=True)

        st.markdown(
            """
        <div class="widget-ultra">
            <div class="widget-ultra-head">📰 Kesekretariatan</div>
            <div class="widget-ultra-body">
        """,
            unsafe_allow_html=True,
        )
        for item in KESEKRETARIATAN:
            st.markdown(
                f"""
            <div class="kesekret-item-ultra">
                <div class="kesekret-icon-ultra">📋</div>
                <div>
                    <div class="kesekret-title-ultra">{item['title']}</div>
                    <div class="kesekret-date-ultra">📅 {item['date']}</div>
                </div>
            </div>
            """,
                unsafe_allow_html=True,
            )
        st.markdown("</div></div>", unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True)

    # STATS
    st.markdown(
        f"""
    <section class="stats-section-ultra">
        <div class="stats-inner-ultra">
            <div class="section-header-modern" style="margin-bottom: 40px;">
                <div class="section-kicker-modern" style="color: #e6c458;">DALAM ANGKA</div>
                <h2 class="section-title-modern" style="color: #ffffff;">DPRK Aceh Jaya</h2>
            </div>
            <div class="stats-grid-ultra">
                <div class="stat-item-ultra">
                    <span class="stat-icon-ultra">👥</span>
                    <div class="stat-num-ultra">20</div>
                    <div class="stat-label-ultra">Anggota DPRK</div>
                </div>
                <div class="stat-item-ultra">
                    <span class="stat-icon-ultra">🏛️</span>
                    <div class="stat-num-ultra">4</div>
                    <div class="stat-label-ultra">Komisi DPRK</div>
                </div>
                <div class="stat-item-ultra">
                    <span class="stat-icon-ultra">📜</span>
                    <div class="stat-num-ultra">120+</div>
                    <div class="stat-label-ultra">Produk Hukum</div>
                </div>
                <div class="stat-item-ultra">
                    <span class="stat-icon-ultra">👁️</span>
                    <div class="stat-num-ultra">{st.session_state.visitor_count:,}</div>
                    <div class="stat-label-ultra">Total Kunjungan</div>
                </div>
            </div>
        </div>
    </section>
    """,
        unsafe_allow_html=True,
    )

    # CHART
    st.markdown('<div class="page-container">', unsafe_allow_html=True)
    st.markdown(
        """
    <div class="section-header-modern">
        <div class="section-kicker-modern">DATA & STATISTIK</div>
        <h2 class="section-title-modern">Dashboard Kinerja</h2>
    </div>
    """,
        unsafe_allow_html=True,
    )

    stat_col1, stat_col2 = st.columns(2)
    with stat_col1:
        fig1 = px.line(STATS_DATA, x="Bulan", y="Rapat", markers=True,
                       title="Jumlah Rapat per Bulan 2026",
                       color_discrete_sequence=["#0d5e3a"])
        fig1.update_layout(plot_bgcolor="rgba(0,0,0,0)", paper_bgcolor="rgba(0,0,0,0)",
                          font=dict(family="Inter", size=10, color="#000000"),
                          margin=dict(l=10, r=10, t=40, b=10), height=280)
        st.plotly_chart(fig1, use_container_width=True)

    with stat_col2:
        fig2 = px.pie(ANGGARAN_DATA, values="Anggaran", names="Kategori",
                     title="Alokasi Anggaran 2026",
                     color_discrete_sequence=["#0d5e3a", "#c9a227", "#14734a", "#e6c458", "#6b7a75"],
                     hole=0.5)
        fig2.update_layout(plot_bgcolor="rgba(0,0,0,0)", paper_bgcolor="rgba(0,0,0,0)",
                          font=dict(family="Inter", size=10, color="#000000"),
                          margin=dict(l=10, r=10, t=40, b=10), height=280)
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
        <p class="section-desc-modern">DPRK Aceh Jaya menjalankan fungsi legislasi, anggaran, dan pengawasan.</p>
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
                <div style="background: #fff; border: 1px solid #e5ebe7; border-radius: 12px; padding: 14px; text-align: center; border-top: 3px solid #0d5e3a; margin-bottom: 10px;">
                    <div style="font-weight: 800; color: #083d26; font-size: 11.5px; margin-bottom: 4px;">{nama}</div>
                    <div style="color: #c9a227; font-size: 9.5px; font-weight: 800;">{jabatan}</div>
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
                <div style="background: #fff; border: 1px solid #e5ebe7; border-radius: 12px; padding: 14px; text-align: center; border-top: 3px solid #c9a227; margin-bottom: 10px;">
                    <div style="font-weight: 800; color: #083d26; font-size: 11.5px; margin-bottom: 4px;">{nama}</div>
                    <div style="color: #4a5a55; font-size: 9.5px;">{jabatan}</div>
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
        filtered = [i for i in filtered if search.lower() in i["title"].lower()]

    for i in range(0, len(filtered), 3):
        cols = st.columns(3)
        for j in range(3):
            if i + j < len(filtered):
                item = filtered[i + j]
                with cols[j]:
                    st.markdown(
                        f"""
                    <div class="warta-card-ultra" style="margin-bottom: 14px;">
                        <div class="warta-card-ultra-img">
                            <span class="warta-card-ultra-cat">{item['kategori']}</span>
                            <span class="warta-card-ultra-views">👁️ {item['views']:,}</span>
                            <img src="{item['image']}">
                        </div>
                        <div class="warta-card-ultra-body">
                            <div class="warta-card-ultra-date">📅 {item['date']}</div>
                            <h3 class="warta-card-ultra-title">{item['title']}</h3>
                            <p class="warta-card-ultra-desc">{item['desc'][:100]}...</p>
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
    <div class="section-header-modern">
        <div class="section-kicker-modern">DOKUMENTASI</div>
        <h2 class="section-title-modern">Galeri Foto & Video</h2>
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

    for i in range(0, len(gallery), 2):
        cols = st.columns(2)
        for j in range(2):
            if i + j < len(gallery):
                title, img = gallery[i + j]
                with cols[j]:
                    st.markdown(
                        f"""
                    <div style="background: #fff; border: 1px solid #e5ebe7; border-radius: 12px; overflow: hidden; margin-bottom: 10px;">
                        <img src="{img}" style="width: 100%; height: 140px; object-fit: cover;">
                        <div style="padding: 10px; text-align: center; font-weight: 700; color: #083d26; font-size: 11px;">{title}</div>
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
        <div class="section-kicker-modern">PELAYANAN</div>
        <h2 class="section-title-modern">Layanan Aspirasi & Pengaduan</h2>
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
            kategori = st.selectbox("Kategori *", ["Pengaduan Masyarakat", "Infrastruktur & Jalan", "Pelayanan Publik", "Legislasi & Qanun", "Lainnya"])
            prioritas = st.selectbox("Prioritas", ["Normal", "Penting", "Mendesak"])
        lokasi = st.text_input("Lokasi Kejadian", placeholder="Desa / Kecamatan")
        isi = st.text_area("Isi Laporan *", height=120, placeholder="Jelaskan laporan Anda...")

        submitted = st.form_submit_button("🚀 Kirim Laporan", type="primary", use_container_width=True)

        if submitted:
            if nama.strip() and isi.strip():
                nomor = datetime.now().strftime("%Y%m%d%H%M%S")
                st.success(f"✅ Laporan diterima! Nomor tiket: **ADU-{nomor}**")
            else:
                st.error("⚠️ Mohon lengkapi data.")

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
    </div>
    """,
        unsafe_allow_html=True,
    )

    cols = st.columns(3)
    contacts = [
        ("📍", "Alamat", "Jl. Merdeka No. 01, Calang"),
        ("📞", "Telepon", "(0655) 12345"),
        ("✉️", "Email", "sekretariat@dprk.acehjaya.go.id"),
    ]
    for i, (icon, title, value) in enumerate(contacts):
        with cols[i]:
            st.markdown(
                f"""
            <div class="layanan-card-ultra">
                <div class="layanan-icon-ultra">{icon}</div>
                <div class="layanan-title-ultra">{title}</div>
                <div class="layanan-desc-ultra">{value}</div>
            </div>
            """,
                unsafe_allow_html=True,
            )

    st.markdown(
        """
    <div style="margin-top: 20px; background: #fff; border: 1px solid #e5ebe7; border-radius: 16px; padding: 16px;">
        <div style="width: 100%; height: 260px; border-radius: 12px; overflow: hidden;">
            <iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3988.5!2d95.39!3d4.71!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x30403e5f3a0b0b0b%3A0x0!2sCalang%2C%20Aceh%20Jaya%20Regency%2C%20Aceh!5e0!3m2!1sen!2sid!4v1600000000000" width="100%" height="100%" style="border:0;" allowfullscreen="" loading="lazy"></iframe>
        </div>
    </div>
    """,
        unsafe_allow_html=True,
    )
    st.markdown("</div>", unsafe_allow_html=True)

# =========================================================
# CHAT WIDGET
# =========================================================
st.markdown(
    """
<div class="chat-widget">
    <div class="chat-label">💬 Chat SAVIRA!</div>
    <a href="?page=layanan" class="chat-btn" title="Chat SAVIRA">💬</a>
</div>
""",
    unsafe_allow_html=True,
)

# =========================================================
# FOOTER
# =========================================================
st.markdown(
    f"""
<footer class="footer-ultra">
<div class="footer-inner-ultra">
<div class="footer-grid-ultra">

<div class="footer-col-ultra">
<div class="footer-brand-ultra">
<div class="footer-logo-ultra">
    <img src="{LOGO_URL}" alt="Logo"
         onerror="this.onerror=null;this.src='data:image/svg+xml,<svg xmlns=%22http://www.w3.org/2000/svg%22 viewBox=%220 0 100 100%22><text y=%22.9em%22 font-size=%2290%22>🏛️</text></svg>'">
</div>
<div>
<div class="footer-brand-title-ultra">DPRK ACEH JAYA</div>
<div class="footer-brand-sub-ultra">SEKRETARIAT DPRK</div>
</div>
</div>
<p style="color: rgba(255,255,255,0.7); font-size: 11.5px; line-height: 1.8; margin: 0 0 8px;">
Portal resmi Sekretariat DPRK Kabupaten Aceh Jaya.
</p>
<div class="footer-social-ultra">
<a href="#" class="footer-social-item-ultra">f</a>
<a href="#" class="footer-social-item-ultra">𝕏</a>
<a href="#" class="footer-social-item-ultra">▶</a>
<a href="#" class="footer-social-item-ultra">◎</a>
</div>
</div>

<div class="footer-col-ultra">
<h4>Navigasi</h4>
<a href="?page=beranda">Beranda</a>
<a href="?page=profil">Profil DPRK</a>
<a href="?page=berita">Berita</a>
<a href="?page=galeri">Galeri</a>
<a href="?page=kontak">Kontak</a>
</div>

<div class="footer-col-ultra">
<h4>Layanan</h4>
<a href="?page=layanan">Pengaduan</a>
<a href="?page=jdih">JDIH</a>
<a href="?page=jdih">Transparansi</a>
<a href="https://elhpkpn.kpk.go.id/" target="_blank">E-LHKPN</a>
</div>

<div class="footer-col-ultra">
<h4>Hubungi Kami</h4>
<p>📍 Jl. Merdeka No. 01</p>
<p>Calang, Aceh Jaya</p>
<p>📞 (0655) 12345</p>
<p>✉️ sekretariat@dprk.acehjaya.go.id</p>
</div>

</div>

<div class="footer-bottom-ultra">
<div>© {datetime.now().year} Sekretariat DPRK Aceh Jaya. Seluruh hak cipta dilindungi.</div>
</div>

</div>
</footer>
""",
    unsafe_allow_html=True,
)

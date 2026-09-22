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
if "form_step" not in st.session_state:
    st.session_state.form_step = 1

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

# MITRA LOGOS (untuk marquee)
MITRA = [
    "🏛️ KPK", "⚖️ Kejaksaan", "🚔 Polri", "🏦 BPK", "📊 BPS",
    "🎓 Universitas", "🏥 RSUD", "📚 Dinas Pendidikan", "🌾 Dinas Pertanian", "🛣️ PUPR"
]

# =========================================================
# CSS STYLE - ULTRA PREMIUM v5.0
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
    --glass: rgba(255, 255, 255, 0.7);
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

/* Custom scrollbar */
::-webkit-scrollbar { width: 10px; height: 10px; }
::-webkit-scrollbar-track { background: #e8f5ef; }
::-webkit-scrollbar-thumb { background: linear-gradient(180deg, #0d5e3a, #c9a227); border-radius: 10px; }

/* ============================================
   TOP BAR - ANNOUNCEMENT & TICKER
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
.topbar-left, .topbar-right { 
    display: flex; 
    gap: 16px; 
    align-items: center; 
    flex-wrap: wrap;
    position: relative;
    z-index: 2;
}
.topbar-item { display: flex; align-items: center; gap: 6px; }
.topbar a { color: #ffffff !important; text-decoration: none; transition: color 0.2s; }
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
.header-logo:hover {
    transform: scale(1.05) rotate(-3deg);
    box-shadow: 0 8px 24px rgba(13,94,58,0.2);
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
    padding: 9px 16px;
    border-radius: 10px;
    font-size: 12px;
    font-weight: 700;
    text-decoration: none;
    transition: all 0.25s;
    position: relative;
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

/* Notification bell */
.notif-btn {
    position: relative;
    background: #f8faf9;
    border: 1px solid #e5ebe7;
    width: 40px;
    height: 40px;
    border-radius: 10px;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 16px;
    cursor: pointer;
    text-decoration: none;
    transition: all 0.25s;
}
.notif-btn:hover {
    background: #0d5e3a;
    border-color: #0d5e3a;
}
.notif-badge {
    position: absolute;
    top: -4px;
    right: -4px;
    background: #ef4444;
    color: #ffffff !important;
    width: 18px;
    height: 18px;
    border-radius: 50%;
    font-size: 9px;
    font-weight: 800;
    display: flex;
    align-items: center;
    justify-content: center;
    border: 2px solid #ffffff;
    animation: notifPulse 2s infinite;
}
@keyframes notifPulse {
    0%, 100% { transform: scale(1); }
    50% { transform: scale(1.15); }
}

/* ============================================
   NAVBAR - ULTRA PREMIUM
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
.nav-link:hover {
    color: #0d5e3a !important;
}
.nav-link:hover::after { width: 60%; }
.nav-link-active {
    color: #0d5e3a !important;
    font-weight: 800;
}
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
   HERO ULTRA PREMIUM
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
    0%, 100% { transform: scale(1) translate(0, 0); }
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
    box-shadow: 0 8px 32px rgba(230,196,88,0.15);
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
    text-shadow: 0 2px 12px rgba(0,0,0,0.4);
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
.hero-ultra-btn:hover {
    transform: translateY(-4px);
    box-shadow: 0 16px 40px rgba(201,162,39,0.6);
}
.hero-ultra-btn-outline {
    background: rgba(255,255,255,0.08);
    color: #ffffff !important;
    border: 2px solid rgba(255,255,255,0.5);
    backdrop-filter: blur(15px);
    box-shadow: none;
}
.hero-ultra-btn-outline:hover {
    background: rgba(255,255,255,0.2);
    border-color: #e6c458;
    transform: translateY(-4px);
}

/* Hero Stats Ultra */
.hero-ultra-stats {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 16px;
    max-width: 900px;
}
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
.hero-stat-ultra:hover {
    background: rgba(230,196,88,0.12);
    border-color: rgba(230,196,88,0.4);
    transform: translateY(-4px);
}
.hero-stat-num-ultra {
    font-family: 'Plus Jakarta Sans', sans-serif;
    color: #e6c458 !important;
    font-size: 30px;
    font-weight: 900;
    line-height: 1;
    display: block;
    letter-spacing: -0.5px;
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
   SECTION STYLES
   ============================================ */
.page-container {
    width: 92%;
    max-width: 1400px;
    margin: 0 auto;
    padding: 60px 0;
}
.section-header-modern {
    text-align: center;
    margin-bottom: 50px;
}
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
.section-desc-modern {
    color: #4a5a55 !important;
    font-size: 14.5px;
    line-height: 1.75;
    max-width: 720px;
    margin: 0 auto;
}

/* ============================================
   GLASSMORPHISM QUICK ACCESS
   ============================================ */
.quick-access-glass {
    background: linear-gradient(135deg, #f8faf9 0%, #ffffff 100%);
    padding: 40px 16px;
    border-bottom: 1px solid #e5ebe7;
    position: relative;
}
.quick-access-glass::before {
    content: '';
    position: absolute;
    top: 0; left: 0; right: 0;
    height: 200px;
    background: radial-gradient(ellipse at 50% 0%, rgba(13,94,58,0.05) 0%, transparent 70%);
}
.quick-access-inner {
    max-width: 1400px;
    margin: 0 auto;
    position: relative;
    z-index: 2;
}
.quick-grid-glass {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 20px;
}
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
.quick-card-glass::before {
    content: '';
    position: absolute;
    top: -50%; left: -50%;
    width: 200%; height: 200%;
    background: radial-gradient(circle, rgba(230,196,88,0.15) 0%, transparent 50%);
    opacity: 0;
    transition: opacity 0.5s ease;
    pointer-events: none;
}
.quick-card-glass:hover::before { opacity: 1; }
.quick-card-glass:hover {
    transform: translateY(-10px);
    box-shadow: 0 30px 60px rgba(13,94,58,0.18);
    border-color: #c9a227;
}
.quick-icon-glass {
    width: 72px;
    height: 72px;
    border-radius: 20px;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 32px;
    margin-bottom: 18px;
    background: linear-gradient(135deg, #e8f5ef, #d1e8dd);
    color: #0d5e3a !important;
    transition: all 0.5s cubic-bezier(0.4, 0, 0.2, 1);
    box-shadow: 0 8px 24px rgba(13,94,58,0.1);
    position: relative;
}
.quick-card-glass:hover .quick-icon-glass {
    background: linear-gradient(135deg, #c9a227, #e6c458);
    color: #ffffff !important;
    transform: scale(1.1) rotate(-10deg);
    box-shadow: 0 12px 32px rgba(201,162,39,0.4);
}
.quick-title-glass {
    font-family: 'Plus Jakarta Sans', sans-serif;
    font-size: 15px;
    font-weight: 800;
    color: #083d26 !important;
    margin: 0 0 6px;
    letter-spacing: -0.2px;
}
.quick-desc-glass {
    font-size: 12px;
    color: #4a5a55 !important;
    font-weight: 500;
}

/* ============================================
   SAMBUTAN PIMPINAN
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
    animation: floatOrb 15s ease-in-out infinite;
}
.sambutan-section-ultra::after {
    content: '';
    position: absolute;
    bottom: -50%; left: -20%;
    width: 600px; height: 600px;
    background: radial-gradient(circle, rgba(201,162,39,0.08) 0%, transparent 60%);
    border-radius: 50%;
    animation: floatOrb 20s ease-in-out infinite reverse;
}
@keyframes floatOrb {
    0%, 100% { transform: translate(0, 0) scale(1); }
    50% { transform: translate(30px, -30px) scale(1.1); }
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
.sambutan-photo-wrap-ultra {
    position: relative;
    text-align: center;
}
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
    transition: transform 0.5s ease;
}
.sambutan-photo-ultra:hover {
    transform: scale(1.02) rotate(-1deg);
}
.sambutan-photo-frame-ultra {
    position: absolute;
    top: 20px; left: 20px;
    width: 100%;
    max-width: 340px;
    aspect-ratio: 3/4;
    border: 3px solid #c9a227;
    border-radius: 20px;
    z-index: 1;
}
.sambutan-photo-frame-ultra::before {
    content: '';
    position: absolute;
    top: -10px; left: -10px;
    right: -10px; bottom: -10px;
    border: 2px dashed rgba(201,162,39,0.3);
    border-radius: 24px;
    animation: rotateDash 30s linear infinite;
}
@keyframes rotateDash {
    0% { transform: rotate(0deg); }
    100% { transform: rotate(360deg); }
}
.sambutan-photo-info-ultra {
    margin-top: 28px;
    background: #ffffff;
    border: 1px solid #e5ebe7;
    border-radius: 16px;
    padding: 20px;
    box-shadow: 0 12px 32px rgba(0,0,0,0.06);
    position: relative;
    z-index: 2;
}
.sambutan-nama-ultra {
    font-family: 'Plus Jakarta Sans', sans-serif;
    font-size: 17px;
    font-weight: 900;
    color: #083d26 !important;
    text-transform: uppercase;
    letter-spacing: 0.3px;
    margin: 0 0 5px;
}
.sambutan-jabatan-ultra {
    color: #c9a227 !important;
    font-size: 12px;
    font-weight: 800;
    text-transform: uppercase;
    letter-spacing: 1.2px;
}
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
.sambutan-text-ultra {
    color: #0a1f18 !important;
    font-size: 14.5px;
    line-height: 1.95;
    margin-bottom: 20px;
}
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
    position: relative;
    box-shadow: 0 8px 24px rgba(201,162,39,0.08);
}
.sambutan-quote-ultra::before {
    content: '"';
    position: absolute;
    top: -10px; left: 16px;
    font-size: 80px;
    color: rgba(201,162,39,0.2);
    font-family: Georgia, serif;
    line-height: 1;
}
.sambutan-salam-ultra {
    margin-top: 32px;
    padding-top: 24px;
    border-top: 2px dashed #e5ebe7;
}
.sambutan-salam-line-ultra {
    color: #4a5a55 !important;
    font-size: 13.5px;
    margin: 0 0 6px;
}
.sambutan-salam-nama-ultra {
    font-family: 'Plus Jakarta Sans', sans-serif;
    font-size: 16px;
    font-weight: 900;
    color: #083d26 !important;
    text-transform: uppercase;
    margin: 10px 0 4px;
}
.sambutan-salam-jabatan-ultra {
    color: #c9a227 !important;
    font-size: 12.5px;
    font-weight: 700;
}

/* ============================================
   TRENDING NEWS
   ============================================ */
.trending-grid {
    display: grid;
    grid-template-columns: 2fr 1fr;
    gap: 24px;
}
.trending-main {
    background: #ffffff;
    border: 1px solid #e5ebe7;
    border-radius: 20px;
    overflow: hidden;
    position: relative;
    transition: all 0.4s ease;
}
.trending-main:hover {
    transform: translateY(-6px);
    box-shadow: 0 30px 60px rgba(13,94,58,0.18);
    border-color: #c9a227;
}
.trending-main-img {
    position: relative;
    width: 100%;
    height: 380px;
    overflow: hidden;
}
.trending-main-img img {
    width: 100%;
    height: 100%;
    object-fit: cover;
    transition: transform 0.8s ease;
}
.trending-main:hover .trending-main-img img {
    transform: scale(1.08);
}
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
    letter-spacing: 0.8px;
    z-index: 2;
    box-shadow: 0 4px 16px rgba(239,68,68,0.4);
    animation: trendingPulse 2s infinite;
}
@keyframes trendingPulse {
    0%, 100% { transform: scale(1); }
    50% { transform: scale(1.05); }
}
.trending-main-content {
    padding: 28px;
}
.trending-main-cat {
    display: inline-block;
    background: linear-gradient(135deg, #c9a227, #e6c458);
    color: #083d26 !important;
    padding: 5px 14px;
    border-radius: 20px;
    font-size: 10.5px;
    font-weight: 800;
    text-transform: uppercase;
    letter-spacing: 0.6px;
    margin-bottom: 14px;
}
.trending-main-title {
    font-family: 'Plus Jakarta Sans', sans-serif;
    font-size: 24px;
    font-weight: 900;
    color: #083d26 !important;
    line-height: 1.35;
    margin: 0 0 12px;
    letter-spacing: -0.5px;
}
.trending-main-desc {
    color: #4a5a55 !important;
    font-size: 14px;
    line-height: 1.75;
    margin: 0 0 18px;
}
.trending-main-meta {
    display: flex;
    gap: 20px;
    color: #c9a227 !important;
    font-size: 11.5px;
    font-weight: 800;
    text-transform: uppercase;
    letter-spacing: 0.5px;
}
.trending-list {
    display: flex;
    flex-direction: column;
    gap: 16px;
}
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
.trending-item:hover {
    border-color: #c9a227;
    transform: translateX(6px);
    box-shadow: 0 12px 32px rgba(13,94,58,0.12);
}
.trending-rank {
    position: absolute;
    top: -8px; left: -8px;
    width: 32px;
    height: 32px;
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
    z-index: 2;
}
.trending-item:nth-child(1) .trending-rank { background: linear-gradient(135deg, #ef4444, #dc2626); }
.trending-item:nth-child(2) .trending-rank { background: linear-gradient(135deg, #f59e0b, #d97706); }
.trending-item:nth-child(3) .trending-rank { background: linear-gradient(135deg, #c9a227, #e6c458); }
.trending-thumb {
    width: 80px;
    height: 80px;
    border-radius: 12px;
    object-fit: cover;
    flex-shrink: 0;
}
.trending-info { flex: 1; min-width: 0; }
.trending-info-cat {
    color: #c9a227 !important;
    font-size: 10px;
    font-weight: 800;
    text-transform: uppercase;
    letter-spacing: 0.8px;
    margin-bottom: 6px;
}
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
.trending-info-meta {
    color: #4a5a55 !important;
    font-size: 10.5px;
    font-weight: 600;
}

/* ============================================
   WARTA GRID ULTRA
   ============================================ */
.warta-grid-ultra {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 24px;
}
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
.warta-card-ultra::before {
    content: '';
    position: absolute;
    top: 0; left: 0; right: 0;
    height: 4px;
    background: linear-gradient(90deg, #0d5e3a, #c9a227, #e6c458);
    transform: scaleX(0);
    transform-origin: left;
    transition: transform 0.5s ease;
    z-index: 2;
}
.warta-card-ultra:hover::before { transform: scaleX(1); }
.warta-card-ultra:hover {
    transform: translateY(-10px);
    box-shadow: 0 30px 70px rgba(13,94,58,0.2);
    border-color: rgba(201,162,39,0.4);
}
.warta-card-ultra-img {
    position: relative;
    width: 100%;
    height: 220px;
    overflow: hidden;
}
.warta-card-ultra-img img {
    width: 100%;
    height: 100%;
    object-fit: cover;
    transition: transform 0.8s ease;
}
.warta-card-ultra:hover .warta-card-ultra-img img {
    transform: scale(1.12);
}
.warta-card-ultra-img::after {
    content: '';
    position: absolute;
    bottom: 0; left: 0; right: 0;
    height: 50%;
    background: linear-gradient(180deg, transparent, rgba(0,0,0,0.5));
}
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
    letter-spacing: 0.6px;
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
    display: flex;
    align-items: center;
    gap: 4px;
}
.warta-card-ultra-body {
    padding: 24px;
    flex: 1;
    display: flex;
    flex-direction: column;
}
.warta-card-ultra-date {
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
.warta-card-ultra-title {
    font-family: 'Plus Jakarta Sans', sans-serif;
    font-size: 16.5px;
    font-weight: 800;
    color: #083d26 !important;
    line-height: 1.4;
    margin: 0 0 12px;
    letter-spacing: -0.3px;
    transition: color 0.25s;
}
.warta-card-ultra:hover .warta-card-ultra-title {
    color: #0d5e3a !important;
}
.warta-card-ultra-desc {
    color: #4a5a55 !important;
    font-size: 13px;
    line-height: 1.65;
    margin: 0 0 16px;
    flex: 1;
}
.warta-card-ultra-more {
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
.warta-card-ultra:hover .warta-card-ultra-more {
    gap: 12px;
    color: #c9a227 !important;
}

/* ============================================
   WIDGET MODERN
   ============================================ */
.widget-ultra {
    background: #ffffff;
    border: 1px solid #e5ebe7;
    border-radius: 20px;
    overflow: hidden;
    margin-bottom: 24px;
    box-shadow: 0 4px 20px rgba(0,0,0,0.04);
    transition: box-shadow 0.3s;
}
.widget-ultra:hover {
    box-shadow: 0 12px 40px rgba(13,94,58,0.1);
}
.widget-ultra-head {
    background: linear-gradient(135deg, #0d5e3a, #14734a);
    color: #ffffff !important;
    padding: 18px 22px;
    font-family: 'Plus Jakarta Sans', sans-serif;
    font-size: 13.5px;
    font-weight: 800;
    text-transform: uppercase;
    letter-spacing: 0.8px;
    display: flex;
    align-items: center;
    justify-content: space-between;
    border-bottom: 3px solid #c9a227;
    position: relative;
    overflow: hidden;
}
.widget-ultra-head::before {
    content: '';
    position: absolute;
    top: 0; left: -100%;
    width: 100%; height: 100%;
    background: linear-gradient(90deg, transparent, rgba(255,255,255,0.1), transparent);
    animation: widgetShine 5s infinite;
}
@keyframes widgetShine {
    0% { left: -100%; }
    100% { left: 100%; }
}
.widget-ultra-body { padding: 0; }

.agenda-item-ultra {
    display: flex;
    gap: 16px;
    padding: 18px 22px;
    border-bottom: 1px solid #e5ebe7;
    transition: all 0.25s ease;
}
.agenda-item-ultra:last-child { border-bottom: none; }
.agenda-item-ultra:hover { 
    background: #f8faf9; 
    padding-left: 26px;
}
.agenda-date-ultra {
    width: 64px;
    height: 72px;
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
.agenda-day-ultra {
    font-family: 'Plus Jakarta Sans', sans-serif;
    font-size: 26px;
    font-weight: 900;
    line-height: 1;
    color: #ffffff !important;
}
.agenda-month-ultra {
    font-size: 9.5px;
    font-weight: 800;
    color: #ffffff !important;
    margin-top: 4px;
    letter-spacing: 0.6px;
}
.agenda-content-ultra { flex: 1; min-width: 0; }
.agenda-title-ultra {
    color: #083d26 !important;
    font-family: 'Plus Jakarta Sans', sans-serif;
    font-size: 13.5px;
    font-weight: 800;
    line-height: 1.4;
    margin: 0 0 6px;
}
.agenda-desc-ultra {
    color: #4a5a55 !important;
    font-size: 11.5px;
    line-height: 1.55;
    margin: 0 0 8px;
    display: -webkit-box;
    -webkit-line-clamp: 2;
    -webkit-box-orient: vertical;
    overflow: hidden;
}
.agenda-footer-ultra {
    display: inline-flex;
    align-items: center;
    gap: 6px;
    color: #c9a227 !important;
    font-size: 10.5px;
    font-weight: 800;
    text-transform: uppercase;
    letter-spacing: 0.5px;
    padding: 4px 10px;
    background: #faf6e8;
    border-radius: 8px;
}

.kesekret-item-ultra {
    display: flex;
    gap: 14px;
    padding: 16px 22px;
    border-bottom: 1px solid #e5ebe7;
    transition: all 0.25s ease;
}
.kesekret-item-ultra:last-child { border-bottom: none; }
.kesekret-item-ultra:hover { 
    background: #f8faf9;
    padding-left: 26px;
}
.kesekret-icon-ultra {
    width: 44px;
    height: 44px;
    border-radius: 12px;
    background: linear-gradient(135deg, #e8f5ef, #d1e8dd);
    color: #0d5e3a !important;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 20px;
    flex-shrink: 0;
    transition: all 0.3s;
}
.kesekret-item-ultra:hover .kesekret-icon-ultra {
    background: linear-gradient(135deg, #c9a227, #e6c458);
    color: #ffffff !important;
    transform: rotate(-10deg) scale(1.1);
}
.kesekret-title-ultra {
    color: #083d26 !important;
    font-size: 13px;
    font-weight: 700;
    line-height: 1.45;
    margin: 0 0 5px;
}
.kesekret-date-ultra {
    color: #c9a227 !important;
    font-size: 10.5px;
    font-weight: 800;
}

/* ============================================
   STATS SECTION - PREMIUM
   ============================================ */
.stats-section-ultra {
    background: 
        linear-gradient(135deg, #062b1b 0%, #0d5e3a 50%, #062b1b 100%);
    padding: 80px 16px;
    position: relative;
    overflow: hidden;
}
.stats-section-ultra::before {
    content: '';
    position: absolute;
    top: -50%; right: -20%;
    width: 800px; height: 800px;
    background: radial-gradient(circle, rgba(230,196,88,0.15) 0%, transparent 60%);
    border-radius: 50%;
    animation: floatOrb 12s ease-in-out infinite;
}
.stats-section-ultra::after {
    content: '';
    position: absolute;
    bottom: -50%; left: -20%;
    width: 600px; height: 600px;
    background: radial-gradient(circle, rgba(13,94,58,0.3) 0%, transparent 60%);
    border-radius: 50%;
    animation: floatOrb 15s ease-in-out infinite reverse;
}
.stats-inner-ultra {
    max-width: 1400px;
    margin: 0 auto;
    position: relative;
    z-index: 2;
}
.stats-grid-ultra {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 24px;
}
.stat-item-ultra {
    text-align: center;
    padding: 36px 24px;
    background: rgba(255,255,255,0.06);
    backdrop-filter: blur(15px);
    border: 1px solid rgba(255,255,255,0.12);
    border-radius: 20px;
    transition: all 0.4s ease;
    position: relative;
    overflow: hidden;
}
.stat-item-ultra::before {
    content: '';
    position: absolute;
    top: 0; left: 0; right: 0;
    height: 3px;
    background: linear-gradient(90deg, transparent, #e6c458, transparent);
    opacity: 0;
    transition: opacity 0.4s;
}
.stat-item-ultra:hover::before { opacity: 1; }
.stat-item-ultra:hover {
    background: rgba(230,196,88,0.12);
    border-color: rgba(230,196,88,0.4);
    transform: translateY(-8px);
    box-shadow: 0 20px 50px rgba(230,196,88,0.15);
}
.stat-icon-ultra {
    font-size: 32px;
    margin-bottom: 12px;
    display: block;
    opacity: 0.9;
}
.stat-num-ultra {
    font-family: 'Plus Jakarta Sans', sans-serif;
    color: #e6c458 !important;
    font-size: 44px;
    font-weight: 900;
    line-height: 1;
    margin-bottom: 10px;
    letter-spacing: -1px;
    text-shadow: 0 4px 24px rgba(230,196,88,0.4);
}
.stat-label-ultra {
    color: #ffffff !important;
    font-size: 12.5px;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 1.2px;
}

/* ============================================
   LAYANAN GRID ULTRA
   ============================================ */
.layanan-grid-ultra {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 20px;
}
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
.layanan-card-ultra::before {
    content: '';
    position: absolute;
    top: 0; left: 0; right: 0;
    height: 4px;
    background: linear-gradient(90deg, #0d5e3a, #c9a227, #e6c458);
    transform: scaleX(0);
    transform-origin: left;
    transition: transform 0.5s ease;
}
.layanan-card-ultra:hover::before { transform: scaleX(1); }
.layanan-card-ultra:hover {
    transform: translateY(-10px);
    box-shadow: 0 30px 60px rgba(13,94,58,0.18);
    border-color: rgba(201,162,39,0.3);
}
.layanan-icon-ultra {
    width: 80px;
    height: 80px;
    margin: 0 auto 20px;
    border-radius: 24px;
    background: linear-gradient(135deg, #e8f5ef, #d1e8dd);
    color: #0d5e3a !important;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 36px;
    transition: all 0.5s cubic-bezier(0.4, 0, 0.2, 1);
    box-shadow: 0 8px 24px rgba(13,94,58,0.1);
}
.layanan-card-ultra:hover .layanan-icon-ultra {
    background: linear-gradient(135deg, #c9a227, #e6c458);
    color: #ffffff !important;
    transform: scale(1.1) rotate(-8deg);
    box-shadow: 0 12px 32px rgba(201,162,39,0.4);
}
.layanan-title-ultra {
    font-family: 'Plus Jakarta Sans', sans-serif;
    font-size: 15px;
    font-weight: 800;
    color: #083d26 !important;
    margin: 0 0 8px;
    letter-spacing: -0.2px;
}
.layanan-desc-ultra {
    color: #4a5a55 !important;
    font-size: 12px;
    line-height: 1.55;
}

/* ============================================
   FOOTER ULTRA PREMIUM
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
.footer-inner-ultra {
    max-width: 1400px;
    margin: 0 auto;
    position: relative;
    z-index: 2;
}
.footer-grid-ultra {
    display: grid;
    grid-template-columns: 1.8fr 1fr 1fr 1.2fr;
    gap: 44px;
    padding-bottom: 44px;
}
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
    border-radius: 2px;
}
.footer-col-ultra p {
    color: rgba(255,255,255,0.7) !important;
    font-size: 12.5px;
    line-height: 1.9;
    margin: 0 0 8px;
}
.footer-col-ultra a {
    display: block;
    color: rgba(255,255,255,0.7) !important;
    font-size: 12.5px;
    line-height: 2.15;
    text-decoration: none;
    transition: all 0.25s ease;
}
.footer-col-ultra a:hover { 
    color: #e6c458 !important; 
    padding-left: 8px;
}
.footer-brand-ultra {
    display: flex;
    align-items: center;
    gap: 16px;
    margin-bottom: 22px;
}
.footer-logo-ultra {
    width: 60px;
    height: 60px;
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
.footer-brand-title-ultra {
    color: #ffffff !important;
    font-family: 'Plus Jakarta Sans', sans-serif;
    font-size: 15px;
    font-weight: 800;
    text-transform: uppercase;
    letter-spacing: 0.3px;
}
.footer-brand-sub-ultra {
    color: #e6c458 !important;
    font-size: 10px;
    letter-spacing: 1.2px;
    margin-top: 4px;
    font-weight: 800;
}
.footer-social-ultra {
    display: flex;
    gap: 10px;
    margin-top: 22px;
}
.footer-social-item-ultra {
    width: 42px;
    height: 42px;
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
.footer-social-item-ultra:hover {
    background: linear-gradient(135deg, #c9a227, #e6c458);
    border-color: #c9a227;
    color: #083d26 !important;
    transform: translateY(-5px) rotate(-5deg);
    box-shadow: 0 10px 24px rgba(201,162,39,0.4);
}
.footer-bottom-ultra {
    border-top: 1px solid rgba(255,255,255,0.08);
    padding: 26px 0;
    display: flex;
    justify-content: space-between;
    align-items: center;
    flex-wrap: wrap;
    gap: 14px;
    font-size: 11.5px;
    color: rgba(255,255,255,0.5) !important;
}
.footer-bottom-ultra * { color: rgba(255,255,255,0.5) !important; }

/* ============================================
   CHAT WIDGET
   ============================================ */
.chat-widget {
    position: fixed;
    bottom: 24px;
    right: 24px;
    z-index: 9999;
    display: flex;
    flex-direction: column;
    align-items: flex-end;
    gap: 12px;
}
.chat-btn {
    width: 68px;
    height: 68px;
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
    position: relative;
    animation: chatPulse 2.5s infinite;
}
@keyframes chatPulse {
    0%, 100% { box-shadow: 0 14px 40px rgba(13,94,58,0.45), 0 0 0 0 rgba(13,94,58,0.5); }
    50% { box-shadow: 0 14px 40px rgba(13,94,58,0.45), 0 0 0 18px rgba(13,94,58,0); }
}
.chat-btn:hover {
    transform: scale(1.1) rotate(-10deg);
    background: linear-gradient(135deg, #c9a227, #e6c458);
    color: #083d26 !important;
}
.chat-label {
    background: #ffffff;
    color: #083d26 !important;
    padding: 10px 18px;
    border-radius: 20px;
    font-size: 12.5px;
    font-weight: 800;
    box-shadow: 0 8px 24px rgba(0,0,0,0.15);
    border: 2px solid #c9a227;
    display: flex;
    align-items: center;
    gap: 8px;
    animation: chatLabelBounce 2s infinite;
}
@keyframes chatLabelBounce {
    0%, 100% { transform: translateY(0); }
    50% { transform: translateY(-4px); }
}

/* ============================================
   FORM & INPUTS
   ============================================ */
.stButton > button {
    background: linear-gradient(135deg, #0d5e3a, #14734a) !important;
    color: #ffffff !important;
    border: none !important;
    border-radius: 10px !important;
    font-weight: 700 !important;
    box-shadow: 0 6px 16px rgba(13,94,58,0.25) !important;
    transition: all 0.3s ease !important;
}
.stButton > button:hover {
    background: linear-gradient(135deg, #14734a, #c9a227) !important;
    transform: translateY(-2px);
    box-shadow: 0 10px 24px rgba(13,94,58,0.35) !important;
}
div[data-testid="stForm"] {
    background: #ffffff;
    border: 1px solid #e5ebe7;
    border-radius: 20px;
    padding: 28px !important;
    box-shadow: 0 8px 32px rgba(0,0,0,0.04);
}
.stTextInput input, .stTextArea textarea, div[data-baseweb="select"] > div {
    border-radius: 10px !important;
    border-color: #e5ebe7 !important;
    color: #000000 !important;
}
.stTextInput input:focus, .stTextArea textarea:focus {
    border-color: #c9a227 !important;
    box-shadow: 0 0 0 4px rgba(201,162,39,0.15) !important;
}

/* Tabs */
.stTabs [data-baseweb="tab-list"] {
    gap: 4px;
    background: transparent;
    border-bottom: 2px solid #e5ebe7;
}
.stTabs [data-baseweb="tab"] {
    background: transparent;
    border-radius: 10px 10px 0 0;
    padding: 14px 22px;
    color: #4a5a55 !important;
    font-weight: 700;
    font-family: 'Plus Jakarta Sans', sans-serif;
    font-size: 13px;
}
.stTabs [aria-selected="true"] {
    background: linear-gradient(180deg, #f0f6f2, transparent) !important;
    color: #0d5e3a !important;
    border-bottom: 3px solid #0d5e3a;
}

/* ============================================
   RESPONSIVE TABLET
   ============================================ */
@media (max-width: 1100px) {
    .quick-grid-glass { grid-template-columns: repeat(2, 1fr); }
    .warta-grid-ultra { grid-template-columns: repeat(2, 1fr); }
    .stats-grid-ultra { grid-template-columns: repeat(2, 1fr); }
    .layanan-grid-ultra { grid-template-columns: repeat(2, 1fr); }
    .trending-grid { grid-template-columns: 1fr; }
    .content-grid-2col { grid-template-columns: 1fr; }
    .footer-grid-ultra { grid-template-columns: 1fr 1fr; gap: 32px; }
    .sambutan-inner-ultra { grid-template-columns: 280px 1fr; gap: 40px; }
    .hero-ultra-stats { grid-template-columns: repeat(2, 1fr); max-width: 600px; }
}

/* ============================================
   RESPONSIVE MOBILE
   ============================================ */
@media (max-width: 768px) {
    .topbar { 
        flex-direction: column; 
        gap: 8px; 
        text-align: center; 
        padding: 10px 12px;
    }
    .topbar-left, .topbar-right { 
        justify-content: center; 
        gap: 10px; 
        font-size: 10.5px;
    }
    .topbar-item { font-size: 10.5px; }
    
    .header-wrap { padding: 14px 12px; }
    .header-inner { gap: 12px; }
    .header-logo { width: 52px; height: 52px; border-radius: 12px; }
    .header-text-title { font-size: 13.5px; }
    .header-text-sub { font-size: 9.5px; }
    .header-actions { 
        width: 100%; 
        justify-content: center; 
        margin-top: 12px; 
        padding-top: 12px;
        border-top: 1px solid #e5ebe7;
    }
    .header-action-btn { font-size: 11px; padding: 8px 14px; }
    
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
    
    .running-text-bar { padding: 10px 12px; gap: 10px; }
    .running-label { font-size: 9.5px; padding: 5px 10px; }
    .running-scroll { font-size: 11.5px; }
    
    .hero-ultra { min-height: 520px; }
    .hero-ultra-content { padding: 44px 0; }
    .hero-ultra-kicker { font-size: 10px; padding: 7px 14px; letter-spacing: 1.2px; margin-bottom: 18px; }
    .hero-ultra-title { font-size: 26px; margin-bottom: 16px; letter-spacing: -0.8px; }
    .hero-ultra-sub { font-size: 13px; margin-bottom: 26px; line-height: 1.6; }
    .hero-ultra-buttons { gap: 8px; margin-bottom: 32px; }
    .hero-ultra-btn { padding: 12px 22px; font-size: 11.5px; }
    .hero-ultra-stats { grid-template-columns: repeat(2, 1fr); gap: 10px; }
    .hero-stat-ultra { padding: 14px 16px; border-radius: 12px; }
    .hero-stat-num-ultra { font-size: 22px; }
    .hero-stat-label-ultra { font-size: 9px; }
    
    .quick-access-glass { padding: 28px 12px; }
    .quick-grid-glass { grid-template-columns: 1fr 1fr; gap: 12px; }
    .quick-card-glass { padding: 20px 14px; border-radius: 16px; }
    .quick-icon-glass { width: 56px; height: 56px; font-size: 24px; border-radius: 16px; margin-bottom: 12px; }
    .quick-title-glass { font-size: 12.5px; }
    .quick-desc-glass { font-size: 10.5px; }
    
    .page-container { width: 95%; padding: 40px 0; }
    
    .section-header-modern { margin-bottom: 32px; }
    .section-kicker-modern { font-size: 10.5px; letter-spacing: 2px; padding: 0 30px; }
    .section-title-modern { font-size: 22px; }
    .section-desc-modern { font-size: 12.5px; }
    
    .sambutan-section-ultra { padding: 44px 12px; }
    .sambutan-inner-ultra { grid-template-columns: 1fr; gap: 32px; }
    .sambutan-photo-wrap-ultra { max-width: 260px; margin: 0 auto; }
    .sambutan-photo-frame-ultra { display: none; }
    .sambutan-assalam-ultra { font-size: 15px; padding: 12px 16px; }
    .sambutan-text-ultra { font-size: 13.5px; line-height: 1.8; }
    .sambutan-quote-ultra { font-size: 14px; padding: 18px 20px; }
    .sambutan-salam-nama-ultra { font-size: 14px; }
    
    .trending-grid { grid-template-columns: 1fr; gap: 20px; }
    .trending-main-img { height: 240px; }
    .trending-main-content { padding: 20px; }
    .trending-main-title { font-size: 18px; }
    .trending-main-desc { font-size: 12.5px; }
    .trending-thumb { width: 64px; height: 64px; }
    .trending-info-title { font-size: 12px; }
    .trending-rank { width: 26px; height: 26px; font-size: 12px; }
    
    .warta-grid-ultra { grid-template-columns: 1fr; gap: 16px; }
    .warta-card-ultra-img { height: 200px; }
    .warta-card-ultra-body { padding: 20px; }
    .warta-card-ultra-title { font-size: 15px; }
    .warta-card-ultra-desc { font-size: 12.5px; }
    
    .widget-ultra { margin-bottom: 16px; border-radius: 16px; }
    .widget-ultra-head { padding: 14px 18px; font-size: 12.5px; }
    .agenda-item-ultra { padding: 14px 18px; gap: 14px; }
    .agenda-date-ultra { width: 56px; height: 64px; border-radius: 10px; }
    .agenda-day-ultra { font-size: 22px; }
    .agenda-title-ultra { font-size: 12.5px; }
    .agenda-desc-ultra { font-size: 11px; }
    .kesekret-item-ultra { padding: 14px 18px; }
    .kesekret-icon-ultra { width: 38px; height: 38px; font-size: 17px; }
    .kesekret-title-ultra { font-size: 11.5px; }
    
    .stats-section-ultra { padding: 48px 12px; }
    .stats-grid-ultra { grid-template-columns: repeat(2, 1fr); gap: 12px; }
    .stat-item-ultra { padding: 24px 14px; border-radius: 16px; }
    .stat-icon-ultra { font-size: 24px; }
    .stat-num-ultra { font-size: 30px; }
    .stat-label-ultra { font-size: 10.5px; }
    
    .layanan-grid-ultra { grid-template-columns: repeat(2, 1fr); gap: 12px; }
    .layanan-card-ultra { padding: 22px 14px; border-radius: 16px; }
    .layanan-icon-ultra { width: 60px; height: 60px; font-size: 26px; border-radius: 16px; margin-bottom: 14px; }
    .layanan-title-ultra { font-size: 12.5px; }
    .layanan-desc-ultra { font-size: 10.5px; }
    
    .footer-ultra { padding: 44px 14px 0; }
    .footer-grid-ultra { grid-template-columns: 1fr; gap: 30px; padding-bottom: 30px; }
    .footer-col-ultra h4 { font-size: 12.5px; margin-bottom: 14px; padding-bottom: 10px; }
    .footer-col-ultra p, .footer-col-ultra a { font-size: 12px; }
    .footer-logo-ultra { width: 52px; height: 52px; }
    .footer-brand-title-ultra { font-size: 13.5px; }
    .footer-social-item-ultra { width: 36px; height: 36px; font-size: 14px; }
    .footer-bottom-ultra { flex-direction: column; text-align: center; padding: 20px 0; font-size: 11px; }
    
    .chat-widget { bottom: 16px; right: 16px; gap: 8px; }
    .chat-btn { width: 58px; height: 58px; font-size: 24px; }
    .chat-label { font-size: 11px; padding: 8px 14px; }
    
    .stTabs [data-baseweb="tab"] { padding: 10px 14px; font-size: 12px; }
}

@media (max-width: 400px) {
    .nav-link { font-size: 9.5px !important; padding: 10px 4px !important; }
    .hero-ultra-title { font-size: 22px; }
    .hero-ultra-sub { font-size: 12px; }
    .quick-icon-glass { width: 48px; height: 48px; font-size: 20px; }
    .stat-num-ultra { font-size: 26px; }
    .layanan-icon-ultra { width: 52px; height: 52px; font-size: 22px; }
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
        <span class="topbar-badge">ONLINE</span>
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
    <span class="running-label">INFO TERKINI</span>
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

    # MITRA MARQUEE
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

    # QUICK ACCESS GLASS
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

    # SAMBUTAN PIMPINAN ULTRA
    st.markdown(
        f"""
    <section class="sambutan-section-ultra">
        <div class="sambutan-inner-ultra">
            <div class="sambutan-photo-wrap-ultra">
                <div class="sambutan-photo-frame-ultra"></div>
                <img class="sambutan-photo-ultra" src="{SAMBUTAN['foto']}" alt="{SAMBUTAN['nama']}">
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

    # LAYANAN PUBLIK ULTRA
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
            <a href="{href}" {tgt} class="layanan-card-ultra">
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

    # Trending layout: 1 utama + 3 list
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
                    <div class="trending-info-meta">👁️ {item['views']:,} • 📅 {item['date'][:10]}</div>
                </div>
            </a>
            """,
                unsafe_allow_html=True,
            )
        st.markdown('</div>', unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True)

    # WARTA + AGENDA 2 COLUMN
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
        # Grid 2 kolom
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
        # Widget Agenda
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

        # Widget Kesekretariatan
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

    # STATS SECTION ULTRA
    st.markdown(
        f"""
    <section class="stats-section-ultra">
        <div class="stats-inner-ultra">
            <div class="section-header-modern" style="margin-bottom: 44px;">
                <div class="section-kicker-modern" style="color: #e6c458;">DALAM ANGKA</div>
                <h2 class="section-title-modern" style="color: #ffffff;">DPRK Aceh Jaya</h2>
                <p class="section-desc-modern" style="color: rgba(255,255,255,0.75);">Data dan statistik terkini kinerja DPRK Aceh Jaya.</p>
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
                <div style="background: #fff; border: 1px solid #e5ebe7; border-radius: 16px; padding: 20px; text-align: center; border-top: 3px solid #0d5e3a; margin-bottom: 14px; transition: all 0.3s; box-shadow: 0 4px 12px rgba(0,0,0,0.03);">
                    <div style="font-weight: 800; color: #083d26; font-size: 13px; margin-bottom: 5px; font-family: 'Plus Jakarta Sans';">{nama}</div>
                    <div style="color: #c9a227; font-size: 11px; font-weight: 800; text-transform: uppercase; letter-spacing: 0.5px;">{jabatan}</div>
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
                <div style="background: #fff; border: 1px solid #e5ebe7; border-radius: 16px; padding: 20px; text-align: center; border-top: 3px solid #c9a227; margin-bottom: 14px; box-shadow: 0 4px 12px rgba(0,0,0,0.03);">
                    <div style="font-weight: 800; color: #083d26; font-size: 13px; margin-bottom: 5px; font-family: 'Plus Jakarta Sans';">{nama}</div>
                    <div style="color: #4a5a55; font-size: 11px; font-weight: 600;">{jabatan}</div>
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

    for i in range(0, len(filtered), 3):
        cols = st.columns(3)
        for j in range(3):
            if i + j < len(filtered):
                item = filtered[i + j]
                with cols[j]:
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
                            <p class="warta-card-ultra-desc">{item['desc'][:130]}...</p>
                            <a href="#" class="warta-card-ultra-more">Baca →</a>
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
                    <div style="background: #fff; border: 1px solid #e5ebe7; border-radius: 16px; overflow: hidden; margin-bottom: 14px; transition: all 0.4s; box-shadow: 0 4px 12px rgba(0,0,0,0.04);">
                        <div style="overflow: hidden;">
                            <img src="{img}" style="width: 100%; height: 200px; object-fit: cover; transition: transform 0.6s;">
                        </div>
                        <div style="padding: 16px; text-align: center;">
                            <div style="font-family: 'Plus Jakarta Sans'; font-weight: 800; color: #083d26; font-size: 13px;">{title}</div>
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
    <div class="widget-ultra" style="margin-top: 24px;">
        <div class="widget-ultra-head">📞 Kontak Kami</div>
        <div class="widget-ultra-body" style="padding: 22px;">
            <p style="font-size: 13px; color: #083d26; line-height: 1.9; margin: 0 0 14px;">
                <strong style="color: #0d5e3a;">📞 Telepon</strong><br>(0655) 12345
            </p>
            <p style="font-size: 13px; color: #083d26; line-height: 1.9; margin: 0 0 14px;">
                <strong style="color: #0d5e3a;">✉️ Email</strong><br>sekretariat@dprk.acehjaya.go.id
            </p>
            <p style="font-size: 13px; color: #083d26; line-height: 1.9; margin: 0 0 14px;">
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
    <div style="margin-top: 30px; background: #fff; border: 1px solid #e5ebe7; border-radius: 20px; padding: 28px; box-shadow: 0 8px 32px rgba(0,0,0,0.04);">
        <div class="section-header-modern" style="margin-bottom: 22px;">
            <h2 class="section-title-modern" style="font-size: 22px;">Peta Lokasi Kantor</h2>
        </div>
        <div style="width: 100%; height: 360px; border-radius: 16px; overflow: hidden; border: 1px solid #e5ebe7;">
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
    <a href="?page=layanan" class="chat-btn" title="Chat dengan SAVIRA">💬</a>
</div>
""",
    unsafe_allow_html=True,
)

# =========================================================
# FOOTER ULTRA
# =========================================================
st.markdown(
    f"""
<footer class="footer-ultra">
<div class="footer-inner-ultra">
<div class="footer-grid-ultra">

<div class="footer-col-ultra">
<div class="footer-brand-ultra">
<div class="footer-logo-ultra">
    <img src="{LOGO_URL}" alt="Logo DPRK Aceh Jaya"
         onerror="this.onerror=null;this.src='data:image/svg+xml,<svg xmlns=%22http://www.w3.org/2000/svg%22 viewBox=%220 0 100 100%22><text y=%22.9em%22 font-size=%2290%22>🏛️</text></svg>'">
</div>
<div>
<div class="footer-brand-title-ultra">DPRK ACEH JAYA</div>
<div class="footer-brand-sub-ultra">SEKRETARIAT DPRK</div>
</div>
</div>
<p style="color: rgba(255,255,255,0.7); font-size: 12.5px; line-height: 1.9; margin: 0 0 8px;">
Portal resmi Sekretariat Dewan Perwakilan Rakyat Kabupaten Aceh Jaya. Menyediakan informasi kelembagaan, berita, agenda, produk hukum, dan layanan aspirasi masyarakat.
</p>
<div class="footer-social-ultra">
<a href="#" class="footer-social-item-ultra">f</a>
<a href="#" class="footer-social-item-ultra">𝕏</a>
<a href="#" class="footer-social-item-ultra">▶</a>
<a href="#" class="footer-social-item-ultra">◎</a>
<a href="#" class="footer-social-item-ultra">in</a>
</div>
</div>

<div class="footer-col-ultra">
<h4>Navigasi</h4>
<a href="?page=beranda">Beranda</a>
<a href="?page=profil">Profil DPRK</a>
<a href="?page=berita">Berita & Agenda</a>
<a href="?page=galeri">Galeri</a>
<a href="?page=kontak">Kontak</a>
</div>

<div class="footer-col-ultra">
<h4>Layanan Publik</h4>
<a href="?page=layanan">Pengaduan Masyarakat</a>
<a href="?page=kontak">Informasi Publik</a>
<a href="?page=jdih">JDIH</a>
<a href="?page=jdih">Transparansi</a>
<a href="https://elhpkpn.kpk.go.id/" target="_blank">E-LHKPN</a>
</div>

<div class="footer-col-ultra">
<h4>Hubungi Kami</h4>
<p>📍 Jl. Merdeka No. 01</p>
<p>Calang, Kabupaten Aceh Jaya</p>
<p>📞 (0655) 12345</p>
<p>✉️ sekretariat@dprk.acehjaya.go.id</p>
<p>🕐 Senin–Jumat, 08.00–16.00 WIB</p>
</div>

</div>

<div class="footer-bottom-ultra">
<div>© {datetime.now().year} Sekretariat DPRK Kabupaten Aceh Jaya. Seluruh hak cipta dilindungi.</div>
<div>Portal Informasi Publik • Kabupaten Aceh Jaya</div>
</div>

</div>
</footer>
""",
    unsafe_allow_html=True,
)

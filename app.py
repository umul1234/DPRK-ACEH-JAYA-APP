# app.py
import streamlit as st
from datetime import datetime
import pandas as pd
import plotly.express as px
import random

# =========================================================
# CEK MODE ADMIN
# =========================================================
if st.query_params.get("admin") == "true":
    from admin_panel import render_admin
    render_admin()
    st.stop()

# =========================================================
# IMPORT DATABASE
# =========================================================
from database import (
    get_all_berita, get_all_agenda, get_all_galeri,
    get_running_text_active, create_pengaduan,
    get_all_kesekretariatan, get_all_jdih,
    get_all_pimpinan, get_all_pejabat,
    seed_default_admin,
)

try:
    seed_default_admin()
except Exception:
    pass

# =========================================================
# KONFIGURASI
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
    "Beranda": "Beranda", "Profil": "Profil", "Berita": "Berita",
    "Galeri": "Galeri", "Layanan": "Layanan", "JDIH": "JDIH", "Kontak": "Kontak",
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
    "paragraf2": "Melalui portal ini, kami berkomitmen untuk menyediakan akses informasi publik yang mudah, cepat, dan transparan.",
    "penutup": "Mari bersama-sama membangun Aceh Jaya yang lebih maju, sejahtera, dan bermartabat.",
}

# Ambil data dinamis dari database
WARTA_DPRK = get_all_berita()
AGENDA_TERKINI = get_all_agenda()
KESEKRETARIATAN = get_all_kesekretariatan()
GALERI_DATA = get_all_galeri()
RUNNING_TEXTS = get_running_text_active()
JDIH_DB = get_all_jdih()
PIMPINAN_DB = get_all_pimpinan()
PEJABAT_DB = get_all_pejabat()

# Fallback
if not WARTA_DPRK:
    WARTA_DPRK = [{"title": "Belum ada berita", "date": "-", "desc_text": "-", "image_url": "", "kategori": "-", "views": 0}]

PIMPINAN_DAN_ANGGOTA = [(p["nama"], p["jabatan"]) for p in PIMPINAN_DB] or [("Belum ada data", "Tambahkan dari admin panel")]
PEJABAT_SEKRETARIAT = [(p["nama"], p["jabatan"]) for p in PEJABAT_DB] or [("Belum ada data", "Tambahkan dari admin panel")]

running_content = " ★ ".join([r["content"] for r in RUNNING_TEXTS]) if RUNNING_TEXTS else "Selamat Datang di Portal Resmi DPRK Kabupaten Aceh Jaya"

if not JDIH_DB:
    JDIH_DB = [{"nomor": "-", "tentang": "Belum ada data", "status": "-"}]

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
# CSS (SAMA dengan kode lama Anda)
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
}
.topbar * { color: #ffffff !important; }
.topbar-left, .topbar-right { display: flex; gap: 16px; align-items: center; flex-wrap: wrap; }
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

.header-wrap {
    background: #ffffff;
    padding: 18px 16px;
    border-bottom: 1px solid #e5ebe7;
    box-shadow: 0 2px 12px rgba(0,0,0,0.03);
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
}

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
    flex-shrink: 0;
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
        radial-gradient(ellipse at 20% 30%, rgba(230,196,88,0.15) 0%, transparent 60%);
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
}
.hero-ultra-title {
    font-family: 'Plus Jakarta Sans', sans-serif;
    font-size: clamp(32px, 5.5vw, 72px);
    font-weight: 900;
    line-height: 1.02;
    letter-spacing: -2px;
    margin-bottom: 26px;
    color: #ffffff !important;
    max-width: 950px;
}
.hero-ultra-title span {
    background: linear-gradient(135deg, #e6c458 0%, #f5e090 30%, #c9a227 70%, #e6c458 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
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
    transition: all 0.35s;
}
.hero-ultra-btn:hover { transform: translateY(-4px); box-shadow: 0 16px 40px rgba(201,162,39,0.6); }
.hero-ultra-btn-outline {
    background: rgba(255,255,255,0.08);
    color: #ffffff !important;
    border: 2px solid rgba(255,255,255,0.5);
    box-shadow: none;
}
.hero-ultra-stats { display: grid; grid-template-columns: repeat(4, 1fr); gap: 16px; max-width: 900px; }
.hero-stat-ultra {
    background: rgba(255,255,255,0.06);
    backdrop-filter: blur(20px);
    border: 1px solid rgba(255,255,255,0.15);
    padding: 20px 22px;
    border-radius: 16px;
    transition: all 0.35s ease;
}
.hero-stat-ultra:hover { background: rgba(230,196,88,0.12); border-color: rgba(230,196,88,0.4); }
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
    transition: all 0.4s;
}
.quick-card-glass:hover { transform: translateY(-10px); box-shadow: 0 30px 60px rgba(13,94,58,0.18); border-color: #c9a227; }
.quick-icon-glass {
    width: 72px; height: 72px; border-radius: 20px;
    display: flex; align-items: center; justify-content: center;
    font-size: 32px; margin-bottom: 18px;
    background: linear-gradient(135deg, #e8f5ef, #d1e8dd);
    color: #0d5e3a !important;
}
.quick-card-glass:hover .quick-icon-glass {
    background: linear-gradient(135deg, #c9a227, #e6c458);
    color: #ffffff !important;
    transform: scale(1.1) rotate(-10deg);
}
.quick-title-glass { font-family: 'Plus Jakarta Sans', sans-serif; font-size: 15px; font-weight: 800; color: #083d26 !important; margin: 0 0 6px; }
.quick-desc-glass { font-size: 12px; color: #4a5a55 !important; font-weight: 500; }

.sambutan-section-ultra {
    background: linear-gradient(135deg, #ffffff 0%, #f8faf9 50%, #faf6e8 100%);
    padding: 80px 16px;
}
.sambutan-inner-ultra {
    max-width: 1400px;
    margin: 0 auto;
    display: grid;
    grid-template-columns: 340px 1fr;
    gap: 60px;
    align-items: start;
}
.sambutan-photo-wrap-ultra { text-align: center; }
.sambutan-photo-ultra {
    width: 100%;
    max-width: 340px;
    aspect-ratio: 3/4;
    object-fit: cover;
    border-radius: 20px;
    box-shadow: 0 30px 80px rgba(13,94,58,0.3);
    border: 5px solid #ffffff;
}
.sambutan-photo-info-ultra {
    margin-top: 28px;
    background: #ffffff;
    border: 1px solid #e5ebe7;
    border-radius: 16px;
    padding: 20px;
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
}
.sambutan-salam-ultra { margin-top: 32px; padding-top: 24px; border-top: 2px dashed #e5ebe7; }
.sambutan-salam-line-ultra { color: #4a5a55 !important; font-size: 13.5px; margin: 0 0 6px; }
.sambutan-salam-nama-ultra { font-family: 'Plus Jakarta Sans', sans-serif; font-size: 16px; font-weight: 900; color: #083d26 !important; text-transform: uppercase; margin: 10px 0 4px; }
.sambutan-salam-jabatan-ultra { color: #c9a227 !important; font-size: 12.5px; font-weight: 700; }

.trending-main {
    background: #ffffff;
    border: 1px solid #e5ebe7;
    border-radius: 20px;
    overflow: hidden;
    transition: all 0.4s ease;
}
.trending-main:hover { transform: translateY(-6px); box-shadow: 0 30px 60px rgba(13,94,58,0.18); }
.trending-main-img { position: relative; width: 100%; height: 380px; overflow: hidden; }
.trending-main-img img { width: 100%; height: 100%; object-fit: cover; }
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
.trending-item:hover { border-color: #c9a227; transform: translateX(6px); }
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
}
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
}
.trending-info-meta { color: #4a5a55 !important; font-size: 10.5px; font-weight: 600; }

.warta-card-ultra {
    background: #ffffff;
    border: 1px solid #e5ebe7;
    border-radius: 20px;
    overflow: hidden;
    text-decoration: none !important;
    color: inherit;
    transition: all 0.4s;
    display: flex;
    flex-direction: column;
}
.warta-card-ultra:hover { transform: translateY(-10px); box-shadow: 0 30px 70px rgba(13,94,58,0.2); }
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

.widget-ultra {
    background: #ffffff;
    border: 1px solid #e5ebe7;
    border-radius: 20px;
    overflow: hidden;
    margin-bottom: 24px;
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
.agenda-item-ultra { display: flex; gap: 16px; padding: 18px 22px; border-bottom: 1px solid #e5ebe7; }
.agenda-item-ultra:last-child { border-bottom: none; }
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
}
.agenda-day-ultra { font-family: 'Plus Jakarta Sans', sans-serif; font-size: 26px; font-weight: 900; line-height: 1; color: #ffffff !important; }
.agenda-month-ultra { font-size: 9.5px; font-weight: 800; color: #ffffff !important; margin-top: 4px; }
.agenda-content-ultra { flex: 1; min-width: 0; }
.agenda-title-ultra { color: #083d26 !important; font-family: 'Plus Jakarta Sans', sans-serif; font-size: 13.5px; font-weight: 800; line-height: 1.4; margin: 0 0 6px; }
.agenda-desc-ultra { color: #4a5a55 !important; font-size: 11.5px; line-height: 1.55; margin: 0 0 8px; }
.agenda-footer-ultra { display: inline-flex; align-items: center; gap: 6px; color: #c9a227 !important; font-size: 10.5px; font-weight: 800; text-transform: uppercase; padding: 4px 10px; background: #faf6e8; border-radius: 8px; }

.kesekret-item-ultra { display: flex; gap: 14px; padding: 16px 22px; border-bottom: 1px solid #e5ebe7; }
.kesekret-item-ultra:last-child { border-bottom: none; }
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

.stats-section-ultra {
    background: linear-gradient(135deg, #062b1b 0%, #0d5e3a 50%, #062b1b 100%);
    padding: 80px 16px;
}
.stats-inner-ultra { max-width: 1400px; margin: 0 auto; }
.stats-grid-ultra { display: grid; grid-template-columns: repeat(4, 1fr); gap: 24px; }
.stat-item-ultra {
    text-align: center;
    padding: 36px 24px;
    background: rgba(255,255,255,0.06);
    border: 1px solid rgba(255,255,255,0.12);
    border-radius: 20px;
}
.stat-item-ultra:hover { background: rgba(230,196,88,0.12); }
.stat-icon-ultra { font-size: 32px; margin-bottom: 12px; display: block; }
.stat-num-ultra { font-family: 'Plus Jakarta Sans', sans-serif; color: #e6c458 !important; font-size: 44px; font-weight: 900; line-height: 1; margin-bottom: 10px; }
.stat-label-ultra { color: #ffffff !important; font-size: 12.5px; font-weight: 700; text-transform: uppercase; letter-spacing: 1.2px; }

.layanan-card-ultra {
    background: #ffffff;
    border: 1px solid #e5ebe7;
    border-radius: 20px;
    padding: 32px 24px;
    text-align: center;
    text-decoration: none !important;
    color: inherit;
    transition: all 0.4s;
}
.layanan-card-ultra:hover { transform: translateY(-10px); box-shadow: 0 30px 60px rgba(13,94,58,0.18); }
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
}
.layanan-card-ultra:hover .layanan-icon-ultra {
    background: linear-gradient(135deg, #c9a227, #e6c458);
    color: #ffffff !important;
    transform: scale(1.1) rotate(-8deg);
}
.layanan-title-ultra { font-family: 'Plus Jakarta Sans', sans-serif; font-size: 15px; font-weight: 800; color: #083d26 !important; margin: 0 0 8px; }
.layanan-desc-ultra { color: #4a5a55 !important; font-size: 12px; line-height: 1.55; }

.footer-ultra {
    background: linear-gradient(180deg, #062b1b 0%, #041f13 100%);
    color: #ffffff !important;
    padding: 70px 16px 0;
}
.footer-ultra * { color: #ffffff !important; }
.footer-inner-ultra { max-width: 1400px; margin: 0 auto; }
.footer-grid-ultra { display: grid; grid-template-columns: 1.8fr 1fr 1fr 1.2fr; gap: 44px; padding-bottom: 44px; }
.footer-col-ultra h4 {
    color: #ffffff !important;
    font-size: 13.5px;
    font-weight: 800;
    margin: 0 0 22px;
    text-transform: uppercase;
    letter-spacing: 1.2px;
    padding-bottom: 14px;
    position: relative;
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
.footer-col-ultra a { display: block; color: rgba(255,255,255,0.7) !important; font-size: 12.5px; line-height: 2.15; text-decoration: none; }
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
}
.footer-social-item-ultra:hover { background: linear-gradient(135deg, #c9a227, #e6c458); color: #083d26 !important; }
.footer-bottom-ultra { border-top: 1px solid rgba(255,255,255,0.08); padding: 26px 0; display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 14px; font-size: 11.5px; }
.footer-bottom-ultra * { color: rgba(255,255,255,0.5) !important; }

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

.stButton > button {
    background: linear-gradient(135deg, #0d5e3a, #14734a) !important;
    color: #ffffff !important;
    border: none !important;
    border-radius: 10px !important;
    font-weight: 700 !important;
}
.stButton > button:hover { background: linear-gradient(135deg, #14734a, #c9a227) !important; }

div[data-testid="stForm"] { background: #ffffff; border: 1px solid #e5ebe7; border-radius: 20px; padding: 28px !important; }

@media (max-width: 1100px) {
    .stats-grid-ultra { grid-template-columns: repeat(2, 1fr); }
    .footer-grid-ultra { grid-template-columns: 1fr 1fr; gap: 32px; }
    .sambutan-inner-ultra { grid-template-columns: 280px 1fr; gap: 40px; }
    .hero-ultra-stats { grid-template-columns: repeat(2, 1fr); max-width: 600px; }
}

@media (max-width: 768px) {
    .topbar { flex-direction: column; gap: 6px; text-align: center; padding: 8px 12px; }
    .header-text-title { font-size: 13px; }
    .header-actions { width: 100%; justify-content: center; margin-top: 10px; }
    .nav-link { font-size: 10px !important; padding: 12px 8px !important; flex: 1 1 calc(25% - 2px); text-align: center; }
    .hero-ultra { min-height: 480px; }
    .hero-ultra-content { padding: 40px 0; }
    .hero-ultra-title { font-size: 24px; }
    .hero-ultra-stats { grid-template-columns: repeat(2, 1fr); }
    .sambutan-inner-ultra { grid-template-columns: 1fr; }
    .stats-grid-ultra { grid-template-columns: 1fr 1fr; gap: 10px; }
    .footer-grid-ultra { grid-template-columns: 1fr; }
    .chat-btn { width: 56px; height: 56px; font-size: 22px; }
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
st.markdown(f"""
<div class="topbar">
    <div class="topbar-left">
        <div class="topbar-item"><span>📞</span><span>(0655) 12345</span></div>
        <div class="topbar-item"><span>✉️</span><span>sekretariat@dprk.acehjaya.go.id</span></div>
    </div>
    <div class="topbar-right">
        <span class="topbar-badge">ONLINE</span>
        <div class="topbar-item"><span>🕐</span><span>{now.strftime('%H:%M WIB')}</span></div>
        <a href="?admin=true" class="topbar-lang">🔐 Admin</a>
    </div>
</div>
""", unsafe_allow_html=True)

# =========================================================
# HEADER
# =========================================================
st.markdown(f"""
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
""", unsafe_allow_html=True)

# =========================================================
# NAVBAR
# =========================================================
nav_items_html = ""
for key in PAGES.keys():
    page_value = PAGES[key]
    url_key = page_value.lower().replace(" & ", "-").replace(" ", "-")
    active_class = "nav-link-active" if st.session_state.page == page_value else ""
    nav_items_html += f'<a href="?page={url_key}" class="nav-link {active_class}">{page_value}</a>'

st.markdown(f"""
<div class="navbar">
    <div class="navbar-inner">
        {nav_items_html}
    </div>
</div>
""", unsafe_allow_html=True)

# =========================================================
# RUNNING TEXT DINAMIS
# =========================================================
st.markdown(f"""
<div class="running-text-bar">
    <span class="running-label">INFO</span>
    <div class="running-scroll-wrap">
        <div class="running-scroll">{running_content}</div>
    </div>
</div>
""", unsafe_allow_html=True)

# =========================================================
# HALAMAN: BERANDA
# =========================================================
if st.session_state.page == "Beranda":
    slide = HERO_SLIDES[st.session_state.slide_index % len(HERO_SLIDES)]
    st.markdown(f"""
    <section class="hero-ultra">
        <div class="hero-ultra-bg" style="background-image: url('{slide['image']}');"></div>
        <div class="hero-ultra-overlay"></div>
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
                    <span class="hero-stat-num-ultra">{len(PIMPINAN_DB) or 20}</span>
                    <div class="hero-stat-label-ultra">Anggota DPRK</div>
                </div>
                <div class="hero-stat-ultra">
                    <span class="hero-stat-num-ultra">4</span>
                    <div class="hero-stat-label-ultra">Komisi</div>
                </div>
                <div class="hero-stat-ultra">
                    <span class="hero-stat-num-ultra">{len(JDIH_DB)}+</span>
                    <div class="hero-stat-label-ultra">Produk Hukum</div>
                </div>
                <div class="hero-stat-ultra">
                    <span class="hero-stat-num-ultra">{st.session_state.visitor_count:,}</span>
                    <div class="hero-stat-label-ultra">Kunjungan</div>
                </div>
            </div>
        </div>
    </section>
    """, unsafe_allow_html=True)

    nav_cols = st.columns([1, 4, 1])
    with nav_cols[0]:
        if st.button("◀ Prev", key="slide_prev", use_container_width=True):
            st.session_state.slide_index = (st.session_state.slide_index - 1) % len(HERO_SLIDES)
            st.rerun()
    with nav_cols[2]:
        if st.button("Next ▶", key="slide_next", use_container_width=True):
            st.session_state.slide_index = (st.session_state.slide_index + 1) % len(HERO_SLIDES)
            st.rerun()

    # MITRA
    mitra_html = "".join([f'<div class="mitra-item">{m}</div>' for m in MITRA * 2])
    st.markdown(f"""
    <div class="mitra-section">
        <div class="mitra-label">DIDUKUNG OLEH INSTANSI & MITRA STRATEGIS</div>
        <div class="mitra-track">{mitra_html}</div>
    </div>
    """, unsafe_allow_html=True)

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
            st.markdown(f"""
            <a href="?page={target}" class="quick-card-glass">
                <div class="quick-icon-glass">{icon}</div>
                <div class="quick-title-glass">{title}</div>
                <div class="quick-desc-glass">{desc}</div>
            </a>
            """, unsafe_allow_html=True)
    st.markdown("</div></div>", unsafe_allow_html=True)

    # SAMBUTAN
    st.markdown(f"""
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
    """, unsafe_allow_html=True)

    # LAYANAN
    st.markdown('<div class="page-container">', unsafe_allow_html=True)
    st.markdown("""
    <div class="section-header-modern">
        <div class="section-kicker-modern">AKSES CEPAT</div>
        <h2 class="section-title-modern">Layanan Publik</h2>
        <p class="section-desc-modern">Akses layanan dan informasi DPRK Aceh Jaya secara mudah dan cepat.</p>
    </div>
    """, unsafe_allow_html=True)

    layanan_items = [
        ("📢", "Pengaduan Masyarakat", "Sampaikan aspirasi & laporan", "layanan"),
        ("📜", "JDIH", "Produk hukum daerah", "jdih"),
        ("📅", "Agenda DPRK", "Jadwal rapat & sidang", "berita"),
        ("📊", "Transparansi", "Informasi publik", "jdih"),
    ]
    lay_cols = st.columns(4)
    for i, (icon, title, desc, target) in enumerate(layanan_items):
        with lay_cols[i]:
            st.markdown(f"""
            <a href="?page={target}" class="layanan-card-ultra">
                <div class="layanan-icon-ultra">{icon}</div>
                <div class="layanan-title-ultra">{title}</div>
                <div class="layanan-desc-ultra">{desc}</div>
            </a>
            """, unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

    # WARTA + WIDGET
    st.markdown('<div class="page-container">', unsafe_allow_html=True)
    main_col, side_col = st.columns([2, 1])

    with main_col:
        st.markdown("""
        <div class="section-header-modern" style="text-align:left; margin-bottom:28px;">
            <div class="section-kicker-modern" style="text-align:left; padding:0;">WARTA DPRK</div>
            <h2 class="section-title-modern" style="text-align:left;">Berita Terbaru</h2>
        </div>
        """, unsafe_allow_html=True)
        for i in range(0, min(4, len(WARTA_DPRK)), 2):
            wcols = st.columns(2)
            for j in range(2):
                if i + j < len(WARTA_DPRK):
                    item = WARTA_DPRK[i + j]
                    with wcols[j]:
                        img = item.get("image_url") or "https://images.unsplash.com/photo-1529107386315-e1a2ed48a620?auto=format&fit=crop&w=800&q=80"
                        st.markdown(f"""
                        <div class="warta-card-ultra" style="margin-bottom: 18px;">
                            <div class="warta-card-ultra-img">
                                <span class="warta-card-ultra-cat">{item.get('kategori', '-')}</span>
                                <span class="warta-card-ultra-views">👁️ {item.get('views', 0):,}</span>
                                <img src="{img}">
                            </div>
                            <div class="warta-card-ultra-body">
                                <div class="warta-card-ultra-date">📅 {item.get('date', '-')}</div>
                                <h3 class="warta-card-ultra-title">{item['title']}</h3>
                                <p class="warta-card-ultra-desc">{(item.get('desc_text', '') or '')[:110]}...</p>
                                <a href="?page=berita" class="warta-card-ultra-more">Baca Selengkapnya →</a>
                            </div>
                        </div>
                        """, unsafe_allow_html=True)

    with side_col:
        st.markdown('<div class="widget-ultra"><div class="widget-ultra-head">📅 Agenda Terkini</div>', unsafe_allow_html=True)
        for item in AGENDA_TERKINI[:3]:
            st.markdown(f"""
            <div class="agenda-item-ultra">
                <div class="agenda-date-ultra">
                    <div class="agenda-day-ultra">{item.get('hari', '00')}</div>
                    <div class="agenda-month-ultra">{item.get('bulan_tahun', '-')}</div>
                </div>
                <div class="agenda-content-ultra">
                    <div class="agenda-title-ultra">{item['judul']}</div>
                    <p class="agenda-desc-ultra">{(item.get('deskripsi', '') or '')[:80]}</p>
                    <div class="agenda-footer-ultra">📅 {item.get('tanggal_full', '-')}</div>
                </div>
            </div>
            """, unsafe_allow_html=True)
        if not AGENDA_TERKINI:
            st.info("Belum ada agenda")
        st.markdown("</div>", unsafe_allow_html=True)

        st.markdown('<div class="widget-ultra"><div class="widget-ultra-head">📰 Kesekretariatan</div>', unsafe_allow_html=True)
        for item in KESEKRETARIATAN[:3]:
            st.markdown(f"""
            <div class="kesekret-item-ultra">
                <div class="kesekret-icon-ultra">📋</div>
                <div>
                    <div class="kesekret-title-ultra">{item['title']}</div>
                    <div class="kesekret-date-ultra">📅 {item.get('date', '-')}</div>
                </div>
            </div>
            """, unsafe_allow_html=True)
        if not KESEKRETARIATAN:
            st.info("Belum ada data")
        st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True)

    # STATS
    st.markdown(f"""
    <section class="stats-section-ultra">
        <div class="stats-inner-ultra">
            <div class="section-header-modern" style="margin-bottom: 40px;">
                <div class="section-kicker-modern" style="color: #e6c458;">DALAM ANGKA</div>
                <h2 class="section-title-modern" style="color: #ffffff;">DPRK Aceh Jaya</h2>
            </div>
            <div class="stats-grid-ultra">
                <div class="stat-item-ultra">
                    <span class="stat-icon-ultra">👥</span>
                    <div class="stat-num-ultra">{len(PIMPINAN_DB) or 20}</div>
                    <div class="stat-label-ultra">Anggota DPRK</div>
                </div>
                <div class="stat-item-ultra">
                    <span class="stat-icon-ultra">🏛️</span>
                    <div class="stat-num-ultra">4</div>
                    <div class="stat-label-ultra">Komisi DPRK</div>
                </div>
                <div class="stat-item-ultra">
                    <span class="stat-icon-ultra">📜</span>
                    <div class="stat-num-ultra">{len(JDIH_DB)}+</div>
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
    """, unsafe_allow_html=True)

    # CHART
    st.markdown('<div class="page-container">', unsafe_allow_html=True)
    st.markdown("""
    <div class="section-header-modern">
        <div class="section-kicker-modern">DATA & STATISTIK</div>
        <h2 class="section-title-modern">Dashboard Kinerja</h2>
    </div>
    """, unsafe_allow_html=True)

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
    st.markdown("""
    <div class="section-header-modern">
        <div class="section-kicker-modern">TENTANG DPRK</div>
        <h2 class="section-title-modern">Profil DPRK Aceh Jaya</h2>
        <p class="section-desc-modern">DPRK Aceh Jaya menjalankan fungsi legislasi, anggaran, dan pengawasan.</p>
    </div>
    """, unsafe_allow_html=True)

    tab1, tab2 = st.tabs(["🏛️ Pimpinan & Anggota", "🏢 Pejabat Sekretariat"])

    with tab1:
        cols = st.columns(2)
        for i, (nama, jabatan) in enumerate(PIMPINAN_DAN_ANGGOTA):
            with cols[i % 2]:
                st.markdown(f"""
                <div style="background: #fff; border: 1px solid #e5ebe7; border-radius: 12px; padding: 14px; text-align: center; border-top: 3px solid #0d5e3a; margin-bottom: 10px;">
                    <div style="font-weight: 800; color: #083d26; font-size: 11.5px; margin-bottom: 4px;">{nama}</div>
                    <div style="color: #c9a227; font-size: 9.5px; font-weight: 800;">{jabatan}</div>
                </div>
                """, unsafe_allow_html=True)

    with tab2:
        cols = st.columns(2)
        for i, (nama, jabatan) in enumerate(PEJABAT_SEKRETARIAT):
            with cols[i % 2]:
                st.markdown(f"""
                <div style="background: #fff; border: 1px solid #e5ebe7; border-radius: 12px; padding: 14px; text-align: center; border-top: 3px solid #c9a227; margin-bottom: 10px;">
                    <div style="font-weight: 800; color: #083d26; font-size: 11.5px; margin-bottom: 4px;">{nama}</div>
                    <div style="color: #4a5a55; font-size: 9.5px;">{jabatan}</div>
                </div>
                """, unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True)

# =========================================================
# HALAMAN: BERITA
# =========================================================
elif st.session_state.page == "Berita":
    st.markdown('<div class="page-container">', unsafe_allow_html=True)
    st.markdown("""
    <div class="section-header-modern">
        <div class="section-kicker-modern">PUBLIKASI</div>
        <h2 class="section-title-modern">Warta DPRK</h2>
    </div>
    """, unsafe_allow_html=True)

    categories = ["Semua"] + list(set(item.get("kategori", "Lainnya") for item in WARTA_DPRK if item.get("kategori")))
    fc1, fc2 = st.columns(2)
    with fc1:
        selected = st.selectbox("🔍 Kategori", categories)
    with fc2:
        search = st.text_input("🔎 Cari", placeholder="Kata kunci...")

    filtered = WARTA_DPRK
    if selected != "Semua":
        filtered = [i for i in filtered if i.get("kategori") == selected]
    if search:
        filtered = [i for i in filtered if search.lower() in i["title"].lower()]

    for i in range(0, len(filtered), 3):
        cols = st.columns(3)
        for j in range(3):
            if i + j < len(filtered):
                item = filtered[i + j]
                with cols[j]:
                    img = item.get("image_url") or "https://images.unsplash.com/photo-1529107386315-e1a2ed48a620?auto=format&fit=crop&w=800&q=80"
                    st.markdown(f"""
                    <div class="warta-card-ultra" style="margin-bottom: 14px;">
                        <div class="warta-card-ultra-img">
                            <span class="warta-card-ultra-cat">{item.get('kategori', '-')}</span>
                            <span class="warta-card-ultra-views">👁️ {item.get('views', 0):,}</span>
                            <img src="{img}">
                        </div>
                        <div class="warta-card-ultra-body">
                            <div class="warta-card-ultra-date">📅 {item.get('date', '-')}</div>
                            <h3 class="warta-card-ultra-title">{item['title']}</h3>
                            <p class="warta-card-ultra-desc">{(item.get('desc_text', '') or '')[:100]}...</p>
                        </div>
                    </div>
                    """, unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True)

# =========================================================
# HALAMAN: GALERI
# =========================================================
elif st.session_state.page == "Galeri":
    st.markdown('<div class="page-container">', unsafe_allow_html=True)
    st.markdown("""
    <div class="section-header-modern">
        <div class="section-kicker-modern">DOKUMENTASI</div>
        <h2 class="section-title-modern">Galeri Foto</h2>
    </div>
    """, unsafe_allow_html=True)

    if not GALERI_DATA:
        st.info("Belum ada foto galeri")
    else:
        for i in range(0, len(GALERI_DATA), 2):
            cols = st.columns(2)
            for j in range(2):
                if i + j < len(GALERI_DATA):
                    item = GALERI_DATA[i + j]
                    with cols[j]:
                        st.markdown(f"""
                        <div style="background:#fff;border:1px solid #e5ebe7;border-radius:12px;overflow:hidden;margin-bottom:10px;">
                            <img src="{item['image_url']}" style="width:100%;height:200px;object-fit:cover;">
                            <div style="padding:10px;text-align:center;font-weight:700;color:#083d26;font-size:12px;">{item['title']}</div>
                        </div>
                        """, unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

# =========================================================
# HALAMAN: LAYANAN
# =========================================================
elif st.session_state.page == "Layanan":
    st.markdown('<div class="page-container">', unsafe_allow_html=True)
    st.markdown("""
    <div class="section-header-modern">
        <div class="section-kicker-modern">PELAYANAN</div>
        <h2 class="section-title-modern">Layanan Aspirasi & Pengaduan</h2>
    </div>
    """, unsafe_allow_html=True)

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
                tiket = f"ADU-{nomor}"
                try:
                    create_pengaduan(nama, nik, kategori, prioritas, lokasi, isi, tiket)
                    st.success(f"✅ Laporan diterima! Nomor tiket: **{tiket}**")
                except Exception as e:
                    st.error(f"Gagal mengirim: {e}")
            else:
                st.error("⚠️ Mohon lengkapi data.")

    st.markdown("</div>", unsafe_allow_html=True)

# =========================================================
# HALAMAN: JDIH
# =========================================================
elif st.session_state.page == "JDIH":
    st.markdown('<div class="page-container">', unsafe_allow_html=True)
    st.markdown("""
    <div class="section-header-modern">
        <div class="section-kicker-modern">DOKUMENTASI HUKUM</div>
        <h2 class="section-title-modern">JDIH & Transparansi</h2>
    </div>
    """, unsafe_allow_html=True)

    df = pd.DataFrame(
        [(i+1, j.get("nomor", "-"), j.get("tentang", "-"), j.get("status", "-")) for i, j in enumerate(JDIH_DB)],
        columns=["No", "Nomor & Tahun", "Tentang", "Status"]
    )
    st.dataframe(df, use_container_width=True, hide_index=True)
    st.markdown("</div>", unsafe_allow_html=True)

# =========================================================
# HALAMAN: KONTAK
# =========================================================
else:
    st.markdown('<div class="page-container">', unsafe_allow_html=True)
    st.markdown("""
    <div class="section-header-modern">
        <div class="section-kicker-modern">INFORMASI KONTAK</div>
        <h2 class="section-title-modern">Hubungi Kami</h2>
    </div>
    """, unsafe_allow_html=True)

    cols = st.columns(3)
    contacts = [
        ("📍", "Alamat", "Jl. Merdeka No. 01, Calang"),
        ("📞", "Telepon", "(0655) 12345"),
        ("✉️", "Email", "sekretariat@dprk.acehjaya.go.id"),
    ]
    for i, (icon, title, value) in enumerate(contacts):
        with cols[i]:
            st.markdown(f"""
            <div class="layanan-card-ultra">
                <div class="layanan-icon-ultra">{icon}</div>
                <div class="layanan-title-ultra">{title}</div>
                <div class="layanan-desc-ultra">{value}</div>
            </div>
            """, unsafe_allow_html=True)

    st.markdown("""
    <div style="margin-top: 20px; background: #fff; border: 1px solid #e5ebe7; border-radius: 16px; padding: 16px;">
        <div style="width: 100%; height: 260px; border-radius: 12px; overflow: hidden;">
            <iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3988.5!2d95.39!3d4.71!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x30403e5f3a0b0b0b%3A0x0!2sCalang%2C%20Aceh%20Jaya%20Regency%2C%20Aceh!5e0!3m2!1sen!2sid!4v1600000000000" width="100%" height="100%" style="border:0;" allowfullscreen="" loading="lazy"></iframe>
        </div>
    </div>
    """, unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

# =========================================================
# CHAT WIDGET
# =========================================================
st.markdown("""
<div class="chat-widget">
    <div class="chat-label">💬 Chat SAVIRA!</div>
    <a href="?page=layanan" class="chat-btn" title="Chat SAVIRA">💬</a>
</div>
""", unsafe_allow_html=True)

# =========================================================
# FOOTER
# =========================================================
st.markdown(f"""
<footer class="footer-ultra">
<div class="footer-inner-ultra">
<div class="footer-grid-ultra">
<div class="footer-col-ultra">
<div class="footer-brand-ultra">
<div class="footer-logo-ultra">
    <img src="{LOGO_URL}" alt="Logo">
</div>
<div>
<div class="footer-brand-title-ultra">DPRK ACEH JAYA</div>
<div class="footer-brand-sub-ultra">SEKRETARIAT DPRK</div>
</div>
</div>
<p style="color: rgba(255,255,255,0.7); font-size: 11.5px; line-height: 1.8;">Portal resmi Sekretariat DPRK Kabupaten Aceh Jaya.</p>
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
<a href="?admin=true">🔐 Admin Panel</a>
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
""", unsafe_allow_html=True)

import streamlit as st
from datetime import datetime
import pandas as pd

# =========================================================
# KONFIGURASI HALAMAN
# =========================================================
st.set_page_config(
    page_title="DPRK Aceh Jaya | Portal Resmi",
    page_icon="🏛️",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# =========================================================
# DATA
# =========================================================
PAGES = {
    "Beranda": "Beranda",
    "Profil": "Profil & Pimpinan",
    "Berita": "Berita & Agenda",
    "Layanan": "Layanan & Pengaduan",
    "JDIH": "JDIH & Transparansi",
    "Kontak": "Hubungi Kami",
}

NEWS = [
    {
        "tag": "PARIPURNA",
        "date": "15 September 2026",
        "title": "Pembahasan KUA-PPAS 2027",
        "desc": "Rapat paripurna membahas kebijakan umum anggaran dan prioritas plafon anggaran sementara tahun 2027.",
        "image": "https://images.unsplash.com/photo-1556761175-b413da4baf72?auto=format&fit=crop&w=1200&q=80",
    },
    {
        "tag": "RESES",
        "date": "10 September 2026",
        "title": "Penjaringan Aspirasi Masyarakat",
        "desc": "Anggota DPRK turun ke daerah pemilihan untuk menampung aspirasi masyarakat terkait infrastruktur pascabanjir.",
        "image": "https://images.unsplash.com/photo-1529107386315-e1a2ed48a620?auto=format&fit=crop&w=900&q=80",
    },
    {
        "tag": "LEGISLASI",
        "date": "02 September 2026",
        "title": "RDPU Penyempurnaan Qanun",
        "desc": "DPRK mendengarkan masukan akademisi dan tokoh masyarakat atas rancangan qanun ketertiban umum.",
        "image": "https://images.unsplash.com/photo-1589578527966-fdac0f44566c?auto=format&fit=crop&w=900&q=80",
    },
]

AGENDA = [
    ("18", "SEP", "Rapat Paripurna", "Pembahasan kebijakan dan agenda pembangunan daerah."),
    ("20", "SEP", "Rapat Komisi", "Evaluasi program dan pelaksanaan kegiatan pemerintahan daerah."),
    ("24", "SEP", "Rapat Dengar Pendapat", "Penyerapan aspirasi dan masukan masyarakat."),
]

PIMPINAN = [
    ("Ketua DPRK", "H. Muhammad Yusuf, S.H.", "Memimpin sidang paripurna dan koordinasi alat kelengkapan dewan."),
    ("Wakil Ketua I", "Drs. H. Ahmad Fauzi, M.M.", "Koordinasi bidang legislasi dan anggaran."),
    ("Wakil Ketua II", "Siti Rahmah, S.IP.", "Koordinasi bidang pengawasan dan hubungan masyarakat."),
]

JDIH_DATA = [
    ["1", "Qanun No. 5/2025", "Ketertiban Umum dan Ketenteraman Masyarakat", "Berlaku", "2.4 MB"],
    ["2", "Perbup No. 12/2026", "Penjabaran APBK Aceh Jaya 2026", "Berlaku", "5.1 MB"],
    ["3", "Qanun No. 2/2024", "Perlindungan Korban Bencana Alam", "Berlaku", "1.8 MB"],
    ["4", "Perwa No. 08/2026", "Tata Tertib DPRK Aceh Jaya", "Berlaku", "980 KB"],
]

# =========================================================
# CSS (LENGKAP & DISEMPURNAKAN)
# =========================================================
st.markdown(
    """
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Plus+Jakarta+Sans:wght@500;600;700;800&display=swap');

:root {
    --primary: #0c4a3e;
    --primary-hover: #09382f;
    --primary-light: #e9f5f1;
    --gold: #d5a52b;
    --gold-light: #fdf6e3;
    --text: #1e293b;
    --text-muted: #64748b;
    --bg: #f8fafc;
    --white: #ffffff;
    --border: #e2e8f0;
    --shadow-sm: 0 1px 3px rgba(0,0,0,0.05);
    --shadow-md: 0 4px 12px rgba(12, 74, 62, 0.08);
    --shadow-lg: 0 12px 32px rgba(12, 74, 62, 0.12);
}

* { box-sizing: border-box; font-family: 'Inter', sans-serif; }
html, body, [class*="css"] { font-family: 'Inter', sans-serif; }
#MainMenu, footer, header { visibility: hidden; height: 0; }
.stApp { background: var(--bg); color: var(--text); }
.block-container { max-width: 100%; padding: 0 !important; }
section[data-testid="stSidebar"] { display: none; }

/* --- TOP BAR --- */
.govbar {
    background: #062e26; color: rgba(255,255,255,0.85); min-height: 36px;
    padding: 0 6%; display: flex; align-items: center; justify-content: space-between; font-size: 11px; letter-spacing: 0.3px;
}
.govbar-left, .govbar-right { display: flex; gap: 16px; align-items: center; }
.govbar strong { color: #fff; font-weight: 600; }

/* --- BRAND & NAV (STICKY + BLUR) --- */
.brand-wrap { background: var(--white); border-bottom: 1px solid var(--border); padding: 16px 6%; }
.brand-inner { display: flex; align-items: center; justify-content: space-between; gap: 24px; }
.brand { display: flex; align-items: center; gap: 14px; }
.brand-logo {
    width: 54px; height: 54px; border-radius: 50%;
    background: linear-gradient(145deg, #0c4a3e, #09382f); color: #fff;
    display: flex; align-items: center; justify-content: center; font-size: 26px;
    box-shadow: var(--shadow-md);
}
.brand-title {
    color: var(--primary); font-family: 'Plus Jakarta Sans', sans-serif;
    font-size: 17px; line-height: 1.2; font-weight: 800; text-transform: uppercase;
}
.brand-subtitle { margin-top: 3px; color: var(--text-muted); font-size: 10px; letter-spacing: 0.8px; font-weight: 600; }

.nav-wrap {
    background: rgba(255, 255, 255, 0.95);
    backdrop-filter: blur(12px);
    border-bottom: 1px solid var(--border);
    padding: 0 6%;
    position: sticky;
    top: 0;
    z-index: 1000;
    box-shadow: var(--shadow-sm);
}
.nav-inner { min-height: 52px; display: flex; align-items: center; gap: 4px; }

.nav-button .stButton > button {
    background: transparent !important; border: none !important; color: var(--text-muted) !important;
    font-size: 13px !important; font-weight: 600 !important; border-radius: 6px !important;
    padding: 10px 14px !important; transition: all 0.2s ease !important;
}
.nav-button .stButton > button:hover { color: var(--primary) !important; background: var(--primary-light) !important; }
.nav-button-active .stButton > button {
    color: var(--primary) !important; background: var(--primary-light) !important; font-weight: 700 !important;
}

/* --- ALERT --- */
.alert {
    background: var(--gold-light); border-bottom: 1px solid #f0dfad; color: #854d0e;
    padding: 10px 6%; font-size: 12px; display: flex; align-items: center; gap: 8px; font-weight: 500;
}

/* --- HERO --- */
.hero {
    position: relative; min-height: 460px; display: flex; align-items: center; overflow: hidden;
    background: linear-gradient(90deg, rgba(6,46,38,0.92) 0%, rgba(12,74,62,0.8) 50%, rgba(12,74,62,0.4) 100%),
    url('https://images.unsplash.com/photo-1529107386315-e1a2ed48a620?auto=format&fit=crop&w=1800&q=85') center/cover no-repeat;
}
.hero-content { width: 88%; max-width: 1250px; margin: 0 auto; padding: 60px 0; color: white; position: relative; z-index: 2; }
.hero-kicker {
    display: inline-block; background: rgba(213, 165, 43, 0.2); color: #fde68a; border: 1px solid rgba(213, 165, 43, 0.4);
    padding: 4px 12px; border-radius: 20px; font-size: 11px; font-weight: 700; letter-spacing: 1.2px; margin-bottom: 16px;
}
.hero h1 {
    max-width: 700px; font-family: 'Plus Jakarta Sans', sans-serif;
    font-size: clamp(32px, 4.5vw, 52px); line-height: 1.1; margin: 0 0 20px; font-weight: 800;
}
.hero p { max-width: 600px; color: rgba(255,255,255,0.85); font-size: 16px; line-height: 1.7; margin-bottom: 28px; }
.hero-buttons { display: flex; flex-wrap: wrap; gap: 12px; }
.hero-btn {
    display: inline-flex; align-items: center; gap: 8px; padding: 12px 24px; border-radius: 8px; background: var(--gold);
    color: #fff !important; text-decoration: none; font-weight: 700; font-size: 13px; transition: all 0.2s;
}
.hero-btn:hover { background: #b88a1e; transform: translateY(-2px); }
.hero-btn.secondary { background: rgba(255,255,255,0.1); border: 1px solid rgba(255,255,255,0.3); backdrop-filter: blur(4px); }
.hero-btn.secondary:hover { background: rgba(255,255,255,0.2); }

/* --- CONTENT LAYOUT --- */
.content { width: 88%; max-width: 1250px; margin: 0 auto; }
.section { padding: 56px 0; }
.section-head { display: flex; justify-content: space-between; align-items: flex-end; gap: 20px; margin-bottom: 28px; }
.section-kicker {
    color: var(--primary); font-size: 11px; font-weight: 800;
    letter-spacing: 1.2px; text-transform: uppercase; margin-bottom: 6px;
}
.section-title { color: #0f172a; font-family: 'Plus Jakarta Sans', sans-serif; font-size: 26px; font-weight: 800; margin: 0; }
.section-desc { color: var(--text-muted); font-size: 14px; line-height: 1.6; margin-top: 8px; max-width: 600px; }

/* --- CARDS --- */
.service-box {
    background: var(--white); border: 1px solid var(--border); border-top: 3px solid transparent;
    min-height: 180px; padding: 28px 20px; text-align: center;
    transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1); border-radius: 12px;
}
.service-box:hover {
    transform: translateY(-6px); border-top-color: var(--primary); box-shadow: var(--shadow-lg);
}
.service-icon {
    width: 56px; height: 56px; margin: 0 auto 16px; border-radius: 14px;
    background: var(--primary-light); color: var(--primary);
    display: flex; align-items: center; justify-content: center; font-size: 26px;
}
.service-title { color: #0f172a; font-size: 15px; font-weight: 700; margin-bottom: 8px; }
.service-desc { color: var(--text-muted); font-size: 12px; line-height: 1.6; }

/* --- NEWS --- */
.news-main { background: var(--white); border: 1px solid var(--border); overflow: hidden; border-radius: 12px; height: 100%; transition: all 0.3s; }
.news-main:hover { box-shadow: var(--shadow-md); }
.news-main-img { width: 100%; height: 240px; object-fit: cover; display: block; }
.news-main-body { padding: 24px; }
.news-tag {
    display: inline-block; background: var(--primary-light); color: var(--primary);
    font-size: 10px; font-weight: 800; letter-spacing: 0.8px; padding: 4px 10px; border-radius: 4px; margin-bottom: 10px;
}
.news-main h3 { color: #0f172a; font-family: 'Plus Jakarta Sans', sans-serif; font-size: 20px; line-height: 1.35; margin: 0 0 10px; }
.news-date { color: var(--text-muted); font-size: 12px; display: flex; align-items: center; gap: 6px; }

.news-side {
    display: flex; gap: 16px; background: var(--white); border: 1px solid var(--border); border-radius: 10px;
    padding: 16px; margin-bottom: 16px; transition: all 0.2s;
}
.news-side:hover { border-color: var(--primary); box-shadow: var(--shadow-sm); }
.news-side-img { width: 120px; height: 90px; object-fit: cover; border-radius: 8px; flex-shrink: 0; }
.news-side h4 { color: #0f172a; font-size: 14px; line-height: 1.4; margin: 0 0 6px; font-weight: 700; }
.news-side p { color: var(--text-muted); font-size: 12px; line-height: 1.5; margin: 0; }

/* --- AGENDA --- */
.agenda-wrap { background: var(--white); border: 1px solid var(--border); border-radius: 12px; padding: 24px; }
.agenda-row { display: flex; gap: 16px; padding: 16px 0; border-bottom: 1px solid var(--border); }
.agenda-row:last-child { border-bottom: none; padding-bottom: 0; }
.agenda-row:first-child { padding-top: 0; }
.agenda-date {
    width: 56px; height: 60px; background: var(--primary); color: white;
    border-radius: 8px; text-align: center; padding-top: 8px; flex-shrink: 0;
    display: flex; flex-direction: column; justify-content: center;
}
.agenda-date strong { display: block; font-size: 22px; line-height: 1; font-family: 'Plus Jakarta Sans'; }
.agenda-date span { font-size: 10px; letter-spacing: 1px; font-weight: 600; opacity: 0.9; }
.agenda-title { color: #0f172a; font-weight: 700; font-size: 14px; margin-bottom: 4px; }
.agenda-desc { color: var(--text-muted); font-size: 12px; line-height: 1.5; }

/* --- INFO STRIP --- */
.info-strip { background: var(--primary); color: white; padding: 40px 6%; }
.info-inner { width: 88%; max-width: 1250px; margin: auto; display: flex; justify-content: space-around; flex-wrap: wrap; gap: 20px; }
.info-item { text-align: center; padding: 10px; }
.info-number { color: var(--gold); font-size: 32px; font-weight: 800; font-family: 'Plus Jakarta Sans'; }
.info-label { color: rgba(255,255,255,0.75); font-size: 12px; font-weight: 500; margin-top: 4px; }

/* --- PROFILE --- */
.profile-card { background: var(--white); border: 1px solid var(--border); border-radius: 12px; padding: 32px 20px; text-align: center; height: 100%; transition: all 0.3s; }
.profile-card:hover { transform: translateY(-4px); box-shadow: var(--shadow-md); }
.profile-photo {
    width: 88px; height: 88px; border-radius: 50%; margin: 0 auto 16px;
    display: flex; align-items: center; justify-content: center;
    background: linear-gradient(145deg, #0c4a3e, #09382f); color: #fff; font-size: 28px; font-weight: 800;
    border: 3px solid var(--white); box-shadow: var(--shadow-sm);
}
.profile-role { color: var(--primary); font-size: 10px; font-weight: 800; text-transform: uppercase; letter-spacing: 0.8px; margin-bottom: 8px; }
.profile-name { color: #0f172a; font-size: 18px; font-weight: 800; margin: 0 0 10px; font-family: 'Plus Jakarta Sans'; }
.profile-desc { color: var(--text-muted); font-size: 12px; line-height: 1.6; }

/* --- FOOTER --- */
.footer { background: #062e26; color: rgba(255,255,255,0.7); margin-top: 40px; padding: 56px 6% 24px; }
.footer-inner { width: 88%; max-width: 1250px; margin: auto; }
.footer-title { color: #fff; font-size: 14px; font-weight: 700; margin-bottom: 16px; font-family: 'Plus Jakarta Sans'; }
.footer p { color: rgba(255,255,255,0.6); font-size: 12px; line-height: 1.8; margin: 0; }
.footer a { color: rgba(255,255,255,0.7); text-decoration: none; transition: all 0.2s ease; display: inline-block; }
.footer a:hover { color: var(--gold) !important; padding-left: 4px; }
.footer-bottom {
    border-top: 1px solid rgba(255,255,255,0.1); margin-top: 40px; padding-top: 20px;
    text-align: center; color: rgba(255,255,255,0.4); font-size: 11px;
}

/* --- STREAMLIT FORM OVERRIDES --- */
div[data-testid="stForm"] { background: var(--white); border: 1px solid var(--border); border-radius: 12px; padding: 28px !important; box-shadow: var(--shadow-sm); }
.stTextInput > div > div > input, .stTextArea > div > div > textarea, div[data-baseweb="select"] > div {
    border-radius: 8px !important; border: 1px solid var(--border) !important; background: #f8fafc !important;
}
.stTextInput > div > div > input:focus, .stTextArea > div > div > textarea:focus {
    border-color: var(--primary) !important; box-shadow: 0 0 0 3px var(--primary-light) !important; background: #fff !important;
}
.stButton > button[kind="primary"], .stFormSubmitButton > button {
    background: var(--primary) !important; border: none !important; color: white !important;
    border-radius: 8px !important; font-weight: 700 !important; padding: 12px 24px !important;
    transition: all 0.2s !important;
}
.stButton > button[kind="primary"]:hover, .stFormSubmitButton > button:hover {
    background: var(--primary-hover) !important; transform: translateY(-1px) !important; box-shadow: var(--shadow-md) !important;
}

/* --- RESPONSIVE --- */
@media (max-width: 850px) {
    .govbar-left { display: none; }
    .govbar { justify-content: flex-end; }
    .brand-inner { flex-direction: column; align-items: flex-start; gap: 12px; }
    .brand-title { font-size: 15px; }
    .hero { min-height: 400px; }
    .content, .hero-content, .info-inner, .footer-inner { width: 92%; }
    .nav-wrap { padding: 0 4%; overflow-x: auto; }
    .nav-inner { min-height: 48px; }
    .section-head { flex-direction: column; align-items: flex-start; gap: 8px; }
    
    /* Footer Mobile Grid */
    .footer-grid-mobile {
        grid-template-columns: 1fr !important;
        gap: 32px !important;
    }
}
</style>
""",
    unsafe_allow_html=True,
)

# =========================================================
# SESSION STATE & NAVIGATION
# =========================================================
if "page" not in st.session_state:
    st.session_state.page = "Beranda"

st.markdown(
    """
<div class="govbar">
    <div class="govbar-left"><span>🇮🇩 Portal Informasi Pemerintahan Daerah</span><span>|</span><strong>DPRK ACEH JAYA</strong></div>
    <div class="govbar-right"><span>PPID</span><span>🇩 ID</span></div>
</div>
""",
    unsafe_allow_html=True,
)

st.markdown(
    """
<div class="brand-wrap">
    <div class="brand-inner">
        <div class="brand">
            <div class="brand-logo">🏛️</div>
            <div>
                <div class="brand-title">Dewan Perwakilan Rakyat<br>Kabupaten Aceh Jaya</div>
                <div class="brand-subtitle">PORTAL INFORMASI PUBLIK DAN ASPIRASI MASYARAKAT</div>
            </div>
        </div>
        <div style="text-align:right;color:var(--text-muted);font-size:11px;line-height:1.6;font-weight:500;">
            Kabupaten Aceh Jaya • Provinsi Aceh
        </div>
    </div>
</div>
""",
    unsafe_allow_html=True,
)

st.markdown('<div class="nav-wrap"><div class="nav-inner">', unsafe_allow_html=True)
nav_cols = st.columns([1.1, 1.1, 1.2, 1.3, 1.3, 1.1, 0.9])
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

st.markdown(
    """
<div class="alert">
    <span>📢</span>
    <span><strong>Informasi:</strong> Portal DPRK Aceh Jaya menyediakan akses informasi publik, produk hukum, agenda dewan, dan penyampaian aspirasi masyarakat.</span>
</div>
""",
    unsafe_allow_html=True,
)

# =========================================================
# HALAMAN: BERANDA
# =========================================================
if st.session_state.page == "Beranda":
    st.markdown(
        """
    <section class="hero">
        <div class="hero-content">
            <div class="hero-kicker">PORTAL RESMI DPRK ACEH JAYA</div>
            <h1>Suara Masyarakat,<br>Bagian dari Pembangunan Aceh Jaya</h1>
            <p>Akses informasi kegiatan DPRK, produk hukum, agenda persidangan, layanan publik, serta sampaikan aspirasi masyarakat melalui satu portal yang mudah diakses.</p>
            <div class="hero-buttons">
                <a class="hero-btn" href="#layanan">Sampaikan Aspirasi</a>
                <a class="hero-btn secondary" href="#berita">Lihat Berita</a>
            </div>
        </div>
    </section>
    """,
        unsafe_allow_html=True,
    )

    st.markdown('<div class="content" id="layanan">', unsafe_allow_html=True)
    st.markdown(
        """
    <section class="section">
        <div class="section-head">
            <div>
                <div class="section-kicker">Akses Cepat</div>
                <h2 class="section-title">Layanan Publik</h2>
                <div class="section-desc">Akses layanan dan informasi DPRK Aceh Jaya secara lebih mudah dan transparan.</div>
            </div>
        </div>
    """,
        unsafe_allow_html=True,
    )

    services = [
        ("📢", "Pengaduan Masyarakat", "Sampaikan aspirasi, keluhan, dan laporan masyarakat.", "Layanan"),
        ("📜", "JDIH", "Akses produk hukum dan dokumen peraturan daerah.", "JDIH"),
        ("📅", "Agenda DPRK", "Lihat agenda rapat, sidang, dan kegiatan DPRK.", "Berita"),
        ("📊", "Transparansi", "Informasi publik dan dokumen penyelenggaraan pemerintahan.", "JDIH"),
        ("📂", "Dokumen Publik", "Dokumen yang dapat diakses secara terbuka oleh masyarakat.", "JDIH"),
        ("ℹ️", "Informasi Kelembagaan", "Profil, struktur organisasi, dan tugas fungsi DPRK.", "Profil"),
    ]

    service_cols = st.columns(6)
    for i, (icon, title, desc, target) in enumerate(services):
        with service_cols[i]:
            st.markdown(
                f"""
            <div class="service-box">
                <div class="service-icon">{icon}</div>
                <div class="service-title">{title}</div>
                <div class="service-desc">{desc}</div>
            </div>
            """,
                unsafe_allow_html=True,
            )
            if st.button(f"Akses →", key=f"btn_{target}", use_container_width=True, type="secondary"):
                st.session_state.page = PAGES[target]
                st.rerun()

    st.markdown("</section></div>", unsafe_allow_html=True)

    st.markdown(
        """
    <div class="info-strip">
        <div class="info-inner">
    """,
        unsafe_allow_html=True,
    )

    stats = [("2024–2029", "Masa Jabatan"), ("3", "Pimpinan DPRK"), ("5", "Komisi / Alat Kelengkapan"), ("24/7", "Akses Informasi")]
    stat_cols = st.columns(4)
    for i, (number, label) in enumerate(stats):
        with stat_cols[i]:
            st.markdown(
                f"""
            <div class="info-item">
                <div class="info-number">{number}</div>
                <div class="info-label">{label}</div>
            </div>
            """,
                unsafe_allow_html=True,
            )

    st.markdown(
        """
        </div>
    </div>
    <div class="content" id="berita">
    """,
        unsafe_allow_html=True,
    )

    st.markdown(
        """
    <section class="section">
        <div class="section-head">
            <div>
                <div class="section-kicker">Informasi Terbaru</div>
                <h2 class="section-title">Berita & Agenda</h2>
                <div class="section-desc">Informasi kegiatan dan agenda terbaru DPRK Aceh Jaya.</div>
            </div>
        </div>
    """,
        unsafe_allow_html=True,
    )

    col_news, col_agenda = st.columns([1.8, 1])

    with col_news:
        main_news = NEWS[0]
        st.markdown(
            f"""
        <div class="news-main">
            <img class="news-main-img" src="{main_news['image']}">
            <div class="news-main-body">
                <div class="news-tag">{main_news['tag']}</div>
                <h3>{main_news['title']}</h3>
                <p style="color:var(--text-muted);font-size:13px;line-height:1.65;margin-bottom:12px;">{main_news['desc']}</p>
                <div class="news-date">🕒 {main_news['date']}</div>
            </div>
        </div>
        """,
            unsafe_allow_html=True,
        )

        for item in NEWS[1:]:
            st.markdown(
                f"""
            <div class="news-side">
                <img class="news-side-img" src="{item['image']}">
                <div>
                    <div class="news-tag">{item['tag']}</div>
                    <h4>{item['title']}</h4>
                    <p>{item['desc']}</p>
                    <div class="news-date" style="margin-top:8px;">🕒 {item['date']}</div>
                </div>
            </div>
            """,
                unsafe_allow_html=True,
            )

    with col_agenda:
        st.markdown('<div class="agenda-wrap">', unsafe_allow_html=True)
        st.markdown(
            """
            <div class="section-kicker">Jadwal</div>
            <div style="font-family:'Plus Jakarta Sans';font-size:19px;font-weight:800;color:#0f172a;margin-bottom:16px;">Agenda Terdekat</div>
            """,
            unsafe_allow_html=True,
        )

        for day, month, title, desc in AGENDA:
            st.markdown(
                f"""
            <div class="agenda-row">
                <div class="agenda-date">
                    <strong>{day}</strong>
                    <span>{month}</span>
                </div>
                <div>
                    <div class="agenda-title">{title}</div>
                    <div class="agenda-desc">{desc}</div>
                </div>
            </div>
            """,
                unsafe_allow_html=True,
            )
        st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("</section></div>", unsafe_allow_html=True)

# =========================================================
# HALAMAN: PROFIL
# =========================================================
elif st.session_state.page == "Profil & Pimpinan":
    st.markdown('<div class="content">', unsafe_allow_html=True)
    st.markdown(
        """
    <section class="section">
        <div class="section-kicker">Tentang DPRK</div>
        <h2 class="section-title">Profil DPRK Aceh Jaya</h2>
        <div class="section-desc">
            Dewan Perwakilan Rakyat Kabupaten Aceh Jaya sebagai unsur penyelenggara pemerintahan daerah bersama pemerintah daerah menjalankan fungsi legislasi, anggaran, dan pengawasan sesuai ketentuan peraturan perundang-undangan.
        </div>
    </section>
    """,
        unsafe_allow_html=True,
    )

    st.markdown(
        """
    <div style="background:var(--white);border:1px solid var(--border);border-radius:12px;padding:32px;margin-bottom:40px;">
        <div class="section-kicker">Pimpinan</div>
        <h2 class="section-title" style="font-size:22px;">Pimpinan DPRK Aceh Jaya</h2>
        <div class="section-desc">Masa Jabatan 2024–2029</div>
    </div>
    """,
        unsafe_allow_html=True,
    )

    cols = st.columns(3)
    for i, (role, name, desc) in enumerate(PIMPINAN):
        with cols[i]:
            initials = "".join([word[0] for word in name.split()[:2]])
            st.markdown(
                f"""
            <div class="profile-card">
                <div class="profile-photo">{initials}</div>
                <div class="profile-role">{role}</div>
                <div class="profile-name">{name}</div>
                <div class="profile-desc">{desc}</div>
            </div>
            """,
                unsafe_allow_html=True,
            )
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
        <h2 class="section-title">Berita & Agenda DPRK</h2>
        <div class="section-desc">Informasi kegiatan, rapat, agenda, dan aktivitas DPRK Aceh Jaya.</div>
    </section>
    """,
        unsafe_allow_html=True,
    )

    for item in NEWS:
        st.markdown(
            f"""
        <div style="background:var(--white);border:1px solid var(--border);border-radius:12px;padding:20px;margin-bottom:20px;display:flex;gap:24px;transition:all 0.2s;">
            <img src="{item['image']}" style="width:280px;height:170px;object-fit:cover;border-radius:8px;flex-shrink:0;">
            <div style="padding:4px 0;flex:1;">
                <div class="news-tag">{item['tag']}</div>
                <h3 style="color:#0f172a;font-family:'Plus Jakarta Sans';font-size:20px;margin:0 0 10px;font-weight:700;">{item['title']}</h3>
                <p style="color:var(--text-muted);font-size:13px;line-height:1.7;margin-bottom:12px;">{item['desc']}</p>
                <div class="news-date">🕒 {item['date']}</div>
            </div>
        </div>
        """,
            unsafe_allow_html=True,
        )

    st.markdown(
        """
    <div style="margin-top:56px;" class="section-kicker">Agenda</div>
    <h2 class="section-title" style="font-size:23px;margin-bottom:20px;">Agenda Terdekat</h2>
    """,
        unsafe_allow_html=True,
    )

    agenda_cols = st.columns(3)
    for i, (day, month, title, desc) in enumerate(AGENDA):
        with agenda_cols[i]:
            st.markdown(
                f"""
            <div class="agenda-wrap" style="height:100%;">
                <div class="agenda-date">
                    <strong>{day}</strong><span>{month}</span>
                </div>
                <div style="margin-top:16px;" class="agenda-title">{title}</div>
                <div class="agenda-desc">{desc}</div>
            </div>
            """,
                unsafe_allow_html=True,
            )
    st.markdown("</div>", unsafe_allow_html=True)

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
        <div class="section-desc">Sampaikan aspirasi, laporan, atau pengaduan kepada DPRK Aceh Jaya.</div>
    </section>
    """,
        unsafe_allow_html=True,
    )

    st.markdown(
        """
    <div style="background:#fffbeb;border-left:4px solid #f59e0b;padding:16px 20px;border-radius:8px;margin-bottom:32px;display:flex;gap:12px;align-items:flex-start;">
        <span style="font-size:20px;">🚨</span>
        <div>
            <strong style="color:#92400e;font-size:14px;">Layanan Tanggap Darurat Banjir</strong>
            <p style="color:#92400e;font-size:13px;margin:4px 0 0;line-height:1.5;">Prioritas pengaduan dampak bencana akan diproses dalam 1x24 jam. Silakan pilih kategori "Bencana / Banjir" pada formulir di bawah.</p>
        </div>
    </div>
    """,
        unsafe_allow_html=True,
    )

    col1, col2 = st.columns([1.8, 1])

    with col1:
        st.markdown(
            """
        <div class="section-kicker">Formulir</div>
        <h3 style="color:#0f172a;font-family:'Plus Jakarta Sans';font-size:20px;margin-bottom:16px;font-weight:700;">Sampaikan Aspirasi Anda</h3>
        """,
            unsafe_allow_html=True,
        )

        with st.form("form_aduan"):
            c1, c2 = st.columns(2)
            with c1:
                nama = st.text_input("Nama Lengkap *", placeholder="Sesuai KTP")
                nik = st.text_input("NIK (Opsional)", placeholder="16 digit untuk verifikasi")
            with c2:
                kategori = st.selectbox(
                    "Kategori Pengaduan *",
                    [
                        "🚨 Bencana / Banjir (Prioritas Tinggi)",
                        "🛣️ Infrastruktur & Jalan",
                        "🏥 Pelayanan Publik",
                        "📜 Legislasi & Qanun",
                        "💡 Lainnya",
                    ],
                )
            lokasi = st.text_input("Lokasi Kejadian (Opsional)", placeholder="Desa / Kecamatan / titik lokasi")
            isi = st.text_area("Isi Laporan / Aspirasi *", height=140, placeholder="Jelaskan aspirasi atau laporan secara jelas, lengkap, dan sertakan bukti jika ada...")

            submitted = st.form_submit_button("Kirim Aspirasi", type="primary", use_container_width=True)

            if submitted:
                if nama.strip() and isi.strip():
                    nomor = datetime.now().strftime("%Y%m%d%H%M%S")
                    st.success(f"✅ **Laporan berhasil dicatat!**\n\nNomor tiket Anda: **ADU-{nomor}**\n\nSimpan nomor ini untuk mengecek tindak lanjut. Kami akan memproses laporan Anda sesuai prioritas.")
                else:
                    st.error("⚠️ Mohon lengkapi **Nama Lengkap** dan **Isi Laporan**.")

    with col2:
        st.markdown(
            """
        <div class="agenda-wrap">
            <div class="section-kicker">Kontak</div>
            <h3 style="color:#0f172a;font-family:'Plus Jakarta Sans';font-size:19px;margin-top:0;font-weight:700;">Hubungi Kami</h3>
            
            <div style="margin-top:20px;">
                <p style="font-size:12px;color:#0f172a;font-weight:700;margin:0 0 4px;"> Telepon</p>
                <p style="font-size:13px;color:var(--text-muted);margin:0 0 16px;">(0655) 12345</p>
                
                <p style="font-size:12px;color:#0f172a;font-weight:700;margin:0 0 4px;">✉️ Email</p>
                <p style="font-size:13px;color:var(--text-muted);margin:0 0 16px;">sekretariat@dprk.acehjaya.go.id</p>
                
                <p style="font-size:12px;color:#0f172a;font-weight:700;margin:0 0 4px;">📍 Alamat</p>
                <p style="font-size:13px;color:var(--text-muted);margin:0 0 16px;">Jl. Merdeka No. 01, Calang, Aceh Jaya</p>
            </div>
            
            <hr style="border:none;border-top:1px solid var(--border);margin:20px 0;">
            <p style="font-size:11px;color:var(--text-muted);line-height:1.6;">
                <strong>Jam layanan:</strong><br>
                Senin–Jumat: 08.00–16.00 WIB<br>
                Sabtu–Minggu: Libur
            </p>
        </div>
        """,
            unsafe_allow_html=True,
        )
    st.markdown("</div>", unsafe_allow_html=True)

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
        <div class="section-desc">Akses daftar produk hukum dan informasi publik DPRK Aceh Jaya.</div>
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

    for i, (icon, title, desc) in enumerate(cards):
        with info_cols[i]:
            st.markdown(
                f"""
            <div class="service-box" style="text-align:left;min-height:150px;">
                <div class="service-icon" style="margin:0 0 14px;">{icon}</div>
                <div class="service-title">{title}</div>
                <div class="service-desc">{desc}</div>
            </div>
            """,
                unsafe_allow_html=True,
            )

    st.markdown(
        """
    <div style="margin-top:56px;">
        <div class="section-kicker">Database</div>
        <h2 class="section-title" style="font-size:23px;margin-bottom:20px;">Produk Hukum Daerah</h2>
    </div>
    """,
        unsafe_allow_html=True,
    )

    df = pd.DataFrame(JDIH_DATA, columns=["No", "Nomor & Tahun", "Tentang", "Status", "Ukuran"])
    
    st.dataframe(
        df,
        use_container_width=True,
        hide_index=True,
        column_config={
            "No": st.column_config.TextColumn("No", width="50px"),
            "Nomor & Tahun": st.column_config.TextColumn("Nomor & Tahun", width="150px"),
            "Tentang": st.column_config.TextColumn("Tentang / Judul Dokumen"),
            "Status": st.column_config.TextColumn("Status"),
            "Ukuran": st.column_config.TextColumn("Unduh", help="Klik untuk mengunduh dokumen"),
        },
    )
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
        <div class="section-desc">Gunakan informasi berikut untuk mendapatkan layanan dan informasi dari Sekretariat DPRK Aceh Jaya.</div>
    </section>
    """,
        unsafe_allow_html=True,
    )

    cols = st.columns(3)
    contacts = [
        ("📍", "Alamat Kantor", "Jl. Merdeka No. 01, Calang, Kabupaten Aceh Jaya, Aceh 23654"),
        ("📞", "Telepon & Faks", "Telp: (0655) 12345\nFaks: (0655) 12346"),
        ("✉️", "Email Resmi", "sekretariat@dprk.acehjaya.go.id\npengaduan@dprk.acehjaya.go.id"),
    ]

    for i, (icon, title, value) in enumerate(contacts):
        with cols[i]:
            st.markdown(
                f"""
            <div class="service-box" style="min-height:180px;text-align:left;">
                <div class="service-icon" style="margin:0 0 16px 0;">{icon}</div>
                <div class="service-title" style="text-align:left;">{title}</div>
                <div class="service-desc" style="font-size:13px;text-align:left;white-space: pre-line;">{value}</div>
            </div>
            """,
                unsafe_allow_html=True,
            )

    st.markdown(
        """
    <div style="margin-top:40px;background:var(--white);border:1px solid var(--border);border-radius:12px;padding:32px;">
        <div class="section-kicker">Sekretariat</div>
        <h3 style="font-family:'Plus Jakarta Sans';color:#0f172a;font-size:20px;font-weight:700;margin-bottom:12px;">Jam Pelayanan</h3>
        <p style="font-size:14px;color:var(--text-muted);line-height:1.8;">
            <strong>Senin – Kamis:</strong> 08.00 – 16.30 WIB<br>
            <strong>Jumat:</strong> 08.00 – 16.30 WIB<br>
            <strong>Sabtu – Minggu:</strong> Libur
        </p>
    </div>
    """,
        unsafe_allow_html=True,
    )
    st.markdown("</div>", unsafe_allow_html=True)

# =========================================================
# FOOTER (DISEMPURNAKAN)
# =========================================================
st.markdown(
    """
<div class="footer">
    <div class="footer-inner">
        <div class="brand" style="margin-bottom:32px; display:flex; align-items:center; gap:14px;">
            <div class="brand-logo" style="width:48px; height:48px; font-size:22px;">🏛️</div>
            <div>
                <div class="brand-title" style="color:#fff; font-size:16px; line-height:1.2;">DPRK ACEH JAYA</div>
                <div class="brand-subtitle" style="color:rgba(255,255,255,0.5); font-size:10px;">PORTAL INFORMASI PUBLIK</div>
            </div>
        </div>

        <div class="footer-grid-mobile" style="display:grid; grid-template-columns:2fr 1fr 1fr 1fr; gap:40px;">
            <div>
                <div class="footer-title">Tentang Portal</div>
                <p style="line-height:1.7;">
                    Portal resmi DPRK Aceh Jaya menyediakan akses transparan terhadap informasi 
                    kelembagaan, berita, agenda persidangan, produk hukum, serta layanan 
                    pengaduan dan aspirasi masyarakat.
                </p>
            </div>
            
            <div>
                <div class="footer-title">Navigasi</div>
                <p><a href="#">Beranda</a></p>
                <p><a href="#">Profil & Pimpinan</a></p>
                <p><a href="#">Berita & Agenda</a></p>
                <p><a href="#">JDIH & Transparansi</a></p>
            </div>
            
            <div>
                <div class="footer-title">Layanan Publik</div>
                <p><a href="#">Pengaduan Masyarakat</a></p>
                <p><a href="#">Permohonan Informasi (PPID)</a></p>
                <p><a href="#">Produk Hukum Daerah</a></p>
                <p><a href="#">Transparansi Anggaran</a></p>
            </div>
            
            <div>
                <div class="footer-title">Hubungi Kami</div>
                <p style="display:flex; gap:8px; align-items:flex-start; margin-bottom:12px;">
                    <span>📍</span> 
                    <span>Jl. Merdeka No. 01, Calang,<br>Kabupaten Aceh Jaya, Aceh 23654</span>
                </p>
                <p style="display:flex; gap:8px; align-items:center; margin-bottom:12px;">
                    <span>📞</span> 
                    <span>(0655) 12345</span>
                </p>
                <p style="display:flex; gap:8px; align-items:center;">
                    <span>✉️</span> 
                    <a href="mailto:sekretariat@dprk.acehjaya.go.id">sekretariat@dprk.acehjaya.go.id</a>
                </p>
            </div>
        </div>

        <div class="footer-bottom">
            <p>© 2026 Dewan Perwakilan Rakyat Kabupaten Aceh Jaya. Hak Cipta Dilindungi.</p>
            <p style="margin-top:4px; font-size:10px; opacity:0.6;">Dikembangkan untuk transparansi dan pelayanan publik yang lebih baik.</p>
        </div>
    </div>
</div>
""",
    unsafe_allow_html=True,
)

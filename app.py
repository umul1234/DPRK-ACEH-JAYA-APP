import streamlit as st
from datetime import datetime, time
import pandas as pd

# =========================================================
# KONFIGURASI HALAMAN
# =========================================================
st.set_page_config(
    page_title="DPRK Aceh Jaya | Portal Informasi Publik",
    page_icon="https://i.imgur.com/bTNXnLF.png",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# =========================================================
# SESSION STATE INIT
# =========================================================
if "page" not in st.session_state:
    st.session_state.page = "Beranda"
if "sub_page" not in st.session_state:
    st.session_state.sub_page = None
if "dark_mode" not in st.session_state:
    st.session_state.dark_mode = False
if "language" not in st.session_state:
    st.session_state.language = "ID"

# =========================================================
# DATA & KONFIGURASI
# =========================================================
LOGO_URL = "https://i.imgur.com/bTNXnLF.png"

# Navigasi Utama (Sesuai Struktur Baru)
MAIN_PAGES = [
    "Beranda", "Profil", "Dewan", "Informasi", 
    "Transparansi", "Aspirasi", "Layanan", "Kontak"
]

# Sub-menu untuk masing-masing halaman utama
SUB_MENUS = {
    "Profil": ["Profil DPRK", "Visi & Misi", "Tugas & Fungsi", "Struktur Organisasi", "Pimpinan", "Anggota DPRK", "Sekretariat"],
    "Dewan": ["Komisi I", "Komisi II", "Komisi III", "Komisi IV", "Badan Musyawarah", "Badan Legislasi", "Badan Anggaran", "Badan Kehormatan"],
    "Informasi": ["Warta DPRK", "Agenda", "Rapat & Sidang", "Risalah", "Reses", "Galeri"],
    "Transparansi": ["Dashboard APBK", "KUA-PPAS", "Qanun", "Rancangan Qanun", "Pusat Dokumen", "JDIH", "PPID"],
    "Aspirasi": ["Sampaikan Aspirasi", "Cek Status Aspirasi", "Peta Aspirasi", "Informasi Reses"],
    "Layanan": ["Pengaduan Masyarakat", "Permohonan Informasi (PPID)", "Survei Kepuasan", "FAQ"],
}

# Data Mock Komisi III (Sesuai Permintaan)
KOMISI_III_DATA = {
    "nama": "Komisi III",
    "ketua": "Sudirman, S.P",
    "fokus": ["Infrastruktur", "Pembangunan", "Pekerjaan Umum"],
    "anggota": ["Sudirman, S.P (Ketua)", "Abdul Muthalleb (Wakil Ketua)", "Drs. H. T. Irfan TB., M.Si (Sekretaris)", "Muhammad Diah, S.E (Anggota)"],
    "agenda_terbaru": [
        {"tipe": "RDP", "judul": "RDP dengan Dinas PUPR terkait Realisasi Jalan", "tanggal": "07 Sep 2026"},
        {"tipe": "Kunjungan Kerja", "judul": "Kunjungan Kerja ke Lokasi Jembatan Krueng Sabee", "tanggal": "12 Sep 2026"},
    ]
}

# Data Mock Pusat Dokumen
DOKUMEN_DATA = [
    {"Nama": "APBK Aceh Jaya", "Tahun": "2026", "Ukuran": "2.4 MB", "Kategori": "APBK"},
    {"Nama": "KUA-PPAS Perubahan", "Tahun": "2026", "Ukuran": "1.8 MB", "Kategori": "KUA-PPAS"},
    {"Nama": "Qanun No. 5/2025", "Tahun": "2025", "Ukuran": "0.8 MB", "Kategori": "Qanun"},
    {"Nama": "Risalah Rapat Paripurna IX", "Tahun": "2026", "Ukuran": "3.1 MB", "Kategori": "Risalah Rapat"},
    {"Nama": "Laporan Kinerja Tahunan", "Tahun": "2025", "Ukuran": "4.5 MB", "Kategori": "Laporan Kinerja"},
]

# =========================================================
# CSS STYLE (DARK MODE SUPPORT & ENHANCED UI)
# =========================================================
st.markdown(
    """
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Plus+Jakarta+Sans:wght@500;600;700;800&display=swap');

:root {
    --primary: #0c4a3e;
    --primary-2: #0f6b58;
    --primary-3: #e9f5f1;
    --gold: #d5a52b;
    --gold-soft: #f7efd4;
    --dark: #17322d;
    --text: #273936;
    --muted: #71817d;
    --bg: #f6f8f7;
    --white: #ffffff;
    --border: #e1e8e5;
    --shadow: 0 8px 28px rgba(12, 74, 62, .08);
}

[data-theme="dark"] {
    --primary: #1a6b5a;
    --primary-2: #228a73;
    --primary-3: #1e3a32;
    --gold: #e0b43a;
    --gold-soft: #3d3215;
    --dark: #e0e0e0;
    --text: #e8e8e8;
    --muted: #a0a0a0;
    --bg: #121212;
    --white: #1e1e1e;
    --border: #333333;
    --shadow: 0 8px 28px rgba(0, 0, 0, 0.3);
}

* { box-sizing: border-box; font-family: 'Inter', sans-serif; transition: background-color 0.3s, color 0.3s; }
html, body, [class*="css"] { font-family: 'Inter', sans-serif; }
#MainMenu, footer, header { visibility: hidden; height: 0; }
.stApp { background: var(--bg); color: var(--text); }
.block-container { max-width: 100%; padding: 0 !important; }
section[data-testid="stSidebar"] { display: none; }

/* Top Bar */
.govbar { 
    background: var(--primary); color: rgba(255,255,255,.9); min-height: 42px; 
    padding: 0 6%; display: flex; align-items: center; justify-content: space-between; font-size: 12px; 
}
.govbar-left, .govbar-right { display: flex; gap: 20px; align-items: center; }
.govbar strong { color: #fff; font-weight: 700; }
.govbar-right a, .govbar-right button { 
    color: rgba(255,255,255,.9); text-decoration: none; background: none; border: none; 
    cursor: pointer; font-size: 12px; font-weight: 600; padding: 4px 8px; border-radius: 4px;
}
.govbar-right a:hover, .govbar-right button:hover { background: rgba(255,255,255,0.15); color: #fff; }

/* Brand */
.brand-wrap { background: var(--white); border-bottom: 1px solid var(--border); padding: 16px 6%; }
.brand-inner { display: flex; align-items: center; justify-content: space-between; gap: 24px; }
.brand { display: flex; align-items: center; gap: 16px; }
.brand-logo { 
    width: 64px; height: 64px; border-radius: 8px; background: var(--white); 
    display: flex; align-items: center; justify-content: center; box-shadow: 0 4px 12px rgba(0,0,0,.08); overflow: hidden; border: 1px solid var(--border);
}
.brand-logo img { width: 100%; height: 100%; object-fit: contain; }
.brand-title { color: var(--dark); font-family: 'Plus Jakarta Sans', sans-serif; font-size: 19px; line-height: 1.2; font-weight: 800; text-transform: uppercase; }
.brand-subtitle { margin-top: 4px; color: var(--muted); font-size: 11px; letter-spacing: .8px; font-weight: 600; }

/* Navigation */
.nav-wrap { background: var(--white); border-bottom: 1px solid var(--border); padding: 0 6%; position: sticky; top: 0; z-index: 100; box-shadow: 0 2px 10px rgba(0,0,0,0.03); }
.nav-inner { min-height: 50px; display: flex; align-items: center; gap: 4px; overflow-x: auto; }
.nav-button .stButton > button, .nav-button-active .stButton > button {
    background: transparent !important; border: none !important; color: var(--muted) !important;
    font-size: 13px !important; font-weight: 600 !important; border-radius: 6px !important;
    padding: 12px 16px !important; min-height: 40px !important; transition: all .2s ease !important; white-space: nowrap !important;
}
.nav-button .stButton > button:hover { color: var(--primary) !important; background: var(--primary-3) !important; }
.nav-button-active .stButton > button { color: var(--primary) !important; font-weight: 700 !important; background: var(--primary-3) !important; }

/* Sub Navigation Tabs */
.stTabs [data-baseweb="tab-list"] { gap: 8px; background: transparent; border-bottom: 2px solid var(--border); }
.stTabs [data-baseweb="tab"] { 
    background: transparent; border-radius: 8px 8px 0 0; padding: 10px 20px; color: var(--muted); 
    font-weight: 600; font-family: 'Plus Jakarta Sans', sans-serif; transition: all 0.2s ease; font-size: 13px;
}
.stTabs [aria-selected="true"] { background: var(--primary-3) !important; color: var(--primary) !important; border-bottom: 2px solid var(--primary); }

/* Hero */
.hero { 
    position: relative; min-height: 420px; display: flex; align-items: center; overflow: hidden; 
    background: linear-gradient(135deg, rgba(8, 59, 50, 0.95) 0%, rgba(12, 74, 62, 0.85) 100%), 
    url('https://images.unsplash.com/photo-1529107386315-e1a2ed48a620?auto=format&fit=crop&w=1800&q=85') center/cover no-repeat; 
}
.hero-content { width: 88%; max-width: 1250px; margin: 0 auto; padding: 60px 0; color: white; position: relative; z-index: 2; }
.hero-kicker { 
    display: inline-block; color: var(--gold); font-size: 11px; font-weight: 800; 
    letter-spacing: 2px; margin-bottom: 16px; background: rgba(213, 165, 43, 0.15); 
    padding: 6px 12px; border-radius: 4px; border: 1px solid rgba(213, 165, 43, 0.3);
}
.hero h1 { max-width: 700px; font-family: 'Plus Jakarta Sans', sans-serif; font-size: clamp(32px, 4vw, 52px); line-height: 1.1; margin: 0 0 20px; font-weight: 800; }
.hero p { max-width: 600px; color: rgba(255,255,255,.85); font-size: 16px; line-height: 1.7; margin-bottom: 28px; }

/* Search Bar */
.search-container { background: var(--white); padding: 24px; border-radius: 12px; box-shadow: var(--shadow); margin-top: -40px; position: relative; z-index: 10; width: 88%; max-width: 1250px; margin-left: auto; margin-right: auto; border: 1px solid var(--border); }

/* Cards & Boxes */
.service-box, .profile-card, .doc-card { 
    background: var(--white); border: 1px solid var(--border); border-radius: 10px; padding: 24px; 
    transition: all .3s ease; height: 100%;
}
.service-box:hover, .profile-card:hover { transform: translateY(-4px); box-shadow: var(--shadow); border-color: var(--primary-2); }
.service-icon { 
    width: 50px; height: 50px; margin-bottom: 16px; border-radius: 10px; background: var(--primary-3); 
    color: var(--primary); display: flex; align-items: center; justify-content: center; font-size: 24px; 
}

/* Timeline Aspirasi */
.timeline { display: flex; flex-direction: column; gap: 0; position: relative; padding-left: 20px; }
.timeline::before { content: ''; position: absolute; left: 7px; top: 10px; bottom: 10px; width: 2px; background: var(--border); }
.timeline-item { position: relative; padding-bottom: 24px; padding-left: 24px; }
.timeline-dot { 
    position: absolute; left: -17px; top: 4px; width: 16px; height: 16px; border-radius: 50%; 
    border: 3px solid var(--white); box-shadow: 0 0 0 1px var(--border);
}
.timeline-dot.active { background: var(--gold); box-shadow: 0 0 0 1px var(--gold); }
.timeline-dot.done { background: var(--primary); box-shadow: 0 0 0 1px var(--primary); }
.timeline-title { font-weight: 700; font-size: 14px; color: var(--dark); margin-bottom: 4px; }
.timeline-desc { font-size: 12px; color: var(--muted); }

/* Status Badge */
.status-badge { 
    display: inline-flex; align-items: center; gap: 6px; padding: 6px 12px; border-radius: 20px; 
    font-size: 12px; font-weight: 700; 
}
.status-open { background: #e6f4ea; color: #1e7e34; }
.status-closed { background: #fce8e6; color: #c5221f; }
[data-theme="dark"] .status-open { background: #1e3a28; color: #4caf50; }
[data-theme="dark"] .status-closed { background: #3a1e1e; color: #f44336; }

/* Footer */
.footer { background: var(--primary); color: rgba(255,255,255,.7); margin-top: 80px; padding: 60px 6% 0; border-top: 4px solid var(--gold); }
.footer-container { width: 88%; max-width: 1250px; margin: 0 auto; }
.footer-grid { display: grid; grid-template-columns: 1.5fr 1fr 1fr 1fr; gap: 40px; padding-bottom: 40px; }
.footer-column h4 { color: #fff; font-size: 14px; font-weight: 800; margin: 0 0 20px; }
.footer-column a { display: block; color: rgba(255,255,255,.6); font-size: 13px; line-height: 2.2; text-decoration: none; transition: all .2s; }
.footer-column a:hover { color: var(--gold); padding-left: 4px; }
.footer-bottom { border-top: 1px solid rgba(255,255,255,.1); padding: 24px 0; display: flex; justify-content: space-between; font-size: 12px; color: rgba(255,255,255,.4); }

@media (max-width: 850px) {
    .footer-grid { grid-template-columns: 1fr 1fr; }
    .brand-inner { flex-direction: column; text-align: center; }
    .hero h1 { font-size: 28px; }
}
</style>
""",
    unsafe_allow_html=True,
)

# =========================================================
# HELPER FUNCTIONS
# =========================================================
def check_service_status():
    now = datetime.now()
    is_weekday = now.weekday() < 5
    is_working_hours = time(8, 0) <= now.time() <= time(16, 0)
    return is_weekday and is_working_hours

def render_sub_nav(page_name):
    if page_name in SUB_MENUS:
        st.markdown(f'<div style="padding: 20px 6% 0; background: var(--bg);">', unsafe_allow_html=True)
        tabs = st.tabs(SUB_MENUS[page_name])
        st.session_state.sub_page_tabs = tabs
        st.markdown('</div>', unsafe_allow_html=True)
        return tabs
    return None

# =========================================================
# TOP BAR & BRAND
# =========================================================
st.markdown(
    f"""
<div class="govbar">
    <div class="govbar-left">
        <span>🇮🇩 Portal Resmi Pemerintahan Daerah</span>
        <span style="opacity:0.5">|</span>
        <strong>KABUPATEN ACEH JAYA</strong>
    </div>
    <div class="govbar-right">
        <button onclick="alert('Fitur Bahasa akan segera hadir!')">🌐 {'Bahasa Aceh' if st.session_state.language == 'ID' else 'Indonesia'}</button>
        <button onclick="document.documentElement.setAttribute('data-theme', document.documentElement.getAttribute('data-theme') === 'dark' ? 'light' : 'dark')">
            {'🌙 Dark' if not st.session_state.dark_mode else '☀️ Light'}
        </button>
        <a href="?page=kontak">Hubungi Kami</a>
    </div>
</div>
""",
    unsafe_allow_html=True,
)

# Script sederhana untuk toggle dark mode di Streamlit (menggunakan session state rerun)
# Catatan: Karena keterbatasan JS di Streamlit murni, kita gunakan tombol Streamlit yang rapi di sidebar atau atas, 
# tapi untuk demo ini, kita simulasikan dengan tombol hidden atau biarkan user menggunakan tema browser, 
# ATAU kita gunakan st.toggle di bagian atas yang di-style.
# Mari kita gunakan st.columns di bawah brand untuk kontrol yang lebih stabil di Streamlit.

st.markdown(
    f"""
<div class="brand-wrap">
    <div class="brand-inner">
        <div class="brand">
            <div class="brand-logo">
                <img src="{LOGO_URL}" alt="Logo DPRK Aceh Jaya" 
                     onerror="this.src='data:image/svg+xml,<svg xmlns=%22http://www.w3.org/2000/svg%22 viewBox=%220 0 100 100%22><text y=%22.9em%22 font-size=%2290%22>🏛️</text></svg>'">
            </div>
            <div>
                <div class="brand-title">Dewan Perwakilan Rakyat<br>Kabupaten Aceh Jaya</div>
                <div class="brand-subtitle">PORTAL INFORMASI PUBLIK DAN ASPIRASI MASYARAKAT</div>
            </div>
        </div>
        <div style="text-align: right;">
            <div class="status-badge {'status-open' if check_service_status() else 'status-closed'}">
                {'🟢 Layanan Buka' if check_service_status() else '🔴 Layanan Tutup'}
            </div>
            <div style="font-size: 11px; color: var(--muted); margin-top: 6px;">
                Senin - Jumat, 08.00 - 16.00 WIB
            </div>
        </div>
    </div>
</div>
""",
    unsafe_allow_html=True,
)

# Kontrol Dark Mode & Bahasa yang fungsional di Streamlit
ctrl_col1, ctrl_col2 = st.columns([5, 1])
with ctrl_col2:
    st.session_state.dark_mode = st.toggle("🌙 Mode Gelap", value=st.session_state.dark_mode, key="dm_toggle")
    # Streamlit akan merender ulang, kita bisa inject JS untuk set attribute
    if st.session_state.dark_mode:
        st.markdown("<script>document.documentElement.setAttribute('data-theme', 'dark');</script>", unsafe_allow_html=True)
    else:
        st.markdown("<script>document.documentElement.setAttribute('data-theme', 'light');</script>", unsafe_allow_html=True)

# =========================================================
# NAVIGATION
# =========================================================
st.markdown('<div class="nav-wrap"><div class="nav-inner">', unsafe_allow_html=True)
nav_cols = st.columns(len(MAIN_PAGES))
for i, page in enumerate(MAIN_PAGES):
    with nav_cols[i]:
        active_class = "nav-button-active" if st.session_state.page == page else "nav-button"
        st.markdown(f'<div class="{active_class}">', unsafe_allow_html=True)
        if st.button(page, key=f"nav_{page}", use_container_width=True):
            st.session_state.page = page
            st.session_state.sub_page = None
            st.rerun()
        st.markdown("</div>", unsafe_allow_html=True)
st.markdown("</div></div>", unsafe_allow_html=True)

# =========================================================
# PAGE ROUTING
# =========================================================

# ---------------------------------------------------------
# 1. BERANDA
# ---------------------------------------------------------
if st.session_state.page == "Beranda":
    st.markdown(
        """
    <section class="hero">
        <div class="hero-content">
            <div class="hero-kicker">PORTAL RESMI DPRK ACEH JAYA</div>
            <h1>Suara Masyarakat, Bagian dari Pembangunan Aceh Jaya</h1>
            <p>Akses informasi kegiatan dewan, produk hukum, agenda persidangan, serta sampaikan aspirasi Anda melalui satu portal terpadu.</p>
        </div>
    </section>
    """,
        unsafe_allow_html=True,
    )

    # Pencarian Terintegrasi
    st.markdown('<div class="search-container">', unsafe_allow_html=True)
    search_cols = st.columns([4, 1, 1])
    with search_cols[0]:
        st.text_input("🔎 Cari berita, qanun, agenda, atau nama anggota...", label_visibility="collapsed", placeholder="Ketik kata kunci...")
    with search_cols[1]:
        st.selectbox("Kategori", ["Semua", "Berita", "Dokumen", "Anggota"], label_visibility="collapsed")
    with search_cols[2]:
        st.button("Cari", type="primary", use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="content" style="width:88%; max-width:1250px; margin: 40px auto;">', unsafe_allow_html=True)
    
    # Dashboard Kinerja Mini & Live Streaming
    dash_cols = st.columns([2, 1])
    with dash_cols[0]:
        st.markdown("### 📈 Dashboard Kinerja DPRK (Tahun 2026)")
        stat_cols = st.columns(4)
        stats = [("124", "Rapat Kerja"), ("18", "Qanun Disahkan"), ("45", "Kunjungan Kerja"), ("12", "Reses")]
        for i, (val, label) in enumerate(stats):
            with stat_cols[i]:
                st.markdown(f"""
                <div class="service-box" style="text-align:center; padding: 16px;">
                    <div style="font-size: 28px; font-weight: 800; color: var(--primary);">{val}</div>
                    <div style="font-size: 12px; color: var(--muted);">{label}</div>
                </div>
                """, unsafe_allow_html=True)
    
    with dash_cols[1]:
        st.markdown("### 🎥 Live Streaming Sidang")
        st.markdown("""
        <div class="service-box" style="padding: 0; overflow: hidden; position: relative;">
            <div style="background: #000; height: 180px; display: flex; align-items: center; justify-content: center; color: white; flex-direction: column;">
                <div style="font-size: 40px; margin-bottom: 10px;">▶️</div>
                <div style="font-size: 14px; font-weight: 600;">Tidak Ada Siaran Langsung</div>
                <div style="font-size: 11px; opacity: 0.7;">Jadwal berikutnya: Rapat Paripurna, 25 Sep 2026</div>
            </div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True)

# ---------------------------------------------------------
# 2. DEWAN (Dengan Fokus Khusus Komisi III)
# ---------------------------------------------------------
elif st.session_state.page == "Dewan":
    tabs = render_sub_nav("Dewan")
    if tabs:
        # Mock: Jika tab Komisi III dipilih (index 2)
        with tabs[2]: 
            st.markdown(f"""
            <div style="width:88%; max-width:1250px; margin: 30px auto;">
                <div style="display: flex; gap: 30px; flex-wrap: wrap;">
                    <!-- Sidebar Info Komisi -->
                    <div style="flex: 1; min-width: 300px;">
                        <div class="profile-card" style="text-align: left;">
                            <div style="font-size: 12px; font-weight: 800; color: var(--gold); text-transform: uppercase; letter-spacing: 1px; margin-bottom: 8px;">Alat Kelengkapan Dewan</div>
                            <h2 style="font-family: 'Plus Jakarta Sans'; color: var(--dark); margin: 0 0 20px 0;">{KOMISI_III_DATA['nama']}</h2>
                            
                            <div style="margin-bottom: 20px;">
                                <div style="font-size: 12px; color: var(--muted); margin-bottom: 4px;">Ketua Komisi</div>
                                <div style="font-size: 18px; font-weight: 700; color: var(--primary);">{KOMISI_III_DATA['ketua']}</div>
                            </div>

                            <div style="margin-bottom: 20px;">
                                <div style="font-size: 12px; color: var(--muted); margin-bottom: 8px;">Fokus Pembahasan:</div>
                                <div style="display: flex; flex-wrap: wrap; gap: 8px;">
                                    {"".join([f'<span style="background: var(--primary-3); color: var(--primary); padding: 4px 10px; border-radius: 4px; font-size: 12px; font-weight: 600;">{f}</span>' for f in KOMISI_III_DATA['fokus']])}
                                </div>
                            </div>

                            <div>
                                <div style="font-size: 12px; color: var(--muted); margin-bottom: 8px;">Daftar Anggota:</div>
                                <ul style="padding-left: 20px; margin: 0; color: var(--text); font-size: 13px; line-height: 1.8;">
                                    {"".join([f"<li>{a}</li>" for a in KOMISI_III_DATA['anggota']])}
                                </ul>
                            </div>
                        </div>
                    </div>

                    <!-- Agenda & Dokumen Komisi -->
                    <div style="flex: 2; min-width: 300px;">
                        <h3 style="font-family: 'Plus Jakarta Sans'; color: var(--dark); margin-top: 0;">Agenda & Aktivitas Komisi</h3>
                        <div class="service-box" style="padding: 0; overflow: hidden;">
                            <table style="width: 100%; border-collapse: collapse; font-size: 14px;">
                                <thead style="background: var(--primary-3); color: var(--primary);">
                                    <tr>
                                        <th style="padding: 12px 16px; text-align: left; font-weight: 700;">Tipe</th>
                                        <th style="padding: 12px 16px; text-align: left; font-weight: 700;">Kegiatan</th>
                                        <th style="padding: 12px 16px; text-align: left; font-weight: 700;">Tanggal</th>
                                        <th style="padding: 12px 16px; text-align: left; font-weight: 700;">Aksi</th>
                                    </tr>
                                </thead>
                                <tbody>
                                    {"".join([f"""
                                    <tr style="border-bottom: 1px solid var(--border);">
                                        <td style="padding: 16px;"><span style="background: var(--gold-soft); color: #a97e1c; padding: 4px 8px; border-radius: 4px; font-size: 11px; font-weight: 700;">{a['tipe']}</span></td>
                                        <td style="padding: 16px; font-weight: 600; color: var(--dark);">{a['judul']}</td>
                                        <td style="padding: 16px; color: var(--muted);">{a['tanggal']}</td>
                                        <td style="padding: 16px;"><a href="#" style="color: var(--primary); font-weight: 600; text-decoration: none;">Detail →</a></td>
                                    </tr>
                                    """ for a in KOMISI_III_DATA['agenda_terbaru']])}
                                </tbody>
                            </table>
                        </div>
                        
                        <div style="display: flex; gap: 12px; margin-top: 20px;">
                            <button style="flex:1; padding: 12px; background: var(--white); border: 1px solid var(--border); border-radius: 8px; font-weight: 600; color: var(--text); cursor: pointer;">📁 Lihat Semua Dokumen</button>
                            <button style="flex:1; padding: 12px; background: var(--white); border: 1px solid var(--border); border-radius: 8px; font-weight: 600; color: var(--text); cursor: pointer;">📰 Berita Komisi</button>
                        </div>
                    </div>
                </div>
            </div>
            """, unsafe_allow_html=True)
        else:
            st.info(f"Halaman {tabs[tabs.index(st.session_state.get('active_tab', tabs[0]))]} sedang dalam pengembangan. Silakan pilih **Komisi III** untuk melihat demo tampilan detail.")

# ---------------------------------------------------------
# 3. TRANSPARANSI (Pusat Dokumen)
# ---------------------------------------------------------
elif st.session_state.page == "Transparansi":
    tabs = render_sub_nav("Transparansi")
    if tabs:
        with tabs[4]: # Pusat Dokumen
            st.markdown('<div style="width:88%; max-width:1250px; margin: 30px auto;">', unsafe_allow_html=True)
            st.markdown("### 📑 Pusat Dokumen DPRK")
            
            doc_ctrl = st.columns([3, 1])
            with doc_ctrl[0]:
                st.text_input("🔎 Cari dokumen...", placeholder="Contoh: APBK 2026", label_visibility="collapsed")
            with doc_ctrl[1]:
                st.selectbox("Kategori", ["Semua", "APBK", "KUA-PPAS", "Qanun", "Rancangan Qanun", "Risalah Rapat", "Reses", "Laporan Kinerja"], label_visibility="collapsed")

            st.markdown("<br>", unsafe_allow_html=True)
            
            # Custom Table untuk Dokumen
            st.markdown("""
            <div class="service-box" style="padding: 0; overflow-x: auto;">
                <table style="width: 100%; border-collapse: collapse; font-size: 14px; text-align: left;">
                    <thead style="background: var(--primary-3); color: var(--primary);">
                        <tr>
                            <th style="padding: 16px; font-weight: 700;">Nama Dokumen</th>
                            <th style="padding: 16px; font-weight: 700;">Kategori</th>
                            <th style="padding: 16px; font-weight: 700;">Tahun</th>
                            <th style="padding: 16px; font-weight: 700;">Ukuran</th>
                            <th style="padding: 16px; font-weight: 700; text-align: center;">Aksi</th>
                        </tr>
                    </thead>
                    <tbody>
            """, unsafe_allow_html=True)
            
            for doc in DOKUMEN_DATA:
                st.markdown(f"""
                    <tr style="border-bottom: 1px solid var(--border); transition: background .2s;">
                        <td style="padding: 16px; font-weight: 600; color: var(--dark);">📄 {doc['Nama']}</td>
                        <td style="padding: 16px;"><span style="background: var(--gold-soft); color: #a97e1c; padding: 4px 8px; border-radius: 4px; font-size: 11px; font-weight: 700;">{doc['Kategori']}</span></td>
                        <td style="padding: 16px; color: var(--muted);">{doc['Tahun']}</td>
                        <td style="padding: 16px; color: var(--muted);">{doc['Ukuran']}</td>
                        <td style="padding: 16px; text-align: center;">
                            <button style="background: var(--primary); color: white; border: none; padding: 6px 12px; border-radius: 6px; font-size: 12px; font-weight: 600; cursor: pointer; display: inline-flex; align-items: center; gap: 4px;">
                                ↓ Download
                            </button>
                        </td>
                    </tr>
                """, unsafe_allow_html=True)
            
            st.markdown("</tbody></table></div>", unsafe_allow_html=True)
            st.markdown('</div>', unsafe_allow_html=True)

# ---------------------------------------------------------
# 4. ASPIRASI (Cek Status & Tracker)
# ---------------------------------------------------------
elif st.session_state.page == "Aspirasi":
    tabs = render_sub_nav("Aspirasi")
    if tabs:
        with tabs[1]: # Cek Status Aspirasi
            st.markdown('<div style="width:88%; max-width:800px; margin: 30px auto;">', unsafe_allow_html=True)
            st.markdown("### 🗳️ Cek Status Aspirasi Masyarakat")
            
            st.markdown("""
            <div style="background: var(--white); border: 1px solid var(--border); border-radius: 12px; padding: 24px; margin-bottom: 30px;">
                <div style="display: flex; gap: 12px;">
                    <input type="text" value="ADU-20260921-001" style="flex: 1; padding: 12px; border: 1px solid var(--border); border-radius: 8px; font-size: 14px; background: var(--bg); color: var(--text);" readonly>
                    <button style="padding: 12px 24px; background: var(--primary); color: white; border: none; border-radius: 8px; font-weight: 700; cursor: pointer;">Cek Status</button>
                </div>
            </div>
            """, unsafe_allow_html=True)

            st.markdown("#### 📍 Status Tindak Lanjut: ADU-20260921-001")
            st.markdown("Pengaduan terkait: *Perbaikan Jalan Lintas Kecamatan Jaya*")
            st.markdown("<br>", unsafe_allow_html=True)

            # Timeline Visual
            st.markdown("""
            <div class="timeline">
                <div class="timeline-item">
                    <div class="timeline-dot done"></div>
                    <div class="timeline-title">🟡 Diterima</div>
                    <div class="timeline-desc">21 September 2026, 09:15 WIB - Sistem mencatat pengaduan Anda.</div>
                </div>
                <div class="timeline-item">
                    <div class="timeline-dot done"></div>
                    <div class="timeline-title">🔵 Diverifikasi</div>
                    <div class="timeline-desc">21 September 2026, 14:30 WIB - Admin Sekretariat memverifikasi kelengkapan data.</div>
                </div>
                <div class="timeline-item">
                    <div class="timeline-dot done"></div>
                    <div class="timeline-title">🟠 Diteruskan ke Komisi</div>
                    <div class="timeline-desc">22 September 2026, 10:00 WIB - Diteruskan ke Komisi III (Bidang Infrastruktur) untuk ditindaklanjuti.</div>
                </div>
                <div class="timeline-item">
                    <div class="timeline-dot active"></div>
                    <div class="timeline-title">🟢 Ditindaklanjuti</div>
                    <div class="timeline-desc">Sedang dalam proses. Komisi III akan melakukan RDP dengan Dinas PUPR pada minggu depan.</div>
                </div>
            </div>
            """, unsafe_allow_html=True)
            st.markdown('</div>', unsafe_allow_html=True)

# ---------------------------------------------------------
# 5. LAYANAN (Survei & FAQ)
# ---------------------------------------------------------
elif st.session_state.page == "Layanan":
    tabs = render_sub_nav("Layanan")
    if tabs:
        with tabs[2]: # Survei Kepuasan
            st.markdown('<div style="width:88%; max-width:800px; margin: 30px auto;">', unsafe_allow_html=True)
            st.markdown("### ⭐ Survei Kepuasan Masyarakat")
            st.markdown("Bagaimana penilaian Anda terhadap pelayanan informasi publik DPRK Aceh Jaya?")
            
            with st.form("survei_form"):
                st.selectbox("Aspek Pelayanan", ["Kemudahan Akses Informasi", "Keramahan Petugas", "Kecepatan Respon Pengaduan", "Kualitas Website"])
                st.slider("Tingkat Kepuasan (1-5)", 1, 5, 4)
                st.text_area("Saran & Masukan", placeholder="Tuliskan saran Anda di sini...")
                st.form_submit_button("Kirim Survei", type="primary", use_container_width=True)
            
            st.markdown("</div>", unsafe_allow_html=True)

# ---------------------------------------------------------
# DEFAULT / KONTAK
# ---------------------------------------------------------
else:
    st.markdown('<div style="width:88%; max-width:1250px; margin: 40px auto;">', unsafe_allow_html=True)
    st.markdown(f"### Halaman {st.session_state.page}")
    st.info("Konten untuk halaman ini sedang dalam tahap pengisian data. Silakan jelajahi menu **Beranda**, **Dewan (Komisi III)**, **Transparansi (Pusat Dokumen)**, atau **Aspirasi (Cek Status)** untuk melihat fitur unggulan yang telah diimplementasikan.")
    st.markdown('</div>', unsafe_allow_html=True)

# =========================================================
# FOOTER
# =========================================================
st.markdown(
    f"""
<div class="footer">
<div class="footer-container">
<div class="footer-grid">
    <div class="footer-column">
        <div style="display: flex; align-items: center; gap: 12px; margin-bottom: 16px;">
            <img src="{LOGO_URL}" style="width: 40px; height: 40px; border-radius: 6px; background: white; padding: 4px;">
            <div>
                <div style="color: #fff; font-weight: 800; font-size: 16px;">DPRK ACEH JAYA</div>
                <div style="color: rgba(255,255,255,0.5); font-size: 10px; letter-spacing: 1px;">KABUPATEN ACEH JAYA</div>
            </div>
        </div>
        <p style="font-size: 13px; line-height: 1.8; color: rgba(255,255,255,0.6);">
            Portal resmi Dewan Perwakilan Rakyat Kabupaten Aceh Jaya yang menyediakan informasi kelembagaan, transparansi anggaran, dan saluran aspirasi masyarakat.
        </p>
    </div>
    <div class="footer-column">
        <h4>Navigasi</h4>
        <a href="#">Beranda</a>
        <a href="#">Profil DPRK</a>
        <a href="#">Alat Kelengkapan Dewan</a>
        <a href="#">Berita & Agenda</a>
    </div>
    <div class="footer-column">
        <h4>Layanan Publik</h4>
        <a href="#">Sampaikan Aspirasi</a>
        <a href="#">Cek Status Pengaduan</a>
        <a href="#">JDIH & Pusat Dokumen</a>
        <a href="#">PPID</a>
    </div>
    <div class="footer-column">
        <h4>Kontak</h4>
        <p style="font-size: 13px; color: rgba(255,255,255,0.6); line-height: 1.8;">
            📍 Jl. Merdeka No. 01, Calang<br>
            Kabupaten Aceh Jaya, Aceh<br>
            📞 (0655) 12345<br>
            ✉️ sekretariat@dprk.acehjaya.go.id
        </p>
    </div>
</div>
<div class="footer-bottom">
    <div>© {datetime.now().year} DPRK Aceh Jaya. Seluruh hak cipta dilindungi.</div>
    <div>Portal Informasi Publik • Kabupaten Aceh Jaya</div>
</div>
</div>
</div>
""",
    unsafe_allow_html=True
)

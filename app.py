import streamlit as st
import streamlit.components.v1 as components
from datetime import datetime

# ============================================================
# CONFIG
# ============================================================
st.set_page_config(
    page_title="Sekretariat DPRK Aceh Jaya",
    page_icon="🏛️",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ============================================================
# PREMIUM CSS
# ============================================================
st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap');

:root {
    --green-950: #022c22;
    --green-900: #064e3b;
    --green-800: #065f46;
    --green-700: #047857;
    --green-600: #059669;
    --green-500: #10b981;
    --green-100: #d1fae5;
    --green-50: #ecfdf5;

    --gold-500: #d97706;
    --gold-400: #f59e0b;
    
    --slate-900: #0f172a;
    --slate-700: #334155;
    --slate-600: #475569;
    --slate-500: #64748b;
    --slate-400: #94a3b8;
    --slate-200: #e2e8f0;
    --slate-100: #f1f5f9;
    --slate-50: #f8fafc;
}

* {
    font-family: 'Plus Jakarta Sans', sans-serif;
}

html {
    scroll-behavior: smooth;
}

body {
    background:
        radial-gradient(circle at 10% 10%, rgba(16,185,129,.07), transparent 25%),
        radial-gradient(circle at 90% 20%, rgba(245,158,11,.05), transparent 25%),
        #f8fafc;
}

#MainMenu,
footer,
header {
    visibility: hidden;
}

.block-container {
    max-width: 1450px;
    padding-top: 1.5rem;
    padding-bottom: 3rem;
}

/* ============================================================
   TOP HEADER
============================================================ */

.top-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    gap: 20px;
    padding: 18px 24px;
    background: rgba(255,255,255,.86);
    backdrop-filter: blur(18px);
    border: 1px solid rgba(226,232,240,.9);
    border-radius: 20px;
    box-shadow: 0 8px 30px rgba(15,23,42,.05);
}

.brand {
    display: flex;
    align-items: center;
    gap: 15px;
}

.brand-logo {
    width: 55px;
    height: 55px;
    border-radius: 16px;
    display: flex;
    align-items: center;
    justify-content: center;
    background: linear-gradient(135deg, #064e3b, #059669);
    color: white;
    font-size: 28px;
    box-shadow: 0 10px 20px rgba(5,150,105,.25);
}

.brand-title {
    font-size: 20px;
    font-weight: 800;
    color: var(--green-900);
    margin: 0;
}

.brand-subtitle {
    color: var(--slate-500);
    font-size: 12px;
    margin-top: 3px;
}

.weather-card {
    display: flex;
    align-items: center;
    gap: 12px;
    padding: 10px 16px;
    border-radius: 15px;
    background: var(--slate-50);
    border: 1px solid var(--slate-200);
}

.weather-icon {
    font-size: 28px;
}

.weather-city {
    color: var(--slate-500);
    font-size: 11px;
    font-weight: 600;
}

.weather-temp {
    color: var(--slate-900);
    font-size: 20px;
    font-weight: 800;
}

.weather-status {
    color: var(--green-600);
    font-size: 10px;
    font-weight: 700;
}

/* ============================================================
   NAVIGATION
============================================================ */

.stRadio > div {
    background: white !important;
    padding: 7px !important;
    border-radius: 17px !important;
    border: 1px solid var(--slate-200) !important;
    box-shadow: 0 6px 25px rgba(15,23,42,.04);
    gap: 3px !important;
}

.stRadio label {
    border-radius: 12px !important;
    padding: 9px 13px !important;
    font-size: 12px !important;
    font-weight: 700 !important;
    color: var(--slate-600) !important;
    transition: all .25s ease !important;
}

.stRadio label:hover {
    background: var(--green-50) !important;
    color: var(--green-700) !important;
}

.stRadio input:checked + label {
    background: linear-gradient(135deg,#064e3b,#059669) !important;
    color: white !important;
    box-shadow: 0 5px 15px rgba(5,150,105,.25);
}

/* ============================================================
   HERO
============================================================ */

.hero {
    position: relative;
    overflow: hidden;
    border-radius: 28px;
    padding: 60px 55px;
    color: white;
    background:
        radial-gradient(circle at 85% 20%, rgba(255,255,255,.18), transparent 22%),
        radial-gradient(circle at 70% 100%, rgba(16,185,129,.4), transparent 35%),
        linear-gradient(135deg,#022c22 0%,#064e3b 45%,#059669 100%);
    box-shadow: 0 25px 60px rgba(4,120,87,.22);
}

.hero::before {
    content: "";
    position: absolute;
    width: 380px;
    height: 380px;
    right: -120px;
    top: -180px;
    border-radius: 50%;
    background: rgba(255,255,255,.05);
}

.hero::after {
    content: "🏛️";
    position: absolute;
    right: 40px;
    bottom: -40px;
    font-size: 190px;
    opacity: .07;
    transform: rotate(-10deg);
}

.hero-content {
    position: relative;
    z-index: 2;
    max-width: 750px;
}

.hero-kicker {
    display: inline-block;
    padding: 7px 13px;
    border-radius: 30px;
    background: rgba(255,255,255,.12);
    border: 1px solid rgba(255,255,255,.18);
    font-size: 11px;
    font-weight: 800;
    letter-spacing: 1px;
    margin-bottom: 18px;
}

.hero h1 {
    font-size: clamp(32px, 4vw, 52px);
    line-height: 1.08;
    margin: 0 0 18px;
    font-weight: 800;
    letter-spacing: -1.5px;
}

.hero p {
    font-size: 16px;
    line-height: 1.8;
    color: rgba(255,255,255,.85);
    max-width: 680px;
    margin: 0;
}

.hero-button {
    display: inline-block;
    margin-top: 28px;
    padding: 12px 20px;
    border-radius: 12px;
    background: white;
    color: var(--green-900);
    font-size: 13px;
    font-weight: 800;
}

/* ============================================================
   SECTION
============================================================ */

.section-title {
    font-size: 24px;
    font-weight: 800;
    color: var(--slate-900);
    margin-bottom: 5px;
}

.section-subtitle {
    color: var(--slate-500);
    font-size: 13px;
    margin-bottom: 22px;
}

/* ============================================================
   STAT CARDS
============================================================ */

.stat-card {
    position: relative;
    overflow: hidden;
    background: white;
    border: 1px solid var(--slate-200);
    border-radius: 20px;
    padding: 23px;
    box-shadow: 0 8px 25px rgba(15,23,42,.04);
    transition: all .3s ease;
}

.stat-card:hover {
    transform: translateY(-5px);
    box-shadow: 0 18px 40px rgba(15,23,42,.09);
    border-color: #a7f3d0;
}

.stat-icon {
    width: 46px;
    height: 46px;
    border-radius: 13px;
    display: flex;
    align-items: center;
    justify-content: center;
    background: var(--green-50);
    font-size: 23px;
}

.stat-number {
    margin-top: 18px;
    font-size: 30px;
    font-weight: 800;
    color: var(--green-700);
}

.stat-label {
    margin-top: 3px;
    font-size: 11px;
    color: var(--slate-500);
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: .6px;
}

/* ============================================================
   CONTENT CARDS
============================================================ */

.card {
    background: white;
    border: 1px solid var(--slate-200);
    border-radius: 20px;
    padding: 25px;
    box-shadow: 0 8px 25px rgba(15,23,42,.035);
}

.card h3 {
    color: var(--green-900);
    font-size: 18px;
    margin-top: 0;
}

.card p,
.card li {
    color: var(--slate-600);
    font-size: 13px;
    line-height: 1.8;
}

/* ============================================================
   NEWS
============================================================ */

.news-card {
    display: flex;
    gap: 18px;
    background: white;
    border: 1px solid var(--slate-200);
    border-radius: 18px;
    padding: 18px;
    margin-bottom: 14px;
    transition: all .25s ease;
}

.news-card:hover {
    transform: translateX(4px);
    border-color: #a7f3d0;
    box-shadow: 0 10px 30px rgba(15,23,42,.06);
}

.news-date {
    min-width: 68px;
    height: 68px;
    border-radius: 14px;
    background: var(--green-50);
    border: 1px solid #bbf7d0;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
}

.news-day {
    font-size: 21px;
    font-weight: 800;
    color: var(--green-700);
}

.news-month {
    font-size: 9px;
    font-weight: 800;
    color: var(--slate-500);
    text-transform: uppercase;
}

.news-tag {
    display: inline-block;
    padding: 4px 9px;
    border-radius: 20px;
    background: #dbeafe;
    color: #1d4ed8;
    font-size: 9px;
    font-weight: 800;
}

.news-title {
    margin: 7px 0 4px;
    color: var(--slate-900);
    font-size: 15px;
    font-weight: 800;
}

.news-desc {
    margin: 0;
    color: var(--slate-500);
    font-size: 12px;
    line-height: 1.6;
}

/* ============================================================
   SERVICES
============================================================ */

.service-card {
    text-align: center;
    background: white;
    border: 1px solid var(--slate-200);
    border-radius: 20px;
    padding: 28px 20px;
    min-height: 215px;
    transition: all .3s ease;
}

.service-card:hover {
    transform: translateY(-6px);
    border-color: #6ee7b7;
    box-shadow: 0 18px 35px rgba(15,23,42,.08);
}

.service-icon {
    width: 58px;
    height: 58px;
    margin: auto;
    display: flex;
    align-items: center;
    justify-content: center;
    border-radius: 17px;
    background: linear-gradient(135deg,#ecfdf5,#d1fae5);
    font-size: 29px;
}

.service-title {
    margin-top: 16px;
    font-weight: 800;
    font-size: 15px;
    color: var(--slate-900);
}

.service-desc {
    color: var(--slate-500);
    font-size: 11px;
    line-height: 1.7;
}

/* ============================================================
   DOCUMENT
============================================================ */

.document-card {
    display: flex;
    justify-content: space-between;
    align-items: center;
    gap: 15px;
    background: white;
    border: 1px solid var(--slate-200);
    padding: 18px 20px;
    border-radius: 16px;
    margin-bottom: 12px;
}

.document-icon {
    width: 43px;
    height: 43px;
    border-radius: 11px;
    display: flex;
    align-items: center;
    justify-content: center;
    background: #fef2f2;
    color: #dc2626;
    font-weight: 800;
}

.document-title {
    font-size: 13px;
    font-weight: 700;
    color: var(--slate-900);
}

.document-meta {
    font-size: 10px;
    color: var(--slate-500);
    margin-top: 3px;
}

/* ============================================================
   PORA
============================================================ */

.pora-hero {
    background:
        radial-gradient(circle at 85% 20%, rgba(255,255,255,.15), transparent 20%),
        linear-gradient(135deg,#451a03,#92400e,#d97706);
    border-radius: 27px;
    padding: 48px;
    color: white;
    box-shadow: 0 25px 55px rgba(180,83,9,.2);
}

.countdown {
    display: flex;
    justify-content: center;
    gap: 12px;
    flex-wrap: wrap;
    margin: 25px 0;
}

.count-box {
    min-width: 100px;
    padding: 18px;
    border-radius: 17px;
    background: linear-gradient(135deg,#064e3b,#059669);
    color: white;
    text-align: center;
    box-shadow: 0 10px 25px rgba(5,150,105,.18);
}

.count-value {
    display: block;
    font-size: 32px;
    font-weight: 800;
}

.count-label {
    font-size: 10px;
    text-transform: uppercase;
    opacity: .8;
    letter-spacing: 1px;
}

/* ============================================================
   FOOTER
============================================================ */

.footer {
    margin-top: 45px;
    padding: 30px;
    text-align: center;
    border-radius: 22px;
    background: #022c22;
    color: rgba(255,255,255,.7);
}

.footer-title {
    color: white;
    font-weight: 800;
    font-size: 14px;
}

.footer-text {
    font-size: 11px;
    margin-top: 7px;
}

/* ============================================================
   STREAMLIT BUTTON
============================================================ */

.stButton > button,
.stDownloadButton > button {
    border-radius: 11px !important;
    border: none !important;
    font-weight: 700 !important;
    background: linear-gradient(135deg,#047857,#059669) !important;
    color: white !important;
    transition: all .25s ease !important;
}

.stButton > button:hover,
.stDownloadButton > button:hover {
    transform: translateY(-2px);
    box-shadow: 0 8px 20px rgba(5,150,105,.25);
}

/* ============================================================
   MOBILE
============================================================ */

@media (max-width: 768px) {

    .block-container {
        padding-left: 1rem;
        padding-right: 1rem;
    }

    .top-header {
        flex-direction: column;
        align-items: flex-start;
    }

    .weather-card {
        width: 100%;
    }

    .hero {
        padding: 38px 25px;
    }

    .hero h1 {
        font-size: 34px;
    }

    .hero::after {
        font-size: 110px;
    }

    .pora-hero {
        padding: 32px 22px;
    }
}

</style>
""", unsafe_allow_html=True)


# ============================================================
# HEADER
# ============================================================

st.markdown("""
<div class="top-header">

    <div class="brand">
        <div class="brand-logo">🏛️</div>
        <div>
            <div class="brand-title">Sekretariat DPRK Aceh Jaya</div>
            <div class="brand-subtitle">
                Dewan Perwakilan Rakyat Kabupaten Aceh Jaya
            </div>
        </div>
    </div>

    <div class="weather-card">
        <div class="weather-icon">⛅</div>
        <div>
            <div class="weather-city">ACEH JAYA, ACEH</div>
            <div class="weather-temp">26°C</div>
            <div class="weather-status">● Cerah Berawan • BMKG</div>
        </div>
    </div>

</div>
""", unsafe_allow_html=True)

st.markdown("<div style='height:18px'></div>", unsafe_allow_html=True)


# ============================================================
# NAVIGATION
# ============================================================

menu_items = [
    "🏠 BERANDA",
    "🏛️ PROFIL",
    "📰 INFORMASI",
    "📸 GALERI",
    "🛎️ LAYANAN",
    "📂 INFO PUBLIK",
    "📞 KONTAK",
    "🏆 PORA 2026",
]

selected_menu = st.radio(
    "",
    menu_items,
    horizontal=True,
    label_visibility="collapsed"
)

st.markdown("""
<div style="
text-align:center;
margin:18px 0 28px;
padding:11px;
border-top:1px solid #e2e8f0;
border-bottom:1px solid #e2e8f0;
color:#64748b;
font-size:12px;
font-weight:600;
letter-spacing:.3px;
">
Mewujudkan Kabupaten Aceh Jaya yang Transparan, Aspiratif, dan Sejahtera
</div>
""", unsafe_allow_html=True)


# ============================================================
# BERANDA
# ============================================================

if selected_menu == "🏠 BERANDA":

    st.markdown("""
    <div class="hero">

        <div class="hero-content">

            <div class="hero-kicker">
                PORTAL RESMI • DPRK ACEH JAYA
            </div>

            <h1>
                Transparansi untuk<br>
                Aceh Jaya yang Lebih Baik
            </h1>

            <p>
                Selamat datang di portal resmi Sekretariat Dewan
                Perwakilan Rakyat Kabupaten Aceh Jaya.
                Akses informasi, layanan publik, agenda, dan
                dokumen DPRK secara mudah dan transparan.
            </p>

            <div class="hero-button">
                ✨ Melayani dengan Integritas
            </div>

        </div>

    </div>
    """, unsafe_allow_html=True)

    st.markdown("<div style='height:30px'></div>", unsafe_allow_html=True)

    # Statistics
    st.markdown(
        '<div class="section-title">Ringkasan Kinerja</div>'
        '<div class="section-subtitle">Informasi singkat aktivitas dan pelayanan DPRK Aceh Jaya</div>',
        unsafe_allow_html=True
    )

    cols = st.columns(4)

    stats = [
        ("📜", "15+", "Perda Disusun"),
        ("🗣️", "250+", "Aspirasi Masyarakat"),
        ("🏛️", "4", "Komisi Aktif"),
        ("⭐", "98%", "Indeks Kepuasan"),
    ]

    for col, (icon, number, label) in zip(cols, stats):
        with col:
            st.markdown(f"""
            <div class="stat-card">
                <div class="stat-icon">{icon}</div>
                <div class="stat-number">{number}</div>
                <div class="stat-label">{label}</div>
            </div>
            """, unsafe_allow_html=True)

    st.markdown("<div style='height:35px'></div>", unsafe_allow_html=True)

    # News + Quick Service
    left, right = st.columns([1.5, 1])

    with left:

        st.markdown(
            '<div class="section-title">Informasi Terkini</div>'
            '<div class="section-subtitle">Agenda dan kegiatan terbaru</div>',
            unsafe_allow_html=True
        )

        news = [
            (
                "15",
                "SEP",
                "RAPAT PARIPURNA",
                "Rapat Paripurna Pembahasan KUA-PPAS Tahun 2027",
                "Pembahasan bersama antara DPRK dan Pemkab Aceh Jaya terkait prioritas anggaran."
            ),
            (
                "10",
                "SEP",
                "MUSRENBANG",
                "Pelaksanaan Musyawarah Rencana Pembangunan Daerah",
                "Penjaringan aspirasi masyarakat untuk rencana pembangunan tahun depan."
            ),
            (
                "01",
                "SEP",
                "SOSIALISASI",
                "Sosialisasi Peraturan Daerah Baru",
                "Kegiatan sosialisasi dan penyampaian informasi peraturan daerah kepada masyarakat."
            ),
        ]

        for day, month, tag, title, desc in news:

            st.markdown(f"""
            <div class="news-card">

                <div class="news-date">
                    <div class="news-day">{day}</div>
                    <div class="news-month">{month}</div>
                </div>

                <div>
                    <span class="news-tag">{tag}</span>
                    <div class="news-title">{title}</div>
                    <p class="news-desc">{desc}</p>
                </div>

            </div>
            """, unsafe_allow_html=True)

    with right:

        st.markdown(
            '<div class="section-title">Akses Cepat</div>'
            '<div class="section-subtitle">Layanan yang sering digunakan masyarakat</div>',
            unsafe_allow_html=True
        )

        quick = [
            ("📢", "Pengaduan Masyarakat", "Sampaikan aspirasi dan keluhan."),
            ("📄", "Informasi Publik", "Akses dokumen dan informasi resmi."),
            ("🗓️", "Agenda DPRK", "Lihat jadwal kegiatan dan persidangan."),
            ("📞", "Hubungi Kami", "Kontak resmi Sekretariat DPRK."),
        ]

        for icon, title, desc in quick:

            st.markdown(f"""
            <div class="card" style="margin-bottom:12px;padding:17px;">
                <div style="display:flex;gap:14px;align-items:center;">
                    <div class="service-icon"
                         style="width:45px;height:45px;min-width:45px;font-size:21px;">
                        {icon}
                    </div>
                    <div>
                        <div style="font-size:13px;font-weight:800;color:#0f172a;">
                            {title}
                        </div>
                        <div style="font-size:10px;color:#64748b;margin-top:3px;">
                            {desc}
                        </div>
                    </div>
                </div>
            </div>
            """, unsafe_allow_html=True)


# ============================================================
# PROFIL
# ============================================================

elif selected_menu == "🏛️ PROFIL":

    st.markdown(
        '<div class="section-title">Profil DPRK Aceh Jaya</div>'
        '<div class="section-subtitle">Mengenal tugas, fungsi, visi, dan misi lembaga</div>',
        unsafe_allow_html=True
    )

    st.markdown("""
    <div class="card">
        <h3>🏛️ Sekretariat DPRK Aceh Jaya</h3>
        <p>
        Sekretariat DPRK merupakan unsur pelayanan terhadap DPRK
        yang mendukung pelaksanaan fungsi legislasi, anggaran,
        pengawasan, serta pelayanan administrasi bagi anggota DPRK.
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<div style='height:20px'></div>", unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("""
        <div class="card">
            <h3>🎯 Visi</h3>
            <p>
            Terwujudnya DPRK Aceh Jaya yang profesional, aspiratif,
            transparan, dan berintegritas dalam mendukung pembangunan
            daerah yang berkeadilan.
            </p>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="card">
            <h3>🚀 Misi</h3>
            <ul>
                <li>Meningkatkan kualitas penyusunan Peraturan Daerah.</li>
                <li>Memperkuat fungsi pengawasan terhadap pemerintah daerah.</li>
                <li>Memfasilitasi aspirasi masyarakat secara transparan.</li>
                <li>Meningkatkan kualitas pelayanan Sekretariat DPRK.</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("<div style='height:25px'></div>", unsafe_allow_html=True)

    st.markdown(
        '<div class="section-title">Struktur Organisasi</div>'
        '<div class="section-subtitle">Unsur pimpinan dan perangkat DPRK</div>',
        unsafe_allow_html=True
    )

    cols = st.columns(4)

    structure = [
        ("👑", "Ketua DPRK", "Pimpinan"),
        ("🤝", "Wakil Ketua", "Pimpinan"),
        ("📁", "Sekretariat", "Administrasi"),
        ("🏛️", "Komisi", "4 Komisi"),
    ]

    for col, (icon, title, desc) in zip(cols, structure):
        with col:
            st.markdown(f"""
            <div class="card" style="text-align:center;">
                <div style="font-size:35px;">{icon}</div>
                <div style="font-weight:800;color:#0f172a;margin-top:10px;">
                    {title}
                </div>
                <div style="font-size:11px;color:#64748b;margin-top:4px;">
                    {desc}
                </div>
            </div>
            """, unsafe_allow_html=True)


# ============================================================
# INFORMASI
# ============================================================

elif selected_menu == "📰 INFORMASI":

    st.markdown(
        '<div class="section-title">Agenda & Informasi Terkini</div>'
        '<div class="section-subtitle">Berita, kegiatan, dan agenda DPRK Aceh Jaya</div>',
        unsafe_allow_html=True
    )

    news_items = [
        {
            "date": "15",
            "month": "SEP",
            "tag": "RAPAT PARIPURNA",
            "title": "Pembahasan KUA-PPAS Tahun 2027",
            "desc": "Pembahasan bersama DPRK dan Pemerintah Kabupaten Aceh Jaya mengenai prioritas anggaran."
        },
        {
            "date": "10",
            "month": "SEP",
            "tag": "MUSRENBANG",
            "title": "Musyawarah Rencana Pembangunan Daerah",
            "desc": "Penjaringan aspirasi masyarakat untuk mendukung perencanaan pembangunan daerah."
        },
        {
            "date": "01",
            "month": "SEP",
            "tag": "SOSIALISASI",
            "title": "Sosialisasi Peraturan Daerah Baru",
            "desc": "Kegiatan penyampaian informasi peraturan daerah kepada masyarakat."
        },
        {
            "date": "27",
            "month": "AGU",
            "tag": "RESES",
            "title": "Kegiatan Reses Anggota DPRK",
            "desc": "Penyerapan aspirasi masyarakat di berbagai wilayah Kabupaten Aceh Jaya."
        },
    ]

    for item in news_items:
        st.markdown(f"""
        <div class="news-card">

            <div class="news-date">
                <div class="news-day">{item['date']}</div>
                <div class="news-month">{item['month']}</div>
            </div>

            <div>
                <span class="news-tag">{item['tag']}</span>
                <div class="news-title">{item['title']}</div>
                <p class="news-desc">{item['desc']}</p>
            </div>

        </div>
        """, unsafe_allow_html=True)


# ============================================================
# GALERI
# ============================================================

elif selected_menu == "📸 GALERI":

    st.markdown(
        '<div class="section-title">Galeri Kegiatan DPRK</div>'
        '<div class="section-subtitle">Dokumentasi kegiatan legislatif dan pelayanan masyarakat</div>',
        unsafe_allow_html=True
    )

    images = [
        (
            "https://images.unsplash.com/photo-1541872703-74c5963631df?auto=format&fit=crop&w=900&q=85",
            "Rapat Koordinasi Komisi"
        ),
        (
            "https://images.unsplash.com/photo-1577962917302-cd874c4e31d2?auto=format&fit=crop&w=900&q=85",
            "Kunjungan Kerja"
        ),
        (
            "https://images.unsplash.com/photo-1556761175-5973dc0f32e7?auto=format&fit=crop&w=900&q=85",
            "Musyawarah Perencanaan Pembangunan"
        ),
    ]

    cols = st.columns(3)

    for col, (url, caption) in zip(cols, images):
        with col:
            st.image(
                url,
                use_container_width=True,
                caption=caption
            )


# ============================================================
# LAYANAN
# ============================================================

elif selected_menu == "🛎️ LAYANAN":

    st.markdown(
        '<div class="section-title">Layanan Publik</div>'
        '<div class="section-subtitle">Akses layanan Sekretariat DPRK Aceh Jaya</div>',
        unsafe_allow_html=True
    )

    services = [
        (
            "📢",
            "Pengaduan Masyarakat",
            "Sampaikan aspirasi, keluhan, atau saran Anda."
        ),
        (
            "📄",
            "Permohonan Informasi",
            "Ajukan permohonan informasi publik secara resmi."
        ),
        (
            "🗓️",
            "Jadwal Reses",
            "Lihat jadwal pertemuan anggota DPRK dengan masyarakat."
        ),
        (
            "⚖️",
            "Layanan Persidangan",
            "Informasi agenda rapat dan persidangan DPRK."
        ),
    ]

    cols = st.columns(4)

    for col, (icon, title, desc) in zip(cols, services):
        with col:
            st.markdown(f"""
            <div class="service-card">
                <div class="service-icon">{icon}</div>
                <div class="service-title">{title}</div>
                <div class="service-desc">{desc}</div>
            </div>
            """, unsafe_allow_html=True)

    st.markdown("<div style='height:25px'></div>", unsafe_allow_html=True)

    st.info(
        "💡 Gunakan layanan ini untuk menyampaikan aspirasi "
        "dan mendapatkan informasi resmi DPRK Aceh Jaya."
    )


# ============================================================
# INFO PUBLIK
# ============================================================

elif selected_menu == "📂 INFO PUBLIK":

    st.markdown(
        '<div class="section-title">Informasi & Dokumen Publik</div>'
        '<div class="section-subtitle">Dokumen resmi yang dapat diakses masyarakat</div>',
        unsafe_allow_html=True
    )

    docs = [
        ("LKPJ Kabupaten Aceh Jaya Tahun 2025", "PDF", "2.4 MB"),
        ("Nota Keuangan APBD Kabupaten Aceh Jaya 2026", "PDF", "5.1 MB"),
        ("Peraturan DPRK Nomor 3 Tahun 2025", "PDF", "1.2 MB"),
        ("Laporan Tahunan Sekretariat DPRK 2025", "PDF", "3.8 MB"),
    ]

    for index, (name, typ, size) in enumerate(docs):

        col1, col2 = st.columns([5, 1])

        with col1:
            st.markdown(f"""
            <div class="document-card">
                <div style="display:flex;align-items:center;gap:14px;">
                    <div class="document-icon">PDF</div>
                    <div>
                        <div class="document-title">{name}</div>
                        <div class="document-meta">
                            Dokumen publik • {size}
                        </div>
                    </div>
                </div>
            </div>
            """, unsafe_allow_html=True)

        with col2:
            st.markdown("<div style='height:12px'></div>", unsafe_allow_html=True)
            st.download_button(
                "📥 Unduh",
                data=f"Dokumen contoh: {name}",
                file_name=f"{name.replace(' ', '_')}.pdf",
                mime="application/pdf",
                key=f"download_{index}",
                use_container_width=True
            )


# ============================================================
# KONTAK
# ============================================================

elif selected_menu == "📞 KONTAK":

    st.markdown(
        '<div class="section-title">Hubungi Kami</div>'
        '<div class="section-subtitle">Sekretariat DPRK Aceh Jaya siap melayani masyarakat</div>',
        unsafe_allow_html=True
    )

    col1, col2 = st.columns([1, 1])

    with col1:

        st.markdown("""
        <div class="card">

            <h3>📍 Informasi Kontak</h3>

            <p>
            <strong>Alamat</strong><br>
            Jl. Merdeka No. 1, Kecamatan Setia,<br>
            Kabupaten Aceh Jaya, Aceh
            </p>

            <p>
            <strong>📞 Telepon</strong><br>
            (0650) 123456
            </p>

            <p>
            <strong>✉️ Email</strong><br>
            sekretariat.dprk@acehjaya.go.id
            </p>

            <p>
            <strong>🕒 Jam Operasional</strong><br>
            Senin – Jumat<br>
            08.00 – 16.00 WIB
            </p>

        </div>
        """, unsafe_allow_html=True)

    with col2:

        st.markdown("""
        <div class="card">
            <h3>✉️ Kirim Pesan</h3>
        </div>
        """, unsafe_allow_html=True)

        with st.form("contact_form"):

            c1, c2 = st.columns(2)

            with c1:
                nama = st.text_input("Nama Lengkap")

            with c2:
                email = st.text_input("Alamat Email")

            pesan = st.text_area(
                "Pesan / Aspirasi",
                height=140
            )

            submitted = st.form_submit_button(
                "Kirim Pesan",
                use_container_width=True,
                type="primary"
            )

            if submitted:

                if nama and email and pesan:
                    st.success(
                        "✅ Pesan berhasil dikirim. "
                        "Terima kasih telah menyampaikan aspirasi."
                    )
                else:
                    st.error(
                        "⚠️ Mohon lengkapi seluruh formulir."
                    )

    st.markdown("<div style='height:25px'></div>", unsafe_allow_html=True)

    st.markdown(
        '<div class="section-title">Lokasi</div>',
        unsafe_allow_html=True
    )

    components.html("""
    <iframe
        src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d127637.898456!2d95.5!3d4.8!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x30403b0000000001%3A0x0!2sAceh+Jaya!5e0!3m2!1sid!2sid!4v1600000000000"
        width="100%"
        height="320"
        style="border:0;border-radius:20px;"
        allowfullscreen=""
        loading="lazy">
    </iframe>
    """, height=320)


# ============================================================
# PORA 2026
# ============================================================

elif selected_menu == "🏆 PORA 2026":

    st.markdown("""
    <div class="pora-hero">

        <div style="
            font-size:11px;
            font-weight:800;
            letter-spacing:1px;
            opacity:.8;
            margin-bottom:10px;">
            EVENT OLAHRAGA ACEH
        </div>

        <h1 style="
            font-size:42px;
            margin:0 0 14px;
            font-weight:800;">
            🏆 PORA ACEH 2026
        </h1>

        <p style="
            max-width:650px;
            line-height:1.7;
            opacity:.9;
            margin:0;">
            Pekan Olahraga Aceh merupakan ajang olahraga terbesar
            di Provinsi Aceh. DPRK Aceh Jaya mendukung penuh
            persiapan dan kesuksesan penyelenggaraan PORA 2026.
        </p>

    </div>
    """, unsafe_allow_html=True)

    st.markdown("<div style='height:30px'></div>", unsafe_allow_html=True)

    st.markdown("""
    <div style="
        text-align:center;
        font-size:18px;
        font-weight:800;
        color:#064e3b;">
        Menuju Pembukaan Resmi
    </div>
    """, unsafe_allow_html=True)

    countdown_html = """
    <style>
    body {
        margin:0;
        background:transparent;
        font-family:Arial,sans-serif;
    }

    .countdown {
        display:flex;
        justify-content:center;
        gap:12px;
        margin:20px 0;
        flex-wrap:wrap;
    }

    .box {
        min-width:90px;
        padding:18px 14px;
        border-radius:16px;
        background:linear-gradient(135deg,#064e3b,#059669);
        color:white;
        text-align:center;
        box-shadow:0 10px 25px rgba(5,150,105,.2);
    }

    .value {
        font-size:32px;
        font-weight:800;
        display:block;
    }

    .label {
        font-size:10px;
        opacity:.8;
        text-transform:uppercase;
        letter-spacing:1px;
    }
    </style>

    <div class="countdown" id="countdown">

        <div class="box">
            <span class="value" id="days">00</span>
            <span class="label">Hari</span>
        </div>

        <div class="box">
            <span class="value" id="hours">00</span>
            <span class="label">Jam</span>
        </div>

        <div class="box">
            <span class="value" id="minutes">00</span>
            <span class="label">Menit</span>
        </div>

        <div class="box">
            <span class="value" id="seconds">00</span>
            <span class="label">Detik</span>
        </div>

    </div>

    <script>

    const target = new Date("October 15, 2026 08:00:00").getTime();

    function updateCountdown() {

        const now = new Date().getTime();
        const distance = target - now;

        if (distance <= 0) {

            document.getElementById("countdown").innerHTML =
                "<div style='font-size:22px;font-weight:800;color:#059669;'>🎉 PORA ACEH 2026 SEDANG BERLANGSUNG!</div>";

            return;
        }

        document.getElementById("days").innerText =
            Math.floor(distance / (1000 * 60 * 60 * 24));

        document.getElementById("hours").innerText =
            Math.floor(
                (distance % (1000 * 60 * 60 * 24))
                / (1000 * 60 * 60)
            );

        document.getElementById("minutes").innerText =
            Math.floor(
                (distance % (1000 * 60 * 60))
                / (1000 * 60)
            );

        document.getElementById("seconds").innerText =
            Math.floor(
                (distance % (1000 * 60))
                / 1000
            );
    }

    updateCountdown();
    setInterval(updateCountdown, 1000);

    </script>
    """

    components.html(
        countdown_html,
        height=150
    )

    st.markdown("<div style='height:15px'></div>", unsafe_allow_html=True)

    st.markdown(
        '<div class="section-title">📅 Agenda Persiapan</div>'
        '<div class="section-subtitle">Timeline persiapan PORA Aceh 2026</div>',
        unsafe_allow_html=True
    )

    st.dataframe(
        {
            "Tanggal": [
                "10 Jan 2026",
                "15 Mar 2026",
                "01 Jun 2026",
                "15 Okt 2026"
            ],
            "Kegiatan": [
                "Rapat Koordinasi Panitia",
                "Finalisasi Anggaran Pendampingan",
                "Monitoring Pembangunan Venue",
                "Upacara Pembukaan"
            ],
            "Status": [
                "✅ Selesai",
                "✅ Selesai",
                "🔄 Berjalan",
                "⏳ Mendatang"
            ]
        },
        use_container_width=True,
        hide_index=True
    )


# ============================================================
# FOOTER
# ============================================================

st.markdown("""
<div class="footer">

    <div style="font-size:32px;margin-bottom:10px;">🏛️</div>

    <div class="footer-title">
        SEKRETARIAT DPRK ACEH JAYA
    </div>

    <div class="footer-text">
        Dewan Perwakilan Rakyat Kabupaten Aceh Jaya
    </div>

    <div style="
        height:1px;
        background:rgba(255,255,255,.12);
        margin:20px auto;
        max-width:500px;">
    </div>

    <div class="footer-text">
        © 2026 Sekretariat DPRK Aceh Jaya
        • Transparansi • Akuntabilitas • Pelayanan Publik
    </div>

    <div style="
        margin-top:12px;
        font-size:10px;
        color:rgba(255,255,255,.45);">
        Dibangun untuk pelayanan publik yang lebih baik ❤️
    </div>

</div>
""", unsafe_allow_html=True)

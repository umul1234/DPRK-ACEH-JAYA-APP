import streamlit as st
import streamlit.components.v1 as components
from datetime import datetime

st.set_page_config(
    page_title="DPRK Aceh Jaya",
    page_icon="🏛️",
    layout="wide",
    initial_sidebar_state="expanded",
)

# DATA GLOBAL
news_list = [
    ("📝", "PARIPURNA", "15 September 2026", "Pembahasan Rancangan KUA-PPAS 2027",
     "Rapat paripurna pembahasan kebijakan umum anggaran dan prioritas plafon anggaran sementara."),
    ("📢", "RESES", "10 September 2026", "Penjaringan Aspirasi Masyarakat Melalui Reses",
     "Anggota DPRK turun ke daerah pemilihan untuk menampung aspirasi masyarakat."),
    ("⚖️", "LEGISLASI", "02 September 2026", "RDPU Qanun Ketertiban",
     "Rapat dengar pendapat umum untuk penyempurnaan rancangan Qanun Daerah.")
]

pages = {
    "Beranda": "Beranda",
    "Profil": "Profil & Kelengkapan",
    "Dewan": "Fungsi & Komisi",
    "Berita": "Berita & Rapat",
    "JDIH": "JDIH & Transparansi",
    "Aspirasi": "Layanan & Pengaduan",
    "PORA": "PORA XV 2026",
    "Kontak": "Kontak & Peta"
}

# CSS STYLING (WARNA TOMBOL TERANG & SERASI)
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');

:root {
    --navy: #0B3C5D;
    --navy-light: #164E75;
    --green: #1D7A46;
    --green-light: #EAF6EF;
    --gold: #D9A05B;
    --bg: #F4F7F9;
    --text: #2C3E50;
    --muted: #6C7A89;
    --line: #E2E8F0;
}

* { font-family: 'Inter', sans-serif; }
.stApp { background: var(--bg) !important; color: var(--text) !important; }

/* Sidebar Background Terang & Elegan */
[data-testid="stSidebar"] {
    background-color: #FFFFFF !important;
    border-right: 1px solid var(--line) !important;
}
[data-testid="stSidebar"] * {
    color: var(--text) !important;
}

/* DESAIN TOMBOL BARU: Serasi, Terang, & Bebas Warna Gelap */
.stButton > button {
    background-color: #FFFFFF !important;
    color: var(--navy) !important;
    border: 1px solid #CBD5E1 !important;
    border-radius: 10px !important;
    font-weight: 600 !important;
    font-size: 13px !important;
    padding: 10px 16px !important;
    box-shadow: 0 2px 5px rgba(0,0,0,0.03) !important;
    transition: all 0.25s ease-in-out !important;
}

/* Efek Hover Tombol (Hijau Aceh yang Lembut) */
.stButton > button:hover {
    background-color: var(--green-light) !important;
    color: var(--green) !important;
    border-color: var(--green) !important;
    box-shadow: 0 4px 10px rgba(29, 122, 70, 0.12) !important;
    transform: translateY(-1px);
}

/* Tombol Aktif / Terpilih */
[data-testid="stSidebar"] .stButton > button[kind="secondary"] {
    border-left: 4px solid var(--navy) !important;
}

.block-container {
    max-width: 1280px;
    padding: 2rem 2rem 4rem;
}

.gov-strip {
    background: var(--navy);
    color: #fff;
    font-size: 11px;
    padding: 10px 18px;
    border-radius: 12px;
    margin-bottom: 20px;
    display: flex;
    justify-content: space-between;
}

.hero {
    min-height: 260px;
    border-radius: 20px;
    background: linear-gradient(135deg, var(--navy), var(--green));
    display: flex;
    align-items: center;
    padding: 35px;
    color: white;
    box-shadow: 0 10px 25px rgba(11, 60, 93, 0.12);
}
.hero h1 { font-size: 32px; font-weight: 800; margin: 8px 0; }

.service-card {
    background: #FFFFFF;
    border: 1px solid var(--line);
    border-radius: 16px;
    padding: 20px;
    min-height: 140px;
    margin-bottom: 12px;
    box-shadow: 0 2px 8px rgba(0,0,0,0.02);
}
.service-icon { font-size: 26px; margin-bottom: 8px; }
.service-title { color: var(--navy); font-weight: 800; font-size: 15px; }
.service-text { color: var(--muted); font-size: 12px; margin-top: 4px; line-height: 1.5; }

.card {
    background: #FFFFFF;
    border: 1px solid var(--line);
    border-radius: 16px;
    padding: 22px;
    margin-bottom: 15px;
}
.card-title { color: var(--navy); font-weight: 800; font-size: 16px; }

.footer {
    margin-top: 40px;
    background: var(--navy);
    color: #fff;
    padding: 25px;
    border-radius: 16px;
    font-size: 12px;
}
</style>
""", unsafe_allow_html=True)

if "page" not in st.session_state:
    st.session_state.page = "Beranda"

# SIDEBAR NAVIGATION
with st.sidebar:
    st.markdown("## 🏛️ DPRK ACEH JAYA")
    st.caption("Dewan Perwakilan Rakyat Kabupaten")
    st.markdown("---")
    
    for label, target in pages.items():
        is_active = (st.session_state.page == target)
        prefix = "📌 " if is_active else "  "
        if st.button(f"{prefix}{label}", key="side_nav_"+label, use_container_width=True):
            st.session_state.page = target
            st.rerun()

    st.markdown("---")
    st.caption("© 2026 Layanan Digital DPRK")

# KONTEN UTAMA
st.markdown("""
<div class="gov-strip">
  <div>PEMERINTAH KABUPATEN ACEH JAYA • INFORMASI PUBLIK</div>
  <div>Portal Resmi DPRK Aceh Jaya</div>
</div>
""", unsafe_allow_html=True)

if st.session_state.page == "Beranda":
    st.markdown("""
    <div class="hero">
      <div>
        <span style="color:#F2D09B; font-size:11px; font-weight:800; letter-spacing:1px;">PORTAL RESMI</span>
        <h1>Informasi, Aspirasi, & Transparansi</h1>
        <p>Akses informasi kelembagaan DPRK, kegiatan dewan, dokumen JDIH, serta layanan pengaduan masyarakat.</p>
      </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<h3 style='color:var(--navy); margin-top:28px;'>Layanan Utama</h3>", unsafe_allow_html=True)
    
    services = [
        ("🏛️","Profil DPRK","Informasi kelembagaan & pimpinan.","Profil"),
        ("📜","Fungsi & Komisi","Informasi komisi & tugas legislasi.","Dewan"),
        ("📂","JDIH","Dokumen Qanun & APBK.","JDIH"),
        ("📢","Aspirasi Publik","Layanan pengaduan masyarakat.","Aspirasi"),
        ("📰","Berita & Agenda","Kabar terbaru kegiatan dewan.","Berita"),
        ("🏆","PORA XV 2026","Informasi tuan rumah PORA 2026.","PORA"),
    ]

    cols = st.columns(3)
    for i, (icon, title, desc, target) in enumerate(services):
        with cols[i % 3]:
            st.markdown(f"""
            <div class="service-card">
              <div class="service-icon">{icon}</div>
              <div class="service-title">{title}</div>
              <div class="service-text">{desc}</div>
            </div>
            """, unsafe_allow_html=True)
            if st.button("Buka Halaman", key="srv_"+target, use_container_width=True):
                st.session_state.page = pages[target]
                st.rerun()

elif st.session_state.page == "Berita & Rapat":
    st.markdown("<h3 style='color:var(--navy);'>Berita & Informasi Terkini</h3>", unsafe_allow_html=True)
    for icon, tag, date, title, desc in news_list:
        st.markdown(f"""
        <div class="card">
          <span style="background:var(--green-light); color:var(--green); padding:4px 10px; border-radius:12px; font-size:10px; font-weight:700;">{tag}</span>
          <span style="color:var(--muted); font-size:11px; float:right;">{date}</span>
          <div class="card-title" style="margin-top:10px;">{icon} {title}</div>
          <div style="color:var(--muted); font-size:13px; margin-top:6px;">{desc}</div>
        </div>
        """, unsafe_allow_html=True)

else:
    st.markdown(f"<h3 style='color:var(--navy);'>{st.session_state.page}</h3>", unsafe_allow_html=True)
    st.markdown('<div class="card"><div style="color:var(--muted);">Halaman ini sedang dalam pembaruan informasi.</div></div>', unsafe_allow_html=True)

# Footer
st.markdown("""
<div class="footer">
  <b>DPRK ACEH JAYA</b><br>
  Sekretariat DPRK Aceh Jaya • Jl. Merdeka No. 01, Calang, Kabupaten Aceh Jaya.<br>
  Email: sekretariat@dprk.acehjaya.go.id
</div>
""", unsafe_allow_html=True)
